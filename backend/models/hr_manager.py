from sqlalchemy import Column, Boolean, ForeignKey, String
from .employee import Employee


class HRManager(Employee):
    __tablename__ = "hr_managers"

    # id = Column(Integer, ForeignKey("employees.id"),primary_key=True, index=True)
    id = Column(String, ForeignKey("employees.id"), primary_key=True) ##for BigQuery since it not supported pk,fk, and auto increments

    can_approve_leaves = Column(Boolean, default=True)
    can_access_salary_data = Column(Boolean, default=True)

    def __repr__(self):
        return (
            f"<HRManager(id={self.id}, name={self.first_name} {self.last_name}, "
            f"email={self.email}, approve_leaves={self.can_approve_leaves}, "
            f"salary_access={self.can_access_salary_data})>"
        )
