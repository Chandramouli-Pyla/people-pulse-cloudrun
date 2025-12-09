# import streamlit as st
# from utils.app_client import get_employees
#
#
# def employee_table():
#     st.subheader("All Employees")
#     response = get_employees()
#
#     if response.status_code == 200:
#         data = response.json().get("data", [])
#         if data:
#             st.dataframe(data)
#         else:
#             st.info("No employees found.")
#     else:
#         st.error(response.json().get("detail") or "Error fetching employees")


import streamlit as st
from utils.app_client import get_employees

def employee_table():
    # Custom CSS for headings + card-like container
    st.markdown("""
        <style>
        /* Section header */
        .custom-subheader {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 10px;
            margin-top: 20px;
        }

        /* Container box */
        .table-container {
            background: #ffffff;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
        }

        /* Dataframe styling of Streamlit container */
        .stDataFrame {
            border-radius: 8px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="custom-subheader">All Employees</div>', unsafe_allow_html=True)


    response = get_employees()

    if response.status_code == 200:
        data = response.json().get("data", [])

        if data:
            st.dataframe(
                data,
                use_container_width=True,
                height=500  # Adjust height if needed
            )
        else:
            st.info("No employees found.")
    else:
        st.error(response.json().get("detail") or "Error fetching employees")

    st.markdown('</div>', unsafe_allow_html=True)
