import json
import unittest
from tests.base_test import BaseTest


class TestMovieResources(BaseTest):
    """Test all endpoints for the movie resources"""

    def setUp(self):
        super(TestMovieResources, self).setUp()

        with self.app_context:
            self.actor = {
                "name": "John Doe",
                "date_of_birth": "1990-01-31",
                "gender": "Male",
            }
            self.movie = {
                "title": "My Great Movie",
                "release_date": "2020-01-31",
            }
            self.patch_movie = {
                "title": "My Other Great Movie",
                "release_date": "2020-02-15",
            }

    def test_post_movies_producer(self):
        """Test POSTing a movie with the producer credentials"""
        with self.client as c:
            with self.app_context:
                results = c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(data["movie"]["title"], self.movie["title"])
                self.assertEqual(
                    data["movie"]["release_date"],
                    "Fri, 31 Jan 2020 00:00:00 GMT",
                )

    def test_get_movies_producer(self):
        """Test GETing all movies with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.get(
                    "/movies", headers=TestMovieResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(len(data["movies"]), 1)
                self.assertEqual(
                    data["movies"][0]["title"], self.movie["title"]
                )

    def test_get_movie_producer(self):
        """Test GETing a movie with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.get(
                    "/movies/1", headers=TestMovieResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(data["movie"]["title"], self.movie["title"])

    def test_patch_movie_producer(self):
        """Test PATCHing a movie with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.patch(
                    "/movies/1",
                    data=json.dumps(self.patch_movie),
                    headers=TestMovieResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["movie"]["title"], self.patch_movie["title"]
                )
                self.assertEqual(
                    data["movie"]["release_date"],
                    "Sat, 15 Feb 2020 00:00:00 GMT",
                )

    def test_add_actor_to_movie_producer(self):
        """Test adding an actor to a movie with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.patch(
                    "/movies/1/actor/1",
                    headers=TestMovieResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(data["movie"]["actors"][0]["id"], 1)

    def test_delete_movie_producer(self):
        """Test DELETEing a movie with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.delete(
                    "/movies/1", headers=TestMovieResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(data["deleted"], 1)

    def test_get_movies_director(self):
        """Test GETing all movies with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.get(
                    "/movies", headers=TestMovieResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(len(data["movies"]), 1)
                self.assertEqual(
                    data["movies"][0]["title"], self.movie["title"]
                )

    def test_get_movie_director(self):
        """Test GETing a movie with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.get(
                    "/movies/1", headers=TestMovieResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(data["movie"]["title"], self.movie["title"])

    def test_patch_movie_director(self):
        """Test PATCHing a movie with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.patch(
                    "/movies/1",
                    data=json.dumps(self.patch_movie),
                    headers=TestMovieResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["movie"]["title"], self.patch_movie["title"]
                )
                self.assertEqual(
                    data["movie"]["release_date"],
                    "Sat, 15 Feb 2020 00:00:00 GMT",
                )

    def test_add_actor_to_movie_director(self):
        """Test adding an actor to a movie with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestMovieResources.headers_director,
                )
                results = c.patch(
                    "/movies/1/actor/1",
                    headers=TestMovieResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(data["movie"]["actors"][0]["id"], 1)

    def test_get_movies_assistant(self):
        """Test GETing all movies with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.get(
                    "/movies", headers=TestMovieResources.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(len(data["movies"]), 1)
                self.assertEqual(
                    data["movies"][0]["title"], self.movie["title"]
                )

    def test_get_movie_assistant(self):
        """Test GETing a movie with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/movies",
                    data=json.dumps(self.movie),
                    headers=TestMovieResources.headers_producer,
                )
                results = c.get(
                    "/movies/1", headers=TestMovieResources.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(data["movie"]["title"], self.movie["title"])


if __name__ == "__main__":
    unittest.main()
