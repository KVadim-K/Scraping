import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"] # start_urls - это та ссылка, от которой начинается парсинг

    def parse(self, response):
# Создаём переменную, в которую будет сохраняться информация
# Пишем ту же команду, которую писали в терминале
        divans = response.css('div._Ud0k')
# Настраиваем работу с каждым отдельным диваном в списке
        for divan in divans: # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(divan.css('a::attr(href)').get())  # response.urljoin() - объединяет две ссылки
            }

# scrapy crawl divannewpars -o output.csv -t csv # Команда для запускаем парсинга в терминале