import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    # 크롤러의 이름
    name = 'book_crawl'
    
    # 크롤러 실행을 허용할 도메인 / 허용된 도메인 이외는 무시함
    allowed_domains = ['hanbit.co.kr']
    
    # 시작점으로 사용할 url / 리스트로 지정해 한 번에 여러 웹 페이지에서 크롤링을 시작하게 할 수 있음
    start_urls = [
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=001001',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?page=1&cate_cd=001001&srt=p_pub_date',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?page=1&cate_cd=001001'
        # 'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=002',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=003',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=004',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=005',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=006',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=007',
        # 'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=008',
                  ]
    # scrapy crawl book_crawl -o book_list.csv -t csv
    # cd ScrapyTest/hanbit_crawling
    # 크롤러가 어떻게 작동할지 규칙을 설정하는 단계
    # 시작점의 모든 링크를 검사한 후,
    # 규칙에 맞는 링크가 있으면 정해진 콜백 메서드를 실행
    # follow가 True면 해당 페이지의 링크를 재귀적으로 위 작업을 반복
    rules = (
        Rule(
            # store/books/look.php?p_code=B8463790401
            LinkExtractor(allow=r'store/books/look.php\?p_code=.*'),  

            # 해당 링크에 요청을 보내고 응답이 오면 실행할 콜백 메서드를 지정
            callback='parse_item', 
            
            # True로 설정되어 있으면, 응답에 다시 한번 rules를 적용해 재귀적으로 실행합니다.
            follow=False),
        
        # 이렇게 여러 개의 규칙을 설정 가능
        # Rule(
        #     LinkExtractor(allow=r'store/books/category_list\.html\?page=\d+&cate_cd=00\d+&srt=p_pub_date'))
        )
#=================================================================================================
    def parse_item(self, response):
        """rules를 통과한 링크에 요청을 보내 응답을 받으면 Rule()에 설정한 콜백 메서드를 해당 
           응답 결과에 실행합니다.
           따라서 response를 파라미터로 받고 XPath라든가 CSS 선택자를 이용해서 원하는 요소를 추출
           할 수 있습니다.
        """
        
        # 앞서 설정한 item에 맞춰 딕셔너리를 채우고 반환합니다.
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        
        # 책 이름
        i['book_title'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3/text()').extract()
                                        # //*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3
        # 저자 이름
        i['book_author'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="저자 : "]/span/text()').extract()
                                         # //*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/span
        # 번역자 이름
        i['book_translator'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="번역 : "]/span/text()').extract()
        
        # 출간일
        i['book_pub_date'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="출간 : "]/span/text()').extract()

        # ISBN
        i['book_isbn'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="ISBN : "]/span/text()').extract()
        return i