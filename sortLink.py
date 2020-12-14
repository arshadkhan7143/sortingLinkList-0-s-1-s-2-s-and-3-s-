class LinkList(object):
    def __init__(self):
        self.head = None

    class Node(object):
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def sortList(self):
        count = [0,0,0,0]
        temp = self.head
        while temp!= None:
            count[temp.data] += 1
            temp = temp.next
        i = 0
        temp = self.head
        while temp!= None:
            if(count[i]== 0):
                i +=1
            temp.data = i
            count[i] -= 1
            temp = temp.next

    def push(self,new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp = temp.next
        print('')

llist = LinkList()
llist.push(0)
llist.push()
llist.push(2)
llist.push(1)
llist.push(3)
llist.push(0)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(3)

print("Link List before sorting")
llist.printList()

llist.sortList()

print("Link List after sorting")
llist.printList()

