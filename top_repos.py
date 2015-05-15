import requests
from bs4 import BeautifulSoup
import datetime
from formatters import print_wrapped_column


extra = ''
weekday = datetime.datetime.now().strftime("%A")
if weekday == 'Monday':
    weekday = 'Tuesday'
    extra = 'For tomorrow,'

blob = requests.get('https://github.com/trending')
soup = BeautifulSoup(blob.text)

selection = soup.select('ol.repo-list > li')


def trending_repos(selection):
    print "Trending Github Repos"
    for repo in selection[:6]:
        name = repo.select('.repo-list-name > a ')[0].text.replace('\n', '').replace('  ', '')
        # url = repo.select('.repo-list-name > a[href] ')[0].get('href').replace('\n', '').replace('  ', '')
        meta = repo.select('.repo-list-meta')
        if meta:
            meta = meta[0].text.replace('\n', '').replace('  ', '')
            stars = ""
            for char in meta:
                try:
                    int(char)
                    stars = stars + char
                except:
                    continue
        else:
            stars = ''

        desc = repo.select('.repo-list-description')
        if not desc:
            desc = ''
        else:
            desc = desc[0].text.replace('\n', '').replace('  ', '')

        print_wrapped_column("%s | %s | %s" % (name, stars, desc), 45)


trending_repos(selection)
