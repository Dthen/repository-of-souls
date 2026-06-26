import jellyfish

existing = ['cadell', 'calden']

def levenshtein(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            curr.append(min(curr[j] + 1, prev[j+1] + 1, prev[j] + (c1 != c2)))
        prev = curr
    return prev[-1]

def jaro_winkler(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    if s1 == s2:
        return 1.0
    l1, l2 = len(s1), len(s2)
    md = max(l1, l2) // 2 - 1
    if md < 0: md = 0
    s1_m = [False]*l1; s2_m = [False]*l2
    matches = 0; trans = 0
    for i in range(l1):
        start = max(0, i - md)
        end = min(i + md + 1, l2)
        for j in range(start, end):
            if s2_m[j] or s1[i] != s2[j]: continue
            s1_m[i] = True; s2_m[j] = True; matches += 1; break
    if matches == 0: return 0.0
    k = 0
    for i in range(l1):
        if not s1_m[i]: continue
        while not s2_m[k]: k += 1
        if s1[i] != s2[k]: trans += 1
        k += 1
    jaro = (matches/l1 + matches/l2 + (matches - trans/2)/matches) / 3
    pref = 0
    for i in range(min(4, l1, l2)):
        if s1[i] == s2[i]: pref += 1
        else: break
    return jaro + pref * 0.1 * (1 - jaro)

if __name__ == '__main__':
    import sys
    candidates = sys.argv[1:] if len(sys.argv) > 1 else []
    if not candidates:
        print(f"Usage: python {__file__} <name1> [name2 ...]")
        print(f"Current souls: {existing}")
        sys.exit(0)

    header = f"{'Cand':10} {'Exist':10} {'Lev':4} {'NLev':6} {'JW':6} {'Result':10}"
    print('=' * len(header))
    print(header)
    print('=' * len(header))

    for cand in candidates:
        for exist in existing:
            lev = levenshtein(cand, exist)
            nlev = lev / max(len(cand), len(exist))
            jw = jaro_winkler(cand, exist)
            dm1 = jellyfish.metaphone(cand)
            dm2 = jellyfish.metaphone(exist)
            
            coll = False
            fl = []
            ml = max(len(cand), len(exist))
            if ml <= 6 and lev <= 2: coll = True; fl.append('LEV<=2')
            elif ml <= 10 and lev <= 3: coll = True; fl.append('LEV<=3')
            if nlev < 0.25: coll = True; fl.append('NORM')
            if jw >= 0.90: coll = True; fl.append('JW')
            if dm1 == dm2: coll = True; fl.append('DM')
            
            result = 'COLLISION' if coll else 'SAFE'
            print(f'{cand:10} {exist:10} {lev:4} {nlev:.3f}  {jw:.3f} {result:10}')
            if fl:
                print(f'{"":10} {"":10} {"":4} {"":6} {"":6} Flags: {fl}')
        print()
