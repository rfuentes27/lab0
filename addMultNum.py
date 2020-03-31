import sys
text = sys.stdin.read().splitlines()

def addMult(f):
    temp = []
    end = int(f[0]) + 1
    for i in range(1, end):
       temp = f[i].split()
       add = int(temp[0]) + int(temp[1])
       mult = int(temp[0]) * int(temp[1])
       print add, mult
    return

if (__name__ == "__main__"):
    def main():
        addMult(text)
        return
    main()
