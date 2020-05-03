import cv2
import os
txt_file="dataset/valid.txt"
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2
image_size=(832,832)
color = (255, 0, 0) 
thickness = 2

car=0
tank=0
t=0
z=0
with open("new_valid.txt", "w") as myfile:
    with open(txt_file, "r") as filelocation:
        locations=filelocation.read()
        files=locations.split("\n")
        print(len(files))
        for file in files:
            if os.path.isfile(file):
                #img=cv2.imread(file)
                #img=cv2.resize(img,image_size)
                with open(file.split(".")[0]+".txt", "r") as file1:
                    text=file1.read()
                    text=text.split('\n')
                    #print(text)
                    for i in range(len(text)):
                        new_text=text[i].split(' ')
                        if len(new_text)>5:
                            with open("problem_annotaions"+".txt", "a") as change_annotation:
                                change_annotation.write(file.split(".")[0]+".txt")
                                change_annotation.write("\n")
                        if len(new_text)<5:
                            print("------------------------------------------------------------------------------------------------------")
                            continue
                                 
                        #print(new_text)
                    # cv2.putText(img,new_text[0],bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
                        x=float(new_text[1])*image_size[0]
                        y=float(new_text[2])*image_size[1]
                        w=float(new_text[3])*image_size[0]
                        h=float(new_text[4])*image_size[1]
                        
                        xmin=int(x-w)
                        ymin=int(y-h)
                        xmax=int(x+w)
                        ymax=int(y+h)
                        if (xmin<0 or ymin<0) and (xmax>832 or ymax>832):
                            print(file)#,x,y,w,h,"---",xmin,ymin,xmax,ymax)
                            if new_text[0]=="0":
                                car+=1
                            else:
                                tank+=1
                            z=z+1
                        else:
                            myfile.write(file)
                            myfile.write("\n")
                            t=t+1
                            break

             #       img = cv2.rectangle(img, (xmin,ymin), (xmax,ymax), color, thickness)
            #cv2.imshow("img",img)
            #cv2.waitKey(0)

        else:
            print("skipped this file",file)
print(car,tank)
print(t,z,t+z)