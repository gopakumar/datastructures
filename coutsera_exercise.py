hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Rate")
rate = float(rate)

if int(h)>40:
    extra = h-40
    pay = 40*rate+float(extra)*1.5*rate
else:
    pay = h * rate
print (pay)



