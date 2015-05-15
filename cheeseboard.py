import requests
from BeautifulSoup import BeautifulSoup
import datetime
from formatters import print_wrapped_column


extra = ''
weekday = datetime.datetime.now().strftime("%A")
if weekday == 'Monday':
    weekday = 'Tuesday'
    extra = 'For tomorrow,'

blob = requests.get('http://www.cheeseboardcollective.coop/pizza')
soup = BeautifulSoup(blob.text)

section = soup.findAll(['h4', 'p'])


def pizza():
    for item in section:
        if item.text[0:2] == weekday[0:2]:
            phrase = "Cheeseboard Today\n%s" % (section[section.index(item)+1].text)
            printable = phrase.split(',')
    for w in printable:
        print_wrapped_column(w.strip(), 30)

pizza()
