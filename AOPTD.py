# -*- coding: utf-8 -*-
import scrapy

from AOPSpider.items import AopspiderItem
class AoptdSpider(scrapy.Spider):
    name = 'AOPTD'
    item = AopspiderItem()
    def parseSUMPAGE(self, response):
    #Extracting the content using css selectors
        CompanyName = response.css("h1.company__name::text")[0].extract()
        EPS = response.css("span.kv__value.kv__primary::text")[9].extract()
        MarketCap = response.css("span.kv__value.kv__primary::text")[3].extract()
        PERatio = response.css("span.kv__value.kv__primary::text")[8].extract()


        #Give the extracted content row wise
        for item in zip(CompanyName,EPS,MarketCap,PERatio):
            #create a dictionary to store the scraped info
            scraped_infoSUMPAGE = {
                'CompanyName' : item[0],
                'EPS' : item[1],
                'MarketCap' : item[2],
                'PERatio' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_infoSUMPAGE

    def parseAIS(self, response):

        REVLYA1 = response.css('td.valueCell::text')[5].extract()
        REVLYA2 = response.css('td.valueCell::text')[4].extract()
        REVLYA3 = response.css('td.valueCell::text')[3].extract()
        REVLYA4 = response.css('td.valueCell::text')[2].extract()
        EBITDALYA1 = response.css('td.valueCell::text')[257].extract()
        EBITDALYA2 = response.css('td.valueCell::text')[256].extract()
        EBITDALYA3 = response.css('td.valueCell::text')[255].extract()
        EBITDALYA4 = response.css('td.valueCell::text')[254].extract()
        SGALYA1 = response.css('td.valueCell::text')[47].extract()
        SGALYA2 = response.css('td.valueCell::text')[46].extract()
        SGALYA3 = response.css('td.valueCell::text')[45].extract()
        SGALYA4 = response.css('td.valueCell::text')[44].extract()
        for item in zip(REVLYA1, REVLYA2, REVLYA3, REVLYA4, EBITDALYA1, EBITDALYA2, EBITDALYA3, EBITDALYA4, SGALYA1, SGALYA2, SGALYA3, SGALYA4):
            items_requestedAIS = {
                'REVLYA1' : item[0],
                'REVLYA2' : item[1],
                'REVLYA3' : item[2],
                'REVLYA4' : item[3],
                'EBITDALYA1' : item[4],
                'EBITDALYA2' : item[5],
                'EBITDALYA3' : item[6],
                'EBITDALYA4' : item[7],
                'SGALYA1' : item[8],
                'SGALYA2' : item[9],
                'SGALYA3' : item[10],
                'SGALYA4' : item[11],
                }
            yield items_requestedAIS


    def parseQIS(self,response):

        REVLQA1 = response.css('td.valueCell::text')[5].extract()
        REVLQA2 = response.css('td.valueCell::text')[4].extract()
        REVLQA3 = response.css('td.valueCell::text')[3].extract()
        REVLQA4 = response.css('td.valueCell::text')[2].extract()
        for item in zip(REVLQA1, REVLQA2, REVLQA3, REVLQA4):
            items_requestedQIS = {
            'REVLQA1' : item[0],
            'REVLQA2' : item[1],
            'REVLQA3' : item[2],
            'REVLQA4' : item[3],

            }
            yield items_requestedQIS


    def parseCFS(self, response):

        CapExLYA1 = response.css('td.valuecell::text')[95].extract()
        CapExLYA2 = response.css('td.valuecell::text')[94].extract()
        CapExLYA3 = response.css('td.valuecell::text')[93].extract()
        CapExLYA4 = response.css('td.valuecell::text')[92].extract()

        for item in zip(CapExLYA1, CapExLYA2, CapExLYA3, CapExLYA4):
            items_requestedCFS = {
            'CapExLYA1' : item[0],
            'CapExLYA2' : item[1],
            'CapExLYA3' : item[2],
            'CapExLYA4' : item[3],
            }

            yield items_requestedCFS

    def parseVAL(self, response):

        item['PtoBV'] = response.css('p.data.lastcolumn::text')[4].extract()
        item['EVtoEBITDA'] = response.css('p.data.lastcolumn::text')[6].extract()
        for item in zip(PtoBV, EVtoEBITDA):
            items_requestedVAL = {
            item['PtoBV'],
            item['EVtoEBITDA']
            }
            yield items_requestedVAL

    def start_requestsSUMPAGE(self):
        urls =  (
        'https://marketwatch.com/investing/stock/sach',
        'https://marketwatch.com/investing/stock/lee',
        )
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseSUMPAGE)

    def start_requestsAIS(self):
        urls = (
        'https://marketwatch.com/investing/stock/sach/financials',
        'https://marketwatch.com/investing/stock/lee/financials',

        )
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseAIS)

    def start_requests(self):
        urls = (

        'https://marketwatch.com/investing/stock/sach/financials/income/quarter',
        'https://marketwatch.com/investing/stock/lee/financials/income/quarter',

        )

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def start_requestsCFS(self):
        urls = (
        'https://marketwatch.com/investing/stock/sach/financials/cash-flow',
        'https://marketwatch.com/investing/stock/lee/financials/cash-flow'

        )
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseCFS)


    def start_requestsVAL(self):
        urls = (
        'https://marketwatch.com/investing/stock/sach/profile',
        'https://marketwatch.com/investing/stock/lee/profile'

        )
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseVAL)


    # https://stackoverflow.com/questions/37604916/scrapy-request-url-must-be-str-or-unicode-got-selector
