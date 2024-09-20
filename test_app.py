import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_roots_calculation(self):
        # Тест на случай, когда есть два корня
        response = self.app.post('/', data={'a': '1', 'b': '-3', 'c': '2'})
        self.assertIn(b'Корень 1:', response.data)
        self.assertIn(b'Корень 2:', response.data)

        # Тест на случай, когда есть один корень
        response = self.app.post('/', data={'a': '1', 'b': '2', 'c': '1'})
        self.assertIn(b'Один корень:', response.data)

        # Тест на случай, когда корней нет
        response = self.app.post('/', data={'a': '1', 'b': '1', 'c': '1'})
        self.assertIn(b'Корней нет', response.data)

if __name__ == '__main__':
    unittest.main()
