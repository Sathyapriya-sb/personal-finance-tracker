import streamlit as st
from pages import Add_transaction, Insights, Your_transactions

def main():
    st.title("Personal Finance Tracker")
    
    st.write("""
    Welcome to Personal Finance Tracker app! This app helps you track your income and expenses.
    
    With this app, you can:
    - Add new transactions
    - View insights into your income and expenses
    - Explore your transaction history
    
    Get started now by adding your first transaction!
    """)

    if st.button("Add your first transaction"):
        st.switch_page("pages/Add_transaction.py")
        
if __name__ == "__main__":
    main()