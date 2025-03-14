# Scenario: Web Scraping
# Web Scraping often involves downloading multiple web pages or files.
# This can be a time-consuming process, especially if the web server is slow
# or if there are many files to download. In this case, you can use multithreading to download multiple files simultaneously.
# This can significantly reduce the time it takes to download all the files by allowing concurrent fectching of multiple files.




import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/docs/introduction/',
        
'https://tailwindcss.com/',

'https://python.langchain.com/docs/concepts/']

def fetch_content(url):
    response = requests.get(url)                                #request for the url is sent which is then got back as response from the web server
    soup = BeautifulSoup(response.content,'html.parser')        #parsing the content of the response
    print(f'Fetched {len(soup.text)} characters from {url}')    #printing the length of the content fetched from the url
    
threads = []

for url in urls:
    thread = threading.Thread(target = fetch_content,args = (url,)) #creating a thread for each url
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
    
print("All web pages are fetched")