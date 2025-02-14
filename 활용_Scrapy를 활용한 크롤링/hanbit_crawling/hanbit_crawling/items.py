# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HanbitCrawlingItem(scrapy.Item):
    
    # 책 이름
    book_title = scrapy.Field()
    
    # 저자 이름
    book_author = scrapy.Field()
    
    # 번역자 이름
    book_translator = scrapy.Field()
    
    # 출간일
    book_pub_date = scrapy.Field()
    
    # ISBN
    book_isbn = scrapy.Field()
    pass

