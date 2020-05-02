import os
import io
import pandas as pd
from shutil import copyfile
import random
import cv2
import numpy as np
dataset_directory="data_set/"
dataset=[]
car=[]
tank=[]
for file in os.listdir(dataset_directory):
    if file.endswith(".txt"):
        dataset.append(file)
        with open(dataset_directory+file, "r") as file1:
            a=file1.read()
            try:
                a[0]
            except :
                print("skipping",file)
                continue
            if a[0]=="0":
                car.append(file)
            else:
                tank.append(file)
random.shuffle(car)
random.shuffle(tank)
train=[]
test=[]
valid=[]
train.extend(car[:int(0.85*len(car))])
train.extend(tank[:int(0.85*len(tank))])
test.extend(car[int(0.85*len(car)):int(0.95*len(car))])
test.extend(tank[int(0.85*len(tank)):int(0.95*len(tank))])
valid.extend(car[int(0.95*len(car)):])
valid.extend(tank[int(0.95*len(tank)):])
random.shuffle(train)
random.shuffle(test)
random.shuffle(valid)
print("train",len(train))
print("test",len(test))
print("valid",len(valid))
print("car:",len(car),",tank:",len(tank))
print(len(train)+len(test)+len(valid))
crop=1
resolution=(832,832)
print("number of files in the dataset directory",len(os.listdir(dataset_directory)))
if crop:
    print("copying and croping image to resolution",resolution)

num=0
count=0

with open("train.txt", "w") as file1:
    directory="train/"
    for file in train:
        try:
            os.mkdir(directory)
        except:
            pass
        if os.path.isfile(dataset_directory+file.split(".")[0]+".jpg"):
            img=cv2.imread(dataset_directory+file.split(".")[0]+".jpg")
            if crop:
                cv2.imwrite(directory+file.split(".")[0]+".jpg",cv2.resize(img,resolution))
                copyfile(dataset_directory+file,directory+file)
                file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
            else:
                cv2.imwrite(directory+file.split(".")[0]+".jpg",img)
                copyfile(dataset_directory+file,directory+file)
                file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
        else:
            print("skipping_file no jpg found",file)
        
            
with open("test.txt", "w") as file1:
    directory="test/"
    for file in test:
        try:
            os.mkdir(directory)
        except:
            pass
        if os.path.isfile(dataset_directory+file.split(".")[0]+".jpg"):

            img=cv2.imread(dataset_directory+file.split(".")[0]+".jpg")
            if crop:
                cv2.imwrite(directory+file.split(".")[0]+".jpg",cv2.resize(img,resolution))
                copyfile(dataset_directory+file,directory+file)
                file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
            else:
                cv2.imwrite(directory+file.split(".")[0]+".jpg",img)
                copyfile(dataset_directory+file,directory+file)
                file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
        else:
            print("skipping_file no jpg found",file)
        file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")

with open("valid.txt", "w") as file1:
    directory="valid/"
    for file in valid:
        try:
            os.mkdir(directory)
        except:
            pass
        if os.path.isfile(dataset_directory+file.split(".")[0]+".jpg"):

            img=cv2.imread(dataset_directory+file.split(".")[0]+".jpg")
            if crop:
                cv2.imwrite(directory+file.split(".")[0]+".jpg",cv2.resize(img,resolution))
                copyfile(dataset_directory+file,directory+file)
                file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
            else:
                cv2.imwrite(directory+file.split(".")[0]+".jpg",img)
                copyfile(dataset_directory+file,directory+file)
                file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
        else:
            print("skipping_file no jpg found",file)
        file1.write("dataset/"+directory+file.split(".")[0]+".jpg"+"\n")
            

d=0
d+=len(os.listdir("train"))
print("train",os.listdir("train"))
d+=len(os.listdir("test"))
print("test",os.listdir("test"))
d+=len(os.listdir("valid"))
print("valid",os.listdir("valid"))

print("number of files copied ",d)