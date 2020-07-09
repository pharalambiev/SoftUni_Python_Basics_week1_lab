days = int(input())
cooks = int(input())
cake_count = int(input())
wafle_count = int(input())
pancake_count = int(input())

cake = 45
wafle = 5.80
pancake = 3.20

cake_income = cake_count*cake
wafle_income = wafle_count*wafle
pancake_income = pancake_count*pancake

daily_income = (cake_income+wafle_income+pancake_income)*cooks
total_income = daily_income*days
total_income = total_income - 1/8*total_income
print(total_income)