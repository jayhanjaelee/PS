class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self) -> None:
        self.size = 0
        self.start = None
        self.end = None

    def push_front(self, data):
        self.size += 1
        node = Node(data)
        if not self.start:
            self.start = start.end = node
            return
        self.start.prev = node
        node.next = self.start
        self.start = node

    def push_back(self, data):
        self.size += 1
        node = Node(data)
        if not self.start:
            self.start = self.end = Node
            return
        self.end.next = node
        node.prev = self.end
        self.end = node

    def pop_front(self):
        if not self.start:
            return -1
        self.size -= 1
        tmp = self.start
        self.start = self.start.next
        if not self.start:
            self.end = None
        else:
            self.start.prev = None
        ret =  tmp.data
        del tmp
        return ret

    def pop_back(self):
        if not self.start:
            return -1
        self.size -= 1
        tmp = self.end
        self.end = self.end.prev
        if not self.end:
            self.start = None
        else:
            self.end.next = None
        ret = tmp.data
        del tmp
        return ret

    def empty(self):
        return (not self.start)

    def front(self):
        return self.start.data if self.start else -1

    def back(self):
        return self.end.data if self.end else -1

deq = Deque()

n = int(input())
for _ in range(n):
    qry = input().split()
    if qry[0] == 'push_back':
        deq.push_back(qry[1])
    elif qry[0] == 'push_front':
        deq.push_front(qry[1])
    elif qry[0] == 'pop_back':
        print(deq.pop_back())
    elif qry[0] == 'pop_front':
        print(deq.pop_front())
    elif qry[0] == 'szie':
        print(deq.size)
    elif qry[0] == 'empty':
        print(deq)
    elif qry[0] == 'front':
        print(deq.front())
    elif qry[0] == 'back':
        print(deq.back())
