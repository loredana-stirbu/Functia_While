l=0
t=0
tp=0
tn=0
ntp=0
ntn=0
while l < 12:
    t=(eval(input("Dati temperatura :")))
    if t>=0:
        tp += t
        ntp += 1
    else:
        tn += t
        ntn += 1
    l += 1    

print("Media temperaturilor pozitive: ", round(tp/ntp,2))            
print("Media temperaturilor negative: ", round(tn/ntn,2))