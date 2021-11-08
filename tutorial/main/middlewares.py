import http

from django.http import JsonResponse
from http import HTTPStatus
from django.http import HttpResponse
import time
TIME_LIMIT = 30
TIMES_LIMIT = 5


class UserRequestsLimiter:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        enter_times = request.session.get('enter_times', 0)
        last_visited = request.session.get('last_visited', time.monotonic())
        request.time_diff = time.monotonic() - last_visited
        enter_times += 1
        request.session['enter_times'] = enter_times

        print(f'Logged data: {request.session["enter_times"]}')
        response = self.get_response(request)

        request.blocked = False
        if request.time_diff < TIME_LIMIT and enter_times > TIMES_LIMIT:
            request.session['last_visited'] = time.monotonic()
            request.blocked = True
        if request.time_diff > TIME_LIMIT:
            request.session['enter_times'] = 0
        request.session['last_visited'] = time.monotonic()

        return self._response(request, response)

    def _response(self, request, response):
        if request.blocked:
            return JsonResponse({
                'status': f'Failed, please wait'
                          f'{int(TIME_LIMIT) - request.time_diff} seconds.'}
            )
            response.status_code = http.HTTPStatus.FORBIDDEN
        return response


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timestamp = time.monotonic()
        response = self.get_response(request)
        print(
            f'Duration of request {request.path} - '
            f'{time.monotonic() - timestamp:.3f} sec.'
        )
        return HttpResponse(f'X-Request-Timing: {time.monotonic() - timestamp:.3f} sec.')
