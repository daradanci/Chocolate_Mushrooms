

def print_hi():
    arr=[]
    f=open('chocolate_mushrooms.txt',"r", encoding="utf8")
    for line in f:
        # print(line.split('\t'))
        arr.append(line.split('\t'))
    f.close()
    for line in arr:
        while('' in line):
            line.remove('')
        while ('\n' in line):
            line.remove('\n')

    for check in arr:
        print(check)
    print(len(arr))

    f=open('output.txt', 'w',encoding="utf8" )
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(str(i+1)+","+ str(arr[i][j]))
            f.write(str(i+1)+","+ str(arr[i][j])+'\n')
    f.close()


if __name__ == '__main__':
    print_hi()

