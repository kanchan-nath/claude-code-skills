#!/usr/bin/env python3
"""
Fast Intelligent Skill Finder & Router for Claude Skills library.
Searches 425+ skills, commands, and agents to find the most powerful and useful skill for any task.
"""

import sys
import os
import json
import re
import math
from pathlib import Path

SKILLS_DIR = Path.home() / ".gemini" / "claude-skills"
INDEX_FILE = SKILLS_DIR / ".gemini" / "skills-index.json"
SKILLS_SYMLINKS = SKILLS_DIR / ".gemini" / "skills"

STOP_WORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both",
    "but", "by", "can", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does",
    "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had",
    "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her",
    "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll",
    "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me",
    "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only",
    "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's",
    "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd",
    "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up",
    "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what",
    "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why",
    "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your",
    "yours", "yourself", "yourselves", "want", "like", "need", "make", "help", "please", "task"
}

ACRONYMS = {
    "tdd": ["test", "driven", "development", "red", "green", "refactor"],
    "bdd": ["behavior", "driven", "development"],
    "seo": ["search", "engine", "optimization", "ranking", "google"],
    "aeo": ["answer", "engine", "optimization"],
    "cro": ["conversion", "rate", "optimization"],
    "prd": ["product", "requirements", "document", "spec"],
    "dcf": ["discounted", "cash", "flow", "valuation"],
    "okr": ["objectives", "key", "results"],
    "soc2": ["soc", "security", "compliance", "audit"],
    "rag": ["retrieval", "augmented", "generation", "embeddings"],
    "llm": ["large", "language", "model", "ai", "prompt"],
    "api": ["rest", "endpoint", "graphql", "interface"],
    "cicd": ["continuous", "integration", "deployment", "pipeline"],
    "hig": ["human", "interface", "guidelines", "apple", "ios"],
    "ux": ["user", "experience", "design", "research"],
    "ui": ["user", "interface", "frontend", "component"],
    "qa": ["quality", "assurance", "testing", "validation"]
}

def stem(word: str) -> str:
    w = word.lower()
    for suffix in ("ing", "tion", "ed", "ies", "es", "s", "er", "ment", "able"):
        if w.endswith(suffix) and len(w) - len(suffix) >= 3:
            return w[:-len(suffix)]
    return w

def tokenize(text: str) -> list[str]:
    words = re.findall(r'[a-zA-Z0-9_\-]+', text.lower())
    tokens = set()
    for w in words:
        parts = re.split(r'[-_]', w)
        for p in parts:
            if len(p) > 1 and p not in STOP_WORDS:
                tokens.add(p)
                tokens.add(stem(p))
                if p in ACRONYMS:
                    tokens.update(ACRONYMS[p])
        if len(w) > 1 and w not in STOP_WORDS:
            tokens.add(w)
            tokens.add(stem(w))
            if w in ACRONYMS:
                tokens.update(ACRONYMS[w])

    # Check for multi-word acronym matches like "test driven development" -> "tdd"
    text_lower = text.lower()
    for acr, words_list in ACRONYMS.items():
        if all(wl in text_lower for wl in words_list[:3]):
            tokens.add(acr)

    return list(tokens)

def load_index():
    if not INDEX_FILE.exists():
        return None
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_skills(query: str, top_k: int = 5):
    index = load_index()
    if not index:
        return []

    q_tokens = tokenize(query)
    if not q_tokens:
        return []

    scored_skills = []
    query_lower = query.strip().lower().lstrip("/")

    for item in index.get("skills", []):
        name = item.get("name", "")
        desc = item.get("description", "")
        cat = item.get("category", "")
        
        name_lower = name.lower()
        desc_lower = desc.lower()
        cat_lower = cat.lower()

        score = 0.0

        # Exact match
        if query_lower == name_lower:
            score += 100.0
        elif query_lower in name_lower:
            score += 50.0

        # Token matches
        name_tokens = tokenize(name)
        desc_tokens = tokenize(desc)
        cat_tokens = tokenize(cat)

        for qt in q_tokens:
            # Match in name
            if qt == name_lower:
                score += 30.0
            elif qt in name_tokens:
                score += 15.0
            elif any(qt in nt for nt in name_tokens):
                score += 8.0

            # Match in category
            if qt in cat_tokens:
                score += 6.0

            # Match in description
            desc_count = desc_tokens.count(qt)
            if desc_count > 0:
                score += min(10.0, desc_count * 3.0)
            elif any(qt in dt for dt in desc_tokens):
                score += 1.5

        if score > 0:
            skill_path = SKILLS_SYMLINKS / name
            skill_md = skill_path / "SKILL.md" if skill_path.is_dir() else skill_path
            
            # Check for scripts directory
            scripts_dir = skill_path / "scripts" if skill_path.is_dir() else None
            available_scripts = []
            if scripts_dir and scripts_dir.exists():
                available_scripts = [f.name for f in scripts_dir.iterdir() if f.is_file() and not f.name.startswith(".")]

            scored_skills.append({
                "name": name,
                "category": cat,
                "description": desc,
                "score": round(score, 2),
                "path": str(skill_md),
                "has_skill_md": skill_md.exists(),
                "scripts": available_scripts
            })

    scored_skills.sort(key=lambda x: x["score"], reverse=True)
    return scored_skills[:top_k]

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Find the best Claude Skill for a task or command")
    parser.add_argument("query", nargs="*", help="The task, command, or problem description")
    parser.add_argument("-k", "--top", type=int, default=5, help="Number of results to return")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--info", metavar="SKILL_NAME", help="Show full details and instructions of a specific skill")
    parser.add_argument("--categories", action="store_true", help="List all available skill categories")
    args = parser.parse_args()

    if args.categories:
        index = load_index()
        if not index:
            print("Skills index not found.")
            sys.exit(1)
        print(f"Categories ({len(index['categories'])}):")
        for cat, meta in sorted(index["categories"].items()):
            print(f"  • {cat.ljust(22)} ({meta['count']} skills)")
        return

    if args.info:
        skill_name = args.info.strip()
        skill_path = SKILLS_SYMLINKS / skill_name
        skill_md = skill_path / "SKILL.md" if (skill_path / "SKILL.md").exists() else skill_path
        if not skill_md.exists():
            print(f"Skill '{skill_name}' not found at {skill_md}")
            sys.exit(1)
        print(f"=== Skill: {skill_name} ===")
        print(f"Location: {skill_md}\n")
        print(skill_md.read_text(encoding="utf-8"))
        return

    query_str = " ".join(args.query).strip()
    if not query_str:
        print("Usage: find-skill <task, query, or command> [options]")
        print("Example: find-skill 'audit frontend performance' or find-skill tdd")
        sys.exit(0)

    results = search_skills(query_str, top_k=args.top)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    if not results:
        print(f"No specific skill found matching '{query_str}'.")
        return

    print(f"\n🎯 Top skills for: \"{query_str}\"\n" + "="*60)
    for i, res in enumerate(results, 1):
        print(f"{i}. [{res['name']}] (Category: {res['category']} | Match: {res['score']})")
        print(f"   Summary: {res['description']}")
        print(f"   Path: {res['path']}")
        if res["scripts"]:
            print(f"   CLI Tools: {', '.join(res['scripts'])}")
        print()

if __name__ == "__main__":
    main()
