def isFull():
    if rear == size-1:
        return True
    else:
        False



def isEmpty():
    if front == rear:
        return True
    else:
        return False



def enQueue(item):
    for i in range(size):
        if Q[i] == 0:
            rear = i
            Q[i] = item


def deQueue():
    for i in range(size):
        if Q[i] != 0:
            front = i
            Q[i] = 0


def Qpeek():
    return  Q[front+1]



size = 100
Q = [0] * size
front, rear = -1, -1

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())