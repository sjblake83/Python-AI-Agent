import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from config import VERBOSE_TESTS

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
        VERBOSE_TESTS and print(result)
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
        VERBOSE_TESTS and print(result)
        for expected in expected_list:
            self.assertIn(expected, result)
    
    def test_get_files_info_bin_dir_not_accessible(self):
        expected = (
            "Result for '/bin' directory:"
            '\nError: Cannot list "/bin" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "/bin")
        VERBOSE_TESTS and print(result)
        self.assertEqual(expected, result)
        
    def test_get_files_info_cannot_step_out_of_project(self):
        expected = (
            "Result for '../' directory:"
            '\nError: Cannot list "../" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "../")
        VERBOSE_TESTS and print(result)
        self.assertEqual(expected, result)
        
        
    # get_file_content tests
    
    def test_get_file_content_main_file(self):
        expected_list = {
            'def main()',
            'if __name__ == "__main__":'
        }
        result = get_file_content("calculator", "main.py")
        VERBOSE_TESTS and print(result)
        for expected in expected_list:
            self.assertIn(expected, result)
            
    def test_get_file_content_calculator_file(self):
        expected_list = {
            "def evaluate(self, expression)",
            "def _evaluate_infix(self, tokens)",
            "def _apply_operator(self, operators, values)"
        }
        result = get_file_content("calculator", "pkg/calculator.py")
        VERBOSE_TESTS and print(result)
        for expected in expected_list:
            self.assertIn(expected, result)
            
    def test_get_file_content_cannot_step_out_of_project(self):
        external_path = "/bin/cat"
        expected = f'Error: Cannot read "{external_path}" as it is outside the permitted working directory'
        result = get_file_content("calculator", external_path)
        VERBOSE_TESTS and print(result)
        self.assertEqual(expected, result)
        
    def test_get_file_content_file_does_not_exist(self):
        nonexistant_file = "pkg/does_not_exist.py"
        expected = f'Error: File not found or is not a regular file: "{nonexistant_file}"'
        result = get_file_content("calculator", nonexistant_file)
        VERBOSE_TESTS and print(result)
        self.assertEqual(expected, result)
    
    

            
            
if __name__ == "__main__":
    unittest.main()