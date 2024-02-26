import queue
# Create a queue
q = queue.Queue() #First In First Out Queue
# EnQueue 0,1,2,3,4
for i in range(5):
    q.put(i)
# DeQueue all elements
while not q.empty():
    print(q.get())