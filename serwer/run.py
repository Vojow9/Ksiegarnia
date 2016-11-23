from bottle import run
import api.books


def main():
    run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
    main()
