#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_creation(self):
        """Test basic rectangle creation."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_auto(self):
        """Test auto id assignment."""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)

    def test_id_provided(self):
        """Test provided id assignment."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_type_error(self):
        """Test TypeError raised for non-integer width."""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, "2")
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_width_value_error(self):
        """Test ValueError raised for width <= 0."""
        with self.assertRaises(ValueError) as ctx:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_height_type_error(self):
        """Test TypeError raised for non-integer height."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_x_type_error(self):
        """Test TypeError raised for non-integer x."""
        with self.assertRaises(TypeError) as ctx:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_y_value_error(self):
        """Test ValueError raised for y < 0."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_x_value_error(self):
        """Test ValueError raised for x < 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area with large values."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_str(self):
        """Test __str__ output."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with positional args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update with keyword args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_skipped_with_args(self):
        """Test that kwargs are skipped when args are provided."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=100)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)

    def test_to_dictionary(self):
        """Test to_dictionary returns correct dict."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 9)
        self.assertEqual(d['id'], 1)

    def test_to_dictionary_type(self):
        """Test to_dictionary returns a dict."""
        r = Rectangle(10, 2)
        self.assertEqual(type(r.to_dictionary()), dict)

    def test_width_zero(self):
        """Test ValueError for width of zero."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        """Test ValueError for height of zero."""
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_y_type_error(self):
        """Test TypeError raised for non-integer y."""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_width_negative(self):
        """Test ValueError raised for negative width."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(-1, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_display_no_offset(self):
        """Test display() without x and y."""
        r = Rectangle(4, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "####\n####\n")

    def test_display_no_y(self):
        """Test display() with x set but y=0."""
        r = Rectangle(3, 2, 1, 0)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ###\n ###\n")

    def test_display_with_x_and_y(self):
        """Test display() with both x and y set."""
        r = Rectangle(2, 3, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_save_to_file_empty_list(self):
        """Test Rectangle.save_to_file([]) writes empty JSON array."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None) writes empty JSON array."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_one_rectangle(self):
        """Test Rectangle.save_to_file with one Rectangle instance."""
        r = Rectangle(1, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"width": 1', content)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test Rectangle.load_from_file() returns [] when file missing."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_existing(self):
        """Test Rectangle.load_from_file() returns correct instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertIsInstance(loaded[0], Rectangle)
        self.assertEqual(loaded[0].width, 10)
        self.assertEqual(loaded[0].height, 7)
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
