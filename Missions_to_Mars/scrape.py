from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:\\Users\\pmaxl\\OneDrive\\Desktop\\webdriver-manager\\chromedriver_win32\\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_news():


    # Visit site
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response= requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_row = soup.find_all('div', class_="content_title")[0]

    title = title_row.find('a').text
    title = title.strip('\n')

    preview = soup.find_all('div', class_="rollover_description_inner")[0]
    
    description = preview.text
    description = description.strip('\n')
    


def scrape_data():

    url2= 'https://space-facts.com/mars/'
    mars_data= pd.read_html(url2)

    mars_df= mars_data[0]
        
    mars_df.columns = ["Parameter", "Measurement"]

    mdf_html= mars_df.to_html()
    mdf_html = mdf_html.replace('\n', '')

def scrape_hemi():

    url3= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response2=requests.get(url3)

    soup3 = BeautifulSoup(response2.text, 'html.parser')

    img_html= soup3.find_all("div", class_="item")

    image_urls=[]

    for x in range(len(img_html)):
        img=img_html[x].find_all("img")[0]['src']
        image_urls.append(img)

    hemisphere_image_urls= [
        {"title": "Valles Marineris Hemisphere", "img_url": image_urls[3]},
        {"title": "Cerberus Hemisphere", "img_url": image_urls[0]},
        {"title": "Schiaparelli Hemisphere", "img_url": image_urls[1]},
        {"title": "syrtis Major Hemisphere", "img_url": image_urls[2]}
    ]














    
    
