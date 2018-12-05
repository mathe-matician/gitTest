from threading
import time


print_lock = threading.Lock()

t = Thread(target = execute_slowly, args = (glacial, plodding, leaden))

def execute_slowly(glacial, plodding, leaden):
    time.sleep(3)
    print(glacial, plodding, leaden)

t.start()

start = time.time()



