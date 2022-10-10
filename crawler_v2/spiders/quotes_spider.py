from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re


class QuotesSpider(CrawlSpider):
    name = "crawler"
    allowed_domains = [str(input('enter the website address in following format abc.xyz: '))]
    start_urls = [f'https://{allowed_domains[0]}']
    valid_links = re.findall('https://[a-z0-9_.\-]+\.[a-z0-9_\-/]+', start_urls[0])
    # Input validation
    if len(valid_links) == 0:
        raise Exception("Please enter valid website in following format abc.xyz")
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        links_ = []
        internals = []
        externals = []
        titles = []
        href_ = response.request.url
        title = response.css('title::text').get()
        # Scrapping all the links from a href tag
        for href in response.css('a::attr(href)'):
            link = href.extract()
            if self.start_urls[0] in href_:
                if href_ + link not in links_:
                    # Checking for externals links
                    if link.split(':')[0] in ['http', 'https']:
                        links_.append(href_ + link)
                        titles.append(title)
                        externals.append(link)
                    else:
                        links_.append(href_ + link)
                        titles.append(title)
                        internals.append(link)
        if len(links_) > 0:
            if links_[0].split(':')[0] != 'http':
                yield {
                    'url': links_[0],
                    'title': titles[links_.index(links_[0])],
                    'internal links count': len(internals),
                    'external links count': len(externals)
                                }
        # Handle url without links
        elif len(links_) == 0:
            if self.start_urls[0] in href_:
                if href_.split(':')[0] != 'http':
                    yield {
                        'url': href_,
                        'title': title,
                        'internal links count': 0,
                        'external links count': 0,
                    }
