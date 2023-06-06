from RenGen.Lab import Lab

import httpx
from bs4 import BeautifulSoup

from concurrent.futures import ThreadPoolExecutor


class Session:
    def __init__(self, base_url):
        self._client = httpx.Client()
        self.base_url = base_url

        with ThreadPoolExecutor() as executor:
            # noinspection PyTypeChecker
            self._future = executor.submit(self._client.get, base_url)

        self._page = None

    def _get_base_page(self) -> BeautifulSoup:
        if self._page is None:
            self._page = BeautifulSoup(self._future.result().text, "html.parser")
            del self._future
        return self._page

    def get_course(self, course_string: str) -> dict[Lab]:
        base_page = self._get_base_page()

        text = base_page.find("span", attrs={"class": "nav-text"}, text=course_string)
        course = text.parent.find("ul")

        return {
            lab.text:Lab(lab["href"], self.base_url, self._client)
            for lab in course.find_all("a", attrs={"class": "nav-link"})
        }
