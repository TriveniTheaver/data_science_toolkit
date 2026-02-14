import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Data Science Toolkit")

menu = st.sidebar.selectbox(
    "Select Tool",
    ["Statistical Calculator", "Loan Calculator", "CSV Analyzer"]
)

# ------------------------------
# 1. Statistical Calculator
# ------------------------------
if menu == "Statistical Calculator":
    st.header("Statistical Calculator")

    numbers = st.text_area("Enter numbers separated by commas")

    if st.button("Calculate Statistics"):
        try:
            data = np.array([float(x) for x in numbers.split(",")])

            st.write("Mean:", np.mean(data))
            st.write("Median:", np.median(data))
            st.write("Standard Deviation:", np.std(data))
            st.write("Variance:", np.var(data))
            st.write("Min:", np.min(data))
            st.write("Max:", np.max(data))

        except:
            st.error("Please enter valid numbers")


# ------------------------------
# 2. Loan Calculator
# ------------------------------
elif menu == "Loan Calculator":
    st.header("Loan EMI Calculator")

    principal = st.number_input("Loan Amount")
    rate = st.number_input("Interest Rate (%)")
    years = st.number_input("Loan Period (years)")

    if st.button("Calculate EMI"):
        r = rate / (12 * 100)
        n = years * 12

        emi = principal * r * (1 + r)**n / ((1 + r)**n - 1)
        total_payment = emi * n
        interest = total_payment - principal

        st.write("Monthly EMI:", round(emi, 2))
        st.write("Total Payment:", round(total_payment, 2))
        st.write("Total Interest:", round(interest, 2))


# ------------------------------
# 3. CSV Analyzer (Impressive)
# ------------------------------
elif menu == "CSV Analyzer":
    st.header("CSV Data Analyzer")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file:
        df = pd.read_csv(file)

        st.subheader("Data Preview")
        st.dataframe(df.head())

        st.subheader("Basic Statistics")
        st.write(df.describe())

        st.subheader("Missing Values")
        st.write(df.isnull().sum())
