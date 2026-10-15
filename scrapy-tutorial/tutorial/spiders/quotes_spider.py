from pathlib import Path

import scrapy

BASE_URL = "https://quotes.toscrape.com"

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    quote_count = 1
    file = open("quotes.txt", "a", encoding="utf-8")
    start_urls = [
        f"{BASE_URL}/page/1/"
    ]

    # def start_requests(self):
    #     urls = [
    #         "https://quotes.toscrape.com/page/1/",
    #         "https://quotes.toscrape.com/page/2/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         title = quote.css("span.text::text").extract_first()
    #         author = quote.css("small.author::text").extract_first()
    #         tags = quote.css("div.tags a.tag::text").extract()

    #         """ NOTE
    #             yield yapisini bu sekilde kullanarak json dosyasi halinde bir cikti uretebiliriz.
    #             Json ciktisi icin kullanilacak komut: `scrapy crawl quotes -o quotes.json`
    #         """
    #         yield {
    #             "title" : title,
    #             "author" : author,
    #             "tags" : tags
    #         }

    # NOTE asagidaki gibi ciktiyi txt dosyasina da yazdirabiliriz
    def parse(self, response):
        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            self.file.write(f"{self.quote_count}***********************\n")
            self.file.write(f"Alıntı: {title}\n")
            self.file.write(f"Alıntı Sahibi: {author}\n")
            self.file.write(f"Etiketler: {str(tags)}\n")
            self.quote_count += 1

        next_url = response.css("li.next a::attr(href)").extract_first()
        if next_url is not None:
            next_url = f"{BASE_URL}{next_url}"
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.file.close()