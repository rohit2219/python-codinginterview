class maxQueue:
    def __init__(self):
        self.queue=[]
        self.queuemap={}
    def insert(self,element):
        if element in self.queuemap:
            self.queuemap[element]=1
        else:
            self.queuemap[element]=self.queuemap[element]+1

        self.queue.append((
            element,self.queuemap[element]
        ))
        self.queue.sort(key=lambda x:x[1])
        return
    def pop(self):
        popped=self.queue.pop()
        self.queuemap[popped[0]]=self.queuemap[popped[0]]-1
        if self.queuemap[popped[0]]==0:
            pass
        else:
            self.queue.append((popped[0],self.queuemap[popped[0]]))
        return

def schedule(taskArr,taskInt):
    maxPrority=maxQueue()
    for i in taskArr():
        maxPrority.insert(i)
    scheduleArr=[]
    prevElem=''
    for i in taskArr:
        maxelem=maxPrority.pop()
        if maxelem == prevElem:
            scheduleArr.append(maxelem)

    return