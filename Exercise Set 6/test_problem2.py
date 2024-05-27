import unittest
from problem2 import Vector, Student

class TestProblem2(unittest.TestCase):
    
    def test_vector_equality(self):
        boo = Vector([1, 2, 3], [4, 5, 6], 5)
        other = Vector([1, 2, 3], [4, 5, 6], 5)
        self.assertEqual(boo, other)
        
    def test_vector_hash_equality(self):
        boo = Vector([1, 2, 3], [4, 5, 6], 5)
        other = Vector([1, 2, 3], [4, 5, 6], 5)
        self.assertEqual(hash(boo), hash(other))
        
    def test_vector_hash_inequality(self):
        boo = Vector([1, 2, 3], [4, 5, 6], 5)
        other = Vector([1, 2, 3], [4, 5, 6], 2)
        self.assertNotEqual(hash(boo), hash(other))
    
    def test_add_single_vector(self):
        boo = Vector([1, 2, 3], [4, 5, 6], 5)
        set = {}
        set[boo] = 1
        self.assertEqual(set[boo], 1)
        
    def test_get_same_vector_different_variable(self):
        boo = Vector([1, 2, 3], [4, 5, 6], 5)
        other = Vector([1, 2, 3], [4, 5, 6], 5)
        
        set = {}
        set[boo] = 1
        self.assertEqual(set[other], 1)
        
    def test_get_vector_different_vector(self):
        boo = Vector([1, 2, 3], [4, 5, 6], 5)
        set = {}
        set[boo] = 1
        other = Vector([1, 2, 3], [4, 5, 6], 2)
        self.assertNotEqual(set.get(other), 1)
        
    def test_student_equality(self):
        student1 = Student("John", 20, "123", 5.5)
        student2 = Student("John", 20, "123", 5.5)
        self.assertEqual(student1, student2)
        
    def test_student_hash_equality(self):
        student1 = Student("John", 20, "123", 5.5)
        student2 = Student("John", 20, "123", 5.5)
        self.assertEqual(hash(student1), hash(student2))
        
    def test_add_single_student(self):
        boo = Student("John", 20, "123", 5.5)
        set = {}
        set[boo] = 1
        self.assertEqual(set[boo], 1)
        
    def test_get_same_student_different_variable(self):
        student1 = Student("John", 20, "123", 5.5)
        set = {}
        set[student1] = 6969699
        self.assertEqual(set[student1], 6969699)
        
    def test_get_student_different_student(self):
        student1 = Student("John", 20, "123", 5.5)
        set = {}
        set[student1] = 1
        student2 = Student("John", 20, "123", 2)
        self.assertNotEqual(set.get(student2), 1)
        
        
if __name__ == "__main__":
    unittest.main()