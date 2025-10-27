# Nicholas Norman Oct 26 2025

# Goal, create a correlation matrix heatmap
# Notes, I would like to do it the easy way using libaries,
# then the hard way by calculating pearson correlation myself
# and making the heatmap myself using matplotlib

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import data
def getData():
    file = open("Final_data.csv","r")
    
    data = []
    
    # for each line
    for line in file.readlines():
        # clean
        line = line.strip()
        
        # split
        elements = line.split(',')
        
        # only take necessary elements
        keepList = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14]
        keepElements = []
        
        for i in range(0,len(keepList)):
            if i in keepList:
                
                tempEl = elements[i]
                
                try:
                    tempEl = float(tempEl)
                except:
                    pass

                keepElements.append(tempEl)

        # save to array
        data.append(keepElements)
    
    return data

# calculate the pearson correlation
def pearsonCorrelation(data):
    
    # put into np array
    npData = np.array(data)
    
    # call correlation
    correlationMatrix = np.corrcoef(npData, rowvar=False)
    
    return correlationMatrix

# create matrix vis
def visualizeMatrix(matrix, header):
    
    plt.figure(figsize=(16,14))
    plt.subplots_adjust(bottom=0.4, left=0.3)
    sns.heatmap(matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, xticklabels=header, yticklabels=header)
    plt.title("Correlation Heatmap")
    plt.savefig('./output/heatmap.png')
    plt.show()
    
    # save picture

if __name__ == "__main__":
    print("Loading data ...")
    data = getData()
    header = data[0]
    data.pop(0)
    print("Data loaded")
    print("Corellating")
    correlationMatrix = pearsonCorrelation(data)
    print("Generating Image")
    visualizeMatrix(correlationMatrix,header)
    print("Image Saved")