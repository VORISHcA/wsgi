class Request:

    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.query_peram = self._get_query(environ)
        self.headers = self._get_headers(environ)


    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:]] = value
        return headers

    def _get_query(self, environ):
        query_peram = {}
        qs = environ.get('QUERY_STRING')
        if not qs:
            return{}
        qs = qs.split('&')

        for q_str in qs:
            key, value in q_str.split('=')
            if query_peram.get(key):
                query_peram[key].append(value)
            else:
                query_peram[key] = [value]
        return query_peram


