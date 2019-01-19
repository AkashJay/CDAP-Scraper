import scrapy
from CDAP_Scraper.items import CdapScraperItem


class QuotesSpider(scrapy.Spider):

    name = 'lankadeepa'
    allowed_domains = ['lankadeepa.lk']
    start_urls = ['http://www.lankadeepa.lk/features/1']

    def parse(self, response):

        # Main headings
        for news_block in response.xpath("//div[contains(@class, 'simple-thumb')]"):
            item = CdapScraperItem()
            heading = news_block.xpath("h3/a/text()").extract_first()
            item["heading"] = heading
            yield item