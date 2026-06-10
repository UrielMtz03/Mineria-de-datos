l=["manzana", "uva", "manzana", "pera", "pera"]
repeticiones={}
for n in l:
      if n in repeticiones:
        repeticiones[n]+=1
      else:
         repeticiones[n]=1
print(repeticiones)