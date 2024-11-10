import logging
import traceback

from django.utils.deprecation import MiddlewareMixin


class APILoggingMiddleware(MiddlewareMixin):
    async_mode = False

    def __init__(self, get_response=None):
        self.get_response = get_response
        self.logger = logging.getLogger('api_logger')

    # TODO:- always has Anonymus user, since the request is not processed yet.
    # def process_request(self, request):
    #     if 'api' in request.path:
    #         user = request.user if request.user.is_authenticated else 'AnonymousUser'
    #         self.logger.debug(f"User authenticated: {request.user.is_authenticated}")
    #         self.logger.info(f"API {request.method} REQUEST from {user}: {request.path}")
    #     return None

    def process_response(self, request, response):
        if 'api' in request.path:
            username = request.user.username if request.user.is_authenticated else 'AnonymousUser'
            log_data = {
                "path": request.path,
                "user": username,
                "status": response.status_code,
                "custom_message":
                    response.data.get('detail', 'Error occurred')
                    if response.status_code >= 400 else ''
            }
            if response.status_code >= 400:
                self.logger.error(
                    f"API {request.method} for {username}: "
                    f"{request.path} - "
                    f"Status: {response.status_code} - {log_data['custom_message']}",
                    extra=log_data)
            else:
                self.logger.info(
                    f"API {request.method} for {username}: "
                    f"{request.path} - "
                    f"Status: {response.status_code}",
                    extra=log_data)
        return response

    def process_exception(self, request, exception):
        username = request.user.username if request.user.is_authenticated else 'AnonymousUser'
        self.logger.error(
            f"Exception occurred during processing request: {request.path}",
            exc_info=exception,
            extra={
                "path": request.path,
                "user": username,
                "exception": str(exception),
                "traceback": traceback.format_exc(),
            }
        )
        return None
