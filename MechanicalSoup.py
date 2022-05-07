import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

url = "http://uzmovi.com/"

browser.open(url)

def Premyera():

    page = browser.get_current_page()

    premyera = page.find_all('a', class_='cs-item')

    prem_link = []

    for i in premyera:
        url = i.get('href')
        img = i.find('img')
        name = img.get('alt')
        image = img.get('src')
        prem_link.append(url)

        respons = f'{image}\n <b>{name}</b>\n{url}'

        print(url)
        print(name)
        print(image)
        print('------')

    print(len(prem_link))
    return respons


browser.select_form('form[action="http://uzmovi.com/search"]')
a = input('film nomini kiriting = ')
browser['q'] = a
browser.submit_selected()

pege1 = browser.get_current_page()
search = pege1.find_all('a', class_='short-images-link')

search_list = []

for n in search:
    url = n.get('href')
    name = n.get('title')
    search_list.append(url)
    print(url)
    print(name)
