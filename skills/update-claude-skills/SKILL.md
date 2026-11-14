---
name: update-claude-skills
description: "Automatically ingests any new or updated AI agent skill into Kanchan's GitHub repository https://github.com/kanchan-nath/claude-code-skills. Trigger this skill whenever Kanchan attaches or shares a skill file (SKILL.md, .skill zip archive, or folder), asks to 'update skill', 'add this skill to my repo', 'upload skill to github', or invokes '/update-claude-skills'. Handles extracting/placing files into skills/<skill-name>/, running sync_skills.py, updating README.md and skills.json, running CI validation, and pushing to GitHub origin main."
---

# Update Claude Skills

Autonomous skill for syncing, updating, and publishing agent skills to [kanchan-nath/claude-code-skills](https://github.com/kanchan-nath/claude-code-skills).

## Trigger Conditions
Activate whenever:
- User attaches or references a `.md`, `.skill`, or folder containing a skill.
- User says "update this skill in my repo", "add this skill to github", "update claude skills", or `/update-claude-skills`.
- A modified skill needs to be published to `main`.

---

## Standard Workflow

### Step 1: Locate Target Repository
Working repository path:
`/Users/kanchannath/Coding/claude-code-skills`

Ensure repository is on `main` and clean:
```bash
cd /Users/kanchannath/Coding/claude-code-skills && git pull origin main
```

### Step 2: Ingest the Attached Skill
Identify skill name from YAML frontmatter (`name: <skill-name>`):
- **If single markdown file (`*SKILL*.md`):**
  Create destination folder `skills/<skill-name>/` and copy file as `skills/<skill-name>/SKILL.md`.
- **If `.skill` archive (zip):**
  Unzip into `skills/<skill-name>/` preserving references, assets, and scripts.
- **If directory:**
  Copy entire directory into `skills/<skill-name>/`.

### Step 3: Run Deterministic Sync Script
Execute the repository sync tool to rebuild `skills.json`, update `install.sh`, and update the badge count:
```bash
python3 /Users/kanchannath/Coding/claude-code-skills/scripts/sync_skills.py
```

### Step 4: Update README Catalog Table (if new skill)
If the skill is newly added, add a row to the Skills Directory table in `README.md`:
```markdown
| [`<skill-name>`](skills/<skill-name>/SKILL.md) | <Category> | `<triggers>` | <Short summary> |
```

### Step 5: Validate
Run the validation check:
```bash
python3 -c "
import os, glob, json

skills = [os.path.basename(d) for d in sorted(glob.glob('skills/*')) if os.path.isdir(d)]
for s in skills:
    md = f'skills/{s}/SKILL.md'
    assert os.path.exists(md), f'Missing {md}'
    with open(md) as f:
        c = f.read()
    assert c.startswith('---') and 'name:' in c and 'description:' in c
assert os.path.exists('skills.json')
print('✓ Validation passed.')
"
```

### Step 6: Commit and Push to GitHub
Stage all changes, create a clean Conventional Commit message, and push directly:
```bash
cd /Users/kanchannath/Coding/claude-code-skills
git add -A
git commit -m "feat(skills): update <skill-name> skill"
git push origin main
```

### Step 7: Report Terse Summary to User
Report:
- Updated / added skill name
- Verified file paths
- Live GitHub commit URL
