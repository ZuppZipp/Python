def funct(*args):
    args+= args
    print('value is', args)

funct(1,2,3)
funct(10,20,20)

def cal(age,food,cig):
    ans= (100*age)+(food*3.5)-(cig*2)
    print('age lived is',ans)

amit = [26,2,0]
cal(*amit)
