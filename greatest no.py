no1=int(input('enter no1'))
no2=int(input('enter no2'))
no3=int(input('enter no3'))
if (no1>no2) and (no2>no3):
    greatest=no1
elif(no2>no1) and (no2>no3):

   greatest=no2
else:
    greatest=no3
    print('the greatest no is',greatest)
