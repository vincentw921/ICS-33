import unittest
import contextlib
import io

from printing import *

class TestPrinting(unittest.TestCase):
    def test_print_values_in_range_start_same_as_stop(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3,3, 1)
            self.assertEqual(out.getvalue(), "")
    
    def test_print_values_in_range_stop_less_than_start(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3,-3, 1)
            self.assertEqual(out.getvalue(), "")
            
    def test_print_values_in_range_step_negative(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3, -3, -1)
            self.assertEqual(out.getvalue(), "")
            
    def test_print_values_in_range_start_less_than_stop(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3, 6, 1)
            self.assertEqual(out.getvalue(), "3\n4\n5\n")
            
    def test_print_values_in_range_step_greater_than_stop_minus_start(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3, 6, 4)
            self.assertEqual(out.getvalue(), "3\n")
            
    def test_print_values_in_range_two_step_greater_than_stop_minus_start(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3, 6, 2)
            self.assertEqual(out.getvalue(), "3\n5\n")
            
    def test_print_values_in_range_continue_until_stop(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3, 5, 2)
            self.assertEqual(out.getvalue(), "3\n")
        
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_values_in_range(3, 4, 2)
            self.assertEqual(out.getvalue(), "3\n")
            
    def test_print_reversed_list_empty_list(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_reversed_list([])
            self.assertEqual(out.getvalue(), "")
            
    def test_print_reversed_list_one_item(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_reversed_list(["abc"])
            self.assertEqual(out.getvalue(), "cba\n")
            
    def test_print_reversed_list_two_items(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_reversed_list(["abc", "def"])
            self.assertEqual(out.getvalue(), "cba\nfed\n")
            
    def test_print_reversed_list_three_items(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_reversed_list(["abc", "def", "ghi"])
            self.assertEqual(out.getvalue(), "cba\nfed\nihg\n")
            
    def test_print_reversed_list_of_lists(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_reversed_list([["abc"], ["def"], ["ghi"]])
            self.assertEqual(out.getvalue(), "['abc']\n['def']\n['ghi']\n")
            
    def test_print_reversed_list_of_tuples(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            print_reversed_list([("abc"), ("def"), ("ghi")])
            self.assertEqual(out.getvalue(), "cba\nfed\nihg\n")
            
    def test_print_reversed_list_of_ints(self):
        with self.assertRaises(TypeError):
            print_reversed_list([1,2,3])
            
    def test_print_reversed_list_of_floats(self):
        with self.assertRaises(TypeError):
            print_reversed_list([1.0,2.0,3.0])
            
    def test_print_reversed_list_of_mixed_types(self):
        with self.assertRaises(TypeError):
            print_reversed_list([1, "abc", 3.0])
            
if __name__ == "__main__":
    unittest.main()