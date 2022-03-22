from lexer import DuckLexer
from parser import DuckParser

FILENAME = 'program2.duck'

def main():
    file = open('programs/' + FILENAME)
    data = file.read()
    file.close()

    lexer = DuckLexer()
    # tokens = lexer.tokenize

    # for token in lexer.tokenize(data):
    #     print(token)

    parser = DuckParser()
    parser.parse(lexer.tokenize(data))

    print('Done')


if __name__ == '__main__':
    main()