path=r'Path to labels folder'
import os
import glob
labels=[ 'plane', 'ship', 'storage-tank', 'baseball-diamond', 'tennis-court', 'basketball-court', 'ground-track-field', 'harbor', 'bridge', 'large-vehicle', 'small-vehicle', 'helicopter', 'roundabout', 'soccer-ball-field', 'swimming-pool', 'container-crane', 'airport','helipad' ]
for filename in glob.glob(os.path.join(path, '*.txt')):
    fin=""
    lin=[]
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        print(filename)
        lines=f.readlines()
        for line in lines:
            words=line.split(" ")
            words.insert(0,str(labels.index(words[8]))) #class label in 0 to classes-1 format at first index
            words.insert(1,str(((float(words[3])+float(words[1]))/2048))) # put value of x of center of object
            words.insert(2,str(((float(words[7])+float(words[5]))/2048))) #y value
            words.insert(3,str(((float(words[5])-float(words[3]))/1024))) #height
            words.insert(4,str(((float(words[9])-float(words[7]))/1024))) #width
            
            words.pop()
            words.pop()
            words.pop()
            words.pop()
            words.pop()
            words.pop()
            words.pop()
            words.pop()
            words.pop()
            words.pop()
            
            words.append("\n")
            line2=[]
            line2=" ".join(words)
            lin.append(line2)

    fin="".join(lin)
    xyz = open(filename,"w")
    xyz.write(fin)
    xyz.close()