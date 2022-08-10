class QueueNode:
    def __init__(self, val, p, n):
        self.val = val
        self.next = n
        self.prev = p


class PriorityQueueReq:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, val):
        self.len += 1
        if self.head is None:
            self.head = QueueNode(val, None, None)
        else:
            for i in self:
                if val <= i.val:
                    if i.prev is None:
                        n = QueueNode(val, None, i)
                        i.prev = n
                        self.head = n
                    else:
                        i.prev.next = QueueNode(val, i.prev, i)
                        i.prev = i.prev.next
                    break
                elif i.next is None:
                    i.next = QueueNode(val, i, None)

    def pop(self):
        if self.head is None:
            self.len = 0
            return None
        else:
            i = self.head.val
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.len -= 1
            return i

    def to_array(self):
        a = []
        for i in self:
            a.append(i.val)
        return a

    def __iter__(self):
        self.i = self.head
        return self

    def __next__(self):
        if self.i is None:
            raise StopIteration
        else:
            i = self.i
            self.i = self.i.next
            return i

    def __repr__(self):
        return repr(self.to_array())


class QNode:
    def __init__(self, n):
        self.n = n
        self.prev = None
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, node):
        # Create a dynamic node
        node = QNode(node)
        node.n = node

        if self.front is None:
            #  When adding a first node of queue
            self.front = node
            self.rear = node

        elif self.front.n.first >= node.first:
            #  Add node at beginning position
            node.next = self.front
            self.front.prev = node
            self.front = node

        elif self.rear.n.first <= node.first:
            #  Add node at last position
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        else:
            temp = self.front
            #  Find the location of inserting priority node
            while temp.n.first < node.first:
                temp = temp.next

            #  Add node
            node.next = temp
            node.prev = temp.prev
            temp.prev = node
            if node.prev is not None:
                node.prev.next = node

        self.size = self.size + 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    #  Get a front element of queue
    def peek(self):
        if self.is_empty():
            #  When Queue is empty
            print("\n Empty Queue ")
            return None
        else:
            return self.front.n

    def is_size(self):
        return self.size

    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            temp.n = None
            if (self.front == self.rear):
                #  When queue contains only one node
                self.rear = None
                self.front = None
            else:
                self.front = self.front.next
                self.front.prev = None

            #  Change queue size
            self.size -= 1

    def print_queue(self):
        node = self.front
        print("\n Queue Element ", end="")
        while node is not None:
            print("\n ", node.n.first, " ", node.n.second, end="")
            node = node.next

        print(end="\n")