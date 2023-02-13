def fraccionToBin(numero): #Método de la División Sucesiva por 2
 n = numero
 x = 1.0
 y = 0.0

 string = ""
 
 while x != 0.0: #termina cuando sea 0
    if y == 1.0: 
       n = n - 1.0              
    n = n*2

    new = str(n).split('.')
    x,y = float(new[1]),float(new[0]) 

    print(y)   

    string = string + str(int(y))


 print("la fraccion " + str(numero) + "  a Binario es: 0." + str(string) )
 
 
fraccionToBin(0.2) 
 
 



