from parser import parser

FILENAME = 'program2.duck'

def main():
    file = open('programs/' + FILENAME)
    data = file.read()
    file.close()

    parser.parse(data)
    print("Done")

if __name__ == '__main__':
    main()