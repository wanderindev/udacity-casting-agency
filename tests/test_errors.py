import json
import unittest
from tests.base_test import BaseTest


class TestErrors(BaseTest):
    """Test all error conditions"""

    def setUp(self):
        super(TestErrors, self).setUp()

        with self.app_context:
            self.actor = {
                "name": "John Doe",
                "date_of_birth": "1990-01-31",
                "gender": "Male",
            }
            self.patch_actor = {
                "name": "Jane Doe",
                "date_of_birth": "1991-01-31",
                "gender": "Female",
            }
            self.movie = {
                "title": "My Great Movie",
                "release_date": "2020-01-31",
            }
            self.patch_movie = {
                "title": "My Other Great Movie",
                "release_date": "2020-02-15",
            }

    def test_auth_header_missing(self):
        """Test GET with missing auth header"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_auth_missing
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["code"], "authorization_header_missing"
                )

    def test_auth_no_bearer(self):
        """Test GET with missing Bearer"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_auth_no_bearer
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"],
                    "Authorization header must start with Bearer.",
                )

    def test_auth_token_not_found(self):
        """Test GET with missing token"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_token_not_found
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Token not found.",
                )

    def test_auth_token_not_bearer(self):
        """Test GET with token not bearer"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_token_not_bearer
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"],
                    "Authorization header must be bearer token.",
                )

    def test_auth_malformed(self):
        """Test GET with malformed auth"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_malformed_auth
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Authorization malformed.",
                )

    def test_auth_token_expired(self):
        """Test GET with expired token"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_token_expired
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Token expired.",
                )

    def test_auth_wrong_token(self):
        """Test GET with invalid token"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_wrong_token
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"],
                    "Unable to parse authentication token.",
                )

    def test_auth_wrong_keys(self):
        """Test GET with invalid keys"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_wrong_keys
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"],
                    "Unable to find the appropriate key.",
                )

    def test_get_movies_not_found(self):
        """Test GETing all movies with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies", headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_get_movie_not_found(self):
        """Test GETing a movie with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/movies/1", headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_patch_movie_not_found(self):
        """Test PATCHing a movie with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.patch(
                    "/movies/1",
                    data=json.dumps(self.patch_movie),
                    headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_delete_movie_not_found(self):
        """Test DELETEing a movie with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.delete(
                    "/movies/1", headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_add_actor_to_movie_not_found(self):
        """Test adding an actor to a movie with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.patch(
                    "/movies/1/actor/1", headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_get_actors_not_found(self):
        """Test GETing all actors with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/actors", headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_get_actor_not_found(self):
        """Test GETing a actor with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.get(
                    "/actor/1", headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_patch_actor_not_found(self):
        """Test PATCHing a actor with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.patch(
                    "/actor/1",
                    data=json.dumps(self.patch_actor),
                    headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_delete_actor_not_found(self):
        """Test DELETEing a actor with empty db table"""
        with self.client as c:
            with self.app_context:
                results = c.delete(
                    "/actor/1", headers=TestErrors.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"], "Not found.",
                )

    def test_post_movies_director(self):
        """Test POSTing a movie with the director credentials"""
        with self.client as c:
            with self.app_context:
                results = c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestErrors.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Permission not found.",
                )

    def test_post_movies_assistant(self):
        """Test POSTing a movie with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                results = c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestErrors.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Permission not found.",
                )

    def test_delete_movie_assistant(self):
        """Test DELETEing a movie with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestErrors.headers_producer,
                )
                results = c.delete(
                    "/movies/1", headers=TestErrors.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Permission not found.",
                )

    def test_delete_actor_assistant(self):
        """Test DELETEing an actor with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestErrors.headers_producer,
                )
                results = c.delete(
                    "/actors/1", headers=TestErrors.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Permission not found.",
                )

    def test_patch_movie_assistant(self):
        """Test PATCHing a movie with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestErrors.headers_producer,
                )
                results = c.patch(
                    "/movies/1",
                    data=json.dumps(self.patch_movie),
                    headers=TestErrors.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Permission not found.",
                )

    def test_add_actor_to_movie_assistant(self):
        """Test adding an actor to a movie with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestErrors.headers_producer,
                )
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestErrors.headers_producer,
                )
                results = c.patch(
                    "/movies/1/actor/1", headers=TestErrors.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Permission not found.",
                )

    def test_patch_actor_assistant(self):
        """Test PATCHing an actor with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestErrors.headers_producer,
                )
                results = c.patch(
                    "/actors/1",
                    data=json.dumps(self.patch_actor),
                    headers=TestErrors.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["message"]["description"], "Permission not found.",
                )


if __name__ == "__main__":
    unittest.main()
