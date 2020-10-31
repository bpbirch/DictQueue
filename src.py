#%%
# writing a dict-based queue to be O(1) performant in both enqueueing and dequeueing

# %%
import numpy as np
import time
import matplotlib.pyplot as plt 
# %%
# implementing a list-based queue, to compare to my dict-based queue:
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __repr__(self):
        return f'{self.items}'

if __name__ == '__main__':
    q = Queue()
    q.enqueue(22)
    q.enqueue(33)
    q.enqueue(44)
    print(q)
    q.dequeue()
    print(q)
    
# %%
# writing dict-based queue structure
class DictQueue:
    """
    This structure keeps count of number of elements enqueued. 
    To dequeue, the key:value pair with the lowest number valued key is deleted. 
    So if our DictQueue were d = {5: 'hello', 6: 'there', 7: 'everyrone', 8: 'today'}, 
    and we ran d.dequeue(), then our dictqueue object would become 
    {6: 'there', 7: 'everyrone', 8: 'today'}. 
    And if we were to then want to enque the element 'saturday', 
    our dictqueue object would become 
    {6: 'there', 7: 'everyrone', 8: 'today', 9: 'saturday'}. 
    This structure substantially outperforms a normal 
    list-based queue because in a list-based structure, 
    enqueueing is actually a l.insert(0, item) operation, which is O(n). 
    Dictionaries store elements by hashkeys, so adding and removing them are both O(1).
    """
    def __init__(self):
        self.items = {}
        self.low = 0
        self.counter = 0
    def size(self):
        return len(self.items.keys())
    def enqueue(self, item):
        self.items[self.counter] = item
        self.counter += 1
    def dequeue(self):
        placeHolder = self.items[self.low]
        del self.items[self.low]
        self.low += 1
        return placeHolder
    def isEmpty(self):
        return self.items == {}
    def __repr__(self):
        return f'{self.items}'
        
if __name__ == '__main__':
    dq = DictQueue()
    dq.enqueue(33)
    dq.enqueue(44)
    dq.enqueue(55)
    print(dq)
    dq.dequeue()
    print(dq)
    dq.enqueue(66)
    print(dq)
    dq.dequeue()
    print(dq)


# tomorrow, run some timers to see if this outperforms a normal list queue

# %%
# let's do some performance comparisons on Queue and dictQueue
def queueTimer(q, n):
    """
    This function will return the time, in seconds, required to 
    enqueue all of i through n to queue structure

    Args:
        q (queue-like structure): queue-like structure, whethere a DictQueue or Queue
        n (int): i through n will be enqueued to q

    Returns:
        float: time in seconds to enqueue all of i through n to queue structure
    """
    start = time.time()
    for i in range(n):
        q.enqueue(i)
    end = time.time()
    return end-start 


if __name__ == '__main__':
    # here we're goint to use matplotlib to pot differences in performance
    # interestingly, list-based queue actually seems to be O(n^2) performance,
    # while DictQueue is O(1)
    nums = list(range(1000, 100000, 10000))
    qTimes = []
    dqTimes = []
    q = Queue()
    dq = DictQueue()    
    for n in nums:
        qTimes.append(queueTimer(q, n))
        dqTimes.append(queueTimer(dq, n))
    fig = plt.figure()
    ax = plt.subplot(111, xlabel='n', ylabel='time to enqueue')
    ax.plot(nums, qTimes, label='Queue')
    ax.plot(nums, dqTimes, label='DictQueue')
    plt.legend()
    plt.show()
