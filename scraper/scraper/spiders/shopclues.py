import scrapy
from scraper.items import ScraperItem
from shop.models import phones
class ShopcluesSpider(scrapy.Spider):
   #name of spider
   name = 'shopclues'

   #list of allowed domains
   allowed_domains = ['www.shopclues.com/mobiles-featured-store-4g-smartphone.html']
   #starting url
   start_urls = ['http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html/']
   #location of csv file
   custom_settings = {
       'FEED_URI' : 'tmp/shopclues.csv'
   }


   def parse(self, response):
       #Extract product information
       titles = response.css('img::attr(title)').extract()
       images = response.css('img::attr(data-img)').extract()
       prices = response.css('.p_price::text').extract()
       #discounts = response.css('.prd_discount::text').extract()


       for i in zip(titles,prices,images):
           item = ScraperItem()
           print(i[0])
        #    phones.objects.create(titles=i[0], prices=i[2],images=i[3])
           item["titles"]= i[0],
           item["prices"]=i[1],
           item["images"]=i[2], #Set's the url for scrapy to download images
        #    item["discount"]=i[3]
           yield item