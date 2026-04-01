#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
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


if __name__ == "__main__":
    unittest.main()
