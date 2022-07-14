#!/usr/bin/python3
"""Unittest for Rectangle class file"""


import unittest
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle
from io import StringIO
import sys
Rectangle = Rectangle
area = Rectangle.area
display = Rectangle.display
update = Rectangle.update
to_dictionary = Rectangle.to_dictionary


class TestRectangle(unittest.TestCase):

    """Unittest for the Rectangle class"""

    def test_documentation(self):
        self.assertTrue(len(rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(area.__doc__) > 0)
        self.assertTrue(len(display.__doc__) > 0)
        self.assertTrue(len(update.__doc__) > 0)
        self.assertTrue(len(to_dictionary.__doc__) > 0)

    def test_getter_setter(self):
        """Test setter and getter"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(5, 2, 1, 1)
        self.assertEqual(r4.id, 3)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 1)

    def test_area_rectangle(self):
        """Test area function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display_rect(self):
        """Test display function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(4, 4)
        local_stdout = StringIO()
        sys.stdout = local_stdout
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("####\n####\n####\n####\n", local_stdout.getvalue())

    def test_dispay_rect2(self):
        """Test display function"""

        Base._Base__nb_objects = 0

        r2 = Rectangle(2, 2)
        local_stdout = StringIO()
        sys.stdout = local_stdout
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("##\n##\n", local_stdout.getvalue())

    def test_display_offset(self):
        """Test display with offset"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 3, 2, 2)
        dis_stdout = StringIO()
        sys.stdout = dis_stdout
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n  ##\n  ##\n  ##\n", dis_stdout.getvalue())

    def test_display_offset2(self):
        """Test display with offset"""

        Base._Base__nb_objects = 0

        r2 = Rectangle(3, 2, 1, 0)
        dis_stdout = StringIO()
        sys.stdout = dis_stdout
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(" ###\n ###\n", dis_stdout.getvalue())

    def test_print_test(self):
        """Test print function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        loc_stdout = StringIO()
        sys.stdout = loc_stdout
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6\n", loc_stdout.getvalue())

    def test_print_test2(self):
        """Test print function"""

        Base._Base__nb_objects = 0

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

        loc_stdout = StringIO()
        sys.stdout = loc_stdout
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual("[Rectangle] (1) 1/0 - 5/5\n", loc_stdout.getvalue())

    def test_update_rect_args_orig(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_rect_1args(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_rect_2args(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10, 89)
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_rect_3args(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 10, 10, 10, 89)
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_rect_4args(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 3, 10, 10, 89)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_rect_5args(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 3, 4, 10, 89)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_rect_kwargs(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_rect_1kwarg(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_rect_2kwarg(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 1, 10, 10, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")

    def test_update_rect_3kwarg(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(1, 1, 2, 10, 1)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_rect_4kwarg(self):
        """Test update function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 1, 3, 1, 89)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_setter_width_type(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, [1, 2], 2)
        self.assertRaises(TypeError, Rectangle, (1, 2), 2)
        self.assertRaises(TypeError, Rectangle, 12.5, 2)
        self.assertRaises(TypeError, Rectangle, {1, 2}, 2)
        self.assertRaises(TypeError, Rectangle, float('inf'), 2)
        self.assertRaises(TypeError, Rectangle, float('NaN'), 2)

    def test_setter_width_zero_neg(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 0, 12)
        self.assertRaises(ValueError, Rectangle, -5, 12)

    def test_setter_height_type(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 2, 12.5)
        self.assertRaises(TypeError, Rectangle, 2, {1, 2})
        self.assertRaises(TypeError, Rectangle, 2, float('inf'))
        self.assertRaises(TypeError, Rectangle, 2, float('NaN'))

    def test_setter_height_zero_neg(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 12, 0)
        self.assertRaises(ValueError, Rectangle, 12, -5)

    def test_setter_x_type(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2], 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, (1, 2), 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, 12.5, 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, {1, 2}, 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, float('inf'), 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, float('NaN'), 2)

    def test_setter_x_neg(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 1, 2, -5, 2)

    def test_setter_y_type(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 1, 2, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, 12.5)
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, {1, 2})
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, float('inf'))
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, float('NaN'))

    def test_setter_y_neg(self):
        """Test errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 1, 2, 2, -5)

    def test_to_dictionary_rect(self):
        """Test dictionary function"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/9 - 10/2")

        r1.update(x=10, y=10, id=10, height=10, width=10)
        r1_dictionary = r1.to_dictionary()
        expected_dict = {'x': 10, 'y': 10, 'id': 10, 'height': 10, 'width': 10}
        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")


if __name__ == '__main__':
    unittest.main()