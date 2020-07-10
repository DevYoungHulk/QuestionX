#encoding: utf-8
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
def find_file_text(root_dir, target_text):
    suffix = ['txt']
    resultArray = []
    dic_size = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            dic_size = dic_size + 1
            file_suffix = file[file.find('.') + 1:len(file)]
            if file_suffix in suffix:
                file_obj = open(os.path.join(root, file), 'rU')
                line_no = 0
                finded = 0
                for eachline in file_obj:
                    line_no = line_no + 1
                    if eachline.startswith("Q:") and target_text in eachline:
                        if eachline in resultArray:
                            continue
                        else:
                            resultArray.append(eachline)
                            finded = 1
                            print (bcolors.OKBLUE + eachline + bcolors.ENDC)
                    elif finded == 1:
                        print (bcolors.OKGREEN + eachline + bcolors.ENDC)
                        finded = 0
    print ( "样本数量" + str(dic_size))
    if len(resultArray) == 0:
        print (bcolors.FAIL + "Nothing found..." + bcolors.ENDC)
    else:
        print (bcolors.OKBLUE + "------ Finish ------" + bcolors.ENDC)
        print ("")

def printHelp():
    print("题库请放入同目录或当前文件夹子目录")
    print("使用 Answer question helper.user.js + tampermonkey 可以导出题目 格式为:\nQ:xxx\nA:xxx")
    print("安装地址：https://greasyfork.org/zh-TW/scripts/406809-pluralsight-answer-question-helper")
    print('输入关键字即可查询\n-h 呼出帮助\n-q(or ctr+c) 退出程序')

def main():
    try:
        hint = '请输入查询的标题'
        s1 = sys.argv[1].strip()
        if len(s1) == 0:
            print(bcolors.FAIL + hint + bcolors.ENDC)
        else:
            find_file_text("./", s1)
    except IndexError:
        try:
            printHelp()
            while True:
                print(bcolors.FAIL + hint + bcolors.ENDC)
                s2 = raw_input().strip()
                if len(s2) == 0:
                    print(bcolors.FAIL+ hint + bcolors.ENDC)
                    print('')
                elif s2 == '-q':
                    break
                elif s2 == '-h':
                    printHelp()
                else:
                    find_file_text("./", s2)
        except KeyboardInterrupt:
            print(" 已退出")
            pass


if __name__ == '__main__':
    main()