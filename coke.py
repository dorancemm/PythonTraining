price = 50
currency_denominations = {5, 10, 25}
income = 0
outstanding_balance = price

while outstanding_balance > 0:
    coin_input = int(input("Enter a coin (5, 10 or 25): "))
    if coin_input in currency_denominations:
        income += coin_input
        outstanding_balance -= coin_input
        print ("Outstandig balance: {} cents".format(outstanding_balance))
    else:
        print ("Coin not accepted. The coin must be 5, 10 or 25 cents.")  

if outstanding_balance == 0:
    print("Tank you!")
else:
    exchange = income - price
    print("Exchange: {}".format(exchange)) 
