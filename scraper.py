import selenium.webdriver as sw
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape(website):
    print("Launching Chrome...")
    driver_path="./chromedriver.exe"
    options=sw.ChromeOptions()
    driver=sw.Chrome(service=Service(driver_path),options=options)
    try:
        driver.get(website)
        print("Page Loaded!")
        html=driver.page_source
        return html
    finally:
        driver.quit()

def extract(content):
    soup=BeautifulSoup(content,"html.parser")
    body_content=soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(content):
    soup=BeautifulSoup(content,"html.parser")
    for script in soup(["script","style"]):
        script.extract()
    clean= soup.get_text(seperator="\n")
    clean="\n".join([i.strip() for i in clean.splitlines() if i.strip()])
    return clean

def split_content(dom_content, max_length=6000):
    return [dom_content[i: i+max_length] for i in range(0, len(dom_content), max_length)]
