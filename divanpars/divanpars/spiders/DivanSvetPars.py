import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divanSvetPars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"] # start_urls - это та ссылка, от которой начинается парсинг

    def parse(self, response):
# Создаём переменную, в которую будет сохраняться информация
# Пишем ту же команду, которую писали в терминале
        svets = response.css('div._Ud0k')
# Настраиваем работу с каждым отдельным диваном в списке
        for svet in svets: # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
            yield {
                'name': svet.css('div.lsooF span::text').get(),  # ::text(псевдокласс) — поиск по тексту
                'price': svet.css('div.pY3d2 span::text').get(),
                'url': svet.css('a::attr(href)').get()
            }
