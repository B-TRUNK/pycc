import unittest #1
from namefunc import formatted_name


class NamesTestCase(unittest.TestCase): #3
    
    """Tests for 'namefunc.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        full_name = formatted_name('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        full_name = formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(full_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()