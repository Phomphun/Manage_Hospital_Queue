class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class HospitalAR:
    def __init__(self): # ใชเช็คคำผิด
        self.AddQ = ['1','1.','addqueue','addQueue','Addqueue','AddQueue','add queue','add Queue','Add queue','Add Queue','ADDQueue','ADD QUEUE','ADDqueue','ADD queue']
        self.ShowQ = ['2','2.','showqueue','show queue','ShowQueue','Show Queue','SHOWQUEUE','SHOW QUEUE']
        self.QLength = ['3','3.','QUEUE LENGTH','queue length','queuelength','QUEUELENGTH','Queue length']
        self.UserInQ = ['3','3.','User In Queue','User in queue','USER IN QUEUE','user in queue']
        self.QNext = ['4','4.','Queue Next']
        self.STOP = ['STOP','stop','Stop']
        self.Red = ['1','1.','r','R','RED','Red','red','red case','Red Case','RED CASE','Red case',]
        self.Yellow = ['2','2.','y','Y','YELLOW','Yellow','yellow','yellow case','Yellow Case','YELLOW CASE','Yellow case',]
        self.Green = ['3','3.','g','G','GREEN','Green','green','green case','Green Case','GREEN CASE','Green case',]
        self.Y = ['y','Y','YES','Yes','yes']
        self.N = ['n','N','NO','No','no']

class Hospital:
    def __init__(self):
        self.head = None

    def printListHead(self,node):
        if node == None:
            print('empty queue')
        else:
            print(node.data)
    
    def printListLoop(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data + ' -> ', end='')
            ptr = ptr.next
        print('Empty queue\n')

    def printListLoopNoNone(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data + ' -> ', end='')
            ptr = ptr.next


    def insertAtEnd_proc(self,node,val):
        if node == None:
            # insert here
            newNode = Node(val)
            node = newNode
        else:
            node.next = self.insertAtEnd_proc(node.next,val)
        return node

    def insertAtEnd(self,val):
        self.head = self.insertAtEnd_proc(self.head,val)

    def search_proc(self,node,val):
        if node == None:
            return False
        elif node.data == val:
            return True
        else:
            return self.search_proc(node.next,val)

    def search(self,val):
        result = self.search_proc(self.head,val)
        return result

    def searchIndex_proc(self,node,val,index=-1):
        if node == None:
            return -1
        elif node.data == val:
            return index+1
        else:
            return self.searchIndex_proc(node.next,val,index+1)

    def searchIndex(self,val):
        return self.searchIndex_proc(self.head,val)

    def deleteHead(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None

    def insertAtHead(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
    
    def numberQ(self):  # ใช้ในการนับจำนวนคิวของคนไข้ที่รับเข้ามาและแสดงผลออกไป
        temp = self.head
        count = 0

        while (temp):
            count += 1
            temp = temp.next

        return count
