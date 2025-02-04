import unittest
from rename_images import get_new_name

class TestGetNewName(unittest.TestCase):

    def test_basic_replacement(self):
        self.assertEqual(get_new_name("IMG_20220101-123456.jpg"), "20220101-123456.jpg")

    def test_space_and_underscore_replacement(self):
        self.assertEqual(get_new_name("IMG 20220101_123456.JPG"), "20220101-123456.jpg")

    def test_remove_patterns(self):
        self.assertEqual(get_new_name("whatsapp image 20220101-123456.png"), "20220101-123456.png")
        self.assertEqual(get_new_name("screenshot_20220101-123456.jpeg"), "20220101-123456.jpg")

    def test_leading_trailing_dashes(self):
        self.assertEqual(get_new_name("-IMG_20220101-123456-.JPG"), "20220101-123456.jpg")

    def test_no_datetime_string(self):
        self.assertEqual(get_new_name("random_filename.jpg"), "random-filename.jpg")
        self.assertEqual(get_new_name("my_portrait_night_photo.png"), "my.png")

    def test_mixed_case_and_patterns(self):
        self.assertEqual(get_new_name("TeLeGrAm ViDeO 20220101-123456.MP4"), "20220101-123456.mp4")

if __name__ == "__main__":
    unittest.main()
