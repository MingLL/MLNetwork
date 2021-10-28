from abc import abstractmethod
from MLNetwork.Core.BaseModel.MLBaseModel import MLBaseModel
from MLNetwork.Core.Network.Context.MLNetworkContext import MLNetworkContext
from MLNetwork.Core.Network.MLHttpClient import MLHttpClient
from MLNetwork.Core.Network.MLNetworkEnum import HttpMethod
class MLBaseRequest(object):
    def __init__(self) -> None:
        super().__init__()
        self.url: str = ''
        self.headers: dict = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
        }
        self.post_data: dict = {}
        self.respose_class: MLBaseModel = MLBaseModel
        self.http_method = HttpMethod.POST
        self.respose_data: any

    @abstractmethod
    def successBlock(res):
        pass

    @abstractmethod
    def failureBlock(res):
        pass

    @abstractmethod
    def cancelBlock():
        pass

    def request(self):
        context = MLNetworkContext(self, self.successBlock, self.failureBlock, self.cancelBlock)
        MLHttpClient.instance().http_request(context=context)
