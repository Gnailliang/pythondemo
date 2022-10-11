import os

def texts():
    inpath = input("请输入需要处理的文件：")
    infile = open(inpath, "rb")
    outfile = open(os.path.dirname(inpath)+"2.txt", "wb")
    for eachline in infile.readlines():
        lines = str(eachline, encoding="utf-8").split(' ') 
        n = 0
        for temp in lines:
            n = n+1
            if n % 2 == 0:
                outfile.write(bytes(temp, encoding="utf-8")+b'\n')
            else:
                outfile.write(bytes(temp, encoding="utf-8")+b'')

    infile.close()
    outfile.close()


def textz():
    infile = open("E:\\2.txt", "rb")
    outfile = open("E:\\3.txt", "wb")
    for eachline in infile.readlines():
        temp = str(int(str(eachline, encoding="utf-8"), 16))
        outfile.write(bytes(temp, encoding="utf-8")+b'\n')


texts()

textz()
