import streamlit as st
import pandas as pd

def load_data():
    try:
        df = pd.read_csv("transactions.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Type", "Name", "Category", "Amount", "Date"])
    return df

def save_data(df):
    df.to_csv("Transactions.csv", index=False)

def add_transaction():
    st.title("Add Transaction")
    transaction_type = st.selectbox("Select Transaction Type", ["Select", "Income", "Expense"])
    name = st.text_input("Enter Name")
    col1, col2 = st.columns(2)
    category = col1.selectbox("Select Category", ["Select"] + categories.get(transaction_type, []))
    amount = col2.number_input("Enter Amount", min_value=0, value=0)
    date = st.date_input("Select Date")
    st.text("")
    
    if st.button("Add Transaction"):
        if transaction_type == "Select" or amount == 0 or not name or category == "Select":
            st.warning("Please ensure that you have filled all the fields.")
        else:
            new_row = {"Type": transaction_type, "Name": name, "Category": category, "Amount": amount, "Date": date}
            df = load_data()
            new_df = pd.DataFrame([new_row])
            df = pd.concat([df, new_df], ignore_index=True)
            save_data(df)
            st.success("Transaction added successfully!")

if __name__ == "__main__":
    categories = {
        "Income": ["Salary", "Allowance", "Freelance", "Gift", "Other"],
        "Expense": ["Housing", "Transportation", "Food", "Groceries", "Utilities", "Grooming", "Entertainment", "Healthcare", "Other"]
    }
    add_transaction()
