import unittest
from models.actors import ActorModel
from tests.base_test import BaseTest


class TestActorModel(BaseTest):
    """Test all methods for the ActorModel"""

    def setUp(self):
        super(TestActorModel, self).setUp()
        with self.app_context:
            self.actor = ActorModel(
                name="John Doe", date_of_birth="1990-01-31", gender="Male"
            )

    def test_init(self):
        with self.app_context:
            self.assertEqual(self.actor.name, "John Doe")
            self.assertEqual(self.actor.date_of_birth, "1990-01-31")
            self.assertEqual(self.actor.gender, "Male")

    def test_find_all(self):
        with self.app_context:
            self.actor.save_to_db()
            actors = ActorModel.find_all()
            self.assertEqual(1, actors[0].id)

    def test_find_by_id(self):
        with self.app_context:
            self.actor.save_to_db()
            actor = ActorModel.find_by_id(1)
            self.assertEqual(1, actor.id)

    def test_find_by_title(self):
        with self.app_context:
            self.actor.save_to_db()
            actor = ActorModel.find_by_name("John Doe")
            self.assertEqual(1, actor.id)

    def test_json(self):
        with self.app_context:
            self.actor.save_to_db()
            actor = ActorModel.find_by_id(1)
            self.assertDictEqual(
                actor.json(),
                {
                    "id": self.actor.id,
                    "name": self.actor.name,
                    "date_of_birth": self.actor.date_of_birth,
                    "gender": self.actor.gender,
                    "movies": [],
                },
            )


if __name__ == "__main__":
    unittest.main()
