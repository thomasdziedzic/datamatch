import unittest
import utilities

class TestUtilityFunctions(unittest.TestCase):
    def test_readCSV(self):
        filename = "./test_data/1.csv"
        
        contents = utilities.readCSV(filename)
       
        self.assertEqual(3, len(contents), 'There should be 3 rows in the file')
       
        for row in contents:
            self.assertEqual(6, len(row), 'There should be 6 columns per row')

if __name__ == '__main__':
    unittest.main()