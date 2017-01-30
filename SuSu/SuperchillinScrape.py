import re, time
from time import sleep
from tqdm import trange

start_time = time.clock()
#downloadURL
downloadURL ="http://google.com/" # input("movie download URL minus movie ID\n" + "\n") or

# Superchillin Latest Text File Raw PHP Source
with open('E:/SuSu/SClatest.txt') as infile:
    rawdata = infile.read()

database = r'C:\Users\v613867\PycharmProjects\SuSu\database.txt'

# SC Regex
string = re.compile("<a .+?id='(.+?)'.+?>(.+?)<.+?decoration:none'>(.+?..).+?( .... )")
movies = re.findall(string, rawdata)

# Iterate through page
count = 0
for movie in movies:
    movID = downloadURL + movie[0] + ".mp4"
    movielist = []; movielist.append(movID)
    movie = movie[-3:]
    movielist.append(movie)
    with open(database,'a') as movie_entry:
        movie_entry.write(str(movielist)+ "\n")
    count += 1

# Progress
for count in trange(len(movies), leave=True):
    sleep(0.1)



print("--- %s seconds ---" % (time.clock() - start_time))