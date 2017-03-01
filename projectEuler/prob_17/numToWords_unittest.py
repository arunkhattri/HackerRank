import unittest
# from num_to_words import num_to_words
from num_to_words import conditions


class NumToWordsTest(unittest.TestCase):

    def setUp(self):
        self.num_tuples = ((426112,
                           'Four Hundred Twenty Six Thousand One Hundred Twelve'),
                           (426, 'Four Hundred Twenty Six'),
                           (45789444999,
                            'Forty Five Billion Seven Hundred Eighty Nine Million Four Hundred Forty Four Thousand Nine Hundred Ninety Nine'),
                           (45263, 'Forty Five Thousand Two Hundred Sixty Three'))
        print('setUp executed')

    def test_num_to_word_conversion(self):
        for i, val in self.num_tuples:
            self.assertEqual(conditions(i), val)

    def tearDown(self):
        self.num_tuples = None
        print("tearDown executed")

if __name__ == "__main__":
    unittest.main(argv=['-v'], exit=False)
