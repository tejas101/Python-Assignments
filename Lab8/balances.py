__author__ = 'TR tr7550@rit.edu'
"""
CSCI-603: Balance - Code to find unknown weight X 
Author: Tejas Raval


"""
def balances():
    gotIN=0
    gotAT=0
    workList=[]
    workListLine = []
    workListLoc = []
    #workListNumber=[]
    with open('file.txt', 'r') as fobj:
        all_lines = [[(num) for num in line.split()] for line in fobj]
    print(all_lines)
    len=all_lines.__len__()
    for i in range(len):
        #print(i)
        for j in range(all_lines[i].__len__()):
            #dataIs= all_lines[i][j]
            if str(all_lines[i][j]) == 'X':
                gotIN=i
                gotAt=j
                break
    # print("Got X in list number ",gotIN)
    # print("Got at ", gotAt)
    # print("there is ", all_lines[gotIN][gotAt])
    for i in range(gotIN, -1, -1):
            for j in range(1,all_lines[i].__len__()):
                if all_lines[i][j].startswith('B'):
                    temp = list(all_lines[i][j])
                    workList.append(int(temp[1])-1)
                    workListLine.append(i)
                    workListLoc.append(j)

    ##print("WorkList", workList)
    ##print("WorkListLine", workListLine)
    ##print("WorkListLoc", workListLoc)

    #tempWorkLine = workListLine
    #tempWorkLine.sort()

    # for i in workList:
    #     temp = list(i)
    #     workListNumber.append(int(temp[1])-1)
    #     #print("I is ",list(i))
    # print("workListNumber", workListNumber)
    #sum=0
    #print("hereer",len(workList))
    for i in range(workList.__len__() - 1, -1, -1) :
        temp=workList[i]
        #print(temp)
        sum=0
        sumBalance=0
        for j in range(1, all_lines[temp].__len__(),2):
          #print("Here",j)
          #print("adding ",all_lines[i][j+1])
          sumBalance += (int(all_lines[i][j]) * int(all_lines[i][j + 1]))
          sum += int(all_lines[temp][j+1])
        #print(sumBalance)
        if sumBalance != 0:
            print("Beam is not balance")
            quit()
        #print("Putting sum ",sum,"on ",all_lines[workListLine[i]][workListLoc[i]])
        all_lines[workListLine[i]][workListLoc[i]]=sum

    sum=0
    #print(all_lines)
    for i in range(1,all_lines[gotIN].__len__(),2):
        #print("It is",(i+1))
        if (i+1) != gotAt :
          sum += (int(all_lines[gotIN][i]) * int(all_lines[gotIN][i + 1]))
        answer=abs(sum/int(all_lines[gotIN][gotAt-1]))


    all_lines[gotIN][gotAt]  = answer
    workListFinal = []
    workListLineFinal = []
    workListLocFinal = []
    len = all_lines.__len__()
    for i in range(len):
        for j in range(1, all_lines[i].__len__(), 2):
                checkThis=all_lines[i][j+1]
                if str(checkThis).startswith('B'):
                    temp = all_lines[i][j+1]
                    #print("GGG", temp)
                    if all_lines[i][j+1] != "B":
                        workListFinal.append(int(temp[1])-1)
                        workListLineFinal.append(i)
                        workListLocFinal.append(j)

    for i in range(workListFinal.__len__() - 1, -1, -1) :
        temp=workListFinal[i]
        #print(temp)
        sum=0
        sumBalance=0
        for j in range(1, all_lines[temp].__len__(),2):
          #print("Here",j)
          #print("adding ",all_lines[i][j+1])
          sumBalance += (int(all_lines[i][j]) * int(all_lines[i][j + 1]))
          sum += int(all_lines[temp][j+1])
        #print(sumBalance)
        if sumBalance != 0:
            print("Beam is not balance")
            quit()
        #print("Putting sum ",sum,"on ",all_lines[workListLineFinal[i]][workListLocFinal[i]+1])
        all_lines[workListLineFinal[i]][workListLocFinal[i]+1]=sum
    #print(all_lines)
    # print(all_lines)
    # len = all_lines.__len__()
    sumBalanceFinal=0
    for i in range(len):
    #     # print(i)
         for j in range(1,all_lines[i].__len__(),2):
             if not (all_lines[i][j].startswith("B")):
              sumBalanceFinal += (int(all_lines[i][j]) * int(all_lines[i][j + 1]))

         if sumBalanceFinal != 0:
            print("Beam is not balance")
            quit()
    #print(all_lines)
    print("The Value of X is",answer)


if __name__ == '__main__':
    balances()
