import abi
import sys


__m = abi.load("script.module.apsw", "apsw")
import sys
sys.modules[__name__] = __m
