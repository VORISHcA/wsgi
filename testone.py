from frametest.wsgi import Frametest
from frametest.url import Url
from frametest.view import View
from frametest.response import Response




class TestView(View):
    print('1')
    def get(self, request):
        return Response(body='GET SUCCESS')
        # 'Гет'

    def post(self, request):
        return Response(status='201 CREATED', body='POST SUCCESS', headers={'Home': '123'})
        #return 'post'


class AboutView(View):
    def get(self, request):
        #return Response(body='GET SUCCESS')
        return 'Гет'

    def post(self, request):
        #return Response(status='201 CREATED', body='POST SUCCESS', headers={'Home': '123'})
        return 'post'


urls = [
    Url('/home', TestView),
    Url('/about', AboutView)
]

app = Frametest(urls)

