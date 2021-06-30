from abc import ABC, abstractmethod
from typing import List

import feedparser


class UrlSource(ABC):

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class RssUrlSource(UrlSource):

    def __init__(self, rss_sources: List[str]):
        """

        :param rss_sources: List[str]
            The rss sources to parse.
            Urls, local files and strings are supported.
        """
        self.rss_sources = rss_sources
        self.entries = self._create_feeds()
        self.article_urls = self._parse_entries()

    def _create_feeds(self):
        entries = []
        for rss_source in self.rss_sources:
            # TODO exception handling, skip and log the error
            feed = feedparser.parse(rss_source)
            entries += feed.entries
        return entries

    def _parse_entries(self):
        urls = []
        for entry in self.entries:
            urls.append(entry.link)
        return urls

    def __iter__(self):
        self.url_index = 0
        return self

    def __next__(self):
        if self.url_index >= len(self.article_urls):
            raise StopIteration
        url = self.article_urls[self.url_index]
        self.url_index += 1
        return url
