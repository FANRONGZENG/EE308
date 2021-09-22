def command_operation(path):

    keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
                'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed',
                'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']#creat a keyword array
    file = open(path)
    lines = file.readlines()

    #0
    # output the total keyword
    total_num = 0
    for keyword in keywords:
        # print(keyword)
        for i in lines:
            index = i.find(keyword)
            if index != -1:
                result = i[index:index + len(keyword) + 1]
                if not result[-1].isalpha():  # 判断最后一个是不是字母，不是就删去
                    result = result[0:-1]
                if (result == keyword):
                    total_num += 1
    file.close()

    #Command:1,2
    #For this command, I need to find out the number of 'switch' and 'case'
    switch_num = 0
    case_num = 0
    case = []
    key_1 = 'switch'
    key_2 = 'case'
    space = 0
    num = 0

    for i in lines:
        num += 1
        space = i.find(key_1)
        if space != -1:    #if find a 'switch',search 'case' in the following line
            for i in lines [num:]:
                if i.find(key_2) != -1:  # if find 'case'
                    case_num += 1
                if i.find('}') == space:
                    switch_num += 1
                    case.append(case_num)
                    case_num = 0
                    break
    file.close()

    #Command:3,4
    #For this command, I need to find the number of 'if else' and 'if elseif else'
    num = 0
    if_else_num = 0
    if_elseif_else_num = 0

    for line in lines:
        num += 1
        if 'if' in line and 'else if' not in line:
            if_space = line.find('if')
            # print("find a if")
            # print("line:",num)
            for line in lines [num:]:
                if 'else' in line and if_space == line.find('else'):
                    if 'else if' in line:
                        # print("find an else if")
                        if_elseif_else_num += 1
                    else:
                        # print("find an else")
                        if_else_num += 1
                    break
    file.close()

    return total_num, switch_num, case, if_else_num, if_elseif_else_num



def main():
    #input the path and command level
    path = input('please enter your path: ')#C:\Users\65660\Desktop\Lab2\Requirement\lab2.txt
    level = input('please enter the completion level: ')

    #call the function
    total_num, switch_num, case, if_else_num, if_elseif_else_num = command_operation(path)

    #output the result
    print('total num:', total_num)
    if level == '1':
        print('switch num:', switch_num)
    elif level == '2':
        print('case num:',end="")
        for i in range(len(case)):
            print(case[i],'',end="")
    elif level == '3':
        print('if else num:', if_else_num)
    elif level == '4':
        print('if-elseif-else num:', if_elseif_else_num)


if __name__ == '__main__':
    main()


