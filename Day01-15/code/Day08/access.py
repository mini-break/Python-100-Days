class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # 类外部可以通过 ”_类名__私有属性（方法）名“ 访问私有属性（方法）
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
