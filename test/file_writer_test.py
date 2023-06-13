import unittest
import json
from file_writer import write_to_json

class FileWriterTest(unittest.TestCase):
    def test_write_to_json(self):
        data = [
            {'id': 1, 'name': 'Pikachu'},
            {'id': 2, 'name': 'Charizard'},
            {'id': 3, 'name': 'Bulbasaur'}
        ]
        file_name = 'test.json'
        write_to_json(data, file_name)

        with open(file_name, 'r') as file:
            written_data = json.load(file)

        self.assertEqual(written_data, data)

        # Clean up: delete the test file
        import os
        os.remove(file_name)

if __name__ == '__main__':
    unittest.main()