import streamlit as st

def grocery(order):
    discount = 25 if order > 200 else 0
    disc_amt = discount * order / 100
    tax = 0.07 * (order - disc_amt)
    return discount, tax

def main():
    st.title("Grocery Discount and Tax Calculator")
    
    order = st.number_input("How much is your order?", min_value=0.0)
    
    if st.button("Calculate"):
        discount, tax = grocery(order)
        st.write(f"The discount is ${discount}")
        st.write(f"The tax is ${round(tax, 2)}")

if __name__ == "__main__":
    main()
