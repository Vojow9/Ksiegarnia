from bottle import run
import api.books, api.authors, api.customers, api.bookcovers
import sys


def main(port = 8080):
    run(host='localhost', port=port, debug=True)


def deployment(port = 8080):
    run(host='localhost', port=port, server ='paste', debug=True)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        deployment(sys.argv[1])
    else:
        main()
