from RenGen.UMLDiagram import UMLDiagram

from bs4 import BeautifulSoup
from httpx import Client
from markdownify import markdownify

from concurrent.futures import ThreadPoolExecutor


class Lab:
    def __init__(self, link: str, base_url: str, client: Client):
        self._client = client

        self.link = link
        self.base_url = base_url

        self.classes = {}

        with ThreadPoolExecutor() as executor:
            # noinspection PyTypeChecker
            self._future = executor.submit(self._client.get, f"{self.base_url}{self.link}")

        self._page = None

    def _get_page(self) -> BeautifulSoup:
        if self._page is None:
            self._page = BeautifulSoup(self._future.result().text, "html.parser").find("article", attrs={"class": "doc"})
            del self._future
        return self._page

    def to_markdown(self) -> str:
        page = self._get_page().__copy__()
        for svg in page.find_all("svg"): svg.decompose()

        return markdownify(str(page))

    def fetch_uml_diagrams(self):
        for svg in self._get_page().find_all("svg"):
            for diagram_child in svg.find_all("rect", attrs={"fill": "#F1F1F1"}):
                diagram = UMLDiagram(diagram_child.parent)
                self.classes[diagram.class_name] = diagram

    def add_explanations(self): pass  # TODO

    def get_java_str(self, class_key: str) -> str:
        _return = f"public class {class_key} {{\n" + str(self.classes[class_key])
        return _return + ('}' if _return[-1] == '\n' else '\n}')
