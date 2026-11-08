#!/usr/bin/env python3
"""
humanizer_lint.py - mechanical checks for AI-sounding LinkedIn drafts.

Usage:
    python humanizer_lint.py draft.txt          # human-readable report
    python humanizer_lint.py draft.txt --json   # JSON report
    cat draft.txt | python humanizer_lint.py -  # read from stdin

Exit code: 0 = no HARD flags, 1 = at least one HARD flag.
HARD flags must be fixed. SOFT flags must be reviewed.
This script cannot judge voice or truthfulness; the reviewer agent does that.
"""
import argparse
import json
import re
import statistics
import sys

HARD_PHRASES = [
    "in today's", "in the ever-evolving", "fast-paced world", "game-changer",
    "game changer", "unlock the", "unleash", "delve", "tapestry",
    "testament to", "at the end of the day", "let that sink in",
    "read that again", "here's the kicker", "the catch is", "here is the catch",
    "here's the catch", "nobody is talking about", "no one is talking about",
    "think about that", "the real story", "the lesson is simple",
    "buckle up", "dive in", "dive into", "thrilled to", "excited to announce",
    "excited to share", "i'm humbled", "humbled to", "proud to announce",
    "the uncomfortable truth", "most people are missing",
    "this is not about", "it's not just", "it is not just",
]
SOFT_PHRASES = [
    "journey", "leverage", "seamless", "robust", "cutting-edge", "revolutionize",
    "transformative", "landscape", "navigate", "quietly", "hot take",
    "unpopular opinion", "here's why", "thoughts?", "agree?", "let's connect",
    "the scary part", "stood out", "game plan", "moving forward",
]

# Specific antithesis / contrast patterns that read as AI (HARD).
ANTITHESIS_HARD = [
    r"\b(?:that'?s|that is|this is|it'?s|it is) not\b[^.!?\n]{0,60}[.;:]\s*(?:that'?s|that is|this is|it'?s|it is)\b",
    r"\b(?:does not|doesn'?t|do not|don'?t) need\b[^.!?\n]{0,60}[.;:]\s*(?:it|they) needs?\b",
    r"\bit (?:reads|looks|sounds|feels) like\b[^.!?\n]{0,70}[.;:]\s*it(?:'s| is) (?:actually|really)\b",
    r"\bnot about\b[^.!?\n]{0,70}[,;:.]\s*(?:it'?s|it is|but) (?:about)?",
    r"\b(?:isn'?t|is not|aren'?t|are not)\b[^.!?\n]{0,60}[.;:,]\s*(?:it'?s|it is|they'?re|they are)\b",
]
# Broader contrast guess (SOFT, may be a false alarm).
ANTITHESIS_SOFT = [
    r"\b(?:not|n'?t|never)\b[^.!?\n]{0,60}[.;:,]\s*(?:it|that|this|they|he|she)(?:'s|'re| is| are| needs?| was)\b",
]
GENERIC_OPENERS = [
    r"^in today", r"^i'?m (?:excited|thrilled|happy|proud|humbled)", r"^have you ever",
    r"^did you know", r"^let me tell", r"^here'?s the thing", r"^unpopular opinion",
    r"^hot take", r"^imagine ", r"^what if ", r"^why ",
]
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2764\uFE0F]")


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p and p.strip()]


def wc(s):
    return len(re.findall(r"\b[\w'’-]+\b", s))


def analyze(text):
    hard, soft = [], []
    text = text.strip()
    low = text.lower()
    lines = [l for l in text.splitlines() if l.strip()]
    first_line = lines[0].strip() if lines else ""
    # The hook is the first line, capped at its first two sentences
    # (a long single-line paste would otherwise count as one giant hook).
    first = " ".join(re.split(r"(?<=[.!?])\s+", first_line)[:2])
    sentences = split_sentences(text)
    lengths = [wc(s) for s in sentences] or [0]

    m = {
        "words": wc(text),
        "sentences": len(sentences),
        "avg_sentence_words": round(statistics.mean(lengths), 1),
        "burstiness": round(statistics.pstdev(lengths) / statistics.mean(lengths), 2) if statistics.mean(lengths) else 0,
        "hook": first,
        "hook_words": wc(first),
        "hook_chars": len(first),
        "emoji": len(EMOJI_RE.findall(text)),
        "hashtags": len(re.findall(r"(?<!\w)#\w+", text)),
        "em_dashes": text.count("\u2014") + text.count("\u2013"),
        "semicolons": text.count(";"),
        "arrows": text.count("\u2192"),
        "exclamations": text.count("!"),
    }

    # HARD checks
    if m["em_dashes"]:
        hard.append(f"{m['em_dashes']} em/en dash(es). Replace with a period or comma.")
    if m["semicolons"]:
        hard.append(f"{m['semicolons']} semicolon(s). Split into two sentences.")
    for p in HARD_PHRASES:
        if p in low:
            hard.append(f"Banned AI phrase: \"{p}\". Delete it and say the plain thing.")
    for pat in ANTITHESIS_HARD:
        for mt in re.finditer(pat, low):
            hard.append(f"Antithesis pattern: \"{text[mt.start():mt.end()].strip()}\". Keep only the plain claim.")
            break
    if re.search(r"https?://|www\.", low):
        hard.append("URL in the body. Use \"link in comments\" instead.")
    if re.search(r"\*\*|^#{1,6}\s|__", text, re.M):
        hard.append("Markdown (bold/headers) found. LinkedIn renders plain text only.")
    if first:
        for pat in GENERIC_OPENERS:
            if re.search(pat, first.lower()):
                hard.append(f"Generic/throat-clearing hook: \"{first[:60]}\".")
                break
    if m["hook_chars"] > 200:
        hard.append(f"Hook is {m['hook_chars']} characters. It must work before \"see more\".")

    # SOFT checks
    for p in SOFT_PHRASES:
        if p in low:
            soft.append(f"Watch phrase: \"{p}\".")
    for pat in ANTITHESIS_SOFT:
        mt = re.search(pat, low)
        if mt:
            soft.append(f"Possible contrast pattern: \"{text[mt.start():mt.end()].strip()}\". Check it is not an X-not-Y move.")
            break
    if m["hook_words"] > 15:
        soft.append(f"Hook is {m['hook_words']} words. Aim for 15 or fewer.")
    if m["hook_chars"] > 140 and m["hook_chars"] <= 200:
        soft.append(f"Hook is {m['hook_chars']} characters. Aim for under 140.")
    if first.endswith("?"):
        soft.append("Hook is a question. Prefer a statement with a concrete anchor.")
    if m["sentences"] >= 5 and m["burstiness"] < 0.5:
        soft.append(f"Sentence lengths are too even (burstiness {m['burstiness']}). Add a fragment and a run-on.")
    triplets = len(re.findall(r"\b[\w'’-]+, [\w'’-]+,? (?:and|or) [\w'’-]+", text))
    if triplets >= 2:
        soft.append(f"{triplets} rule-of-three lists. Cut to the one that matters.")
    if m["emoji"] > 3:
        soft.append(f"{m['emoji']} emoji. Use 0 to 2.")
    if m["hashtags"] > 3:
        soft.append(f"{m['hashtags']} hashtags. Use 0 to 3, at the end only.")
    if m["arrows"] > 4:
        soft.append(f"{m['arrows']} arrow bullets. Max 4, and only for genuine lists.")
    if m["exclamations"] > 3:
        soft.append(f"{m['exclamations']} exclamation marks. Too many.")
    if m["words"] < 15 or m["words"] > 250:
        soft.append(f"{m['words']} words. Outside the usual 20 to 250 range.")
    para_blocks = [b for b in re.split(r"\n\s*\n", text) if b.strip()]
    if any(len(b.splitlines()) > 4 for b in para_blocks):
        soft.append("A paragraph is longer than 4 lines. Break it up.")
    if len(para_blocks) <= 1 and m["words"] > 60:
        soft.append("No paragraph breaks. Add blank lines between short paragraphs.")
    last = sentences[-1] if sentences else ""
    if last and wc(last) <= 8 and re.search(r"\b(is|are|was|isn't|not)\b", last.lower()) and not last.endswith("?"):
        soft.append(f"Closer looks like a tidy aphorism: \"{last}\". Prefer a plain question, blunt line, or stop earlier.")
    if re.search(r"thoughts\?\s*$", low):
        soft.append("Ends with \"Thoughts?\" filler.")
    alpha_starts = [s for s in sentences if s[0].isalpha()]
    if len(alpha_starts) >= 3 and sum(1 for s in alpha_starts if s[0].islower()) / len(alpha_starts) > 0.5:
        soft.append("Mostly lowercase sentence starts. Use normal capitalization.")

    return {"metrics": m, "hard_flags": hard, "soft_flags": soft}


def main():
    ap = argparse.ArgumentParser(description="Lint a LinkedIn draft for AI-sounding patterns.")
    ap.add_argument("path", help="draft text file, or - for stdin")
    ap.add_argument("--json", action="store_true", help="print JSON instead of text")
    a = ap.parse_args()
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    r = analyze(text)
    if a.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        m = r["metrics"]
        print(f"Words: {m['words']} | Sentences: {m['sentences']} | Avg sentence: {m['avg_sentence_words']} words | Burstiness: {m['burstiness']}")
        print(f"Hook ({m['hook_words']} words, {m['hook_chars']} chars): {m['hook']}")
        print(f"Emoji: {m['emoji']} | Hashtags: {m['hashtags']} | Arrows: {m['arrows']}")
        print(f"\nHARD flags ({len(r['hard_flags'])}):")
        for f in r["hard_flags"] or ["none"]:
            print(f"  - {f}")
        print(f"\nSOFT flags ({len(r['soft_flags'])}):")
        for f in r["soft_flags"] or ["none"]:
            print(f"  - {f}")
    sys.exit(1 if r["hard_flags"] else 0)


if __name__ == "__main__":
    main()
