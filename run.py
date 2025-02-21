from crawler import Crawler
from parser import Parser
from classifier import Classifier

class PageCollection:
    def __init__(self, crawler: Crawler, parser: Parser, classifier: Classifier) -> None:
        self.crawler = crawler
        self.parser = parser
        self.classifier = classifier

    def collect(self, url) -> tuple:
        html_content = self.crawler.fetch(url)
        # Can have a robots.txt parser placed here to handle adhering to the rules of rate-limiting, url allow/disallow
        if html_content:
            metadata = self.parser.parse(html_content)
            topics = self.classifier.classify(metadata)
            # This data can then be pushed to db/storage
            return metadata, topics
        # Once the data has been parsed, the url needs to be pushed to centralized visited nodes
        return dict(), list()


if __name__ == '__main__':
    crawler = Crawler()
    parser = Parser()
    classifier = Classifier()

    collector = PageCollection(crawler, parser, classifier)

    urls = [
        "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster",
        "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/",
        "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"
    ]

    # Improvement: we can turn this into async tasks to handle the request I/Os

    for url in urls:
        metadata, topics = collector.collect(url)
        print(f"URL: {url}")
        print(f"Metadata: {metadata}")
        print(f"Topics: {topics}")
        print("-" * 40)
