import unittest
from models.movies import MovieModel
from tests.base_test import BaseTest


class TestMovieModel(BaseTest):
    """Test all methods for the MovieModel"""

    def setUp(self):
        super(TestMovieModel, self).setUp()
        with self.app_context:
            self.movie = MovieModel(
                title="My Great Movie", release_date="2020-01-31"
            )

    def test_init(self):
        with self.app_context:
            self.assertEqual(self.movie.title, "My Great Movie")
            self.assertEqual(self.movie.release_date, "2020-01-31")

    def test_find_all(self):
        with self.app_context:
            self.movie.save_to_db()
            movies = MovieModel.find_all()
            self.assertEqual(1, movies[0].id)

    def test_find_by_id(self):
        with self.app_context:
            self.movie.save_to_db()
            movie = MovieModel.find_by_id(1)
            self.assertEqual(1, movie.id)

    def test_find_by_title(self):
        with self.app_context:
            self.movie.save_to_db()
            movie = MovieModel.find_by_title("My Great Movie")
            self.assertEqual(1, movie.id)

    def test_json(self):
        with self.app_context:
            self.movie.save_to_db()
            movie = MovieModel.find_by_id(1)
            self.assertDictEqual(
                movie.json(),
                {
                    "id": self.movie.id,
                    "title": self.movie.title,
                    "release_date": self.movie.release_date,
                    "actors": [],
                },
            )


if __name__ == "__main__":
    unittest.main()
