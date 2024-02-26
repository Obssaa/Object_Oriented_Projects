import queue# Create a Stack
s = queue.LifoQueue() #LIFO stands for Last In First Out (which means it is a stack)
# Push numbers 0,1,2,3,4
for i in range(5):
    s.put(i)
# Pop all the elements
while not s.empty():
    print(s.get())
