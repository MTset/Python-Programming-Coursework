"""
Test mod_func_def module
"""
import unittest
from mod_func_def import *
import sys
from io import TextIOWrapper, BytesIO
sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)

class TestMod_Func_Def(unittest.TestCase):
        
        def test_mod_func_def(self):
            expected = [
"'def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)'\n",
"'def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)'\n",
"'def load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)'\n",
"'def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)'\n"
           ]
            mod_func_def("json")
            sys.stdout.seek(0)
            observed = sys.stdout.readlines()
            self.assertEqual(expected, observed)
            
if __name__ == "__main__":
    unittest.main()