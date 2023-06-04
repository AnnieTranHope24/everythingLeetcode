# Queues (double ended queue)
from collections import deque
queue = deque()

print('Test append queue')
queue.append(1)
queue.append(2)
print(queue)

print('queue.popLeft() is: ', queue.popleft())
print('queue now is: ', queue)

print('queue.appendLeft() is: ', queue.appendleft(1))
print('queue now is: ', queue)

print('queue.pop() is: ', queue.pop())
print('queue now is: ', queue)