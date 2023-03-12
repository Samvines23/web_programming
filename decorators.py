def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("ran the function")
    return wrapper()

@announce
def hello():
    print("Hello, world!")

#x = announce(hello)
#print(x)
#print(announce(hello))
hello

for x in range(3):
    print(x)

hello