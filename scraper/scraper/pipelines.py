# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from shop.models import phones

class ScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            phones.objects.create(titles=item['titles'], prices=item["prices"],images=item["images"])
            print("\n")
            #logger.warn("Loaded phone {}".format(item['titles']))
            # print("pass")
            # print(item)
        except Exception as e:
            print("\n")
            #logger.error("\nFailed to load quote, Reason For Failure:{}".format(e))
            # print("fail")
            # print(item)
        return item
