import unittest
from app import app, validate_form_data

class TestContactFormValidation(unittest.TestCase):

    def test_valid_data(self):
        data = {
            'name': 'Jan',
            'email': 'jan@example.com',
            'message': 'To jest testowa wiadomość.'
        }
        is_valid, errors = validate_form_data(data)
        self.assertTrue(is_valid)
        self.assertEqual(errors, {})

    def test_missing_name(self):
        data = {
            'name': '',
            'email': 'jan@example.com',
            'message': 'Treść'
        }
        is_valid, errors = validate_form_data(data)
        self.assertFalse(is_valid)
        self.assertIn('name', errors)

    def test_invalid_email(self):
        data = {
            'name': 'Jan',
            'email': 'niepoprawny-email',
            'message': 'Treść'
        }
        is_valid, errors = validate_form_data(data)
        self.assertFalse(is_valid)
        self.assertIn('email', errors)

    def test_empty_message(self):
        data = {
            'name': 'Jan',
            'email': 'jan@example.com',
            'message': ''
        }
        is_valid, errors = validate_form_data(data)
        self.assertFalse(is_valid)
        self.assertIn('message', errors)


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Batony Proteinowe', response.data)

    def test_kontakt_route(self):
        response = self.client.get('/kontakt')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Skontaktuj si', response.data)

class TestContactPOST(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_contact_form_valid_post(self):
        response = self.client.post('/kontakt', data={
            'name': 'Jan',
            'email': 'jan@example.com',
            'message': 'Wiadomość testowa'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wiadomosc zostala wyslana!', response.data)

    def test_contact_form_invalid_post(self):
        response = self.client.post('/kontakt', data={
            'name': '',
            'email': 'zly_email',
            'message': ''
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Imie jest wymagane', response.data)
        self.assertIn(b'email: Poprawny email jest wymagany.', response.data)
        self.assertIn(b'message: Wiadomosc nie moze byc pusta.', response.data)
