from bottle import run
import api.books, api.authors, api.customers


def main():
    run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
    main()
