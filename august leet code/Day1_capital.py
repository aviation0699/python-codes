p=[]
        for i in word:
            if i.isupper()==True:
                p.append(1)
            else:
                p.append(0)
        if p[0]==1 and sum(p)==1:
            return 1
        elif sum(p)==0:
            return 1
        elif sum(p)==len(word):
            return 1
        else:
            return 0
