import os


global ypath


def texts():
    global ypath
    print("将一组16进制数每4个字节分组并转成10进制数\n")
    ypath = input("请输入需要处理的文件：")
    infile = open(ypath, "rb")
    outfile = open(os.path.dirname(ypath)+"\\tempHEX.txt", "w")
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
    infile = open(os.path.dirname(ypath)+"\\tempHEX.txt", "rb")
    outfile = open(os.path.dirname(ypath)+"/result.txt", "w")
    for eachline in infile.readlines():
        temp = str(int(str(eachline, encoding="utf-8"), 16))
        print(temp)
        outfile.write(temp+'\n')


texts()

textz()
