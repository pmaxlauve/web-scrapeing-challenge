from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests







def init_browser():
    
    executable_path = {"executable_path": "C:\\Users\\pmaxl\\OneDrive\\Desktop\\webdriver-manager\\chromedriver_win32\\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


    

def scrape_data():

    browser = init_browser()
    m2m_vars = {}








    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    html = browser.html


    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all('div', class_="content_title")[-1].text

    preview = soup.find_all('div', class_="rollover_description_inner")[-1].text

    description = preview
    


    m2m_vars["title"]= title
    m2m_vars["description"] = description

    browser.quit()

    url2= 'https://space-facts.com/mars/'
    mars_data= pd.read_html(url2)

    mars_df= mars_data[0]
        
    mars_df.columns = ["Parameter", "Measurement"]

    m2m_vars["table"]= mars_df.to_html()
    

    url3= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response2=requests.get(url3)

    soup3 = BeautifulSoup(response2.text, 'html.parser')

    img_html= soup3.find_all("div", class_="item")

    image_urls=[]

    for x in range(len(img_html)):
        img=img_html[x].find_all("img")[0]['src']
        base_url='https://astrogeology.usgs.gov'
        image_urls.append(f'{base_url}{img}')

    hemisphere_image_urls= [
        {"title": "Valles Marineris Hemisphere", "img_url": image_urls[3]},
        {"title": "Cerberus Hemisphere", "img_url": image_urls[0]},
        {"title": "Schiaparelli Hemisphere", "img_url": image_urls[1]},
        {"title": "syrtis Major Hemisphere", "img_url": image_urls[2]}
    ]

    m2m_vars["hem_img"]= hemisphere_image_urls

    url4="https://www.nasa.gov/mission_pages/msl/images/index.html"

    browser = init_browser()

    browser.visit(url4)

    html2 = browser.html

    soup4 = BeautifulSoup(html2, 'html.parser')

    browser.quit()

    img_src=soup4.find_all("img")[4]['src']

    baseURL = "https://www.nasa.gov"

    feat_img=f'{baseURL}{img_src}'
    
    m2m_vars["feat_img"] = feat_img








    return m2m_vars
