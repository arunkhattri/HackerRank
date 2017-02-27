import unittest
from coltz_seq_3 import result


class CollatzTest(unittest.TestCase):

    def setUp(self):
        self.coltz_elems = ((10, 9), (15, 9), (20, 19))
        print("setUp executed")

    def testCalculation(self):
        ans = result(20)
        # self.assertEqual(cs_arr(9), 9)
        # self.assertEqual(cs_arr(14), 9)
        # self.assertEqual(cs_arr(19), 19)
        for (i, val) in self.coltz_elems:
            self.assertEqual(ans[i-1], val)

    def tearDown(self):
        self.coltz_elems = None
        print("tearDown executed!")

if __name__ == "__main__":
    unittest.main(argv=['-v'], exit=False)
