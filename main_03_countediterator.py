#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

# Test data to iterate
data = [1, 2, 3, 4]
# Create an instance of CountedIterator with the test data
counted_iter = CountedIterator(data)

try:
    # Iterate through the items using the iterator
    while True:
        item = next(counted_iter)  # Get the next item from the iterator
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    # Once the iterator is exhausted, StopIteration will be raised
    print("No more items.")
