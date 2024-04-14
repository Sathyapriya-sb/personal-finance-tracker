import streamlit as st

def load_data():
    try:
        transactions = st.session_state.transactions
    except AttributeError:
        st.session_state.transactions = []
        transactions = []
    return transactions

def save_data(transactions):
    st.session_state.transactions = transactions

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
            new_transaction = {"Type": transaction_type, "Name": name, "Category": category, "Amount": amount, "Date": date}
            transactions = load_data()
            transactions.append(new_transaction)
            save_data(transactions)
            st.success("Transaction added successfully!")

if __name__ == "__main__":
    categories = {
        "Income": ["Salary", "Allowance", "Freelance", "Gift", "Other"],
        "Expense": ["Housing", "Transportation", "Food", "Groceries", "Utilities", "Grooming", "Entertainment", "Healthcare", "Other"]
    }
    add_transaction()
