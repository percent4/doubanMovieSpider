import scrapy
from scrapy.spiders import Spider  
from scrapy.selector import Selector  
from doubanMovie.items import DoubanmovieItem  

class movieSpider(Spider):
    # name of Spider  
    name = "movie"
    #start urls
    start_urls = ["https://movie.douban.com/top250"] 
    for i in range(1,10):
        start_urls.append("https://movie.douban.com/top250?start=%d&filter="%(25*i))

    #parse function
    def parse(self, response):
        
        item = DoubanmovieItem()
        sel = Selector(response)
        images = sel.xpath('//*[@id="content"]/div/div[1]/ol/li')

        item['url'] = [] 
        item['img_name'] = []
        # append the url and name of the image in item
        for image in images:
            # extract url and name of the image   
            site = image.xpath('div/div[1]/a/img/@src').extract_first()
            img_name = image.xpath('div/div[1]/a/img/@alt').extract_first()
            
            item['url'].append(site)
            item['img_name'].append(img_name)
   
        yield item
