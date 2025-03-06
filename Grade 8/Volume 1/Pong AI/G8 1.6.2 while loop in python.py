# while loop used when you want to repeat instructions until a condition is false
# True and False are Boolean values.
running = True
num = 0
while running:
    num = num + 5
    print(num, " in while loop")
    if num > 20:
        running = False
print("done running while loop")
