import unittest
from zad2 import serialize_student_data


class TestSerializeStudentData(unittest.TestCase):
    def test_serialize_student_data(self):
        # Test case when data is given correctly
        student_data = {
            "id": 1,
            "first_name": "Jan",
            "last_name": "Kowalski",
            "email": "jan.kowalski@example.com",
            "birth_date": "2000-01-01"
        }
        expected_serialized_data = {
            'id': 1,
            'first_name': 'Jan',
            'last_name': 'Kowalski',
            'email': 'jan.kowalski@example.com',
            'birth_date': '2000-01-01'
        }

        serialized_data = serialize_student_data(student_data)

        self.assertEqual(serialized_data, expected_serialized_data)

    def test_serialize_student_data_missing_fields(self):
        # Test case when one element is missing
        student_data = {
            "id": 1,
            "first_name": "Jan",
            "last_name": "Kowalski",
            # Missing 'email' field
            "birth_date": "2000-01-01"
        }
        expected_error_message = "{'email': ['Missing data for required field.']}"

        serialized_data = serialize_student_data(student_data)

        self.assertEqual(serialized_data, expected_error_message)


if __name__ == '__main__':
    unittest.main()