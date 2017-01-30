### Reliant on sleep via time and trange via tqdm
#  for i in trange(count, leave=True):
#    sleep(0.1)

from bs4 import BeautifulSoup
import urllib.request # For opening URL

url = "http://superchillin.com/latest.php"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read())

Entry_url = soup.find_all(string)

string = re.compile("<a .+?id='(.+?)'.+?>(.+?)<.+?decoration:none'>(.+?..).+?( .... )")

print(Entry_url)