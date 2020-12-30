#Name : AnnieoYang
#Finished Date:30/12/2020
#Question Num:7a

import numpy as np
import pandas as pd


'''
Conversion of coordinates to index
Mathematical formula required to make conversions
Index to coordinates
i = x1 + x2(L1)

 Coordinates to index
 x1 = i%L1
 x2 = i/L1

'''

def parse_input(coordinate_str, index_str):
    coordinates = np.loadtxt(coordinate_str, dtype=np.int, skiprows=1) # N x 2 2d array
    print(coordinates.shape[0], coordinates.shape[1])
    indices = np.loadtxt(index_str, dtype=np.int, skiprows = 1) #N x 1 array
    print(indices.shape[0])
    return coordinates, indices
    
def convert(coordinate_str, index_str, L1, L2):
    coordinates, indices = parse_input(coordinate_str, index_str)
    
    
    indexResult = np.empty([coordinates.shape[0], 1], dtype=np.int)
    
    for i in range(coordinates.shape[0]):
        indexResult[i][0] = coordinates[i][0]+ coordinates[i][1]*L1
    
        
    coordinateResult = np.empty([indices.shape[0], 2], dtype=np.int)
        
    for k in range(indices.shape[0]):
        coordinateResult[k][0] = indices[k]%L1
        coordinateResult[k][1] = indices[k]//L1
    
    #print(indexResult)
    #print(coordinateResult)
    write_data(indexResult, coordinateResult)


def write_data(index, coordinates):
    indexHeader = ["index"]
    coordinateHeader = ["x1", "x2"]
    pd.DataFrame(index, columns = indexHeader).to_csv("output_index_7_1.txt", sep=' ', index=False)
    pd.DataFrame(coordinates, columns = coordinateHeader).to_csv("output_coordinates_7_1.txt", sep = ' ', index=False)
    #np.savetxt("output_index_7_1.txt", index, fmt="%s")
    #np.savetxt("output_coordinates_7_1.txt", coordinates, fmt="%s")

def main():
    convert("input_coordinates_7_1.txt", "input_index_7_1.txt", 50, 57)
    
main()
