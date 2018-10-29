import scrapy

class Test_Spider(scrapy.Spider):
    name="test"

    def start_requests(self):
        File = getattr(self,'File','url.text')
        print "=================="
        print File
        print "=================="

    def parse(self, response):
        pass
