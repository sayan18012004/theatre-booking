import unittest
from unittest.mock import patch, mock_open
import csv
import main  # assuming the code is in a file named main.py

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['login', 'testuser'])
    @patch('builtins.print')
    @patch('csv.reader')
    def test_login_existing_user(self, mock_csv_reader, mock_print, mock_input):
        mock_csv_reader.return_value = iter([['testuser', 'Test User', '25', '1234567890', 'Normal']])
        main.login()
        mock_print.assert_called_with('Welcome ', 'Test User', '\n')

    @patch('builtins.input', side_effect=['login', 'nonexistentuser'])
    @patch('builtins.print')
    @patch('csv.reader')
    def test_login_nonexistent_user(self, mock_csv_reader, mock_print, mock_input):
        mock_csv_reader.return_value = iter([['testuser', 'Test User', '25', '1234567890', 'Normal']])
        main.login()
        mock_print.assert_called_with('User not found\n')

    @patch('builtins.input', side_effect=['register', 'newuser', 'New User', '30', '0987654321', 'Admin'])
    @patch('builtins.print')
    @patch('csv.writer')
    @patch('builtins.open', new_callable=mock_open)
    def test_register_new_user(self, mock_open, mock_csv_writer, mock_print, mock_input):
        main.login()
        mock_open.assert_called_with('user_data.csv', 'a', newline='')
        mock_csv_writer.return_value.writerow.assert_called_with(['newuser', 'New User', '30', '0987654321', 'Admin'])

    # Add more tests for other functions and edge cases

if __name__ == '__main__':
    unittest.main()