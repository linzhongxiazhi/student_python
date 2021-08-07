ls =[1,3,5,7,9,11,13,15,30,2,0]
for x in  ls:
    for y in ls:
        for z in  ls:
            if x+y+z ==30:
                print("{}+{}+{}=30".format(x,y,z))
            else:
                pass