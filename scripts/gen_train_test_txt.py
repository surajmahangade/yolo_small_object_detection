import os
import io
import pandas as pd
from shutil import copyfile
import random
directory="data_set/"
dataset=[]
for file in os.listdir(directory):
    if file.endswith(".txt"):
        dataset.append(file)
dataframe=pd.DataFrame(dataset)
dataframe.to_csv("train_test.csv")
random.shuffle(dataset)
train_directory="train/"
test_directory="test/"
try:
    os.mkdir(train_directory)
    os.mkdir(test_directory)
except:
    pass
with open("train.txt", "w") as file1:
    for file in dataset[:int(len(dataset)*0.8)]:
        try:
            copyfile(directory+file.split(".")[0]+".jpg",train_directory+file.split(".")[0]+".jpg")
        except :
            print("skipping_file")
            continue
        copyfile(directory+file,train_directory+file)
        
        file1.write(train_directory+file+"\n")
with open("test.txt", "w") as file1:
    for file in dataset[int(len(dataset)*0.8):]:
        try:
            copyfile(directory+file.split(".")[0]+".jpg",test_directory+file.split(".")[0]+".jpg")
        except :
            print("skipping_test file")
            continue
        copyfile(directory+file,test_directory+file)
        
        file1.write(test_directory+file+"\n")