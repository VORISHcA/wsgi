from pprint import pprint
from frametest.request import Request
from frametest.view import View
from frametest.response import Response
from frametest.render import render
from jinja2 import Template
from jinja2.environment import Environment
from jinja2 import FileSystemLoader

class Frametest:
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        # pprint(environ)
        #print(environ['wsgi.input'].read())
        #print(request.method)
        #print(request.path)
        #print(request.headers)
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        print(response)
        start_response(response.status, list(response.headers.items()))
        #start_response('200 OK', [('Content-Type', 'text/html')])
        #rew2 = render('index.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
        #print('2')
        #return rew2.encode(encoding="utf-8")
        #return [b'kefkdfk']
        return [response.body.encode()]


    def _get_view(self, request: Request):
        path = request.path
        print(path, self.urls)
        for url in self.urls:
            if url.path == path:
                return url.view
            return ['Ошибка url']

    def _get_response(self, request: Request, view: View):
        print('3')
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        return 'Метод не поддерживается'

