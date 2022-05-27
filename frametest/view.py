from frametest.response import Response

class View:
    def post(self, request, *args, **kwargs) -> Response:
        pass

    def get(self, request, *args, **kwargs) -> Response:
        pass

