#Name : AnnieoYang
#Finished Date:30/12/2020
#Question No.:7b

import numpy as np
import pandas as pd

'''
 Pandas used to place headers easily to dataframe when outputting file
 refer to image uploaded for mathametical equation
 
'''

def parse_input(coordinate_str, index_str):
    coordinates = np.loadtxt(coordinate_str, dtype=np.int, skiprows=1) # N x 2 2d array
    print(coordinates.shape[0], coordinates.shape[1])
    indices = np.loadtxt(index_str, dtype=np.int, skiprows = 1) #N x 1 array
    print(indices.shape[0])
    return coordinates, indices
    
def convert(coordinate_str, index_str, dim):
    coordinates, indices = parse_input(coordinate_str, index_str)
    
    L = 1
    Ln = []
    Ln.append(L)
    for i in range(len(dim)):
        L *= dim[i]
        Ln.append(L)
        
    indexResult = ravel_coordinates(coordinates, Ln)
    coordinateResult = ravel_index(indices, Ln)

    #print(indexResult)
    #print(coordinateResult)
    write_data(indexResult, coordinateResult)


def ravel_coordinates(coordinates, Ln):
    indexResult = np.empty([coordinates.shape[0], 1], dtype=np.int)
    #print(Ln)
    for k in range(coordinates.shape[0]):
        index = 0
        for i in range(coordinates.shape[1]):
            index += Ln[i]*coordinates[k][i]
        indexResult[k] = index
        
    return indexResult


def ravel_index(indices, Ln):
    coordinateResult = np.empty([indices.shape[0], 6], dtype=np.int)
    
    for k in range(indices.shape[0]):
        coordinates = []
        prev_sum = 0
        I = indices[k]
        for i in range(len(Ln)-1):
            n = i+1
            prev = (I % Ln[n] - prev_sum) / Ln[i]
            prev_sum += prev * Ln[i]
            coordinateResult[k][i] = int(prev)
     
    return coordinateResult
                       
def write_data(index, coordinates):
    indexHeader = ["index"]
    coordinateHeader = ["x1", "x2", "x3", "x4", "x5", "x6"]
    pd.DataFrame(index, columns = indexHeader).to_csv("output_index_7_2.txt", sep=' ', index=False)
    pd.DataFrame(coordinates, columns = coordinateHeader).to_csv("output_coordinates_7_2.txt", sep=' ', index=False)
    #np.savetxt("output_index_7_1.txt", index, fmt="%s")
    #np.savetxt("output_coordinates_7_1.txt", coordinates, fmt="%s")

def main():
    convert("input_coordinates_7_2.txt", "input_index_7_2.txt", (4, 8, 5, 9, 6, 7))
    
    
main()
