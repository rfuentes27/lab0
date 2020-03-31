import sys
text = sys.stdin.read().splitlines()

def addMult(f):
    temp = []
    end = int(f[0]) + 1
    for i in range(1, end):
       temp = f[i].split()
       print(int(temp[0]) + int(temp[1]), end =" ")
       print(int(temp[0]) * int(temp[1]))
    return

if (__name__ == "__main__"):
    def main():
        addMult(text)
        return
    main()
