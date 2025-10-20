import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from config import MAX_CHARS

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        pass
    
    # get_files_info function tests
    
    def test_get_files_info_current_dir(self):
        expected_list = {
            "Result for current directory:",
            "main.py: file_size=",
            "tests.py: file_size=",
            "pkg: file_size=",
            "is_dir="
        }
        result = get_files_info("calculator", ".")
        for expected in expected_list:
            self.assertIn(expected, result)
        
    def test_get_files_info_calculator_pkg_dir(self):
        expected_list = {
            "Result for 'pkg' directory:",
            "- render.py: file_size=",
            "- calculator.py: file_size=",
            "- __pycache__: file_size=",
            "is_dir="
        }
        result = get_files_info("calculator", "pkg")
        for expected in expected_list:
            self.assertIn(expected, result)
    
    def test_get_files_info_bin_dir_not_accessible(self):
        expected = (
            "Result for '/bin' directory:"
            '\nError: Cannot list "/bin" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "/bin")
        self.assertEqual(expected, result)
        
    def test_get_files_info_cannot_step_out_of_project(self):
        expected = (
            "Result for '../' directory:"
            '\nError: Cannot list "../" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "../")
        self.assertEqual(expected, result)
        
    # get_file_content tests
    
        
if __name__ == "__main__":
    unittest.main()