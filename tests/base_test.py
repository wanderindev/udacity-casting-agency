import requests
from unittest import TestCase
from app import create_app, db

app = create_app("testing")


class BaseTest(TestCase):
    """Base class which is inherited by all system test classes."""

    auth_payload = {
        "grant_type": "password",
        "client_id": "e898Rd2i0qF7N9df8CJN8iNlTcM2pdzm",
        "client_secret": "rX8Zc_gB4_dK5oHruO6uf7SKRkAVfawXF8rofkBrccM707yL"
        "jkDHhGEI0A8L0CYq",
        "audience": "udacity-casting",
        "username": "producer@udacity-casting.com",
        "password": "fGKMEKeFF3n5",
    }
    auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    auth_url = "https://udacity-casting.auth0.com/oauth/token"

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        """Create all db tables before each test."""
        self.client = app.test_client()
        self.app_context = app.app_context()

        with self.app_context:
            db.create_all()

    def tearDown(self):
        """Clear db tables after each test"""
        with self.app_context:
            db.drop_all()

    @classmethod
    def get_asistant_headers(cls):
        cls.auth_payload.username = "asistant@udacity-casting.com"
        token = requests.post(
            cls.auth_url, data=cls.auth_payload, headers=cls.auth_headers
        ).json()["access_token"]

        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }

    @classmethod
    def get_director_headers(cls):
        cls.auth_payload.username = "director@udacity-casting.com"
        token = requests.post(
            cls.auth_url, data=cls.auth_payload, headers=cls.auth_headers
        ).json()["access_token"]

        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }

    @classmethod
    def get_producer_headers(cls):
        token = requests.post(
            cls.auth_url, data=cls.auth_payload, headers=cls.auth_headers
        ).json()["access_token"]

        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }
