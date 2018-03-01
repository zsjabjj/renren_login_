# -*- coding: utf-8 -*-
import scrapy

from Renren.items import RenrenItem


class RenrenSpider(scrapy.Spider):
    name = 'renren_form'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']


    def parse(self, response):
        '''模拟登录, 因为只有登录后才有我们需要的数据, 所以需要重写此类'''

        # post数据
        post_data = {
            'email': '17173805860',
            'password': '1qaz@WSX3edc'
        }
        # 发送post请求
        # from_response这个类方法只针对响应源码中有表单的进行模拟登录, post请求后得到的数据, 交给另一个方法进行处理
        yield scrapy.FormRequest.from_response(response, formdata=post_data, callback=self.parse_login)

    def parse_login(self, response):
        '''解析数据, 将post请求发送后得到的数据进行解析'''
        with open('renren2.html', 'wb') as f:
            f.write(response.body)
