from sqlalchemy import Column, String
from backend.db.connection import Base
import uuid

class Person(Base):
    __tablename__ = "persons"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=True)
    house_number = Column(String, nullable=True)
    street = Column(String, nullable=True)
    apartment = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)




# from sqlalchemy import Column, Integer, String
# from backend.app.db.connection import Base
#
# class Person(Base):
#     __tablename__ = "persons"
#
#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     phone_number = Column(String, nullable=True)
#
#     # Address fields
#     house_number = Column(String, nullable=True)
#     street = Column(String, nullable=True)
#     apartment = Column(String, nullable=True)
#     city = Column(String, nullable=True)
#     state = Column(String, nullable=True)
#     country = Column(String, nullable=True)
#     zip_code = Column(String, nullable=True)
#
#     def __repr__(self):
#         return (
#             f"<Person(id={self.id}, name={self.first_name} {self.last_name}, "
#             f"email={self.email}, city={self.city}, state={self.state})>"
#         )
