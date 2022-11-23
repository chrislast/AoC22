from utils import TESTS
from pathlib import Path
import traceback
import importlib

REPORT = """
###### Totals #######

EXECUTED = {}
PASSED = {}
FAILED = {}
ERRORS = {}
SKIPPED = {}
"""

def test():
    # import each module and run it's tests
    for n in range(1,26):
        module_name = f"day{n}"
        if (Path(__file__).parent / f"{module_name}.py").is_file():
            try:
                print(f"\n####### Day {n} #######\n")
                mod = importlib.import_module(module_name)
                mod.main()
            except:
                TESTS.ERRORS += 1
                traceback.print_exc()

    # print test report
    print(REPORT.format(
        TESTS.EXECUTED,
        TESTS.PASSED,
        TESTS.FAILED,
        TESTS.ERRORS,
        TESTS.SKIPPED))

if __name__ == "__main__":
    test()
