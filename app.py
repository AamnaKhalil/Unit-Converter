import streamlit as st

# Set app title and description
st.title("🧲⏳ Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Enter a value, choose a unit, and get the converted result instantly! 🌡")

# Sidebar for category selection
conversion_type = st.sidebar.radio("Select Conversion Type:", ["Length", "Weight", "Time"])

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, 
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 1000, "Milligrams": 1_000_000, "Pounds": 2.20462, "Ounces": 35.274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_time(value, from_unit, to_unit):
    time_units = {
        "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400
    }
    return value * (time_units[to_unit] / time_units[from_unit])

# User input for value
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Choose units based on conversion type
if conversion_type == "Length":
    from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    if from_unit != to_unit:
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    if from_unit != to_unit:
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Time":
    from_unit = st.selectbox("From:", ["Seconds", "Minutes", "Hours", "Days"])
    to_unit = st.selectbox("To:", ["Seconds", "Minutes", "Hours", "Days"])
    if from_unit != to_unit:
        result = convert_time(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# Footer
st.markdown("💡 **Tip:** Select a conversion type from the sidebar to begin!")
