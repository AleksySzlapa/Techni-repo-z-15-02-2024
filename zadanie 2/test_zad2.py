from unittest import TestCase
from zad2 import serialize_student_data

class Test(TestCase):
    def test_serialize_student_data(self):
        student_data = {
            "id": 1,
            "first_name": "Jan",
            "last_name": "Kowalski",
            "email": "jan.kowalski@example.com",
            "birth_date": "2000-01-01"
        }
        expected_serialized_data = '{"id": 1, "first_name": "Jan", "last_name": "Kowalski", "email": "jan.kowalski@example.com", "birth_date": "2000-01-01"}'

        serialized_data = serialize_student_data(student_data)

        self.assertEqual(serialized_data, expected_serialized_data)

    def test_serialize_student_data_missing_fields(self):
        # Testowanie, czy funkcja obsługuje brakujące pola w danych ucznia
        student_data = {
            "id": 1,
            "first_name": "Jan",
            "last_name": "Kowalski",
            "email": "jan.kowalski@example.com",
            # Brakuje pola birth_date
        }
        expected_error_message = "ValidationError: {'birth_date': ['Missing data for required field.']}"

        with self.assertRaises(Exception) as context:
            serialize_student_data(student_data)

        self.assertTrue(expected_error_message in str(context.exception))

    def test_serialize_student_data_invalid_email(self):
        # Testowanie, czy funkcja obsługuje nieprawidłowy format adresu e-mail
        student_data = {
            "id": 1,
            "first_name": "Jan",
            "last_name": "Kowalski",
            "email": "jan.kowalski.example.com",  # Nieprawidłowy format adresu e-mail
            "birth_date": "2000-01-01"
        }
        expected_error_message = "ValidationError: {'email': ['Not a valid email address.']}"

        with self.assertRaises(Exception) as context:
            serialize_student_data(student_data)

        self.assertTrue(expected_error_message in str(context.exception))
