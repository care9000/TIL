def isFull():
    global rear
    return rear == len(Q) - 1

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print('Queue Full')
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print('Queue Empty')
    else:
        front += 1
        return Q[front]

def Qpeek():
    global front, rear
    if isEmpty():
        print('Queue Empty')
    else:
        return Q[front+1]

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


# Q =[]
#
# Q.append(1)
# print(Q)
# Q.append(2)
# print(Q)
# Q.append(3)
# print(Q)
#
# print(Q.pop(0))
# print(Q.pop(0))
# print(Q.pop(0))