import requests
from bs4 import BeautifulSoup
import urllib.request


# print list of runes
def printRune(list0):
    print('[ ' + list0[0] + ' ]')
    for i in range(1, len(list0)):
        print(' ' + list0[i])


champName = input('Enter champion\'s name: ')
print()

# main, rune, spell urls
url = 'https://poro.gg/champions/' + champName + '/aram?hl=ko-KR'
url_r = '#wrapper > div > div > div > div:nth-child(7) > div.row.row-small > div.col-lg-8.col-xl-7 > div.champion-box.champion-box--rune-build > div.champion-box__content > div > div.champion-rune__content > div.champion-rune-tab-content.active.h-auto > div:nth-child(1)'
url_s = '#wrapper > div > div > div > div:nth-child(7) > div.row.row-small > div.col-lg-4.col-xl-5 > div > div.champion-box__content > div.champion-build.champion-build--spells > div.champion-build__content > div:nth-child(1) > div.champion-build__icons'

response = requests.get(url)

if response.status_code == 200:
    # basic settings
    # --------------------------------------------------------------
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # open Rune page
    # --------------------------------------------------------------
    sample = soup.select_one(url_r)
    runes_html = sample.find_all('img', {'class': 'active'})

    rune_img_urls = [str(a.attrs['src']) for a in runes_html]

    main_r = [str(a.attrs['alt']) for a in runes_html[:5]]  # primary rune
    second_r = [str(a.attrs['alt']) for a in runes_html[5:8]]  # secondary rune
    other_r = [str(a.attrs['alt']) for a in runes_html[8:]]  # adapt ability

    # for item in rune_img_urls:
    #    print(item)
    # print('\n')

    printRune(main_r)
    print('-'*20)
    printRune(second_r)
    print('-'*20)
    for item in other_r:
        print(' ' + item)
    print('\n')

    # open Spell page
    # --------------------------------------------------------------
    sample = soup.select_one(url_s)
    spells_html = sample.find_all('img')

    spell_img_urls = [str(a.attrs['src']) for a in spells_html]
    spells = [str(a.attrs['alt']) for a in spells_html]

    # for item in spell_img_urls:
    #    print(item)
    print('\n', end='\n< ')

    for item in spells:
        print(item, end=' ')
    print('>\n')

    # download images
    # --------------------------------------------------------------
    for item in rune_img_urls:
        download_url = url + item
        img_name = item.replace('/', '')

        print(item)
        print(download_url)
        print(img_name)
        print('\n\n')
        # urllib.request.urlretrieve(download_url, './img/' + img_name)
else:
    print(response.status_code + ' not found: Not correct champion name')
