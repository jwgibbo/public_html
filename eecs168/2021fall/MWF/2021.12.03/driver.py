from circle import Circle

def main():
    circ1 = Circle(5)
    circ2 = Circle(4)
    circ3 = Circle(1)

    circs = [circ1, circ2, circ3]

    print(circs)
    sorted_circs = sorted(circs)
    print(sorted_circs)

if __name__ == '__main__':
    main()
