from typing import Dict, List, Union
from db import db
from models.actors import ActorModel


MovieJSON = Dict[str, Union[int, str, List[str]]]
movies_actors = db.Table(
    "movies_actors",
    db.Column(
        "movie_id", db.Integer, db.ForeignKey("movies.id"), nullable=False
    ),
    db.Column(
        "actor_id", db.Integer, db.ForeignKey("actors.id"), nullable=False
    ),
    db.PrimaryKeyConstraint("movie_id", "permission_id"),
)


class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    actors = db.relationship(
        ActorModel,
        secondary="movies_actors",
        lazy=True,
        backref=db.backref("movies", lazy=True),
    )

    @classmethod
    def find_all(cls) -> List["MovieModel"]:
        return cls.query.order_by(MovieModel.title).all()

    @classmethod
    def find_by_title(cls, title) -> "MovieModel":
        return cls.query.filter_by(title=title).first()

    def json(self) -> MovieJSON:
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "actors": [actor.name for actor in self.actors],
        }