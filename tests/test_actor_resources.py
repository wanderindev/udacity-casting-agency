import json
import unittest
from tests.base_test import BaseTest


class TestActorResources(BaseTest):
    """Test all endpoints for the actor resources"""

    def setUp(self):
        super(TestActorResources, self).setUp()

        with self.app_context:
            self.actor = {
                "name": "John Doe",
                "date_of_birth": "1990-01-31",
                "gender": "Male",
            }
            self.patch_actor = {
                "name": "Jane Doe",
                "date_of_birth": "1991-01-31",
                "gender": "Female"
            }

    def test_post_actors_producer(self):
        """Test POSTing an actor with the producer credentials"""
        with self.client as c:
            with self.app_context:
                results = c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(data["actor"]["name"], self.actor["name"])
                self.assertEqual(data["actor"]["gender"], self.actor["gender"])
                self.assertEqual(
                    data["actor"]["date_of_birth"],
                    "Wed, 31 Jan 1990 00:00:00 GMT",
                )

    def test_get_actors_producer(self):
        """Test GETing all actors with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_producer,
                )
                results = c.get(
                    "/actors", headers=TestActorResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(len(data["actors"]), 1)
                self.assertEqual(
                    data["actors"][0]["name"], self.actor["name"]
                )

    def test_get_actor_producer(self):
        """Test GETing an actor with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_producer,
                )
                results = c.get(
                    "/actors/1", headers=TestActorResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(data["actor"]["name"], self.actor["name"])

    def test_patch_actor_producer(self):
        """Test PATCHing an actor with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_producer,
                )
                results = c.patch(
                    "/actors/1",
                    data=json.dumps(self.patch_actor),
                    headers=TestActorResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["actor"]["name"], self.patch_actor["name"]
                )
                self.assertEqual(
                    data["actor"]["gender"], self.patch_actor["gender"]
                )
                self.assertEqual(
                    data["actor"]["date_of_birth"],
                    "Thu, 31 Jan 1991 00:00:00 GMT",
                )

    def test_delete_actor_producer(self):
        """Test DELETEing an actor with the producer credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_producer,
                )
                results = c.delete(
                    "/actors/1", headers=TestActorResources.headers_producer,
                )

                data = json.loads(results.data)

                self.assertEqual(data["deleted"], 1)

    def test_get_actors_director(self):
        """Test GETing all actors with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_director,
                )
                results = c.get(
                    "/actors", headers=TestActorResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(len(data["actors"]), 1)
                self.assertEqual(
                    data["actors"][0]["name"], self.actor["name"]
                )

    def test_get_actor_director(self):
        """Test GETing an actor with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_director,
                )
                results = c.get(
                    "/actors/1", headers=TestActorResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(data["actor"]["name"], self.actor["name"])

    def test_patch_actor_director(self):
        """Test PATCHing an actor with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_director,
                )
                results = c.patch(
                    "/actors/1",
                    data=json.dumps(self.patch_actor),
                    headers=TestActorResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(
                    data["actor"]["name"], self.patch_actor["name"]
                )
                self.assertEqual(
                    data["actor"]["gender"], self.patch_actor["gender"]
                )
                self.assertEqual(
                    data["actor"]["date_of_birth"],
                    "Thu, 31 Jan 1991 00:00:00 GMT",
                )

    def test_delete_actor_director(self):
        """Test DELETEing an actor with the director credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_director,
                )
                results = c.delete(
                    "/actors/1", headers=TestActorResources.headers_director,
                )

                data = json.loads(results.data)

                self.assertEqual(data["deleted"], 1)

    def test_get_actors_assistant(self):
        """Test GETing all actors with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_producer,
                )
                results = c.get(
                    "/actors", headers=TestActorResources.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(len(data["actors"]), 1)
                self.assertEqual(
                    data["actors"][0]["name"], self.actor["name"]
                )

    def test_get_actor_assistant(self):
        """Test GETing an actor with the assistant credentials"""
        with self.client as c:
            with self.app_context:
                c.post(
                    "/actors",
                    data=json.dumps(self.actor),
                    headers=TestActorResources.headers_producer,
                )
                results = c.get(
                    "/actors/1", headers=TestActorResources.headers_assistant,
                )

                data = json.loads(results.data)

                self.assertEqual(data["actor"]["name"], self.actor["name"])


if __name__ == "__main__":
    unittest.main()
