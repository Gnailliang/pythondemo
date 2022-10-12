import os


global ypath


def texts():
    global ypath
    ypath = input("请输入需要处理的文件：")
    infile = open(ypath, "rb")
    outfile = open(os.path.dirname(ypath)+"2.txt", "w")
    for eachline in infile.readlines():
        lines = str(eachline, encoding="utf-8").split(' ')
        n = 0
        for temp in lines:
            n = n+1
            if n % 2 == 0:
                outfile.write(temp+'\n')
            else:
                outfile.write(temp+'')

    infile.close()
    outfile.close()


def textz():
    global ypath
    infile = open(os.path.dirname(ypath)+"2.txt", "rb")
    outfile = open(os.path.dirname(ypath)+"3.txt", "w")
    for eachline in infile.readlines():
        temp = str(int(str(eachline, encoding="utf-8"), 16))
        print(temp)
        outfile.write(temp+'\n')


texts()

textz()
