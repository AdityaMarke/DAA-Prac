def karatsuba(X, Y):

    if X < 10 or Y < 10:
        return X * Y
    
    m = min(len(str(X)), len(str(Y)))
    m2 = m // 2
    
    a, b = divmod(X, 10**m2)
    c, d = divmod(Y, 10**m2)
    
    ac = karatsuba(a, c) 
    apb_m_cpd = karatsuba((a + b), (c + d))
    bd = karatsuba(b, d)

    return ac * 10**(2 * m2) + (apb_m_cpd - ac - bd) * 10**m2 + bd

def square_large_number(number):
    return karatsuba(number, number)

num = int(input("Enter the Number: "))
result = square_large_number(num)
print("The square of" ,num, "is" ,result)