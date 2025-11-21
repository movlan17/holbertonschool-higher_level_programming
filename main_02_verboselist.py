#!/usr/bin/env python3
from task_02_verboselist import VerboseList

# Create an instance of VerboseList with initial values
vl = VerboseList([1, 2, 3])

# Test the append method
vl.append(4)

# Test the extend method
vl.extend([5, 6])

# Test the remove method
vl.remove(2)

# Test the pop method (pop the last element)
vl.pop()

# Test the pop method with an index (pop the first element)
vl.pop(0)
