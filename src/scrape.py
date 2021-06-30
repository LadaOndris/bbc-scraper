from src.parser import BbcContentParser
from src.source import RssUrlSource
from src.web import HttpClient
from src.writer import CsvWriter

if __name__ == '__main__':
    writer = CsvWriter('../db/scrape.csv')
    source = RssUrlSource(['http://feeds.bbci.co.uk/news/rss.xml'])
    http = HttpClient()
    parser = BbcContentParser(source)

    for page_url in source:
        page_content = http.request_html_page(page_url)
        header, content = parser.parse(page_content)
        writer.write_row(header, content)
