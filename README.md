**Repository for improved yolov5 for small target detection
**

DotaToYolo converts DOTA annotation format to YOLO annotation format in txt

VisDronetoYOLO converts VisDrone annotation format to YOLO annotation format in txt

pngtojpg converts png files to jpg in a folder

Repository also contains two jupyter notebooks:
  DataExplorationClasswise: This notebook contains all classwise pixel area size analysis of objects in both DOTA and VisDrone dataset
  DataExploration: this notebook calculates average pixel area of all the objects of all classes in both DOTA and VisDrone dataset


The trained weights can be downloaded from gdrive below:


[Yolov5x 40 epochs DOTA](https://drive.google.com/file/d/19O4kdomab0MzXtWNo3vgL9yRRhNM0WZA/view?usp=sharing)

[Yolov5x 40 epochs VisDrone](https://drive.google.com/file/d/1R0JlQBuK7x4Ttp87IHvofR1yI0KN6ojU/view?usp=sharing)

[Yolov5 improved 40 epochs VisDrone](https://drive.google.com/file/d/1KUQLH9mtCcBxoENZHclcMAss8sy5FV4V/view?usp=sharing)

[Yolov5 improved 40 epochs DOTA](https://drive.google.com/file/d/1_hU4ib7kfwvDZrCC0d35WtORBVkpXDJv/view?usp=sharing)


These trained weights can be used with Yolov5 official github repository [here](https://github.com/ultralytics/yolov5) to reproduce the results, the custom model file is also provided as yolov5-small-target.yaml that can be used in their models folder
