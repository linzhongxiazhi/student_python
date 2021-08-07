numbers = []
totals = []
everyone = []
onlyone=[]
print("enter 5 number from 1-10")
i = 0
while i < 5:
    x = int(input(" input 5 number:"))
    numbers.append(x)
    i += 1
print(numbers)
x = 0
while x <= len(numbers) - 3:
    i = x + 1
    while i <= len(numbers) - 2:
        j = i + 1
        while j <= len(numbers) - 1:
            # print(x,i,j)
            total = numbers[x] + numbers[i] + numbers[j]
            if total % 10 == 0:
                ijx = [numbers[x], numbers[i], numbers[j]]
                print(numbers[x], "+", numbers[i], "+", numbers[j], "=", total)
                # print(ijx)
                sumq = sum(numbers) - sum(ijx)
                print("其余两个数的和为：！！！", sumq)
                totals.append(ijx)

            j += 1
        i += 1
    x += 1
print(totals)
for i in totals:
    everyone.append(sorted((i)))
for j in everyone:
    if j not in onlyone:
        onlyone.append(j)
print("唯一值:",onlyone)
if len(totals) == 0:
    print("this list is none!!!,you can compare the list")
    print(sorted(numbers))