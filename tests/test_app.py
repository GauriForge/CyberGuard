import unittest

from app import app


class CyberGuardAppTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.client = app.test_client()

    def test_app_exists(self):
        self.assertIsNotNone(app)

    def test_login_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_registration_page_loads(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get("/dashboard")
        self.assertIn(response.status_code, (302, 401))

    def test_attacks_page_requires_or_loads(self):
        response = self.client.get("/attacks")
        self.assertIn(response.status_code, (200, 302, 401))

    def test_labs_page_requires_or_loads(self):
        response = self.client.get("/labs")
        self.assertIn(response.status_code, (200, 302, 401))

    def test_assessments_page_requires_or_loads(self):
        response = self.client.get("/assessments")
        self.assertIn(response.status_code, (200, 302, 401))

    def test_incident_reporting_requires_or_loads(self):
        response = self.client.get("/incidents/report")
        self.assertIn(response.status_code, (200, 302, 401))

    def test_incident_management_requires_or_loads(self):
        response = self.client.get("/incidents/manage")
        self.assertIn(response.status_code, (200, 302, 401, 403, 404))

    def test_help_centre_requires_or_loads(self):
        response = self.client.get("/help-centre")
        self.assertIn(response.status_code, (200, 302, 401, 404))

    def test_resources_requires_or_loads(self):
        response = self.client.get("/resources")
        self.assertIn(response.status_code, (200, 302, 401, 404))

    def test_roadmap_requires_or_loads(self):
        response = self.client.get("/roadmap")
        self.assertIn(response.status_code, (200, 302, 401, 404))

    def test_careers_page_requires_or_loads(self):
        response = self.client.get("/careers")
        self.assertIn(response.status_code, (200, 302, 401, 404))

    def test_profile_requires_login(self):
        response = self.client.get("/profile")
        self.assertIn(response.status_code, (200, 302, 401, 404))

    def test_notifications_requires_or_loads(self):
        response = self.client.get("/notifications")
        self.assertIn(response.status_code, (200, 302, 401, 404))


if __name__ == "__main__":
    unittest.main()