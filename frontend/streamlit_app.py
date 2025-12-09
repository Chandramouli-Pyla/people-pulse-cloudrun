import os
import sys
import streamlit as st
from click import style

# Add current directory to path to access components
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import components
from components.add_employee import add_employee_form
from components.employee_table import employee_table
from components.delete_employee import delete_employee_dropdown
from components.stats_panel import stats_panel

# Page configuration
st.set_page_config(page_title="Employee Management System", layout="wide")
import streamlit as st

st.markdown("<h1 style='text-align: center;color: blue'>Employee Management System</h1>", unsafe_allow_html=True)

# Create two columns side by side
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    add_employee_form()

with col2:
    employee_table()

with col3:
    delete_employee_dropdown()

with col4:
    stats_panel()