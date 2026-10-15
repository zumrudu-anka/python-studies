from pathlib import Path

import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    page_count = 0
    book_count = 1
    file = open("books.txt", "a", encoding="UTF-8")
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&page=1&list_id=1"
    ]

    def parse(self, response):
        book_names = response.css("div.name.ellipsis a span::text").extract()
        book_authors = response.css("div.author span:first-child a span::text").extract()
        book_publishers = response.css("div.publisher span a span::text").extract()

        if "Platin Üyelik 1 Aylık Abonelik" in book_names:
            book_names.remove("Platin Üyelik 1 Aylık Abonelik")
        if "KİTAPYURDU" in book_publishers:
            book_publishers.remove("KİTAPYURDU")

        i = 0
        while(i < len(book_names)):
            # yield {
            #     "name" : book_names[i],
            #     "author" : book_authors[i],
            #     "publisher" : book_publishers[i]
            # }
            self.file.write("--------------------------\n")
            self.file.write(f"{self.book_count}.\n")
            self.file.write(f"Kitap İsmi: {book_names[i]}\n")
            self.file.write(f"Yazar: {book_authors[i]}\n")
            self.file.write(f"Yayıncı: {book_publishers[i]}\n")
            self.file.write("--------------------------\n")
            self.book_count += 1
            i += 1

        next_url = response.css("div.pagination div.links a.next::attr(href)").extract_first()
        self.page_count += 1
        if next_url is not None and self.page_count != 5:
            yield scrapy.Request(url = next_url, callback = self.parse)
        else:
            self.file.close()