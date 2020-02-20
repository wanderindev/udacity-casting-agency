from datetime import datetime
from typing import Dict, List, Union
from sqlalchemy.dialects.postgresql import ENUM
from db import db
from models.model_mixin import ModelMixin


ActorJSON = Dict[str, Union[int, str, List[str]]]
gender_enum = ENUM("Male", "Female", name="gender")


class ActorModel(db.Model, ModelMixin):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    date_of_birth = db.Column(db.DateTime)
    gender = db.Column(gender_enum)

    def __init__(self, **kwargs):
        super(ActorModel, self).__init__(**kwargs)

    @property
    def age(self) -> int:
        return (abs(datetime.now() - self.date_of_birth)).years

    @age.setter
    def age(self, age):
        raise AttributeError("age is not a writable attribute")

    @classmethod
    def find_all(cls) -> List["ActorModel"]:
        return cls.query.order_by(ActorModel.name).all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name) -> "ActorModel":
        return cls.query.filter_by(name=name).first()

    def json(self) -> ActorJSON:
        return {
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "movies": [movie.title for movie in self.movies],
        }
