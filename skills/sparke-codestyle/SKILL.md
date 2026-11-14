---
name: sparke-codestyle
description: >
  Kanchan's Spark.E backend codestyle guide. Enforces exact patterns from the live codebase:
  ESM imports, asyncHandler wrapper, ApiError/ApiResponse classes, Zod safeParse validation,
  named exports, Mongoose + Prisma dual-DB conventions, BullMQ queue patterns, logger usage,
  and file/folder naming. Use this skill whenever writing or editing any Node.js/Express backend
  code for the Spark.E project — controllers, routes, middlewares, validators, services, models,
  workers, or queue files. Trigger on phrases like "write a controller", "add a route", "new
  service", "follow my style", "/codestyle", or any Spark.E backend code task.
---

# Spark.E Backend Codestyle

Kanchan's live codebase patterns. Follow exactly — no deviation.

---

## Project Stack

- **Runtime**: Node.js ESM (`"type": "module"` in package.json)
- **Framework**: Express 5
- **Databases**: MongoDB (Mongoose) + PostgreSQL (Prisma 7) — dual DB
- **Queue**: BullMQ + Redis (ioredis)
- **Validation**: Zod v4
- **Logging**: Winston (`logger` from `../logger/index.js`)
- **Auth**: httpOnly cookie JWT (`accessToken` cookie)
- **File uploads**: Multer
- **Prettier**: double quotes, 2-space tabs, semi: true, printWidth: 100, trailingComma: es5

---

## Import Style

Always ESM. Always `.js` extension on local imports. No default export for named utilities.

```js
import { asyncHandler } from "../utils/asyncHandler.js"
import { ApiError, ApiResponse } from "../utils/Async.js"
import logger from "../logger/index.js"
import { SomeModel } from "../models/some.model.js"
import { someValidator } from "../validators/some.validator.js"
import mongoose from "mongoose"
```

Import order: node built-ins → third-party → internal (utils → lib → models → validators → services).

---

## Core Utilities

### ApiResponse (utils/Async.js)
```js
class ApiResponse {
    constructor(statusCode, data, message = "Success") {
        this.statusCode = statusCode
        this.data = data
        this.message = message
        this.success = statusCode < 400
    }
}
```

### ApiError (utils/Async.js)
```js
class ApiError extends Error {
    constructor(statusCode, message = "Something went wrong", errors = [], stack = "") {
        super(message)
        this.statusCode = statusCode
        this.data = null
        this.message = message
        this.success = false
        this.errors = errors
        if (stack) {
            this.stack = stack
        } else {
            Error.captureStackTrace(this, this.constructor)
        }
    }
}
```

### asyncHandler (utils/asyncHandler.js)
```js
const asyncHandler = (requestHandler) => {
    return (req, res, next) => {
        Promise.resolve(requestHandler(req, res, next)).catch((err) => next(err))
    }
}
```

All controllers must be wrapped in `asyncHandler`. Throw `ApiError` to propagate errors — never call `next(err)` manually in controllers.

---

## Controller Pattern

```js
import { asyncHandler } from "../utils/asyncHandler.js"
import { ApiError, ApiResponse } from "../utils/Async.js"
import { someValidator } from "../validators/some.validator.js"
import { SomeModel } from "../models/some.model.js"
import logger from "../logger/index.js"

const doSomething = asyncHandler(async (req, res) => {
    const { data, error } = someValidator.safeParse(req.body)

    if (error) {
        throw new ApiError(400, error.issues.map(e => e.message).join(", "))
    }
    const { field1, field2 } = data

    const userId = req.user.id

    const result = await SomeModel.create({ userId, field1, field2 })

    return res
        .status(201)
        .json(new ApiResponse(201, result, "Created successfully"))
})

const getAll = asyncHandler(async (req, res) => {
    const userId = req.user.id

    const data = await SomeModel.find({ userId }).sort({ createdAt: -1 })

    return res
        .status(200)
        .json(new ApiResponse(200, data, "Fetched successfully"))
})

export {
    doSomething,
    getAll
}
```

Rules:
- Always `return res` (chained `.status().json()` on separate lines)
- Always `const userId = req.user.id` (not `req.user?.id` unless truly optional)
- Named exports at bottom — never `export default`
- No unused imports, no `console.log` in production code (use `logger`)
- File cleanup in `finally` block when handling uploaded files

---

## Validation Pattern (Zod)

```js
// validators/thing.validator.js
import { z } from "zod"

export const thingValidator = z.object({
    name: z.string().min(1, "Name is required"),
    count: z.number().int().positive("Count must be positive"),
})
```

In controller, always use `.safeParse()` — never `.parse()`:
```js
const { data, error } = thingValidator.safeParse(req.body)
if (error) {
    throw new ApiError(400, error.issues.map(e => e.message).join(", "))
}
const { name, count } = data
```

For params validation:
```js
const { data, error } = idParamValidator.safeParse(req.params)
```

---

## MongoDB ID Validation

Inline helper in file or use `idParamValidator` from `validators/params.validator.js`:

```js
const isValidId = (id) => mongoose.Types.ObjectId.isValid(id)

// Usage
if (!isValidId(id)) {
    throw new ApiError(400, "Invalid Id")
}
```

Always validate before any DB query that takes an `_id`.

---

## Mongoose Model Pattern

```js
// models/thing.model.js
import mongoose, { Schema } from "mongoose"

const thingSchema = new Schema(
    {
        userId: {
            type: String,
            required: true,
        },
        name: {
            type: String,
            required: true,
        },
    },
    { timestamps: true }
)

export const Thing = mongoose.model("Thing", thingSchema)
```

- Named export, PascalCase model name
- Always `{ timestamps: true }` unless explicit reason not to
- `userId` is always `String` type in Mongoose (Prisma user ID is `Int`, stored as string in Mongo docs when referencing cross-DB)

---

## Mongoose Query Style

```js
// find with userId always
const data = await Thing.find({ userId })
const item = await Thing.findOne({ _id: id, userId })
const updated = await Thing.findOneAndUpdate(
    { _id: id, userId },
    { field: value },
    { returnDocument: "after" }   // NOT `new: true` for findOneAndUpdate
)
const deleted = await Thing.findOneAndDelete({ userId, _id: id })

// check existence before use
if (!data) {
    throw new ApiError(404, "Thing not found")
}
```

Note: some older code uses `new: true` — prefer `returnDocument: "after"` for new code.

---

## Prisma Pattern

```js
// lib/prisma.js — singleton
import { PrismaClient } from "@prisma/client"
const prisma = new PrismaClient()
export default prisma
```

Usage in controllers/services:
```js
import prisma from "../lib/prisma.js"

const user = await prisma.user.findUnique({ where: { id: userId } })
const created = await prisma.thing.create({ data: { userId, name } })
```

---

## Route Pattern

```js
// routes/thing.route.js
import { Router } from "express"
import { doSomething, getAll } from "../controllers/thing.controller.js"
import { verifyJWT } from "../middlewares/auth.middleware.js"

const router = Router()

router.use(verifyJWT)   // apply auth to all routes in file when all protected

router.post("/things", doSomething)
router.get("/things", getAll)
router.get("/things/:id", getById)
router.patch("/things/:id", updateThing)
router.delete("/things/:id", deleteThing)

export default router
```

In `app.js`, mount as:
```js
import thingRouter from "./routes/thing.route.js"
app.use("/api", thingRouter)
// or
app.use("/api/things", thingRouter)
```

---

## Auth Middleware

JWT stored in httpOnly cookie `accessToken`. Middleware sets `req.user`:
```js
// auth.middleware.js attaches req.user = { id, email, ... }
// Access in controller always as:
const userId = req.user.id
```

---

## Logger Usage

```js
import logger from "../logger/index.js"

logger.info("Something happened")
logger.error("Error context:", error)
logger.warn("Warning message", { key: value })
```

Never use `console.log` in controllers/services/workers. `console.log` only acceptable during active debugging, must be removed before commit.

---

## BullMQ Queue Pattern

```js
// services/queue.js
import { Queue } from "bullmq"
import redisClient from "../lib/redisClient.js"

const SomeQueue = new Queue("some-queue", { connection: redisClient })

export const addToQueue = async (data) => {
    await SomeQueue.add("job-name", data, {
        attempts: 3,
        backoff: { type: "exponential", delay: 2000 },
    })
}

export const closeSomeQueue = async () => SomeQueue.close()
```

```js
// worker/some.worker.js
import { Worker } from "bullmq"
import redisClient from "../lib/redisClient.js"
import logger from "../logger/index.js"

const someWorker = new Worker(
    "some-queue",
    async (job) => {
        const { data } = job
        // process...
    },
    { connection: redisClient }
)

someWorker.on("failed", (job, err) => {
    logger.error("Job failed all retries", { jobId: job?.id, error: err.message })
})
```

---

## Error Handling

Global error handler in `app.js`:
```js
app.use((err, req, res, next) => {
    const statusCode = err.statusCode || 500
    logger.error(err)
    res.status(statusCode).json({
        success: false,
        message: err.message || "Internal Server Error",
        ...(process.env.NODE_ENV === "development" && { stack: err.stack }),
    })
})
```

Controllers: always `throw new ApiError(statusCode, message)` — never `return res.status(xxx).json({ error: ... })` for errors (except legacy payment code which mixes patterns — new code uses ApiError).

---

## File/Folder Naming

| Type | Convention | Example |
|------|-----------|---------|
| Controllers | `name.controller.js` | `note.controller.js` |
| Routes | `name.route.js` | `note.route.js` |
| Models | `name.model.js` | `note.model.js` |
| Validators | `name.validator.js` | `note.validator.js` |
| Middlewares | `name.middleware.js` | `auth.middleware.js` |
| Services | `camelCase.js` | `vectordb.js`, `xpService.js` |
| Workers | `name.worker.js` | `payment.worker.js` |
| Queue | `name.queue.js` | `payment.queue.js` |
| Lib/clients | `camelCase.js` | `redisClient.js`, `prisma.js` |
| Constants | `name.constant.js` | `plansData.constant.js` |

---

## Response Shape

Success via `ApiResponse`:
```json
{ "statusCode": 200, "data": {...}, "message": "...", "success": true }
```

Error via global handler:
```json
{ "success": false, "message": "...", "stack": "..." }
```

Never return raw objects directly — always wrap in `new ApiResponse(...)`.

---

## File Upload Pattern

```js
const doUpload = asyncHandler(async (req, res) => {
    const localFile = req.files?.file?.[0]

    if (!localFile) {
        throw new ApiError(400, "No file uploaded")
    }

    let result
    try {
        result = await processFile(localFile)
    } finally {
        if (localFile?.path && fs.existsSync(localFile.path)) {
            fs.unlinkSync(localFile.path)
        }
    }

    return res
        .status(200)
        .json(new ApiResponse(200, result, "File processed"))
})
```

Always clean up temp files in `finally` block.

---

## Non-Fatal Operations

Wrap non-critical side effects in try-catch, log error, don't rethrow:
```js
try {
    await grantXP(req.user.id, "SOME_ACTION")
} catch (err) {
    logger.error("XP grant failed:", err.message) // non-fatal
}
```

Background cleanup (don't await, don't block response):
```js
Promise.all([
    Documents.findByIdAndDelete(docId).catch(e => logger.error("Cleanup failed:", e)),
    deleteVectors(userId, docId).catch(e => logger.error("Vector cleanup failed:", e))
])
```

---

## Environment / Config

```js
// configs/env.js — imported once at top of app.js
import "./configs/env.js"
```

Env-specific files: `.env.development`, `.env.production`. Access via `process.env.VAR_NAME`.

---

## Anti-Patterns to Avoid

- ❌ `export default` for controllers/validators (use named exports)
- ❌ `console.log` in non-debug code
- ❌ Raw `{ error: "..." }` responses — use `ApiError` + global handler
- ❌ `new: true` in `findOneAndUpdate` — use `returnDocument: "after"`
- ❌ Missing `.js` extension on local imports
- ❌ Destructuring `req.user?.id` when user is guaranteed (post-auth middleware)
- ❌ Forgetting to validate ObjectId before DB query
- ❌ `import { data }` from safeParse — destructure as `{ data, error }` then check error first
