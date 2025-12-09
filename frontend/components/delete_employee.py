import streamlit as st

from utils.app_client import get_employees, delete_employee

def delete_employee_dropdown():
    st.subheader("Delete Employee")
    response = get_employees()

    if response.status_code == 200:
        employees = response.json().get("data", [])
        options = [e["employee_code"] for e in employees]
        selected = st.selectbox("Select Employee to Delete", options)

        if st.button("Delete"):
            res = delete_employee(selected)
            if res.status_code == 200:
                st.success(res.json().get("message"))
            else:
                st.error(res.json().get("detail") or "Error deleting employee")
    else:
        st.error("Cannot fetch employees")
