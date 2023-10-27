import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)

    def test_carregar(self):
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU MEGA MAN')
        self.assertEqual(megaman.bateria, 49, 'A bateria deveria estar em 49%')


if __name__ == '__main__':
    unittest.main()

