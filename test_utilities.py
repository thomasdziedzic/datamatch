import unittest
import utilities

class TestUtilityFunctions(unittest.TestCase):
    def test_readCSV(self):
        filename = "./test_data/1.csv"
        
        contents = utilities.readCSV(filename)
       
        self.assertEqual(3, len(contents), 'There should be 3 rows in the file')
       
        for row in contents:
            self.assertEqual(6, len(row), 'There should be 6 columns per row')

    def test_lowerCSV(self):
        contents = [['A','a']]
        
        lower_contents = utilities.lowerCSV(contents)
        
        for row in lower_contents:
            for column in row:
                self.assertTrue(column.islower(), 'All strings should have been set to lower case')

if __name__ == '__main__':
    unittest.main()