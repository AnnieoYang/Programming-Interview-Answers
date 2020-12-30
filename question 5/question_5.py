#Name : AnnieoYang
#Finished Date:24/12/2020
#Question No.:5

'''
Algorithm:

Optimization problem with least penalty,try to place largest number beads in even 
grid position and remaining beads in odd grid position.Then Keep a track of bead 
colors and numbers in a sorted hashmap and decrement accordingly.

'''
import numpy as np
import pandas as pd


def find_optimal_configuration(grid, color_map):
    
    colors = list(color_map.keys())
    print(colors)
    index = 0
    max_color  = colors[index]
    
    for i in range(grid.shape[0]):
       for j in range(grid.shape[1]):
            if(i%2)==(j%2):
                grid[i][j] = max_color
                color_map[max_color] -= 1 
            
                if color_map[max_color] == 0 and (index<len(colors)-1):
                    index += 1
                    max_color = colors[index]
    
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if i%2 != j%2:
                grid[i][j] = max_color
                color_map[max_color] -= 1
                
                if color_map[max_color] == 0 and (index<len(colors)-1):
                    #print(index)
                    #print(len(colors))
                    index += 1
                    max_color = colors[index]
                    
    print(grid)
    return grid

def parse_input(str):
    df = pd.read_csv(str, delim_whitespace=True, header=None)
    return df
    
def write_output(arr):
    np.savetxt("output_question_5_2.txt", arr, fmt="%s")
    #np.savetxt("output_question_5_1.txt", arr, fmt="%s")
    
def main():

    df = parse_input("input_question_5_2.txt")
    #parameters = parse_input("input_question_5_1,txt")
    #Format
    #parameters = [64, 'R', 139, 'B', 1451, 'G', 977, 'W', 1072, 'Y', 457]   
    
    parameters = df.values.tolist()
    parameters = parameters[0]
    n = parameters[0]
    color_map = {}
    
    for i in range(1, len(parameters), 2):
        color_map[parameters[i]] = parameters[i+1]
        
    # Sorting the Hashmap according to values in descending order
    color_map = {k: v for k, v in sorted(color_map.items(), key=lambda item: item[1], reverse=True)}
    print(color_map)
    grid = np.empty([n,n], dtype=str)
    
    grid = find_optimal_configuration(grid, color_map)
    write_output(grid)

main()
    
    
