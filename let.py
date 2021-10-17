n = int(input())
m = list()
for i in range(n):
    func, *op = input().split()
    ch = list(map(int, op))
    if len(ch) == 2:
        q = ch[0]
        r = ch[1]
    elif len(ch) == 1:
        q = ch[0]
    if func == "insert":
        m.insert(q(0), r[0])
    elif func == "append":
        m.append(q[0])
    elif func == "remove":
        m.remove(q[0])
    elif func == "print":
        print(m)
    elif func == "reverse":
        m.reverse()
    elif func == "pop":
        m.pop()
    elif func == "sort":
        m.sort()
