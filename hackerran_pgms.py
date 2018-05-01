def helloworld():
    print "Hello World"

def plusMinus(arr):
    # Complete this function
    #    print arr
    pos = 0
    neg = 0
    zer = 0
    l = float(len(arr))
    for x in arr:

        if x >0:
            pos+=1
        elif x<0:
            neg+=1
        else:
            zer+=1

    print "%1.6f"% (pos/l)
    print "%1.6f"% (neg/l)
    print "%1.6f"% (zer/l)

def staircase(n):
    #
    # Write your code here.
    #
    for x in range(1,n+1):
        print "{}{}".format(" "*(n-x),"#"*x)

        
    

    
if (__name__ == "__main__"):
#    helloworld()
    
#    arr = [-4, 3, -9, 0, 4, 1]
#    plusMinus(arr)

    n = 6
    staircase(n)

        
