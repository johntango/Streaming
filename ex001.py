# example of advanage of stream processing
# rather than batch processing
import numpy as np
numbers = range(100000)

# Example 1, list comprehension. No streaming.
# First create an array of squares, then sum it.
# Note the inner array is simply looped over: no random access, just iteration.
# Wasteful, isn't it?
sum([n**2 for n in numbers])
333328333350000

# Generator: square and sum one value after another
# No extra array created = lazily evaluated stream of numbers!
sum(n**2 for n in numbers)
333328333350000

# Geneerators
generator = (word + '!' for word in 'hey time to iterate'.split())
# The generator object is now created, ready to be iterated over.
# No exclamation marks added yet at this point.

for val in generator:  # real processing happens here, during iteration
    print(val)

for val in generator:
    print(val)
# Nothing printed! No more data, generator stream already exhausted above.


def getFunc():
    for word in 'crazy girl'.split():
        yield word + '!'  # uses yield => __iter__ is a generator


def get_a_number(some_iterable):
    for item in some_iterable:
        np.random.randint(100)
        yield item


myGen = get_a_number(range(100))
print(next(myGen))
print(next(myGen))
