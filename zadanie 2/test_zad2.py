from unittest import TestCase
import datetime as dt
from zad2 import serialize

class Test(TestCase):
    def test_normal_serialization(self):
        #Given
        id = 1
        first_name = "Jan"
        last_name = "Kowal"
        email = "Jan_Kowal32@gmail.com"
        birth_day = dt.datetime.now()
        expected = '{"id": "1", "first_name": "Jan", "last_name": "Kowal", "email": "Jan_Kowal32@gmail.com", "birth_day": "2024-02-29"}'
        #When
        result = serialize(id, first_name, last_name, email, birth_day)
        #Then
        self.assertEqual(expected, result)
    def test_missing_required_field(self):
        #Given
        id = 1
        first_name = "Jan"
        last_name = "Kowal"
        birth_day = dt.datetime.now()
        expected = None
        #When
        with self.assertRaises(ValueError):
            # Then
            serialize(id=id, first_name=first_name, last_name=last_name, mail= None, birth_day = birth_day)

    def test_wrong_data_types(self):
        # Given
        id = 1
        first_name = "Jan"
        last_name = "Kowal"
        emial = 5
        birth_day = dt.datetime.now()
        # When
        with self.assertRaises(TypeError):
            # Then
            serialize(id, first_name, last_name, emial, birth_day)
