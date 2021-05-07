import sys

def hello(name):
    print('Hello ' + name)

def goodbye(name):
    print('Goodbye ' + name)

name = sys.argv[1]

hello(name)
goodbye(name)