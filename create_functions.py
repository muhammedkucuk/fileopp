import os
import glob, re
from jinja2 import Template

dict = {'800': 'Time', '801': 'Number','802': 'String','803': 'Object','804': 'List of Objects','806': 'Void'}

class myObject:
    parameters = []
    line1 = []
    param_list = []
    code = ""
    param_str = ""
    ReturnType = 0

dummy_str = "asdf123"
wanted_classes = []
with open("AllFunctions.csv", "r") as lines:
    lines.readline()
    for line in lines:
        readLine = line.split(',')
        if(readLine[0]!=dummy_str):
            wanted_classes.append(readLine[0])
            dummy_str=readLine[0]

template_file = open("functionsTemplate.md")
template = Template(template_file.read())

weight = 0
for classes in wanted_classes:
    myList = []
    file_name = "output/" + classes + ".md"
    directory = "output\\"+ classes +"\\images"
    with open("AllFunctions.csv", "r") as lines:
        lines.readline()
        for line in lines:
            myline = myObject()
            readLine = line.split(',')
            if(readLine[0]==classes):
                a=re.split('\n',readLine[-1])
                readLine[-1]=a[0]
                myline.line1 = readLine[0:10]  
                myline.parameters = readLine[10:] 
                myline.param_list=[""]

                for i in range(len(myline.parameters) -1):
                    myline.parameters[i]+= ', '
                for item in myline.parameters:
                    myline.param_str+=item
                if (myline.param_str!=""):
                    myline.param_list[0] = myline.param_str
                else:
                    del myline.param_list[0]
                myline.code=myline.line1[3]
                myline.ReturnType=dict[myline.line1[4]]
                myList.append(myline)

    print(len(myList))
    weight+=1
    rendered = template.render(
        Lines = myList,
        weight = weight,
        cls = classes
    )

    if not os.path.exists(directory):
        os.makedirs(directory)
    with open("output\\{}\\index.md".format(classes), "w") as f:
        f.write(rendered)