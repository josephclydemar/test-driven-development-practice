from complex import Complex


def main():
    c1 = Complex(1, 3)
    c2 = Complex(3, 2)
    c3 = Complex(6, 1)
    print(c1 + c2)
    print(c1 - c3)
    print(c2 * c3)


if __name__ == '__main__':
    main()