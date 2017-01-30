import re
import time

start_time = time.clock()

patt = re.compile("\w+")
words = patt.findall("Hello World")

print(words)
print("--- %s seconds ---" % (time.clock() - start_time))

