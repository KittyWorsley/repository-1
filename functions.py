#a=celcius
#b=fahrenhet
#c=total

option=input("do you want me to convert the temperature into celcius or fahrenheit?")
if option=="c":
    fahrenheit =int(input("please put the temperature into fahrenheit"))
    total=fahrenheit - 32/1.8
    print(fahrenheit, "converted into celcius is",total)
    
elif option=="f":
    fahrenheit=int(input("please put the temperature  into celcius"))
total=celcius - 9/5 + 32
print(celcius,"converted into fahrenheit",total)
