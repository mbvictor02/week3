principal_loan_ammount = float(input("Principal load amount: "))  
annual_interest_rate = float(input("Annual interest rate: "))                
loan_term = float(input("Loan term (in years): "))  

months_number = float(loan_term*12)                               
monthly_interest_rate = float(annual_interest_rate/12) 

monthly_payment = float(principal_loan_ammount/((((1+monthly_interest_rate)**months_number)-1)/(monthly_interest_rate*(1+monthly_interest_rate)**months_number)))
print(f"Your monthly payment is {monthly_payment}")