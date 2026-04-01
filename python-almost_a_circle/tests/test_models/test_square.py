#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_creation(self):
        """Test basic square creation."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_id_auto(self):
        """Test auto id assignment."""
        s = Square(5)
        self.assertEqual(s.id, 1)

    def test_area(self):
        """Test area of square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test __str__ output."""
        s = Square(5, 2, 1, 3)
        self.assertEqual(str(s), "[Square] (3) 2/1 - 5")

    def test_size_getter(self):
        """Test size getter returns correct value."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        """Test TypeError for non-integer size."""
        with self.assertRaises(TypeError) as ctx:
            s = Square(5)
            s.size = "9"
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_size_value_error(self):
        """Test ValueError for size <= 0."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_update_args(self):
        """Test update with positional args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with keyword args."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_update_args_skip_kwargs(self):
        """Test kwargs skipped when args provided."""
        s = Square(5)
        s.update(10, 2, size=99)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)

    def test_to_dictionary(self):
        """Test to_dictionary returns correct dict."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d['id'], 1)
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 1)

    def test_to_dictionary_type(self):
        """Test to_dictionary returns a dict."""
        s = Square(5)
        self.assertEqual(type(s.to_dictionary()), dict)

    def test_x_validation(self):
        """Test TypeError for non-integer x."""
        with self.assertRaises(TypeError):
            Square(5, "1")

    def test_y_validation(self):
        """Test ValueError for negative y."""
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_inherits_rectangle(self):
        """Test Square inherits from Rectangle."""
        from models.rectangle import Rectangle
        s = Square(5)
        self.assertIsInstance(s, Rectangle)


if __name__ == "__main__":
    unittest.main()
