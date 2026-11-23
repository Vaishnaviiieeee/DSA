
stack = []

# 1. Push
def push(element):
    stack.append(element)
    print(element, "pushed into stack")


# 2. Pop
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element:", stack.pop())


# 3. Display
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack:", stack[::-1])


# 4. Reverse String using Stack
def reverse_string(string):
    temp = []

    for ch in string:
        temp.append(ch)

    result = ""

    while temp:
        result += temp.pop()

    print("Reversed string:", result)


# 5. Reverse Stack using another Stack
def reverse_stack():
    temp = []

    while stack:
        temp.append(stack.pop())

    stack.extend(temp)

    print("Reversed stack:", stack)


# Function calls
push(10)
push(20)
push(30)

display()

pop()

display()

reverse_string("SUMIT")

reverse_stack()

display()
