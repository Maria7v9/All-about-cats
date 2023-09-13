class LinkedList:
     def __init__(self, num=0, next=None):
         self.num = num
         self.next = next

input = [1,2,3, 5, 8,10] #входной массив
tail = None #хвост списка
head = None #голова списка, пригодится.

#First element
head = LinkedList(input[0], None)
tail = head

#Остальные элементы
#tail.next = LinkedList(input[1], None)
#tail = tail.next
#tail.next = LinkedList(input[2], None)
#tail = tail.next
#tail.next = LinkedList(input[3], None)

for i in range(1, len(input)):
    tail.next = LinkedList(input[i], None)
    tail = tail.next

# печатаем элементы связного списка
#list_node1 = head
#while list_node1 is not None:
#    print(list_node1.num)
#    list_node1 = list_node1.next

# вставляем в отсортированный список элемент 

def insert(head, n):
    new = None
#если на вход подается пустой список
    if head == None:
        new = LinkedList(n,None)
        return new

    p = head
    prew = None
# выполнение цикла для поиска места значению n
    while p!=None and p.num <n:
        prew = p
        p = p.next
#если голова больше значения n
    if prew ==None:
        new = LinkedList(n,head)
        return new
# если хвост меньше значения n
    if p == None:
        new = LinkedList(n,None)
        prew.next = new
        return head

    new = LinkedList(n,p)
    prew.next = new
    return head

# Вызов функции insert 
head = insert(head, 11)

# печатаем элементы связного списка
list_node1 = head
while list_node1 is not None:
    print(list_node1.num)
    list_node1 = list_node1.next




