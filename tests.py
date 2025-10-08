import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_current_dir(self):
        expected = (
            "Result for current directory:"
            "\n - main.py: file_size=729 bytes, is_dir=False"
            "\n - tests.py: file_size=1342 bytes, is_dir=False"
            "\n - pkg: file_size=4096 bytes, is_dir=True"
        )
        result = get_files_info("calculator", ".")
        self.assertEqual(expected, result)
        
    def test_calculator_pkg_dir(self):
        expected = (
            "Result for 'pkg' directory:"
            "\n - render.py: file_size=388 bytes, is_dir=False"
            "\n - calculator.py: file_size=1737 bytes, is_dir=False"
            "\n - __pycache__: file_size=4096 bytes, is_dir=True"
        )
        result = get_files_info("calculator", "pkg")
        self.assertEqual(expected, result)
    
    def test_bin_dir_not_accessible(self):
        expected = (
            "Result for '/bin' directory:"
            '\nError: Cannot list "/bin" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "/bin")
        self.assertEqual(expected, result)
        
    def test_cannot_step_out_of_project(self):
        expected = (
            "Result for '../' directory:"
            '\nError: Cannot list "../" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "../")
        self.assertEqual(expected, result)
        
if __name__ == "__main__":
    unittest.main()