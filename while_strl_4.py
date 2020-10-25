i=1
suma=0
produs=1
n=eval(input("Dati un numar:"))
while (i<=n):
    suma+=i
    produs*=i
    med=suma/n
    i+=1

print(" suma= ",suma)
print("produsul= ",produs)
print("media aritmetica= ",med)