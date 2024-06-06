import streamlit as st

def categorize_income(income):
    if income > 8000:
        return 'High income'
    elif income > 4000:
        return 'Medium high income'
    elif income > 2000:
        return 'Medium income'
    elif income > 1000:
        return 'Medium low income'
    else:
        return 'Low income'

def main():
    st.title('Income Categorization App')
    income = st.number_input('What is your income?', min_value=0)
    
    if st.button('Categorize Income'):
        income_level = categorize_income(income)
        st.write(f'Your income level is: {income_level}')

if __name__ == "__main__":
    main()
