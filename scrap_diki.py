#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def find_connected_words(url):
    # url = 'https://www.diki.pl/slownik-angielskiego?q=mleko'
    if url[:19] == 'https://www.diki.pl':
        request = requests.get(url)
        html_text = request.text
        Soup = BeautifulSoup(html_text, 'html.parser')

        conn_dict = {}
        for tag in Soup.find_all('div', class_='fentry'):
            f = tag.find('a', class_='plainLink')
            g = tag.find('span', class_='hw')
            print(f"{g.text} = {f.text}")
            conn_dict[g.text] = f.text
        return conn_dict
    else:
        print('Error')
        return 0