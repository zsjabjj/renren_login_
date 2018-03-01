# -*- coding: utf-8 -*-
import scrapy

from Renren.items import RenrenItem


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        '''模拟登录, 因为只有登录后才有我们需要的数据, 所以需要重写此类'''
        # form表单提交的url
        url = self.start_urls[0]
        # post数据
        post_data = {
            'email': '17173805860',
            'password': '1qaz@WSX3edc'
        }
        # 发送post请求
        # 在源码中, 如果有formdata传入, 会将请求设置为POST请求, 如果没有, 就仍然是GET请求的Request类
        yield scrapy.FormRequest(url, formdata=post_data)

    def parse(self, response):
        '''解析数据, 将post请求发送后得到的数据进行解析'''
        # with open('renren.html', 'wb') as f:
        #     f.write(response.body)
        item = RenrenItem()
        item['data'] = response.body
        yield item
