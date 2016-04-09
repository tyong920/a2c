""" Unit test for a2c.py """

import unittest

import a2c

class KnowValues(unittest.TestCase):
    know_values = ((1, '一'),
                  (10, '一十'),
                  (100, '一百'),
                  (101, '一百零一'),
                  (110, '一百一十'),
                  (1000, '一千'),
                  (1001, '一千零一'),
                  (1010, '一千零一十'),
                  (1100, '一千一百'),
                  (1101, '一千一百零一'),
                  )

    def test_to_chinese(self):
        """ to_chinese should give known result with known input """
        for integer, numeral in self.know_values:
            result = a2c.to_chinese(integer)
            self.assertEqual(numeral, result)


# class ToChineseBadInput(unittest.TestCase):
#     def testNonInteger(self):
#         """ to_chinese should fail with non-integer input """
#         self.assertRaises(a2c.NotIntegerError, a2c.to_chinese, 0.5)


if __name__ == '__main__':
    unittest.main()
