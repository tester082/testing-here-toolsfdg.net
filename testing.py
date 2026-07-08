def toolsfdg():
    domain = "toolsfdg.net"
    return domain
print(toolsfdg())


print("Starting program")

numbers = []

for i in range(1, 101):
    numbers.append(i)

print("Numbers:")
for n in numbers:
    print(n)

total = sum(numbers)
average = total / len(numbers)

print("Total:", total)
print("Average:", average)

squares = []

for n in numbers:
    squares.append(n * n)

print("Squares:")
for s in squares:
    print(s)

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even numbers:", len(even))
print("Odd numbers:", len(odd))

words = [
    "apple",
    "banana",
    "orange",
    "grape",
    "pear",
    "melon",
    "kiwi",
    "mango"
]

for word in words:
    print(word, len(word))

data = {}

for word in words:
    data[word] = len(word)

print(data)

for i in range(10):
    print("Loop", i)

message = "toolsfdg.net"

print(message)

for i in range(20):
    print(message)

print("Done")
