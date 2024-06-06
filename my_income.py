income = input('What is your income?' )
income = int(income)
if income > 8000:
    print('High income')
elif income > 4000:
    print('Medium high income')
elif income > 2000:
    print('Medium income')
elif income > 1000:
    print('Medium low income')
else:
    print("Low income")
