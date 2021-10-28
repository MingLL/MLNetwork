from tests.Request.MLOneWorkRequest import MLOneWorkRequest
class MLOneWorkServices:
    @classmethod
    def http_request(cls):
        request = MLOneWorkRequest()
        request.request()
        return request.respose_data