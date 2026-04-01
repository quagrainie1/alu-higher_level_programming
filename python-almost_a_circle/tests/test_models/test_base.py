#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test that id auto-increments when not provided."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_provided(self):
        """Test that id is set correctly when provided."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Test that id auto-increments when None is passed."""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_id_zero(self):
        """Test that id can be set to zero."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test that id can be negative."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_to_json_string_normal(self):
        """Test to_json_string with a normal list of dicts."""
        d = [{'id': 1, 'width': 10}]
        result = Base.to_json_string(d)
        self.assertEqual(type(result), str)
        self.assertEqual(json.loads(result), d)

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_normal(self):
        """Test from_json_string with a valid JSON string."""
        s = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(s)
        self.assertEqual(type(result), list)
        self.assertEqual(result[0]['id'], 1)

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file_rectangle(self):
        """Test save_to_file creates a valid JSON file for Rectangle."""
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn("10", content)
        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file with None saves empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        """Test create returns a proper Rectangle instance."""
        r = Rectangle.create(**{'id': 1, 'width': 3, 'height': 5, 'x': 1})
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_create_square(self):
        """Test create returns a proper Square instance."""
        s = Square.create(**{'id': 2, 'size': 4, 'x': 1, 'y': 2})
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 4)

    def test_load_from_file_no_file(self):
        """Test load_from_file returns empty list if file missing."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """Test load_from_file returns correct Rectangle instances."""
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].width, 10)
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
