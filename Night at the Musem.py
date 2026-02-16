    n = input().strip()
     
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']
     
    tm = 0
    pos = 0
     
    for k in n:
        idx = l.index(k)
        diff = abs(idx - pos)
        tm += min(diff, 26 - diff)
        pos = idx
     
    print(tm)
