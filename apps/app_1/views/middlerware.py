from django.utils.decorators import decorator_from_middleware
import time

# Django 中间件， 可以用来处理  request ,response 之间的很多东西


class RequestLogMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_resquest(self, request, *args, **kwargs):
        request_data = request.body
        request.start_time = time.time()

    def process_view(self, request, view_func, *args, **kwargs):
        pass

    def process_response(self, request, response):
        end_time = time.time()
        method = request.method
        code = response.status_code
        path = request.get_full_path()
        match = request.resolver_match.kwargs

        # 此处可自定义方法， 来处理 request,response 的各种值。

        return response


class RequestLogView(object):
    """
    Adds RequestLongMiddleware to any Django View by overriding as_view.
    """

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(RequestLogView, cls).as_view(*args, **kwargs)
        view = decorator_from_middleware(RequestLogMiddleware)(view)
        return view
