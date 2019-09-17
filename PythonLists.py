#Lists
#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())

arr = []
allvals = []
solution = []
for x in range(n):
    allvals.append(input())

for i in allvals:
    arr.append(i.split(" "))

for i in arr:
    if i[0] == "append":
        solution.append(int(i[1]))
    elif i[0] == "extend":
        solution.extend([int(x) for x in i[1:]])
    elif i[0] == "insert":
        solution.insert(int(i[1]), int(i[2]))
    elif i[0] == "remove":
        solution.remove(int(i[1]))
    elif i[0] == "pop" and len(solution) != 0:
        solution.pop()
    elif i[0] == "index":
        solution.index(int(i[1]))
    elif i[0] == "count":
        solution.count(int(i[1]))
    elif i[0] == "sort":
        solution.sort()
    elif i[0] == "reverse":
        solution.reverse()
    elif i[0] == "print":
        print(solution)
