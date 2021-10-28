from MLNetwork.Core.Network.BaseReqeust.MLBaseRequest import MLBaseRequest
from MLNetwork.Core.Network.MLNetworkEnum import HttpMethod
from tests.Model.MLOneWordModel import MLOneWordModel
class MLOneWorkRequest(MLBaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.url = 'https://v1.hitokoto.cn'
        self.respose_class = MLOneWordModel
        self.http_method = HttpMethod.GET
    
    def successBlock(self, response):
        if response:
            model = self.respose_class.decoder(response)
            self.respose_data = model
            

    def failureBlock(self, response):
        if response :
            print("请求出错啦")
