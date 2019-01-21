import scrapy
from CDAP_Scraper.items import CdapScraperItem


class LankadeepaSpider(scrapy.Spider):
    name = 'lankadeepa'
    allowed_domains = ['lankadeepa.lk']
    start_urls = ['http://www.lankadeepa.lk/features/1/%d' % page for page in range(1, 30, 30)]
    # start_urls = ['http://www.lankadeepa.lk/features/1/300']

    def parse(self, response):

        # Main headings
        for news_block in response.xpath("//div[contains(@class, 'simple-thumb')]"):
            item = CdapScraperItem()
            heading = news_block.xpath("h3/a/text()").extract_first()
            content_link = news_block.xpath("a/@href").extract_first()

            item["heading"] = heading
            item["link"] = content_link

            request = scrapy.Request(content_link, callback=self.parse_content)
            request.meta['item'] = item
            yield request


    # Parse content of the news article
    def parse_content(self, response):

        item = response.meta['item']
        content = response.xpath("string(//div[contains(@class, 'post-header')]/header)").extract_first()
        # date = response.xpath("//div[contains(@class, 'lts-cntbx2')]//div[contains(@class, 'time')]/text()").extract_first()
        # date = response.xpath("//div[contains(@class, 'emp-date-bar-main')]/p/text()").extract_first()

        item['content'] = content
        # item['date'] = date
        yield item
