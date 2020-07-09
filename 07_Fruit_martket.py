price_strawberries = float(input())
bannanas_amnt = float(input())
oranges_amnt = float(input())
raspberries_amnt = float(input())
strawberries_amnt = float(input())

rasp_price = price_strawberries*0.5
orange_price = rasp_price - rasp_price*0.4
bannana_price = rasp_price - rasp_price*0.8

money = (price_strawberries*strawberries_amnt)+(bannanas_amnt*bannana_price)+(orange_price*oranges_amnt)+(raspberries_amnt*rasp_price)

print (money)