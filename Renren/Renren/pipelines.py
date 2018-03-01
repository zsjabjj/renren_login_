# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RenrenPipeline(object):
    def __init__(self):
        # self.f = open('renren.html', 'wb')
        pass
        
    def process_item(self, item, spider):
        # print('-' * 30)
        # print(len(item['data']))
        # print('-' * 30)
        # self.f.write(item['data'])
        # return item
        return '------------------OK------------------'

    def __del__(self):
        # self.f.close()
        pass