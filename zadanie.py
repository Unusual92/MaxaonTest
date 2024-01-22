kol = 0
diaposon = int(input())
with open(r'Perepis.txt', 'r') as f:
    
    
    for i in f:
        
        s = i.split() 
        print(s[3][6:10])
        if int(s[3][6:10]) < diaposon:
            print(s[0],s[1],s[2])
            kol+=1
print(kol)