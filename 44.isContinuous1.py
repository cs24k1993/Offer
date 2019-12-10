def isContinuous(list):
    for i in range(len(list)):
        if list[i] == "A":
            list[i] = 1
            continue
        elif list[i] == "J":
            list[i] == 11
            continue
        elif list[i] == "Q":
            list[i] == 12
            continue
        elif list[i] == "K":
            list[i] == 13
            continue
        elif i >= "1" and i <= "10":
            continue
        else:
            print "Wrong input!"

    list.sort()
    list = [int(j) for j in list]

    for i in range(len(list)-1):
        if list[i+1] - list[i] == 1:
            if i == len(list)-2:
                print "YES"
            else:
                continue
        else:
            print "NOT"

list = ["Q","2","3","4","5"]
isContinuous(list)



