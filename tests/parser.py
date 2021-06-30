import unittest

from src.parser import BbcContentParser


class TestBbcContentParser(unittest.TestCase):

    def test_parse_single_article(self):
        with open('test_article.html', 'r') as file:
            source_html = file.read()

        with open('test_article_content.txt', 'r') as file:
            expected_content = file.read()

        reader = BbcContentParser()
        heading, content = reader.parse(source_html)

        self.assertEqual(heading, 'Bill Cosby freed after top Pennsylvania court overturns sex conviction')
        self.assertEqual(len(content), 2437)
        self.assertEqual(content, expected_content)
