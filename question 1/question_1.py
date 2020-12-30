# Name : AnnieoYang
#Finished Date:16/12/2020
#Question No.:1

'''
Solution:
O(1)
Five steps to solve the questions:
1.Find num rights to go from top left cell
2.Find num of downs to go based on next colum values
3.If possible take one step
4.Go down all the way t the bottom of the grid
5.If possible then go right to the end 
'''
import math
import numpy as np
import pandas as pd
import io

'''
Traversal of maze with summed value variation
Attempted a purely mathematical approach with no iterations to find the path, only iteration needed in this solution is while input/output_question_1 
an example is explained with the 5 step approach in the image within the same dir to explain visually the working of this algorithm
This should be the most computationally efficient algorithm
'''
def find_path(m, n, SN):

    max = get_max(m, n) #max summed number possible
    min = get_min(m, n)
    path = np.empty(m+n-2, dtype = str) # number of operations + first index will be summed number as stated in example output later added
    index = 0
    
    #needed for q1b as 87127231192 exceeds max
    if SN>max or SN<min:
        #print("Summed value out of max-min range")
        return write_path(SN, "No possible operations! Desired sum is larger than the maximum sum that can be achieved. Maximum sum from a 90000 x 100000 matrix is 13049955000.")
        
  
    d = m-1 #difference in summed values starting between columns
    
    #step 1
    r = math.ceil((max-SN)/(m-1)) #last rank of col (1...m) to go right until from top left
    numRights = r - 1 #one less as already starting from top left
    if (numRights > 0):
        index, path = add_to_path(numRights, path, 'R', index)
    
    # step 2
    nextRMax = max - r*d #the max summed number possible if down taken in the col after 'r' last rank col
    numDowns = int(SN - nextRMax) # the number of downs taken from last rank 'r', explained in working image uploaded
    if (numDowns > 0):
        index, path = add_to_path(numDowns, path, 'D', index)
   
    # step 3
    numRights += 1
    index, path = add_to_path(1, path, 'R', index)
    
    # step 4
    DownsToBottom = m-numDowns-1 #num rows - number of downs taken so far - one as starting at top left)
    index, path = add_to_path(DownsToBottom, path, 'D', index)
    
    # step 5
    #already at bottom row
    rightsRemainng = n-numRights-1 #number of right moves needed to go from current col index to right corner
    if (rightsRemainng > 0):
        index, path = add_to_path(rightsRemainng, path, 'R', index)
    
    #print(path)
    return write_path(SN, path)
    
def get_max(m, n):
           #AP sum (1..m) +  #(Num cols - first col)*bottom row value
    return (m/2)*(m+1)    +  (n-1)*(m) 
    #down all the way then right all the way

def get_min(m, n):
    return n + ((m-1)/2)*(m+2)
    
# number of times to go a direction is provided along with index and the paths are updated accordingly     
def add_to_path(num, path, char, index):
    
    for n in range(int(num)):
        path[index] = char
        index += 1
    
    return index, path
    
def write_path(SN, path):
    indexHeader = [str(SN)]
    df = pd.DataFrame(io.StringIO(''.join(path)), index=indexHeader)
    return df

# Input are queries in part a and b in the format M N SN with a blank space when changing grids 
def read_input(str):
    parameters = np.loadtxt(str, dtype= np.int64, delimiter=' ')
    return parameters
        
def main():
    parameters = read_input("input_question_1.txt")
    dfmain = pd.DataFrame()
    m,n = parameters[0][0], parameters[0][1]
    for i in range(parameters.shape[0]):
        df = find_path(parameters[i][0], parameters[i][1], parameters[i][2])
        
        if (m==parameters[i][0] and n==parameters[i][1]):
            dfmain = dfmain.append(df)
        else:
            dfmain = dfmain.append(pd.DataFrame([''], index=[''])) # Add an empty space when changing grids according to the example output provided
            dfmain = dfmain.append(df)
            m=parameters[i][0]
            n=parameters[i][1]
    dfmain.to_csv("output_question_1.txt", sep=' ', header=False)
    
main()