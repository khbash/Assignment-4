def process_princes(prices, discount_percent):
    new = []

    for price in prices:
        if price > 0:
            discount = price * (1 - discount_percent/100)
            new.append(round(discount))
    return(new)

old = [1000, -50, 300, 0, 500]
result=process_princes(old, 20)
print(result)