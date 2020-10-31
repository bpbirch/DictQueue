# DictQueue
I had the goal of creating a queue whose performance for both enqueuing and dequeueing would be O(1). To achieve this, instead of using a list, I wrote a dictionary queue structure, DictQueue. This structure keeps count of number of elements enqueued. To dequeue, the key:value pair with the lowest number valued key is deleted. So if our DictQueue were d = {5: 'hello', 6: 'there', 7: 'everyrone', 8: 'today'}, and we ran d.dequeue(), then our dictqueue object would become {6: 'there', 7: 'everyrone', 8: 'today'}. And if we were to then want to enque the element 'saturday', our dictqueue object would become {6: 'there', 7: 'everyrone', 8: 'today', 9: 'saturday'}. This structure substantially outperforms a normal list-based queue because in a list-based structure, enqueueing is actually a l.insert(0, item) operation, which is O(n). Dictionaries store elements by hashkeys, so adding and removing them are both O(1).
