import scrapy
from CDAP_Scraper.items import CdapScraperItem


class FootballSpider(scrapy.Spider):
    name = 'Football'
    allowed_domains = ['kelimandala.lankadeepa.lk']
    start_urls = ['http://kelimandala.lankadeepa.lk/more/football/%d' % page for page in range(1,8000,20)]
    # start_urls = ['http://kelimandala.lankadeepa.lk/more/cricket']

    def parse(self, response):

        # Main headings
        for news_block in response.xpath("//div[contains(@class, 'krida_puwath_thawaduratath_content_wrapper')]"):
            item = CdapScraperItem()
            # heading = news_block.xpath("h3/a/text()").extract_first()
            heading = news_block.xpath("//div[contains(@class, 'krida_puwath_thawaduratath_inner_heading')]/text()").extract_first()
            content_link = news_block.xpath("a/@href").extract_first()

            item["heading"] = heading
            item["link"] = content_link

            request = scrapy.Request(content_link, callback=self.parse_content)
            request.meta['item'] = item
            yield request


    # Parse content of the news article
    def parse_content(self, response):

        item = response.meta['item']
        content = response.xpath("string(//div[contains(@class, 'left_inner_temp')])").extract_first()
        # date = response.xpath("//div[contains(@class, 'lts-cntbx2')]//div[contains(@class, 'time')]/text()").extract_first()
        # date = response.xpath("//div[contains(@class, 'emp-date-bar-main')]/p/text()").extract_first()

        item['content'] = content
        # item['date'] = date
        yield item
