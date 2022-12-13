# import our helpers
from utils import load, show, day

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()

INPUT_GROUPS = [TEXT[n:n+2] for n in range(0,len(TEXT),3)]

DEBUG = False
if not DEBUG: # Hide prints
    print = lambda *a, **kw: None

######## Part 1 ##########

def rcmp(sig1, sig2, indent=0):
    """recursively compare nested integer "signal" lists"""
    indent_text = ' ' * indent * 2
    res = None
    try:
        for a,b in zip(sig1, sig2, strict=True):
            print(f"{indent_text}- Compare {a} vs {b}")
            if isinstance(a, int) and isinstance(b, int):
                if a > b:
                    print(f"{indent_text}  - Right side is smaller, so inputs are not in the right order")
                    return False
                elif b > a:
                    print(f"{indent_text}  - Left side is smaller, so inputs are in the right order")
                    return True
            elif isinstance(a, int):
                print(f"{indent_text}  - Mixed types; convert left to [{a}] and retry comparison")
                res = rcmp([a], b, indent+1)
            elif isinstance(b, int):
                print(f"{indent_text}  - Mixed types; convert right to [{b}] and retry comparison")
                res = rcmp(a, [b], indent+1)
            else:
                res = rcmp(a,b,indent+1)
            if res is not None:
                return res
    except:
        res = len(sig1) < len(sig2)
        if res:
            print(f"{indent_text}  - Left side ran out of items, so inputs are in the right order")
        else:
            print(f"{indent_text} - Right side ran out of items, so inputs are not in the right order")
        return res

def p1(expect=5682):
    tot = 0
    pair = 1
    for sig1,sig2 in INPUT_GROUPS:
        print(f"== Pair {pair} ==\nCompare {sig1} vs {sig2}")
        if rcmp(eval(sig1), eval(sig2)):
            tot += pair
        pair += 1
    return tot

######## Part 2 ##########
class Signal:
    def __init__(self,txt):
        self.sig = eval(txt)

    def __lt__(self, signal):
        """declaring this enables sorted() to compare objects"""
        return rcmp(self.sig, signal.sig)

def p2(expect=20304):
    div1_signal = "[[2]]"
    div2_signal = "[[6]]"
    signals = [Signal(sigtxt) for sigtxt in TEXT+[div1_signal, div2_signal] if sigtxt]
    ordered=[str(signal.sig) for signal in sorted(signals)]
    div1_index = ordered.index(div1_signal) + 1
    div2_index = ordered.index(div2_signal) + 1
    return div1_index * div2_index

if __name__ == "__main__":
    show(p1, p2)
