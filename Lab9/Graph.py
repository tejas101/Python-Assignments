__author__ = 'TR tr7550@rit.edu'
"""
CSCI-603: Ice-Maze Partial Solution
Author: Tejas Raval


"""

def makeGraphFunction(maze,g_nodes):
    for i in range(maze.__len__()):
        for j in range(maze[i].__len__()):
            # if i ==0 and j==0:
            #     try:
            #      g_nodes[maze[i][j]].append(maze[i][j])
            #     except KeyError:
            #      g_nodes[maze[i][j]] = [maze[i][j]]
            k=j
            #print(k)
            #left to right
            if maze[i][j]!=0:
             for k in range(k,maze[i].__len__()):
                if(maze[i][k]==0 or k==maze[i].__len__()-1):
                    break
             #print('k is ',k, 'when element is',maze[i][j])
             if(k==maze[i].__len__()-1):
                if(maze[i][k]==0):#if edge element is stone
                     if(maze[i][k-1]!=maze[i][j])  :#not to added duplicate element ie A to A
                      try:
                       g_nodes[maze[i][j]].append(maze[i][k-1])
                      except KeyError:
                       g_nodes[maze[i][j]] = [maze[i][k-1]]
                else:
                     if(maze[i][j]!=maze[i][k]):
                      try:
                       g_nodes[maze[i][j]].append(maze[i][k])
                      except KeyError:
                       g_nodes[maze[i][j]] = [maze[i][k]]
             if(k<maze[i].__len__()-1):
                   if(maze[i][j]!=maze[i][k-1]):
                    try:
                      g_nodes[maze[i][j]].append(maze[i][k-1])
                    except KeyError:
                      g_nodes[maze[i][j]] = [maze[i][k-1]]

             #now right to left
             k2=j
             if maze[i][j] != 0:
              for k2 in range(j,-1,-1):
                #print(k)
                if(maze[i][k2]==0 or k2==0):
                    break
             #print('k is ',k, 'when element is',maze[i][j])
              if(k2==0):
                if(maze[i][k2]==0):#if edge element is stone
                   if(maze[i][j]!=maze[i][k2+1]) :
                    try:
                        g_nodes[maze[i][j]].append(maze[i][k2+1])
                        #print('adding 111 ',maze[i][k2],'to ',maze[i][j])
                    except KeyError:
                        g_nodes[maze[i][j]] = [maze[i][k2+1]]
                else:
                   if(maze[i][j]!=maze[i][k2]):
                    try:
                      g_nodes[maze[i][j]].append(maze[i][k2])
                      #print('adding 222 ',maze[i][k2],'to ',maze[i][j])
                    except KeyError:
                      g_nodes[maze[i][j]] = [maze[i][k2]]
              if(k2>0):
                  if(maze[i][j]!=maze[i][k2+1]):
                    try:
                      g_nodes[maze[i][j]].append(maze[i][k2+1])
                      #print('adding 333 ', maze[i][k2+1], 'to ', maze[i][j])
                    except KeyError:
                      g_nodes[maze[i][j]] = [maze[i][k2+1]]

            #now  - top to bottom
            k3=i
            if maze[i][j]!=0:
             for k3 in range(k3,maze.__len__()):
                if(maze[k3][j]==0 or k3==maze.__len__()-1):
                    break
             #print('k is ',k, 'when element is',maze[i][j])
             if(k3==maze.__len__()-1):
                 if(maze[k3][j]==0):#if edge element is stone
                    if(maze[i][j]!=maze[k3 - 1][j]):
                        try:
                         g_nodes[maze[i][j]].append(maze[k3 - 1][j])
                        except KeyError:
                         g_nodes[maze[i][j]] = [maze[k3 - 1][j]]
                 else:
                     if(maze[i][j]!=maze[k3][j]):
                        try:
                          g_nodes[maze[i][j]].append(maze[k3][j])
                        except KeyError:
                          g_nodes[maze[i][j]] = [maze[k3][j]]
             if(k3<maze.__len__()-1):
                   if(maze[i][j]!=maze[k3-1][j]) :
                    try:
                     g_nodes[maze[i][j]].append(maze[k3-1][j])
                    except KeyError:
                     g_nodes[maze[i][j]] = [maze[k3-1][j]]

            #now bottom to up

            k4 = i
            if maze[i][j] != 0:
                       for k4 in range(i, -1,-1):
                           if (maze[k4][j] == 0 or k4 == 0):
                               break
                       # print('k is ',k, 'when element is',maze[i][j])
                       if (k4 == 0):
                           if (maze[k4][j] == 0):#if edge element is stone
                             if(maze[i][j]!=maze[k4 + 1][j]):
                               try:
                                   g_nodes[maze[i][j]].append(maze[k4 + 1][j])
                                   #print('adding ', maze[k4 + 1][j], 'to ', maze[i][j])
                               except KeyError:
                                   g_nodes[maze[i][j]] = [maze[k4 + 1][j]]
                           else:
                              if(maze[i][j]!=maze[k4][j]):
                               try:
                                   g_nodes[maze[i][j]].append(maze[k4][j])
                                   #print('adding ', maze[k4 + 1][j], 'to ', maze[i][j])
                               except KeyError:
                                   g_nodes[maze[i][j]] = [maze[k4][j]]
                       if (k4 > 0):
                          if(maze[i][j]!=maze[k4 + 1][j]):
                           try:
                               g_nodes[maze[i][j]].append(maze[k4 + 1][j])
                           except KeyError:
                               g_nodes[maze[i][j]] = [maze[k4 + 1][j]]



    #print(g_nodes)


    print(g_nodes)




if __name__ == "__main__":
        # Initialising the maze
        maze = [['A', 'B', 0, 'C','D'],
                ['E', 'F', 'G', 'H','I'],
                ['J', 'K', 'L', 'M', 'N'],
                ['O', 'P', 'Q', 0, 'R'],
                ['S', 0, 'T', 'U', 'V']]
        #print(maze[0][0])
        g_nodes= dict()
        #g_nodes["Escape Node"] = maze[1][4]
maze=makeGraphFunction(maze,g_nodes)
