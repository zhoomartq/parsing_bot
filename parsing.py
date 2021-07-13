import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_new_page_data(html):
    soup = BeautifulSoup(html,"lxml")
    product_list = soup.find("div",class_="Article--text").text
    return product_list

def get_page_data_for_new(html):
    soup = BeautifulSoup(html,"lxml")
    list2 = []
    count2 = 0
    for link in soup.findAll("a",class_="ArticleItem--name"):
        count2 +=1
        if count2 == 21:
            break 
        title_info = link.get("href")
        list2.append(get_new_page_data(get_html(title_info)))
    return list2


def get_page_data(html):
    soup = BeautifulSoup(html,"lxml")
    product_list = soup.find("div",class_="Tag--articles")
    products = product_list.find_all("div",class_="Tag--article")
    list_ = []
    global list_img
    list_img = []
    count1 = 0
    for i in products:
        count1 +=1
        if count1 == 21:
            break
        title = i.find("a",class_="ArticleItem--name").text
        img = i.find("img").get("data-src")
        list_img.append(img)
        list_.append(title)
    return list_


from datetime import datetime
def main():
    current_datetime = datetime.now()
    part1 = "https://kaktus.media/?date="
    part2 = str(current_datetime.year)+"-"+str(current_datetime.month)+"-"+str(current_datetime.day)
    part3 = "&lable=8&order=time/"
    notebooks_url = part1+part2+part3
    # notebooks_url = 'https://kaktus.media/?date=2021-04-26&lable=8&order=time/'
    global title_
    global big_title
    title_ = get_page_data(get_html(notebooks_url))
    big_title = get_page_data_for_new(get_html(notebooks_url))


main()

    