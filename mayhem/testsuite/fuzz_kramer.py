#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers
import io
from contextlib import contextmanager

@contextmanager
def nostdout():
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr

sys.path.append('../') #This project is not distributed as an installable package
with atheris.instrument_imports():
    import kramer

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    sent = fdp.ConsumeRemainingString()
    num = fdp.ConsumeInt(4)
    try:
        with nostdout():
            kramer.kramer(sent, num)
    except AttributeError:
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
