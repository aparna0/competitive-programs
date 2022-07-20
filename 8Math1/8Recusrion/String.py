def f1(string, res):
    if(len(string) == 0):
        print(res)
        return
    for i in range(len(string)):
        res.append(string[0:i+1])
        print("Inner :",res)
        f1(string[i+1:],res)

        res.pop()

string = input()
f1(string, [])
