import json
import requests
from MLNetwork.Core.Network.Context.MLNetworkContext import MLNetworkContext
from MLNetwork.Core.Network.MLNetworkEnum import HttpMethod
class MLNetworkPipline:
    def __init__(self, context) -> None:
        self.context: MLNetworkContext = context
        self.executing = False
        self.finished = False
        self.canceled = False
    
    def execte(self):
        if self.executing :
            print("请求正在执行,{}".format(self.context.request.url))
            return
        self.executing = True
        http_method = self.context.request.http_method
        url = self.context.request.url
        headers = self.context.request.headers
        data = self.context.request.post_data
        print("正在发起网络请求 url:{}, http_method:{}, headers:{}, post_data:{}".format(url, http_method, headers, data))
        try:
            if http_method == HttpMethod.GET:
                res = requests.get(url=url, headers=headers, json=data)
                print("获取到数据 Response:{}".format(res.text))
                if res.ok:
                    res_dic = json.loads(res.text)
                    if self.context.successBlock : self.context.successBlock(res_dic)
                else:
                    if self.context.failureBlock : self.context.failureBlock(res)
            elif http_method == HttpMethod.POST:
                res = requests.post(url=url, json=data, headers=headers)
                print("获取到数据 Response:{}".format(res.text))
                if res.ok:
                    res_dic = json.loads(res.text)
                    if self.context.successBlock : self.context.successBlock(res_dic)
                else:
                    if self.context.failureBlock : self.context.failureBlock(res)
            else:
                print("不支持当前请求方法")
        except Exception as e:
            print("请求出错了:{0}".format(e))
        
        
        