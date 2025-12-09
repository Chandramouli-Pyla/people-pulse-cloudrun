from sqlalchemy import Column, String, Float, Date, ForeignKey
from .person import Person


class Employee(Person):
    __tablename__ = "employees"

    # id = Column(Integer, ForeignKey("persons.id"), primary_key=True) ##for postgresql
    id = Column(String, ForeignKey("persons.id"), primary_key=True) ##for BigQuery since it not supported pk,fk, and auto increments
    employee_code = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)
    position = Column(String, nullable=False)
    salary = Column(Float, nullable=True)
    date_of_birth = Column(Date, nullable=False)
    date_of_joining = Column(Date, nullable=False)

    def __repr__(self):
        return (
            f"<Employee(id={self.id}, code={self.employee_code}, "
            f"name={self.first_name} {self.last_name}, "
            f"department={self.department}, position={self.position})>"
        )
