#list of Minimum Spanning Tree from MST_2.py

MST = [[73, 47, 32], [59, 71, 52], [21, 28, 100], [12, 42, 205], [76, 77, 266], [1, 75, 271], [23, 76, 305], [76, 68, 327], [28, 70, 345], [76, 4, 358], [2, 9, 374], [30, 67, 416], [5, 74, 502], [56, 7, 542], [1, 50, 552], [37, 62, 580], [51, 21, 583], [33, 34, 689], [4, 30, 871], [9, 61, 905], [23, 2, 918], [23, 19, 965], [58, 3, 1051], [37, 78, 1054], [47, 54, 1083], [19, 17, 1092], [76, 37, 1150], [78, 32, 1154], [23, 31, 1200], [20, 53, 1228], [22, 52, 1234], [76, 14, 1279], [62, 13, 1330], [54, 24, 1391], [68, 27, 1425], [14, 10, 1431], [23, 63, 1439], [66, 60, 1450], [77, 33, 1475], [57, 1, 1483], [20, 18, 1491], [34, 64, 1566], [76, 51, 1574], [14, 66, 1594], [73, 72, 1661], [52, 49, 1730], [46, 79, 1744], [21, 58, 1836], [65, 40, 1848], [3, 8, 1923], [47, 15, 1926], [14, 11, 1936], [5, 0, 1941], [23, 43, 2005], [7, 44, 2065], [56, 35, 2093], [69, 38, 2118], [73, 57, 2178], 
[1, 20, 2292], [10, 59, 2301], [76, 69, 2325], [76, 29, 2359], [63, 25, 2415], [66, 48, 2488], [43, 46, 2506], [46, 41, 2609], [76, 12, 2659], [65, 
16, 2675], [73, 36, 2788], [19, 39, 2797], [12, 73, 2845], [28, 56, 2853], [19, 26, 2955], [44, 55, 2970], [12, 22, 2975], [51, 5, 2991], [48, 6, 3023], [22, 65, 3042], [51, 45, 3121]]

MST[6][0] ='A'
MST[6][1] = 'B'
MST[4][1] = 'F'
MST[38][1] = 'AJ'
MST[17][1] = 'AT'
MST[41][1] = 'BW'

 # Python3 program to print longest path
# from root to leaf in a Binary tree
 
# Tree node Structure
class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None
         
# Function to find and return the
# longest path
def longestPath(root):
     
    # If root is null means there
    # is no binary tree so
    # return a empty vector
    if (root == None):
        return []
 
    # Recursive call on root.right
    rightvect = longestPath(root.right)
 
    # Recursive call on root.left
    leftvect = longestPath(root.left)
 
    # Compare the size of the two vectors
    # and insert current node accordingly
    if (len(leftvect) > len(rightvect)):
        leftvect.append(root.data)
    else:
        rightvect.append(root.data)
 
    # Return the appropriate vector
    if len(leftvect) > len(rightvect):
        return leftvect
 
    return rightvect
 
# Driver Code
if __name__ == '__main__':
    
    #redraw the tree
    root = Node(MST[6][0])
    root.left = Node(MST[6][1])
    root.right = Node(MST[21][1])
    root.left.left = Node(MST[4][1])
    root.left.right = Node(MST[9][1])
    root.left.left.left = Node(MST[38][1])
    root.left.left.left.left = Node(MST[17][1])
    root.left.left.left.left.left = Node(MST[41][1])
    
    totald =(MST[6][2] + MST[4][2] + MST[38][2] + MST[17][2] + MST[41][2])/299792458*1000000
    output = longestPath(root)
    n = len(output)
    f = '{0:.5g}'.format(totald)
    
    print('Furthest Propagation Delay is :', f,'ms')
    print(output[n - 1], end = "")
    for i in range(n - 2, -1, -1):
      print(" ->", output[i], end = " ")
    
   
   


