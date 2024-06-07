import streamlit as st

def grocery(order):
    discount = 25 if order > 200 else 0
    disc_amt = discount * order / 100
    tax = 0.07 * (order - disc_amt)
    return discount, tax

def main():
    st.title("Grocery Discount and Tax Calculator")
    
    order_options = [i * 100 for i in range(1, 11)]  # Generate options with intervals of 100
    order = st.selectbox("How much is your order?", options=order_options)
    
    if st.button("Calculate"):
        discount, tax = grocery(order)
        st.write(f"The discount is ${discount}")
        st.write(f"The tax is ${round(tax, 2)}")

if __name__ == "__main__":
    main()
