import os
def solve(s):
    n=s.split()
    #for i in range(len(n)):
    f = n[0].capitalize()
    g = n[1].capitalize()
    final = f +" "+ g
    return final

print(solve("hello world"))

'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s=input()
    result = solve(s)
    fptr.write(result+'\n')
    fptr.close()'''