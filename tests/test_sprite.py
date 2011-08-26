from unittest import TestCase

from physics.sprite import Sprite


class SpriteTestCase(TestCase):

    def setUp(self):
        self.sprite = Sprite(x=10, y=15, x_velocity=1, y_velocity=1)

    def test_sprite_should_have_x_attribute(self):
        self.assertEqual(10, self.sprite.x)

    def test_sprite_should_have_y_attribute(self):
        self.assertEqual(15, self.sprite.y)

    def test_step_should_increment_x_sprite_position(self):
        self.sprite.step()
        self.assertEqual(11, self.sprite.x)

    def test_step_should_increment_y_sprite_position(self):
        self.sprite.step()
        self.assertEqual(16, self.sprite.y)
