def main():
    s1 = 'hello ' * 3
    print(s1)  # hello hello hello
    s2 = 'world'
    s1 += s2
    print(s1)  # hello hello hello world
    print('ll' in s1)  # True
    print('good' in s1)  # False
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    # 整数值-1是列表中最后一个索引，-2从倒数第二个开始
    print(str2[-3:-1])  # 45


if __name__ == '__main__':
    main()
