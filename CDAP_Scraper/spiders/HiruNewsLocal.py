import scrapy
import CDAP_Scraper.items as scraper

class HiruLocal(scrapy.Spider):
    name = 'HiruLocal'
    allowed_domains = ['hirunews.lk']
    start_urls = ['http://www.hirunews.lk/sinhala/all-news.php?pageID=%d' % page for page in range(2000, 3552)]
    # start_urls = ['http://www.hirunews.lk/local-news.php']

    def parse(self, response):

        # Main headings
        for news_block in response.xpath("//div[contains(@class, 'lts-cntp')]"):
            item = scraper.CdapScraperItem()
            heading = news_block.xpath("a/text()").extract_first()
            content_link = news_block.xpath("a/@href").extract_first()

            item["heading"] = heading
            item["link"] = content_link

            request = scrapy.Request(content_link, callback=self.parse_content)
            request.meta['item'] = item
            yield request

    # Parse content of the news article
    def parse_content(self, response):
        item = response.meta['item']
        content = response.xpath("string(//div[contains(@class, 'lts-txt2')])").extract_first()
        # date = response.xpath("//div[contains(@class, 'lts-cntbx2')]//div[contains(@class, 'time')]/text()").extract_first()
        item['content'] = content
        # item['date'] = date
        yield item