x=int(input('enter a decimal number,please:'))
result=[]
while x>0:
    result.append(x%2)
    x//=2
result.reverse()
print('the binary number is  :',result)

