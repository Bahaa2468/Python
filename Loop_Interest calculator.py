print ("loan Calculator")
user_loan= int(input ("Loan amount:$ "))
user_Years= int(input("Duration in years:"))
user_Interest= float(input("Interest: "))
requested_loan=user_loan
payout_months = user_Years * 12

for i in range (user_Years):
    interest = float (user_Interest/100)
    interest_amount = float(interest*user_loan)
    user_loan+=interest_amount
    user_loan=round(user_loan,2)
    user_loan_interest = float(user_loan + interest_amount)
    print("Year",i+1," the amount is: ",user_loan)

monthly_installment= user_loan/payout_months
monthly_installment=round(monthly_installment,2)
net_interest= user_loan-requested_loan
net_interest=round(net_interest,2)
print ("""
       The amount requested: $ """,requested_loan,"""
       Duration of Years: """,user_Years,"""
       You will pay in interest: $ """,net_interest,"""
       The total amount payable: $ """,user_loan,"""
       Your monthly installement: $ """,monthly_installment)
print()
print ("Thank ... You ... For ... running ... my ... Code")
print ("B...A...H....A...A")
