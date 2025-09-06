import streamlit as st

# STREAMLIT UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fifth power.")

# Get user input
n=st.number_input("Enter a number", value=1, step=2)

# calculate result
square = n**2
cube = n**3
fifth_power = n**5

# Display results
st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is {cube}")
st.write(f"The fifth power of {n} is {fifth_power}")