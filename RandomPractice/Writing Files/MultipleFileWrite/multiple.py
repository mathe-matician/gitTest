from random import randint

def multi(files: int = 3, length: int = 5) -> open:
    """create x1 amount of txt files containing x2 amount of random ints from 0 - 100"""
    for file in range(files):
        with open("multi" + str(file) + ".txt", "w") as f:
            for i in range(length):
                f.write(str(randint(0, 100)) + "\n")
