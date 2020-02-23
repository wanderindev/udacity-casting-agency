import sys
from sqlalchemy import exc
from typing import Dict, Union
from db import db


# noinspection PyUnresolvedReferences
class ModelMixin:
    def delete_from_db(self) -> Dict[str, bool]:
        try:
            db.session.delete(self)
            db.session.commit()
            return {"error": False}
        except exc.SQLAlchemyError as e:  # pragma: no cover
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()

    def save_to_db(self) -> Dict[str, Union[bool, int]]:
        try:
            db.session.add(self)
            db.session.commit()
            return {"error": False, "id": self.id}
        except exc.SQLAlchemyError as e:  # pragma: no cover
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()
