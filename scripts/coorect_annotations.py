txt_file="problem_annotaions.txt"
with open(txt_file, "r") as txtfile:
    files=txtfile.read()
    files=files.split("\n")
    #print(files)
    for file in files:
        print(file)
        with open(file, "r") as file1:
            text=file1.read()
            print(text)
            hg
            #text=text.split('\n')
            #if len(text)>1:
             #   print(file)
            new_text=text.split(' ')
        with open(file, "w") as file1:
            val=new_text[0]
            i=5
            to_write=val+" "+new_text[1]+" "+new_text[2]+" "+new_text[3]+" "+new_text[4]+"\n"
            file1.write(to_write)
            while(i<len(new_text)):
                to_write=val+" "+new_text[i]+" "+new_text[i+1]+" "+new_text[i+2]+" "+new_text[i+3]+"\n"
                file1.write(to_write)
                i=i+4

                
              