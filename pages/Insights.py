import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def connect_db():
    conn = sqlite3.connect("transactions.db")
    return conn

def load_data():
    conn = connect_db()
    try:
        df = pd.read_sql("SELECT * FROM transactions", conn)
    except pd.io.sql.DatabaseError:
        df = pd.DataFrame(columns=["Type", "Name", "Category", "Amount", "Date"])
    conn.close()
    return df

def generate_insights():
    st.title("Insights")
    df = load_data()
    if not df.empty:
        income_df = df[df["Type"] == "Income"]
        expense_df = df[df["Type"] == "Expense"]

        st.subheader("Income Insights")
        income_by_category = income_df.groupby("Category")["Amount"].sum()
        st.write("Income by Category:")
        st.write(income_by_category)

        fig, ax = plt.subplots()
        ax.pie(income_by_category, labels=income_by_category.index, autopct='%1.1f%%')
        st.pyplot(fig)

        st.subheader("Expense Insights")
        expense_by_category = expense_df.groupby("Category")["Amount"].sum()
        st.write("Expense by Category:")
        st.write(expense_by_category)

        fig, ax = plt.subplots()
        ax.pie(expense_by_category, labels=expense_by_category.index, autopct='%1.1f%%')
        st.pyplot(fig)

        st.subheader("Top Expense Categories:")
        sorted_expense = expense_by_category.sort_values(ascending=False)
        st.write(sorted_expense)
    else:
        st.warning("No transactions found!")

if __name__ == "__main__":
    generate_insights()