from unittest import TestCase

from physics.sprite import Sprite


class SpriteTestCase(TestCase):

    def setUp(self):
        self.sprite = Sprite(x=10, y=15)

    def test_sprite_should_have_x_attribute(self):
        self.assertEqual(10, self.sprite.x)

    def test_sprite_should_have_y_attribute(self):
        self.assertEqual(15, self.sprite.y)
