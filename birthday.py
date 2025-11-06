import streamlit as st
from datetime import date, datetime

st.title("🎂 Age Calculator")


birth_date = st.date_input("Select your Birth Date:",
                           min_value=date(1900, 1, 1),  # ← gives full range
                           max_value=date.today()
                           )


today = date.today()
age_years = today.year - birth_date.year
age_months = today.month - birth_date.month
age_days = today.day - birth_date.day


if age_days < 0:
    age_months -= 1
    age_days += 30

if age_months < 0:
    age_years -= 1
    age_months += 12


if birth_date:
    st.subheader(f"✅ Your Age is:")
    st.write(f"**{age_years} years, {age_months} months, {age_days} days**")

# Extra - Show Birth Year
st.write("**Birth Year:**", birth_date.year)

st.write('-arik')
st.write('(demo/practice)')



