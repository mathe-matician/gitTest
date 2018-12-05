import sys

try:
    with open("example.txt") as fh:
        read_text = fh.read()
    print(read_text)
except:
    err = sys.exc_info()
    for e in err:
        print(e)
print()

try:
    1/0
except:
    err = sys.exc_info()
    for e in err:
        print(e)

print()

try:
    1/0
except Exception as err:
    print("Error was: ", str(err))

print()

try:
    with open("example.txt") as fh:
        read_text = fh.read()
    print(read_text)
except Exception as err:
    print("Error was: ", str(err))
