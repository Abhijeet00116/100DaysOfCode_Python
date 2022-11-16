def intgerToRoman(num):
    value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbols = ['M','CM','D','CD','C','CD','L','XL','X','IX','V','IV','I']
    
    roman = ""
    i=0
    while num>0:
        division = num // value[i]
        num = num % value[i]
        while division:
            roman = roman + symbols[i]
            division = division -1
        
        i = i+1
    return roman
if __name__=='__main__':
    n = int(input("ENTER AN INTEGER -> "))
    print("Roman value of ",n,"is",end=" ")
    print("-> ",intgerToRoman(n))