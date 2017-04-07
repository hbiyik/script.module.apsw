import abi
import sys

sys.modules[__name__] = abi.loadfile("script.module.apsw", "apsw")