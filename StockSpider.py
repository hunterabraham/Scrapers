import scrapy

class YhlradspiderSpider(scrapy.Spider):
    name = 'YHLRADSPIDER'
    def parse(self, response):
        
        items_requested = {
            'Company Name':response.css("span.stock-title::text").extract_first(),
            'Current Price':response.css("dd::text")[0].extract(),
            'Previous Close':response.css("dd::text")[7].extract(),
            'Market Cap':response.css("dd::text")[16].extract(),
            'P/E Ratio':response.css("dd::text")[19].extract(),

                }
        yield items_requested
                     # get this css field through inspect function and find areas

    # https://stackoverflow.com/questions/37604916/scrapy-request-url-must-be-str-or-unicode-got-selector

    def start_requests(self):
        urls = (

        'https://research.tdameritrade.com/grid/public/research/stocks/summary?symbol=LPTH',
        'https://research.tdameritrade.com/grid/public/research/stocks/summary?symbol=AMAG',
        'https://research.tdameritrade.com/grid/public/research/stocks/summary?symbol=PGNX',
        'https://research.tdameritrade.com/grid/public/research/stocks/summary?symbol=CVGI',
        'https://research.tdameritrade.com/grid/public/research/stocks/summary?symbol=LRAD',
        'https://research.tdameritrade.com/grid/public/research/stocks/summary?symbol=JONE'

        )

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
