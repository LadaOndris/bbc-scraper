import unittest

from src.source import RssUrlSource


class TestRssUrlSource(unittest.TestCase):

    def test_reading_single_rss_source(self):
        rss_sources = ['test_rss.xml']
        source = RssUrlSource(rss_sources)

        urls = [url for url in source]
        first_url = urls[0]
        last_url = urls[-1]

        self.assertEqual(len(urls), 57)
        self.assertEqual(first_url, 'https://www.bbc.co.uk/news/world-us-canada-57671012')
        self.assertEqual(last_url, 'https://www.bbc.co.uk/news/stories-57520169')
