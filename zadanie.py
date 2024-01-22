kol = 0
with open(r'Perepis.txt', 'r') as f:
    
    print('punkt_a')
    for i in f:
        s = i.split() 
        if int(s[3][6:10]) < 1978:
            print(s[0])
            kol+=1
            
    print(kol)
with open(r'Perepis.txt', 'r') as f:
    print('punkt_b')
    fist_chislo = int(input())
    second_chislo = int(input())

    for i in f:
        s = i.split() 
        if (fist_chislo < int(s[3][6:10]) and int(s[3][6:10]) < second_chislo):
            print(s[0],s[1],s[2],s[3][6:10])






