from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


path = r'C:/Users/Owner/AppData/Local/Programs/Python/chromedriver_win32/chromedriver.exe'
options = Options()
options.headless = True
args = ['hide_console']
driver = webdriver.Chrome(executable_path=path,chrome_options=options,service_args=args)
    
def all_psi_dengue():
    url = 'https://www.nea.gov.sg'
    page_source = driver.get(url)
    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')
    psi_level = soup.find_all('div',class_='number')[0].text
    dengue_case = soup.find_all('div',class_='number')[3].text
    print('(ALL)The 24 hr PSI is ' + psi_level)
    print('(ALL)The number of dengue cases are ' + dengue_case)

def psi(content_id):
    url2 = 'https://www.haze.gov.sg/'
    page_source = driver.get(url2)
    source = driver.page_source
    soup2 = BeautifulSoup(source, 'html.parser')
    psi_all = soup2.find_all('div',class_='top')
    for psi in psi_all:
        psi = psi.find_all('span',{'id':content_id})
        if (len(psi)>0 ):
            result = psi[0].text
            return result
## ContentPlaceHolderTicker_C049_LitValueNorth,South,East,Central,West

def weather(time,location):
    url3 = 'https://www.nea.gov.sg/weather'
    page_source = driver.get(url3)
    source = driver.page_source
    soup3 = BeautifulSoup(source,'html.parser')
    weather_all = soup3.find_all('div',{'data-day':time})
    for weather1 in weather_all:
        weather1 = weather1.find_all('span',{'id':location})
        if(len(weather1)>0):
            result = weather1[0]['title']
            return result
## morn,afternoon,nextnight ##north,south,east,central,west

all_psi_dengue()

psi_north = psi('ContentPlaceHolderTicker_C049_LitValueNorth')
weather_north = weather('morn','north-{day}')
print('(NORTH)Weather is '+weather_north+ ' and PSI is '+psi_north)

psi_south = psi('ContentPlaceHolderTicker_C049_LitValueSouth')
weather_south = weather('morn','south-{day}')
print('(SOUTH)Weather is '+weather_south+ ' and PSI is '+psi_south)

psi_central = psi('ContentPlaceHolderTicker_C049_LitValueCentral')
weather_central = weather('morn','central-{day}')
print('(CENTRAL)Weather is '+weather_central+ ' and PSI is '+psi_central)

psi_west = psi('ContentPlaceHolderTicker_C049_LitValueWest')
weather_west = weather('morn','west-{day}')
print('(WEST)Weather is '+weather_west+ ' and PSI is '+psi_west)

psi_east = psi('ContentPlaceHolderTicker_C049_LitValueEast')
weather_east = weather('morn','east-{day}')
print('(EAST)Weather is '+weather_east+ ' and PSI is '+psi_east)


