with open('travels.txt','r', encoding='utf-8-sig') as f:
    max_gruz = [0,0,0]
    for i in f:
        s = i.split() 
        print(s)
        if s[0] == '1':
            print(s[6])
            max_gruz[0] += int(s[6])
        elif s[0] == '2':
            print(s[6])
            max_gruz[1] += int(s[6])
        elif s[0] == '3':
            print(s[6])
            max_gruz[2] += int(s[6])
    print(max(max_gruz))
with open('travels.txt','r', encoding='utf-8-sig') as f:
    sum = 0
    for i in f:
        s = i.split() 
        print(s)
        if s[2] == 'Липки':
            sum += int(s[6])
    print(sum)
with open('travels.txt','r', encoding='utf-8-sig') as f:
    sum_rast = 0
    for i in f:
        s = i.split() 
        print(s)
        if s[0] == '1':
            sum_rast += int(s[4])
    print(sum_rast)

        