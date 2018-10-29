import scrapy
from bs4 import BeautifulSoup

class Amazon_Spider(scrapy.Spider):
    name="amazon1"

    def start_requests(self):
        File = getattr(self,'File','url.text')
        f = open(File)
        urls = f.readlines()
        #urls = ['https://www.amazon.in/VOTO-V2I-2GB-32GBROM-Black/product-reviews/B075NLQWX2/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2']
        for url in urls:
            print url
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        #print response.body
        #opinions = response.xpath('//*[@id="all-opinions"]/div/p/text()')
        opinions = response.xpath('//*[@id="cm_cr-review_list"]/div/div/div[4]/span')
        ratings =  response.xpath('//*[@id="cm_cr-review_list"]/div/div/div/a[@class="a-link-normal"]/@title')
        urls =  response.xpath('//*[@id="cm_cr-review_list"]/div/div/div/a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/@href')
        dates=  response.xpath('//*[@id="cm_cr-review_list"]/div/div/div/span[@class="a-size-base a-color-secondary review-date"]/text()')
        users =  response.xpath('//*[@id="cm_cr-review_list"]/div/div/div/span/a[@class="a-size-base a-link-normal author"]/text()')

        #username = response.xpath('//*[@id="all-opinions"]/div/ul/li/text()')
        #time = response.xpath('//*[@id="all-opinions"]/div/ul/li/time/text()')
        #print("===================")
        #print len(opinions)
        #print("===================")

        for i in range(0,len(opinions)):
            opinion = BeautifulSoup(opinions[i].extract(), 'html.parser')
            opinion = opinion.get_text()
            rating = ratings[i].extract()[0:3]
            url = urls[i].extract()
            date = dates[i].extract()
            user = users[i].extract()
            yield {
                "user" :  user,
                "date" :  date,
                "url" :  url,
                "opinion" :  opinion,
                "rating" :  rating
            }

