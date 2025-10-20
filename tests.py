import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        pass
    
    # get_files_info function tests
    
    def test_current_dir(self):
        expected_list = {
            "Result for current directory:",
            "main.py: file_size=",
            "tests.py: file_size=",
            "pkg: file_size=",
            "is_dir="
        }
        result = get_files_info("calculator", ".")
        print(result)
        for expected in expected_list:
            self.assertIn(expected, result)
        
    def test_calculator_pkg_dir(self):
        expected_list = {
            "Result for 'pkg' directory:",
            "- render.py: file_size=",
            "- calculator.py: file_size=",
            "- __pycache__: file_size=",
            "is_dir="
        }
        result = get_files_info("calculator", "pkg")
        print(result)
        for expected in expected_list:
            self.assertIn(expected, result)
    
    def test_bin_dir_not_accessible(self):
        expected = (
            "Result for '/bin' directory:"
            '\nError: Cannot list "/bin" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(expected, result)
        
    def test_cannot_step_out_of_project(self):
        expected = (
            "Result for '../' directory:"
            '\nError: Cannot list "../" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual(expected, result)
        
    # get_file_content tests
        
if __name__ == "__main__":
    unittest.main()