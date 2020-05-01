import os
import io
import pandas as pd
from shutil import copyfile
import random
import cv2
import numpy as np
dataset_directory="data_set/"
dataset=[]
for file in os.listdir(dataset_directory):
    if file.endswith(".txt"):
        dataset.append(file)
dataframe=pd.DataFrame(dataset)
dataframe.to_csv("train_test.csv")
random.shuffle(dataset)
crop=1
resolution=(832,832)
print("number of files in the dataset directory",len(os.listdir(dataset_directory)))
if crop:
    print("copying and croping image to resolution",resolution)

train_files=np.linspace(0, 0.8, num=10, endpoint=False)
trainstep=train_files[1]-train_files[0]
test_files=np.linspace(0.8,1,num=5, endpoint=False)
teststep=test_files[1]-test_files[0]
print(train_files)
print(test_files)
num=0
count=0

with open("train.txt", "w") as file1:
    for i in train_files:
        num+=1
        try:
            os.mkdir("train"+str(num)+"/")
        except: 
            pass
        directory="train"+str(num)+"/"
        print(int(len(dataset)*i),int(len(dataset)*(i+trainstep)))
        for file in dataset[int(len(dataset)*i):int(len(dataset)*(i+trainstep))]:
            count+=1    
            try:
                copyfile(dataset_directory+file.split(".")[0]+".jpg",directory+file.split(".")[0]+".jpg")
                if crop:
                    img=cv2.imread(directory+file.split(".")[0]+".jpg")
                    cv2.imwrite(directory+file.split(".")[0]+".jpg",cv2.resize(img,resolution))
            except :
                print("skipping_file no jpg found",file)
                continue
            copyfile(dataset_directory+file,directory+file)
            file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
            

num=0
with open("test.txt", "w") as file1:
    for i in test_files:
        num+=1
        try:
            os.mkdir("test"+str(num)+"/")
        except: 
            pass
        directory="test"+str(num)+"/"
        print(int(len(dataset)*i),int(len(dataset)*(i+teststep)))
        for file in dataset[int(len(dataset)*i):int(len(dataset)*(i+teststep))]:
            count+=1
            try:
                copyfile(dataset_directory+file.split(".")[0]+".jpg",directory+file.split(".")[0]+".jpg")
                if crop:
                    img=cv2.imread(directory+file.split(".")[0]+".jpg")
                    cv2.imwrite(directory+file.split(".")[0]+".jpg",cv2.resize(img,resolution))
            except :
                print("skipping_file no jpg found",file)
                continue
            copyfile(dataset_directory+file,directory+file)
            file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")

d=0
d+=len(os.listdir("train1"))
d+=len(os.listdir("train2"))
d+=len(os.listdir("train3"))
d+=len(os.listdir("train4"))
d+=len(os.listdir("train5"))
d+=len(os.listdir("train6"))
d+=len(os.listdir("train7"))
d+=len(os.listdir("train8"))
d+=len(os.listdir("train9"))
d+=len(os.listdir("train10"))
d+=len(os.listdir("test1"))
d+=len(os.listdir("test2"))
d+=len(os.listdir("test3"))
d+=len(os.listdir("test4"))
d+=len(os.listdir("test5"))
print("number of files copied ",d)