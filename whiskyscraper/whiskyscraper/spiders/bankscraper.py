import time
import scrapy
from scrapy.http import Request
from scrapy_splash import SplashRequest

class BankSpider(scrapy.Spider):
    name = "bankscraper"
    start_urls = ["https://www.sikayetvar.com/banka"]
    for i in range(2,1001):
        start_urls.append('https://www.sikayetvar.com/banka?page='+str(i))
    def start_requests(self):
        #urls = ["https://www.sikayetvar.com/banka"]
        for url in self.start_urls:
            time.sleep(1)
            yield SplashRequest(url = url, callback = self.parse)
    def parse(self,response):
        for complaints in response.css("article.story-card"):
            try:
                yield {
                    'name': complaints.css('a.complaint-layer::text').get(),
                    'text': complaints.css('p::text').get(),
                    'link': 'https://www.sikayetvar.com' + complaints.css('a.complaint-layer::attr(href)').get()
                }
            except:
                yield {
                    'name': None,
                    'text': None,
                    'link': None
                }
        next_page = 'https://www.sikayetvar.com'+response.css('ul.pagination>li>a.page-link::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

