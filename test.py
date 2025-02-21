import unittest
from unittest.mock import MagicMock
from run import PageCollection

class TestPageCollection(unittest.TestCase):
    def test_collector(self):
        # Mock the dependencies
        mock_crawler = MagicMock()
        mock_parser = MagicMock()
        mock_classifier = MagicMock()

        # Set up the return values for the mocks
        mock_crawler.fetch.return_value = '<html><title>Test Page</title></html>'
        mock_parser.parse.return_value = {'title': 'Test Page', 'description': None, 'body': None}
        mock_classifier.classify.return_value = ['Test']

        # Create the collector with the mocked dependencies
        collector = PageCollection(mock_crawler, mock_parser, mock_classifier)

        # Call the collect method
        metadata, topics = collector.collect('http://google.com')

        # Assert the results
        self.assertEqual(metadata, {'title': 'Test Page', 'description': None, 'body': None})
        self.assertEqual(topics, ['Test'])

if __name__ == '__main__':
    unittest.main()