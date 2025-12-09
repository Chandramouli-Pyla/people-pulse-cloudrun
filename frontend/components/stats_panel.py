import streamlit as st
from utils.app_client import get_median_age, get_median_salary


def stats_panel():
    st.subheader("Employee Stats")

    age_res = get_median_age()
    salary_res = get_median_salary()

    if age_res.status_code == 200:
        st.metric("Median Age", age_res.json()["data"]["median_age"])
    else:
        st.error("Error fetching median age")

    if salary_res.status_code == 200:
        st.metric("Median Salary", salary_res.json()["data"]["median_salary"])
    else:
        st.error("Error fetching median salary")
