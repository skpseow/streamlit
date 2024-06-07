import streamlit as st

def calculate_contributions(age, salary):
    if age > 65:
        employer_contribution = salary * 0.075
        employee_contribution = salary * 0.05
    elif age > 60:
        employer_contribution = salary * 0.09
        employee_contribution = salary * 0.075
    elif age > 55:
        employer_contribution = salary * 0.13
        employee_contribution = salary * 0.13
    else:
        employer_contribution = salary * 0.17
        employee_contribution = salary * 0.20
    return employer_contribution, employee_contribution

def main():
    st.title("CPF Contribution Calculator")
    
    age = st.number_input("What is your age?", min_value=0, step=1)
    salary = st.number_input("What is your salary?", min_value=0)
    
    if st.button("Calculate"):
        employer_contribution, employee_contribution = calculate_contributions(age, salary)
        st.write(f"Employer contribution is: ${employer_contribution}")
        st.write(f"Employee contribution is: ${employee_contribution}")

if __name__ == "__main__":
    main()
