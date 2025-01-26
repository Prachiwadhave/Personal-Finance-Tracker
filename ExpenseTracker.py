import streamlit as st
import os
import csv
from datetime import datetime

# File to store expenses
file_name = os.path.join(os.path.dirname(__file__), "expenses.csv")

# Initialize file
if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Transaction Type", "Category", "Amount", "Description", "Payment Method"])

st.title("Expense Tracker")

# Menu
menu = st.sidebar.selectbox("Menu", ["Add Expense", "View Expenses", "Export Data"])

if menu == "Add Expense":
    st.header("Add Expense")
    category = st.text_input("Category (e.g., Food, Transport):")
    amount = st.number_input("Amount:", min_value=0.0)
    description = st.text_area("Description:")
    date = st.date_input("Date:", value=datetime.now().date())
    transaction_type = st.selectbox("Transaction Type:", ["Credit", "Debit"])
    payment_method = st.selectbox("Payment Method:", ["UPI", "Card", "Cash", "Check"])
    
    if st.button("Add Expense"):
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, transaction_type, category, amount, description, payment_method])
        st.success(f"Added {transaction_type}: {category} - {amount} - {description}")

elif menu == "View Expenses":
    st.header("View Expenses")
    try:
        with open(file_name, mode='r') as file:
            data = list(csv.reader(file))
        if len(data) > 1:
            st.table(data[1:])
        else:
            st.info("No expenses to show.")
    except FileNotFoundError:
        st.error("Expenses file not found!")

elif menu == "Export Data":
    st.header("Export Data")
    with open(file_name, mode='rb') as file:
        st.download_button(
            label="Download Expenses CSV",
            data=file,
            file_name="expenses.csv",
            mime="text/csv"
        )
