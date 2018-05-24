import unittest
from app import create_app


class ApiTestCase(unittest.TestCase):
    """This class represents the api test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    # cpf
    def test_api(self):
        res = self.client().get('/base_2?cpf=12345678910')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()

