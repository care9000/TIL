import queue

q = queue.Queue()
q.put(1)
print(q)
q.put(2)
print(q)
q.put(3)
print(q)

print(q.get())
print(q.get())
print(q.get())