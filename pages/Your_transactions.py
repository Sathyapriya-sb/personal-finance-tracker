import streamlit as st

def load_data():
    try:
        transactions = st.session_state.transactions
    except AttributeError:
        st.session_state.transactions = []
        transactions = []
    return transactions

def main():
    st.title("Your Transactions")
    transactions = load_data()
    transactions_sorted = sorted(transactions, key=lambda x: x["Date"], reverse=True)

    # Calculate sum of income, sum of expenses, and total
    income = sum(t["Amount"] for t in transactions if t["Type"] == "Income")
    expenses = sum(t["Amount"] for t in transactions if t["Type"] == "Expense")
    total = income - expenses
    
    # Display sums as three columns next to each other
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("##### Income:", income)
    with col2:
        st.write("##### Expenses:", expenses)
    with col3:
        st.write("##### Balance:", total)

    if transactions:
        st.table(transactions_sorted)
    else:
        st.warning("No transactions found!")

if __name__ == "__main__":
    main()