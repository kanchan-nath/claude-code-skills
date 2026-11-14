#!/usr/bin/env python3
"""
Sync Skills: Deterministic registry & README builder for claude-code-skills repo.
Scans skills/*/SKILL.md, synchronizes skills.json, updates install.sh list, and validates all skills.
"""

import os
import glob
import json
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
SKILLS_JSON = os.path.join(REPO_ROOT, "skills.json")
INSTALL_SH = os.path.join(REPO_ROOT, "install.sh")
README_MD = os.path.join(REPO_ROOT, "README.md")

CATEGORY_MAP = {
    "cold-email": "Outreach",
    "content-ideas": "Content & Media",
    "create-linkedin-post": "Social Publishing",
    "dsa": "Software Development",
    "hashnode": "Technical Writing",
    "job": "Career & Jobs",
    "linkedin-humanizer": "Content & Review",
    "linkedin-orchestrator": "Social Publishing",
    "linkedin-post-image": "Media Design",
    "motion-prompt-director": "AI Video & Motion",
    "referral": "Career & Outreach",
    "seo": "Web Development",
    "shorts-script-writer": "Video & Scriptwriting",
    "sparke-codestyle": "Backend Architecture",
    "update-claude-skills": "Repo & Skill Ops"
}

def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    raw_fm = parts[1].strip()
    body = parts[2].strip()
    
    data = {}
    lines = raw_fm.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" in line and not line.startswith(" ") and not line.startswith("\t"):
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val in [">", "|", ""]:
                # Multi-line block
                desc_lines = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t") or not lines[i].strip()):
                    if lines[i].strip():
                        desc_lines.append(lines[i].strip())
                    i += 1
                data[key] = " ".join(desc_lines)
                continue
            else:
                data[key] = val.strip("\"'")
        i += 1
    return data, body

def main():
    skill_dirs = sorted([d for d in glob.glob(os.path.join(SKILLS_DIR, "*")) if os.path.isdir(d)])
    skills = []

    for d in skill_dirs:
        skill_name = os.path.basename(d)
        skill_md = os.path.join(d, "SKILL.md")
        if not os.path.exists(skill_md):
            print(f"Warning: {skill_name} missing SKILL.md, skipping.")
            continue
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        name = fm.get("name", skill_name)
        desc = fm.get("description", "")
        category = CATEGORY_MAP.get(skill_name, "General")
        
        # Extract triggers from description or common patterns
        triggers = []
        if "/" in desc:
            slash_cmds = re.findall(r"(/[a-zA-Z0-9_-]+)", desc)
            triggers.extend(slash_cmds)
        quoted = re.findall(r'["\']([^"\']{3,35})["\']', desc)
        if quoted:
            triggers.extend(quoted[:2])
        if not triggers:
            triggers = [f'"{skill_name}"']
        
        trigger_str = ", ".join(f"`{t}`" for t in list(dict.fromkeys(triggers))[:3])

        skills.append({
            "name": skill_name,
            "category": category,
            "triggers": trigger_str,
            "description": desc,
            "path": f"skills/{skill_name}/SKILL.md"
        })

    # 1. Update skills.json
    registry = {
        "repository": "https://github.com/kanchan-nath/claude-code-skills",
        "description": "Production AI Agent Skills for Claude Code, Antigravity, OpenHands, and Agentic Workflows.",
        "version": "1.0.0",
        "total_skills": len(skills),
        "skills": skills
    }
    with open(SKILLS_JSON, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    print(f"✓ Updated {SKILLS_JSON} ({len(skills)} skills)")

    # 2. Update install.sh AVAILABLE_SKILLS
    if os.path.exists(INSTALL_SH):
        with open(INSTALL_SH, "r", encoding="utf-8") as f:
            install_content = f.read()
        skills_bash_list = "\n".join(f'  "{s["name"]}"' for s in skills)
        new_install_content = re.sub(
            r'AVAILABLE_SKILLS=\([\s\S]*?\)',
            f'AVAILABLE_SKILLS=(\n{skills_bash_list}\n)',
            install_content
        )
        with open(INSTALL_SH, "w", encoding="utf-8") as f:
            f.write(new_install_content)
        print(f"✓ Updated {INSTALL_SH}")

    # 3. Update README badge count
    if os.path.exists(README_MD):
        with open(README_MD, "r", encoding="utf-8") as f:
            readme_content = f.read()
        readme_content = re.sub(
            r'Skills-\d+%20Available',
            f'Skills-{len(skills)}%20Available',
            readme_content
        )
        with open(README_MD, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"✓ Updated {README_MD} badge ({len(skills)} available)")

    print(f"✓ Sync complete: {len(skills)} skills verified.")

if __name__ == "__main__":
    main()
