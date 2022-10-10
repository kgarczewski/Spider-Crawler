<h2>Spider-crawler</h2> 
Spider-crawler is a simple crawling and scraping script, used to crawl websites and extracted data from their pages.
Script is looking for every links on the webiste and divide them into two categories: externals and internals links.
Script provides user with detailed data about every link including site title, quantity and types of the links.

Installation

    Clone this repository to local folder
    Open project with python
    Run pip install -r requirements.txt

Use the app

    Run the script with following code: scrapy crawl 'crawler' -o output.<specify output format (csv/json)>
    Enter a website url which you want to check in following format: abc.xyz
    Check created output in selected format
    
  

