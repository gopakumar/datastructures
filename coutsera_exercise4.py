largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            num = float(num)
            if largest is None or largest < num:
                largest = num
            if smallest is None or smallest > num:
                smallest = num            
        except:
            print ("Invalid input")
            continue

print("Maximum is ",int(largest))
print("Minimun is ",int(smallest))

    

