def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fib_generator()

for n in range(5):
    number_5 = next(fib_gen)
for n in range(195):
    number_200 = next(fib_gen)
for n in range(800):
    number_1000 = next(fib_gen)
for n in range(99000):
    number_100000 = next(fib_gen)    

print(f'5 число {number_5}')
print(f'200 число {number_200}')
print(f'1000 число {number_1000}')
print(f'100000 число {number_100000}')
