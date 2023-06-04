import heapq

# Under the hood are arrays
# By default it's a mean heap
minHeap = []
print('First do a bunch of heappush')
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print('minHeap[0] is: ', minHeap[0])

# Loop thru the heap and pop
while len(minHeap):
    print(heapq.heappop(minHeap))
print('minHeap after heappop: ', minHeap)

# No maxHeap by default
# A workaround is multiplying by -1 when push or pop

maxHeap = []
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print('The max value is:', -1*maxHeap[0])

print('Loop thru the max heap and pop')
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
print('maxHeap after heappop: ', maxHeap)

# Build heap from initial value
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
print('arr after heapify() is: ', arr)
print('Now we can loop thru the heap arr and pop the elements')
while len(arr):
    print(heapq.heappop(arr))
print('arr heap after heappop: ', arr)



