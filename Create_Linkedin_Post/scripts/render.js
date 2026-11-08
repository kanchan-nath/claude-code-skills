#!/usr/bin/env node
// Usage: node render.js <post-dir> [--size 1080x1350] [--scale 2] [--wait 800] [--pdf]
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);
const valueFlags = ["--size", "--scale", "--wait"];
const postDir = args.find((a, i) => !a.startsWith("--") && !valueFlags.includes(args[i - 1]));
if (!postDir) { console.error("Usage: node render.js <post-dir> [--size WxH] [--scale N] [--wait ms] [--pdf]"); process.exit(1); }
const opt = (name, def) => { const i = args.indexOf(`--${name}`); return i > -1 ? args[i + 1] : def; };
const [W, H] = opt("size", "1080x1350").split("x").map(Number);
const scale = Number(opt("scale", 2));
const wait = Number(opt("wait", 800));
const makePdf = args.includes("--pdf");

(async () => {
  const slidesDir = path.resolve(postDir, "slides");
  const outDir = path.resolve(postDir, "exports");
  fs.mkdirSync(outDir, { recursive: true });
  const files = fs.readdirSync(slidesDir).filter((f) => f.endsWith(".html")).sort();
  if (!files.length) { console.error("No slide HTML files found in", slidesDir); process.exit(1); }

  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: scale });
  const page = await ctx.newPage();
  const pngs = [];

  for (const f of files) {
    await page.goto("file://" + path.join(slidesDir, f), { waitUntil: "networkidle" }).catch(() => {});
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.waitForTimeout(wait);
    const overflow = await page.evaluate(() => {
      const b = document.body;
      return b.scrollHeight > window.innerHeight + 2 || b.scrollWidth > window.innerWidth + 2;
    });
    if (overflow) console.warn(`WARNING: ${f} overflows ${W}x${H}. Shorten copy or split the slide.`);
    const out = path.join(outDir, f.replace(/\.html$/, ".png"));
    await page.screenshot({ path: out, type: "png", clip: { x: 0, y: 0, width: W, height: H } });
    console.log(`saved ${path.basename(out)} (${Math.round(fs.statSync(out).size / 1024)} KB)`);
    pngs.push(out);
  }

  if (makePdf) {
    const html = `<html><body style="margin:0">${pngs
      .map((p) => `<img src="file://${p}" style="display:block;width:${W}px;height:${H}px;page-break-after:always">`)
      .join("")}</body></html>`;
    const tmp = path.join(outDir, "_pdf.html");
    fs.writeFileSync(tmp, html);
    const pdfPage = await ctx.newPage();
    await pdfPage.goto("file://" + tmp);
    await pdfPage.pdf({ path: path.join(outDir, "carousel.pdf"), width: `${W}px`, height: `${H}px`, printBackground: true });
    fs.unlinkSync(tmp);
    console.log("saved carousel.pdf");
  }

  await browser.close();
})();
