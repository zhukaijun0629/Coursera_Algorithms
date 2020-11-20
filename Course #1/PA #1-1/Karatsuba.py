def karatsuba(x,y):
    if x<10 and y<10:
        return x*y
    else:
        n=max(len(str(x)),len(str(y)))

        a=x//(10**(n//2))
        b=x%(10**(n//2))
        c=y//(10**(n//2))
        d=y%(10**(n//2))

        ac=karatsuba(a,c)
        bd=karatsuba(b,d)
        abcd=karatsuba(a+b,c+d)-ac-bd

        return ac*(10**(2*(n//2)))+abcd*(10**(n//2))+bd
Results=karatsuba(3141592653589793238462643383279502884197169399375105820974944592\
            ,2718281828459045235360287471352662497757247093699959574966967627)
print(Results)
#8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
