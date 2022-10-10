from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(CrawlSpider):
    name = "crawler"
    allowed_domains = [str(input('enter the website address in pattern abc.xyz:'))]
    start_urls = [f'https://{allowed_domains[0]}']
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
        for href in response.css('a::attr(href)'):
            link = href.extract()
            if self.start_urls[0] in href_:
                if href_ + link not in links_:
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
        elif len(links_) == 0:
            if self.start_urls[0] in href_:
                if href_.split(':')[0] != 'http':
                    yield {
                        'url': href_,
                        'title': title,
                        'internal links count': 0,
                        'external links count': 0,
                    }