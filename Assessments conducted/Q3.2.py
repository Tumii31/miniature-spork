from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('Pastries')
stack.append('Fruits')
stack.append('Vegetables')
stack.append('Meat')

print('Initial stack:')
print(stack)

# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())