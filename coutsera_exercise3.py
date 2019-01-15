def computepay(h,rate):
    if int(h)>40:
        extra = h-40
        pay = 40*rate+float(extra)*1.5*rate
    else:
        pay = h * rate
        print (pay)
    return pay

hrs = input("Enter Hours:")
rate = input ("Enter Rate")
p = computepay(float(hrs),float(rate))
print("Pay",p)
