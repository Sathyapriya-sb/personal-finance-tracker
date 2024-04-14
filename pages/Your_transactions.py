import streamlit as st
import pandas as pd

def load_data():
    try:
        df = pd.read_csv("transactions.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Type", "Name", "Category", "Amount", "Date"])
    return df

def main():
    st.title("Your Transactions")
    df = load_data()
    df = df.sort_values(by="Date", ascending=False).reset_index(drop=True)
    df.index += 1  # Increment index by 1

    # Calculate sum of income, sum of expenses, and total
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    total = income - expenses
    
    # Display sums as three columns next to each other
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("##### Income:", income)
    with col2:
        st.write("##### Expenses:", expenses)
    with col3:
        st.write("##### Balance:", total)

    st.table(df)

if __name__ == "__main__":
    main()
