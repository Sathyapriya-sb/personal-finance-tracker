import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        transactions = st.session_state.transactions
    except AttributeError:
        st.session_state.transactions = []
        transactions = []
    return transactions

def generate_insights():
    st.title("Insights")
    transactions = load_data()
    if transactions:
        income_transactions = [t for t in transactions if t["Type"] == "Income"]
        expense_transactions = [t for t in transactions if t["Type"] == "Expense"]

        st.subheader("Income Insights")
        income_by_category = {}
        for transaction in income_transactions:
            income_by_category[transaction["Category"]] = income_by_category.get(transaction["Category"], 0) + transaction["Amount"]

        # Convert income_by_category to a DataFrame for tabular display
        income_df = pd.DataFrame(income_by_category.items(), columns=["Category", "Amount"])
        st.write("Income by Category:")
        st.table(income_df)


        fig, ax = plt.subplots()
        ax.pie(income_by_category.values(), labels=income_by_category.keys(), autopct='%1.1f%%')
        st.pyplot(fig)

        st.subheader("Expense Insights")
        expense_by_category = {}
        for transaction in expense_transactions:
            expense_by_category[transaction["Category"]] = expense_by_category.get(transaction["Category"], 0) + transaction["Amount"]

        # Convert expense_by_category to a DataFrame for tabular display
        expense_df = pd.DataFrame(expense_by_category.items(), columns=["Category", "Amount"])
        st.write("Expense by Category:")
        st.table(expense_df)


        fig, ax = plt.subplots()
        ax.pie(expense_by_category.values(), labels=expense_by_category.keys(), autopct='%1.1f%%')
        st.pyplot(fig)

        st.subheader("Top Expense Categories:")
        sorted_expense = sorted(expense_by_category.items(), key=lambda x: x[1], reverse=True)
        st.write(sorted_expense)
    else:
        st.warning("No transactions found!")

if __name__ == "__main__":
    generate_insights()