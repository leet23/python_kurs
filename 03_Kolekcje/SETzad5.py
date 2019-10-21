'''Porównaj zachowanie discard() vs remove() dla typu set.'''

example_set = {1, 2, 3, 4, 23, 'adam', 'x', 'asdf'}
print(example_set.discard(1))
print(example_set.discard(0))
print(example_set)

example_set2 = {1, 2, 3, 4, 23, 'adam', 'x', 'asdf'}
print(example_set2.remove(1))
print(example_set2)