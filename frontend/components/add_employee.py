from utils.app_client import add_employee
import streamlit as st
from datetime import date
import re

def add_employee_form(height=500, button_color="#1e88e5", button_hover="#1565c0"):
    # CSS for scrollable form and colored inputs/buttons
    st.markdown(
        f"""
        <style>
        /* Scrollable form container */
        div[data-testid="stForm"] {{
            max-height: {height}px;
            overflow-y: auto;
            padding: 10px;
        
            border-radius: 10px;
        }}

        /* Form header */
        .stHeader h2, .stHeader h1 {{
            color: #1e88e5;
            font-weight: 700;
        }}

        /* Labels */
        label {{
            font-weight: 600;
            color: #424242;
        }}

        /* Input fields */
        .stTextInput>div>div>input, 
        .stNumberInput>div>div>input, 
        .stDateInput>div>div>input {{
            background-color: #ffffff;
            border-radius: 5px;
            padding: 5px;
        }}

        /* Submit button */
        div.stButton>button {{
            background-color: {button_color};
            color: white;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 8px;
        }}

        div.stButton>button:hover {{
            background-color: {button_hover};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Add New Employee")

    with st.form("employee_form"):
        # Personal Info
        first_name = st.text_input("First Name", max_chars=50)
        last_name = st.text_input("Last Name", max_chars=50)
        email = st.text_input("Email")
        phone_number = st.text_input("Phone Number (Optional, e.g., +12345678901)")
        house_number = st.text_input("House Number (Optional)")
        street = st.text_input("Street (Optional)")
        apartment = st.text_input("Apartment (Optional)")
        city = st.text_input("City")
        state = st.text_input("State")
        country = st.text_input("Country")
        zip_code = st.text_input("Zip Code (5 digits or 5-4 digits)")

        # Employee Info
        employee_code = st.text_input("Employee Code (Format: FD12345)")
        department = st.text_input("Department")
        position = st.text_input("Position")
        salary = st.number_input("Salary (Optional)", min_value=0.0, step=100.0)
        date_of_birth = st.date_input("Date of Birth", min_value=date(1900, 1, 1),
                                      max_value=date.today())
        date_of_joining = st.date_input("Date of Joining", min_value=date(2000, 1, 1),
                                        max_value=date.today())

        submitted = st.form_submit_button("Add Employee")

        if submitted:
            # Validations
            errors = []
            if not re.match(r'^FD\d{5}$', employee_code):
                errors.append("Employee Code must be in format FD followed by 5 digits.")
            if phone_number and not re.match(r'^\+?\d{10,15}$', phone_number):
                errors.append("Phone Number must be 10-15 digits, optional leading '+'.")
            if not re.match(r'^\d{5}(-\d{4})?$', zip_code):
                errors.append("Zip Code must be 5 digits or 5-4 digits (12345 or 12345-6789).")
            if salary > 150000:
                errors.append("Salary must be less than 150000.")

            if errors:
                for error in errors:
                    st.error(error)
                return

            # Construct payload
            payload = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number or None,
                "house_number": house_number or None,
                "street": street or None,
                "apartment": apartment or None,
                "city": city,
                "state": state,
                "country": country,
                "zip_code": zip_code,
                "employee_code": employee_code,
                "department": department,
                "position": position,
                "salary": salary if salary > 0 else None,
                "date_of_birth": date_of_birth.isoformat(),
                "date_of_joining": date_of_joining.isoformat()
            }

            # Call API
            try:
                response = add_employee(payload)
                if response.status_code == 201:
                    st.success(f"Employee {first_name} {last_name} added successfully!")
                else:
                    st.error(f"Error: {response.json().get('detail') or response.json()}")
            except Exception as e:
                st.error(f"Failed to add employee: {str(e)}")
