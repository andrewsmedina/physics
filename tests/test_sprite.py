from unittest import TestCase

from physics.sprite import Sprite


class SpriteTestCase(TestCase):

    def test_sprite_should_have_x_attribute(self):
        sprite = Sprite(x=10)
        self.assertEqual(10, sprite.x)
