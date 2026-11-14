#!/usr/bin/env python3
"""Draw motion techniques at random so every film stops converging on the same fade-up, push-in and end card.

Adapted from the Cinetic skill's pick.py (MIT, Leonxlnx/cinetic). Works on assets/techniques.json.

Usage:
  python3 scripts/pick_techniques.py --format launch --energy high --seconds 30
  python3 scripts/pick_techniques.py --format loop --energy calm --seed 41
  python3 scripts/pick_techniques.py --category transition --n 3 --format launch
  python3 scripts/pick_techniques.py --category logo_and_end_card --exclude le-hard-cut-lockup
  python3 scripts/pick_techniques.py --list [--category camera]
  python3 scripts/pick_techniques.py --show tr-mask-wipe-swap

Formats: launch, feature, loop, sting, walkthrough, vertical.  Energy: calm, medium, high.
A plan holds about one technique per 2.5 s. Entries that rely on a banned look are shown with their ban-safe variant.
"""
import argparse, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.normpath(os.path.join(HERE, '..', 'assets', 'techniques.json'))
ROLE_W = {'workhorse': 3.0, 'accent': 2.0, 'signature': 1.0}
ORDER = {
 'launch': ['opening_hook','transition','typography_motion','product_demo','ui_choreography','logo_and_end_card','camera','transition','data_and_numbers','micro_interaction','color_and_light','pacing_structure'],
 'feature': ['product_demo','ui_choreography','opening_hook','transition','micro_interaction','typography_motion','logo_and_end_card','data_and_numbers','camera','color_and_light'],
 'loop': ['ui_choreography','product_demo','micro_interaction','typography_motion','transition','camera','pacing_structure','color_and_light'],
 'sting': ['logo_and_end_card','opening_hook','typography_motion','micro_interaction','camera','texture_and_finish'],
 'walkthrough': ['product_demo','ui_choreography','opening_hook','transition','micro_interaction','camera','typography_motion','logo_and_end_card','ui_choreography','product_demo','transition','pacing_structure'],
 'vertical': ['opening_hook','product_demo','ui_choreography','typography_motion','transition','logo_and_end_card','micro_interaction','data_and_numbers','camera','color_and_light'],
}
DEFAULT_SECONDS = {'launch':30,'feature':15,'loop':10,'sting':6,'walkthrough':45,'vertical':15}
MIN_PICKS = {'launch':6,'feature':5,'loop':4,'sting':4,'walkthrough':6,'vertical':5}

def load():
    with open(LIB, encoding='utf-8') as f:
        return json.load(f)['techniques']

def weight(e, energy):
    w = ROLE_W[e['role']] * min(3.0, 1.0 + float(e.get('evidence') or 0) / 4.0)
    if energy:
        w *= 1.0 if e['energy'] == energy else (0.7 if e['energy'] == 'any' else 0.25)
    return w

def fits(e, fmt):
    return not fmt or 'any' in e['formats'] or fmt in e['formats']

def show(e, brand_supplied=False):
    print(f"- {e['id']}  [{e['category']} | {e['energy']} | {e['role']}]  {e['name']}")
    print(f"    what: {e['summary']}")
    if not e['ban_safe'] and not brand_supplied:
        print(f"    SAFE VARIANT (original uses {', '.join(e['bans'])}): {e['ban_safe_variant']}")
    print(f"    use when: {e['use_when']}")
    print(f"    avoid when: {e['avoid_when']}")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--format', choices=list(ORDER)); ap.add_argument('--energy', choices=['calm','medium','high'])
    ap.add_argument('--seconds', type=float); ap.add_argument('--seed', type=int)
    ap.add_argument('--category'); ap.add_argument('--n', type=int)
    ap.add_argument('--exclude', action='append', default=[])
    ap.add_argument('--list', action='store_true'); ap.add_argument('--show')
    ap.add_argument('--brand-supplied', action='store_true', help='the brand owns a banned look; show original recipes')
    ap.add_argument('--json', help='also write the draw to this file')
    a = ap.parse_args()
    lib = load()
    if a.show:
        e = next((x for x in lib if x['id'] == a.show), None)
        if not e: sys.exit(f'no such id: {a.show}')
        show(e, a.brand_supplied); return
    if a.list:
        for e in lib:
            if not a.category or e['category'] == a.category:
                print(f"{e['id']:44} {e['energy']:7} {','.join(e['formats']):38} {e['name']}")
        return
    seed = a.seed if a.seed is not None else random.randrange(1, 10**6)
    rng = random.Random(seed)
    taken = set(a.exclude)
    picks = []
    def draw(cat, k, sig_left):
        pool = [e for e in lib if e['category'] == cat and fits(e, a.format) and e['id'] not in taken]
        out = []
        while len(out) < k and pool:
            if sig_left <= 0: pool = [e for e in pool if e['role'] != 'signature']
            if not pool: break
            e = rng.choices(pool, weights=[weight(x, a.energy) for x in pool], k=1)[0]
            out.append(e); taken.add(e['id']); pool = [x for x in pool if x['id'] != e['id']]
            if e['role'] == 'signature': sig_left -= 1
        return out, sig_left
    if a.category:
        picks, _ = draw(a.category, a.n or 3, 99)
    else:
        if not a.format: sys.exit('give --format (or --category)')
        secs = a.seconds or DEFAULT_SECONDS[a.format]
        n = max(MIN_PICKS[a.format], min(len(ORDER[a.format]), round(secs / 2.5)))
        sig = 2 if n >= 10 else 1
        for cat in ORDER[a.format][:n]:
            got, sig = draw(cat, 1, sig); picks += got
    print(f"# draw: --seed {seed} --format {a.format} --energy {a.energy}  ({len(picks)} techniques)")
    print("# Build the picks the concept can carry, retold in THIS product's objects. Reroll at most twice (--exclude id), or drop with a written reason.\n")
    for e in picks: show(e, a.brand_supplied)
    if a.json:
        json.dump({'seed': seed, 'picks': [e['id'] for e in picks]}, open(a.json, 'w'), indent=1)

if __name__ == '__main__':
    main()
