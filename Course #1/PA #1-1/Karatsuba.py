def karatsuba(x,y):
    # Base Case: if both x and y are single digit integers
    # Then return the multilication product
    if x < 10 and y < 10:
        return x * y

    # General Case: divide and conquer
    # Recursively split x into a, b and y into c, d
    # e.g. 1st step   x = 1234 -> a = 12, b = 34
    #                 y = 567  -> c = 5,  d = 67
    # Then returns (a*c)*10000 + (a*d+b*c)*100 + b*d
    # The above step will be called recursively until it hits the Base Case
    else:
        n = max( len(str(x)) , len(str(y)) ) // 2 #split longer length in half
        digits = 10**(n)

        a = x // digits
        b = x % digits
        c = y // digits
        d = y % digits

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_bc = karatsuba(a + b,c + d) - ac - bd
        # a*d+b*c = (a+b)*(c+d) - a*c - b*d

        return ac*(digits**2) + ad_bc*(digits) + bd

results=karatsuba(3141592653589793238462643383279502884197169399375105820974944592\
            ,2718281828459045235360287471352662497757247093699959574966967627)
print(results)
#8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
