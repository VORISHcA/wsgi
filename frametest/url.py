from dataclasses import dataclass
from frametest.view import View


@dataclass
class Url:
    path: str
    view: View
