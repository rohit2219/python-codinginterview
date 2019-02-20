csvFile='./data.csv'

fileObj=open('./data.csv')
for i in fileObj:
    print(i.rstrip().split(','))
fileObj.close()
