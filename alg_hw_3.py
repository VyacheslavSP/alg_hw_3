import copy
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def append_tail(self,val):
        end= Node(val)
        n=self
        while(n.next):
            n=n.next
        n.next=end
    def reverse_list(head, tail=None):
        while head:
            head.next,tail,head=tail,head,head.next
        return tail
    def print_list(self):
        node=self
        print(node.data)
        while node.next:
            node=node.next
            print(node.data)
    def find_tail(self, find_number): ## решение явно не идеальное но рабчее. а временный перевернутый массив удаять из памяти после отработки
        i=0
        tmp=self.reverse_list()
        if find_number==0:
            return tmp.data
        else:
            while tmp.next:
                if(i==find_number):
                    return tmp.data
                tmp=tmp.next
                i+=1


    
    #### для проверки
link=Node(100)
link.append_tail(20)
link.append_tail("z")
link.append_tail(90)
link.print_list()
print("\n")
begin_list=copy.deepcopy(link)
print("\n")
rev_list=link.reverse_list()
rev_list.print_list()
print("\n")
begin_list.print_list()
print("\n")
print(begin_list.find_tail(2))