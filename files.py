import os
import glob
import codecs

path = 'Documantation/'
fNAmeList = []
for filename in os.listdir(path):
    newpath=path + filename + '/markdown'
    newpath2=path + filename + '/rmarkdown/index.Rmd'
    newpath3=path + filename + '/unifiedPDF/mds/' + filename + '.md'

    for filename in glob.glob(os.path.join(newpath, '*.md')):
        print(filename)

    for root, dirs, files in os.walk(newpath, topdown=False):
        for name in files:
            p=os.path.join(root, name)
            with codecs.open(p,'r','utf-8-sig') as fileContent:
                content = fileContent.read()
            with codecs.open(newpath2, 'a', "utf-8") as indexFile:
                indexFile.write("\n\n\n")
                indexFile.write(content)
                fileContent.close()
                indexFile.close()
            with codecs.open(p,'r','utf-8-sig') as fileContent:
                content = fileContent.read()
            with codecs.open(newpath3, 'a', "utf-8") as unifiedMd:
                unifiedMd.write("\n\n\n")
                unifiedMd.write(content)
                fileContent.close()
                unifiedMd.close()