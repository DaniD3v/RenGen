from RenGen.Objects import Attribute, Method, Line

from bs4 import Tag


class UMLDiagram:
    # noinspection PyTypeChecker
    def __init__(self, diagram: Tag):
        self.class_name = diagram.find("line").find_previous("text").text
        self.objects = []

        for obj in diagram.find_all():
            match obj.name:
                case "text":
                    if obj.previous.name == "rect": self.objects.append(Attribute(obj))
                    if obj.previous.name == "ellipse": self.objects.append(Method(obj, self.class_name))
                case "line": self.objects.append(Line(obj))
                case _: pass

        self.objects.pop(0)  # line at the top of the class. Looks kinda weird.
        self.objects.sort(key=lambda tag: float(tag.height))

    def __repr__(self) -> str:
        return '\n'.join([str(obj) for obj in self.objects])
