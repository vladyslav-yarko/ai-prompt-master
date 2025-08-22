from jinja2 import Template


# This class is the same as src.utils.prompt
# But i thought that here I can break "DRY" for better structure

class Text:
    def __init__(self, text: str):
        self.text = text

    def render(self, **kwargs) -> str:
        return Template(self.text).render(**kwargs)
