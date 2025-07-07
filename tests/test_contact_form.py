import unittest
from app import app, validate_form_data

class TestContactFormValidation(unittest.TestCase):

    def test_valid_data(self):
        data = {
            'name': 'Jan',
            'user_email': 'jan@example.com',
            'content': 'To jest testowa wiadomość.'
        }
        is_valid, errors = validate_form_data(data)
        self.assertTrue(is_valid)
        self.assertEqual(errors, {})

    def test_missing_name(self):
        data = {
            'name': '',
            'user_email': 'jan@example.com',
            'content': 'Treść'
        }
        is_valid, errors = validate_form_data(data)
        self.assertFalse(is_valid)
        self.assertIn('name', errors)

    def test_invalid_email(self):
        data = {
            'name': 'Jan',
            'user_email': 'niepoprawny-email',
            'content': 'Treść'
        }
        is_valid, errors = validate_form_data(data)
        self.assertFalse(is_valid)
        self.assertIn('user_email', errors)

    def test_empty_message(self):
        data = {
            'name': 'Jan',
            'user_email': 'jan@example.com',
            'content': ''
        }
        is_valid, errors = validate_form_data(data)
        self.assertFalse(is_valid)
        self.assertIn('content', errors)


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

    def test_index_view_increments_visit_count(self):
        with self.client.session_transaction() as sess:
            sess['visits'] = 0
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Odwiedziles strone 1 razy', response.data)


class TestContactPOST(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_contact_form_valid_post(self):
        response = self.client.post('/kontakt', data={
            'name': 'Jan',
            'user_email': 'jan@example.com',
            'content': 'Wiadomość testowa'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wiadomosc zostala wyslana!', response.data)

    def test_contact_form_invalid_post(self):
        response = self.client.post('/kontakt', data={
            'name': '',
            'user_email': 'zly_email',
            'content': ''
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Imie jest wymagane', response.data)
        self.assertIn(b'user_email: Poprawny email jest wymagany.', response.data)
        self.assertIn(b'content: Wiadomosc nie moze byc pusta.', response.data)
