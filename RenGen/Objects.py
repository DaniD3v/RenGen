from bs4 import BeautifulSoup, Tag


class UMLObject:
    def __init__(self, tag: Tag):
        self.og_text = tag.text.replace('\n', '').replace(';', '').strip()

        self.comment = ""
        text = [t.strip() for t in self.og_text.split("//")]
        if len(text) == 2: self.comment = f" // {text[1]}"

        self.og_text = text[0]
        self.invalid = False

        if tag.name == "line": self.height = tag["y1"]
        elif tag.name == "[document]": self.height = None  # height isn't needed here
        else: self.height = tag["y"]

    def __repr__(self):
        if self.og_text:
            if self.og_text.startswith("//"): return f"\t{self.og_text}"
            else: return f"\t// {self.og_text}"
        return ""


class Line(UMLObject):
    def __init__(self, tag: Tag):
        if tag.next.name == "text": super().__init__(tag.next)
        else: super().__init__(tag)


class Attribute(UMLObject):
    def __init__(self, tag: Tag, is_parameter=False):
        super().__init__(tag)
        self.is_parameter = is_parameter

        text = [t.strip() for t in self.og_text.split('=')]
        name_type = [t.strip() for t in text[0].split(':')]

        self.name = name_type[0]
        try: self.type = name_type[1]
        except IndexError: self.invalid = True; return

        self.value = None
        if len(text) == 2: self.value = text[1]

    def check_valid(self) -> bool:
        if self.invalid: return False
        return (
            self.name.isalnum() and
            self.type.replace("[", "").replace("]", "").isalnum()
        )

    def __repr__(self) -> str:
        if self.check_valid():
            if self.is_parameter: return f"{self.type} {self.name}" + (f" = {self.value}" if self.value else "")
            else: return f"\t{self.type} {self.name}" + (f" = {self.value}" if self.value else "") + ';' + self.comment

        if self.is_parameter: return f"/* {super().__repr__()[4:]} */"
        else: return super().__repr__()


class Method(UMLObject):
    def __init__(self, tag: Tag, class_name: str):
        super().__init__(tag)

        if self.og_text == "": self.invalid = True; return

        text = [t.strip() for t in self.og_text.split(")") if t != ""]
        if len(text) == 0: print(self.og_text)

        name_param = text[0].split('(')
        if len(name_param) != 2: self.invalid = True; return

        self.type = "void"
        if len(text) == 2: self.type = text[1]
        if ':' in self.type: self.type = self.type.split(':')[1].strip()

        self.name = name_param[0]
        if self.name.lower() in ["constructor", "konstruktor", "constructor " + class_name.lower(), "konstruktor " + class_name.lower(), class_name.lower()]:
            self.name = class_name
            self.type = None

        self.modifier = "public"  # TODO get rect from tag.previous and check for color

        self.params = [Attribute(self._make_fake_tag(param.strip()), True) for param in name_param[1].split(',') if param != '']

    @staticmethod
    def _make_fake_tag(text: str) -> Tag:
        return BeautifulSoup(f"<fake_tag>{text}</fake_tag>", "html.parser")

    def check_valid(self) -> bool:
        if self.invalid: return False
        if not (self.type is None or self.type.replace('[', '').replace(']', '').isalnum()): print("2: " + self.type)
        return (
            self.name.isalnum() and
            (self.type is None or self.type.replace("[", "").replace("]", "").isalnum())
            #not (False in [param.check_valid() for param in self.params])
        )

    def __repr__(self):
        if self.check_valid(): return f"\t{self.modifier} {(self.type + ' ') if self.type else ''}{self.name}({', '.join([str(param) for param in self.params])}) " + '{' + self.comment + "\n\t\t\n\t}\n"
        return super().__repr__()
