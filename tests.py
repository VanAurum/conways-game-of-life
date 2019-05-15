#Standard python library imports
import unittest

#Local imports
from solution import (
    get_bottom,
    get_left,
    get_right,
    get_top,
)


class TestSolution(unittest.TestCase):
    
    
    def test_matrix_is_square(self):
        matrix=create_matrix(5)
        self.assertEqual(len(matrix),5)
        self.assertEqual(len(matrix[0]),5)
        self.assertLessEqual(max(matrix[0]),1)
        self.assertGreaterEqual(min(matrix[0]),0)

    def test_neighbour_values(self):
        
        matrix=[
                [0,1,1,0],
                [1,1,0,0],
                [0,0,0,1],
                [1,1,1,1],
            ]
        
        self.assertEqual(get_top(matrix,0,0),0)
        self.assertEqual(get_right(matrix,0,3),0)
        self.assertEqual(get_bottom(matrix,3,0),0)
        self.assertEqual(get_left(matrix,0,0),0)
        self.assertEqual(get_top(matrix,2,0),1)
        self.assertEqual(get_right(matrix,3,2),1)
        self.assertEqual(get_bottom(matrix,2,2),1)
        self.assertEqual(get_left(matrix,3,1),1)
        
    def test_sum_neighbours(self):    
        
        matrix=[
                [0,1,1,0],
                [1,1,0,0],
                [0,0,0,1],
                [1,1,1,1],
            ]
        
        self.assertEqual(sum_neighbours(matrix,0,0),2)
        self.assertEqual(sum_neighbours(matrix,0,1),2)
        self.assertEqual(sum_neighbours(matrix,0,2),1)
        self.assertEqual(sum_neighbours(matrix,0,3),1)
        self.assertEqual(sum_neighbours(matrix,1,0),1)
        self.assertEqual(sum_neighbours(matrix,1,1),2)
        self.assertEqual(sum_neighbours(matrix,1,2),2)
        self.assertEqual(sum_neighbours(matrix,1,3),1)

if __name__=='__main__':
    
    test=True 
    
    if test:
        suite=unittest.defaultTestLoader.loadTestsFromTestCase(TestSolution)
        unittest.TextTestRunner(verbosity=2).run(suite)        