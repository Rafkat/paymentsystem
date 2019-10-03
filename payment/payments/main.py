def method(a, b, *args, **kwargs):
    print(f'{a} {b} {args} {kwargs}')


def main():
    method(1, 2, 3, 6, c=4)


if __name__ == '__main__':
    main()
