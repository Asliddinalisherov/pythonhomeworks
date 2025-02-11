def invest(amount, rate, years):
    for i in range(1, years+1, 1):
        amount = round(amount * (1+ rate), 2)
        print(f"year {i}: ${amount}")

amount = int(input())
rate = float(input("Rate in percent: %")) * (1/100)
years = int(input())
invest(amount, rate, years)