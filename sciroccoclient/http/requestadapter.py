import json

from urllib3.request import urlencode

from sciroccoclient.systemdata import SystemData


class RequestsAdapter:
    def __init__(self, request_manager, request_manager_response_handler,
                 system_data_http):
        self._api_url = None
        self._node_id = None
        self._auth_token = None
        self.request_manager = request_manager
        self.request_manager_response_handler = request_manager_response_handler
        self.system_data_http = system_data_http

    @property
    def api_url(self):
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        self._api_url = api_url

    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        self._node_id = node_id

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        self._auth_token = auth_token

    def get_fixed_headers(self):

        return {
            self.system_data_http.get_by_name('fromm'): self._node_id,
            'Authorization': self._auth_token
        }

    def get_uri(self, resource):

        url = '/'.join([self.api_url, resource.strip("/")])
        return url

    def request(self, method, resource='', data=None, headers=None):

        if self.api_url is None or self.auth_token is None or self.node_id is None:
            raise RuntimeError

        method = method.upper()
        url = self.get_uri(resource)

        if isinstance(headers, dict):
            headers.update(self.get_fixed_headers())
        else:
            headers = self.get_fixed_headers()

        if isinstance(data, dict):

            if method in ['GET', 'DELETE']:
                url = ''.join([url, '?', urlencode(data)])
                data = None
            else:
                data = json.dumps(data)
        request_manager_result = self.request_manager.urlopen(method, url, headers=headers, body=data)

        return self.request_manager_response_handler.handle(request_manager_result)


class RequestManagerResponseHandler:
    def __init__(self, system_data_http_headers_filter, system_data_hydrator, data_treatment):
        self.system_data_http_headers_filter = system_data_http_headers_filter
        self.system_data_hydrator = system_data_hydrator
        self.data_treatment = data_treatment

    def handle(self, response):
        ro = RequestAdapterResponse()

        system_headers = self.system_data_http_headers_filter.filter_system(response.headers)
        ro.system_data = self.system_data_hydrator.hydrate(SystemData(), system_headers)
        ro.http_headers = self.system_data_http_headers_filter.filter_http(response.headers)
        ro.http_status = response.status
        ro.message_data = self.data_treatment.treat(response.data)
        return ro


class RequestAdapterDataResponseHandler:
    def treat(self, data):

        try:
            return json.loads(data.decode())
        except ValueError or TypeError:
            return data.decode()


class RequestAdapterResponse:
    def __init__(self):
        self._system_data = None
        self._message_data = None
        self._http_headers = None
        self._http_status = None

    @property
    def system_data(self):
        return self._system_data

    @system_data.setter
    def system_data(self, data):
        self._system_data = data

    @property
    def message_data(self):
        return self._message_data

    @message_data.setter
    def message_data(self, data):
        self._message_data = data

    @property
    def http_headers(self):
        return self._http_headers

    @http_headers.setter
    def http_headers(self, data):
        self._http_headers = data

    @property
    def http_status(self):
        return self._http_status

    @http_status.setter
    def http_status(self, status):
        self._http_status = status
