from bs4 import BeautifulSoup

class Parser:
    def parse(self, html_content: str) -> dict:
        soup = BeautifulSoup(html_content, 'html.parser')
        # there can be one more method to extract links and push to the centralized queue
        metadata = {
            'title': self._extract_title(soup),
            'description': self._extract_description(soup),
            'body': self._extract_body(soup)
        }
        return metadata

    def _extract_title(self, soup) -> str|None:
        title_tag = soup.find('title')
        return title_tag.get_text() if title_tag else None

    def _extract_description(self, soup) -> str|None:
        meta_tag = soup.find('meta', attrs={'name': 'description'})
        return meta_tag['content'] if meta_tag else None

    def _extract_body(self, soup) -> str|None:
        body_tag = soup.find('body')
        return body_tag.get_text() if body_tag else None
