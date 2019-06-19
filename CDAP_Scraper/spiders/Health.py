import scrapy
import CDAP_Scraper.items as scraper

class Health(scrapy.Spider):
    name = 'Health'
    allowed_domains = ['sinhalahealth.com']
    start_urls = ['http://sinhalahealth.com/si/page/%d' % page for page in range(1, 199)]
    # start_urls = ['http://www.hirunews.lk/local-news.php']

    def parse(self, response):

        # Main headings
        for news_block in response.xpath("//header/h2"):
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
        content = response.xpath("string(//p)").extract_first()
        # date = response.xpath("//div[contains(@class, 'lts-cntbx2')]//div[contains(@class, 'time')]/text()").extract_first()
        item['content'] = content
        # item['date'] = date
        yield item
