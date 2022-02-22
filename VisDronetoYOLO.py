path=r'Path to labels folder'
import os
import glob
labels=['pedestrian', 'people', 'bicycle', 'car', 'van', 'truck', 'tricycle', 'awning-tricycle', 'bus', 'motor']
for filename in glob.glob(os.path.join(path, '*.txt')):
    fin=""
    lin=[]
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        print(filename)
        lines=f.readlines()
        for line in lines:
            words=line.split(" ")
            if(words[5]!=0 and words[5]!=11):
                h=words[3]
                w=words[2]
                cx=words[0]+(w/2)
                cy=words[1]+(h/2)
                cid=words[5]
                words=[]
                words=[cid,cx,cy,h,w]
            else:
                continue
            words.append("\n")
            line2=[]
            line2=" ".join(words)
            lin.append(line2)

    fin="".join(lin)
    xyz = open(filename,"w")
    xyz.write(fin)
    xyz.close()