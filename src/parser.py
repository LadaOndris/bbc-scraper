from abc import ABC, abstractmethod

from bs4 import BeautifulSoup


class ContentParser(ABC):

    @abstractmethod
    def parse(self, string: str):
        pass


class BbcContentParser(ContentParser):

    def parse(self, html_content: str):
        soup = self._get_page_soup(html_content)
        header, content = self._parse_soup(soup)
        return header, content

    def _get_page_soup(self, html_content: str):
        soup = BeautifulSoup(html_content, "html.parser")
        return soup

    def _parse_soup(self, soup):
        heading = soup.find_all('h1')[0].text
        article_elem = soup.find('article')
        text_elems = self._get_text_elems(article_elem)
        paragraph_elems = [elem.find('p') for elem in text_elems]
        paragraphs = [elem.text for elem in paragraph_elems]
        content = ' '.join(paragraphs)
        content = self._remove_whitespaces(content)
        return heading, content

    def _get_text_elems(self, parent):
        elems = parent.find_all('div', attrs={'data-component': 'text-block'})
        return elems

    def _remove_whitespaces(self, text):
        text = ' '.join(text.split())
        return text
