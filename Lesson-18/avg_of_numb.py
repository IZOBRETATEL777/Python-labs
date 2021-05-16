sumd=0
Fin=open("input.txt" )
lst=Fin.readlines()
for s in lst:
    sumd+=int(s)
mean=sumd/len(lst)
Fout=open("output.txt","w")
Fout.write(str(mean))
Fin.close()
Fout.close()
