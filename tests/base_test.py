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
    headers_assistant = {}
    headers_director = {}
    headers_producer = {}
    headers_auth_missing = {"Content-Type": "application/json"}
    headers_auth_no_bearer = {}
    headers_token_not_found = {
        "Content-Type": "application/json",
        "Authorization": "Bearer",
    }
    headers_token_not_bearer = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
        + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw"
        "ibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT"
        "4fwpMeJf36POk6yJV_adQssw5c HelloWorld",
    }
    headers_malformed_auth = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
        + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibm"
        "FtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMe"
        "Jf36POk6yJV_adQssw5c",
    }

    headers_token_expired = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
        + "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EQkVSVEk1TlVSR1FUaz"
        "RPRFpET1RsQk5rVXhNRUZETWpSQk9VRTVOVFUzTnpjNE5FRTRRdyJ9.eyJpc3MiOiJo"
        "dHRwczovL3VkYWNpdHktY2FzdGluZy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NW"
        "U0ZjQ4YTg4ZTNiNDYwZWNjYmI2YmRhIiwiYXVkIjoidWRhY2l0eS1jYXN0aW5nIiwia"
        "WF0IjoxNTgyMjU2Mzc3LCJleHAiOjE1ODIyNTY5NzcsImF6cCI6ImU4OThSZDJpMHFG"
        "N045ZGY4Q0pOOGlObFRjTTJwZHptIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9u"
        "cyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1v"
        "dmllIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0"
        "OmFjdG9yIl19.NQup_SawuvK89UbUHA0EZno4AGlTbYEuUrrOMAZ6ZZwGiQ-jSt9m7A"
        "cVSrnrQc9O0i8xLZlHBO-3xapRUCKQQGRrjXvKuYvxVnF9cDUeqGpTKgX6W8voe1llrZ"
        "4Ett5NaF5Wazd337KFSr5fHLLDdTMDWwQuqSZC7wvIImm-PeDaVcO0RpqKEoMaUf9Md3"
        "dej-PCFbmrlzKao_SKHbtvmxQfeuFpoQQpLtZy_gTsyJBNA8D4YEQjnjlhC_S7nfuw2Q"
        "cBBZneq8S4xs98ELR0DNWgWhOUgB8-YkypmUKUUzWlOBFd0o9asdgltFphXys7r50jj2a"
        "abERhRdVnS2tdWA",
    }

    headers_wrong_token = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
        + "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EQkVSVEk1TlVSR1FUazR"
        "PRFpET1RsQk5rVXhNRUZETWpSQk9VRTVOVFUzTnpjNE5FRTRRdyJ9.eyJpc3MiOiJodH"
        "RwczovL2Rldi11LWNhZmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlMTE0N2E0O"
        "WMwMjdhMGU5ZTQ2YWZiYyIsImF1ZCI6InUtY2FmZSIsImlhdCI6MTU3ODE5MDk2Niwi"
        "ZXhwIjoxNTc4MTk4MTY2LCJhenAiOiIwVENPRzJYeHBGV29sWTNrYnRkMXFSVEhBR2p"
        "QVjNHcyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsI"
        "mdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0"
        ".NQup_SawuvK89UbUHA0EZno4AGlTbYEuUrrOMAZ6ZZwGiQ-jSt9m7AcVSrnrQc9O0i"
        "8xLZlHBO-3xapRUCKQQGRrjXvKuYvxVnF9cDUeqGpTKgX6W8voe1llrZ4Ett5NaF5Waz"
        "d337KFSr5fHLLDdTMDWwQuqSZC7wvIImm-PeDaVcO0RpqKEoMaUf9Md3dej-PCFbmrlz"
        "Kao_SKHbtvmxQfeuFpoQQpLtZy_gTsyJBNA8D4YEQjnjlhC_S7nfuw2QcBBZneq8S4xs"
        "98ELR0DNWgWhOUgB8-YkypmUKUUzWlOBFd0o9asdgltFphXys7r50jj2aabERhRdVnS2"
        "tdWA",
    }

    headers_wrong_keys = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
        + "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9EWTN"
        "PVU0wTlRNME1qQXdOMFF4TlVGQk9FWTVNVVpDUWpkQ056SkdOa1J"
        "HTXpnMVJqRkJOdyJ9.eyJpc3MiOiJodHRwczovL2Rldi11LWNhZ"
        "mUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlMTE0NzQ3Mzc1"
        "MmQyMGU3MDFmNWMxMSIsImF1ZCI6InUtY2FmZSIsImlhdCI6MT"
        "3ODE5MTA5OSwiZXhwIjoxNTc4MTk4Mjk5LCJhenAiOiIwVENPRz"
        "JYeHBGV29sWTNrYnRkMXFSVEhBR2pQVjNHcyIsInNjb3BlIjoiIi"
        "wicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.BC"
        "DSNyAR92F7MHpP7iAXEDT6TPvV8NR9BtFGKIvv0EUOT38iqTInOx"
        "vGaevnitcdObZ1ZDmn2dvwxB_ppqQXnzMGbdwd9GD6_kgGvGXqtn"
        "V0FvWk8Q9OvdpyXyS3BAycIHL9IlbHo5A4sDR9_fePMSyfG44XAD"
        "szFXq3SmwDqZ1q87I9kK01TMB8PEznDePhgJp_Q3QqqRUiA-O3AT"
        "pFJcKBsM1K2P3QNmjIOPysR-F_PWOl_-6v9Fwmms1s7xVcGFmn0r"
        "E-_T6XlzmcUejNHdU-9UH4CPV2Nl58W5vxjb1brOZXiPrNOnCx"
        "a3VBtJAGntBYzJG6LVwXaNtR25BNrw",
    }

    @classmethod
    def setUpClass(cls) -> None:
        cls.headers_producer = cls.get_producer_headers()
        cls.headers_director = cls.get_director_headers()
        cls.headers_assistant = cls.get_assistant_headers()
        cls.headers_auth_no_bearer = cls.get_no_bearer_headers()

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
    def get_assistant_headers(cls):
        cls.auth_payload["username"] = "assistant@udacity-casting.com"
        token = requests.post(
            cls.auth_url, data=cls.auth_payload, headers=cls.auth_headers
        ).json()["access_token"]

        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }

    @classmethod
    def get_director_headers(cls):
        cls.auth_payload["username"] = "director@udacity-casting.com"
        token = requests.post(
            cls.auth_url, data=cls.auth_payload, headers=cls.auth_headers
        ).json()["access_token"]

        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }

    @classmethod
    def get_no_bearer_headers(cls):
        cls.auth_payload["username"] = "other@udacity-casting.com"
        token = requests.post(
            cls.auth_url, data=cls.auth_payload, headers=cls.auth_headers
        ).json()["access_token"]

        return {
            "Content-Type": "application/json",
            "Authorization": token,
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
