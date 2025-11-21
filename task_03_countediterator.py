class CountedIterator:
    def __init__(self, iterable):
        """Initialize the iterator with the given iterable and set the count to zero."""
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0  # Initialize the counter to track iterations
    
    def __next__(self):
        """Fetch the next item from the iterator and increment the count."""
        try:
            item = next(self.iterator)  # Get the next item from the iterator
            self.count += 1  # Increment the counter
            return item  # Return the item
        except StopIteration:
            raise StopIteration  # StopIteration is raised automatically when no more items are available
    
    def get_count(self):
        """Return the current count of how many items have been iterated over."""
        return self.count
