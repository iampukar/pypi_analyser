import unittest
from src.pypi_analyser.pypi_analyser import pypi_analyser

class Test(unittest.TestCase):
    def test_cases(self):
        """
        Test Case1: babel-core
        """
        package_name = 'pandas'
        package_details = pypi_analyser(package_name)

        self.assertEqual(package_details.package_name, 'pandas')
        self.assertEqual(package_details.released, 'Dec 25, 2009')
        self.assertEqual(package_details.author, 'The Pandas Development Team')
        self.assertEqual(package_details.homepage, 'https://pandas.pydata.org')        
        
if __name__ == '__main__':
    unittest.main()
