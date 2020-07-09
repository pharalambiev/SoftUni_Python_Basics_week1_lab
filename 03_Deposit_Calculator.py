amount = float(input())
term = int(input())
annual_interest = float(input())

deposit = (amount*annual_interest)/100
deposit = deposit/12
deposit = (term*deposit)+amount
print (deposit)