import queue
word = "Ann"
s = queue.LifoQueue()
for i in word:
    s.put(i)
revword = ""
while not s.empty():
    revword = revword + s.get()
if revword.__eq__(word):
    print("Palindrome")
else:
    print("Not a Palindrome")
