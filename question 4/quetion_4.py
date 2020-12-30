#Name : AnnieoYang
#Finished Date:22/12/2020
#Question No.:4

'''
Algorithm:
Union of Quick find and Quick approach 
Steps:
1. Parsing the matrix row wise assigning segments with associated values (done while reading rows from code)
2. Parsing the matrix column wise assigning the segment for column.
Defining the use of segments as the array containing the number of possible segments

'''
import numpy as np #importing for faster matrix manipulation

index = 1
segment=[0] #initialized as a list of 0 indicating the background pixels
col = 0 # defines the number of columns
row = 0 # defines the number of rows
'''
    calculates the segments row wise. 
    Each of the neighboring pixels are valued to one segement and the non neighboring pixel the segment value is incremented
    params:
    l indicating the row list
'''    
def rowPass(l):
    
    l1 = l.copy()
    global index,segment
    ind = 0
    #index of first non zero value
    while ind<len(l) and l[ind]==0:
        ind+=1
    #if the row has non zero pixels    
    if ind<len(l):  
        l1[ind] = index # assigning segment value
        segment.append(index)
        index+=1
        #assigning each neighboring pixel the value of the segment
        for i in range(ind+1,len(l)):
            if l[i]==l[i-1] and l[i-1]==1:
                l1[i]=l1[i-1]
            elif l[i]!=l[i-1] and l[i-1]==0:
                l1[i]=index
                segment.append(index)   
                index+=1

    return l1            
    '''
    Calculating the 4 connected component column wise
    The indexes ((x+1),y) , ((x-1),y) are already labelled in the row parse
    (x,y-1) and(x,y+1) are labelled in this approach
    params:
    arr: defines the input matrix row parsed
    '''
def conn4way(arr):
    
    """
    #finding segments column wise
    for i in range(col):
        start=0
        for j in arr[:,i]:
            if start>0 and j>0:
                m_val = min(start,j)
                if start!=m_val:
                    arr[arr==start]=m_val
                else:
                    arr[arr==j] = m_val
            else:
                start=j
    #rows columns initialized            
    rows,columns = arr.shape
    #resuts written to the file
    w = open("output_question_4_4connected","w")
    for i in range(rows):
        for j in range(columns):
           w.write(str(arr[i,j])+(2-len(str(arr[i,j]))+1)*" ")
        w.write("\n")
    w.close()        
    return arr                        
def isValid(r,c):
    """
    If the index is a valid index or not
    params:
    r : row index
    c : column index
    """
    if r>=0 and r<row and c>=0 and c<col:
        return True
    else: 
        return False

def minValInd(l):

    """
    returns the minimum value and the index of the value in l
    params:
    l: list of values
    """
    ind = np.argmin(l)
    val = min(l)
    return ind,val


def conn8way(arr):
    """
    8  connected makes use of 8 neighboring points namely
    x-1,y : mapped in first pass
    x,y-1: mapped in 4 connection
    x+1,y: mapped in first pass
    x,y+1: mapped in 4 connection
    x+1,y+1 
    x-1,y-1
    x+1,y-1
    x-1,y+1
    Function takes 4 connected array and checks for 8 connected components
    params:
    arr: 4 connected input segment.
    """
    for i in range(row):
        for j in range(col):
            l=[]
            if arr[i,j]>0:
                l.append(arr[i,j])
                if isValid(i-1,j-1) and arr[i-1,j-1]!=0:
                    l.append(arr[i-1,j-1])
                if isValid(i-1,j+1) and arr[i-1,j+1]!=0:
                    l.append(arr[i-1,j+1])
                if isValid(i+1,j-1) and arr[i+1,j-1]!=0:
                    l.append(arr[i+1,j-1])
                if isValid(i+1,j+1) and arr[i+1,j+1]!=0:
                    l.append(arr[i+1,j+1])
                if len(l)>1:    
                    ind,val = minValInd(np.array(l))
                    for k in range(len(l)):
                        if k!=ind:
                            arr[arr==l[k]]=val
    rows,columns = arr.shape
    w = open("output_question_4_8connected","w")
    for i in range(rows):
        for j in range(columns):
            w.write(str(arr[i,j])+(2-len(str(arr[i,j]))+1)*" ")
        w.write("\n")
    w.close()    

#reading input
f = open('input_question_4')
#w = open('output_question_4_4connect','w') 
l=[]

#reading input array
while True:
    line = f.readline()
    if not line or len(line.strip())==0:
        break
    else:
        row+=1
        l.append(rowPass(list(map(int,line.split('\t')))))
    if col==0:
        col = len(l[0])
l = np.array(l)
l4conn = l.copy() # defining 4 connected components

#performing 4 connection
l8conn = conn4way(l4conn)
#performing 8 connection 
conn8way(l8conn)
