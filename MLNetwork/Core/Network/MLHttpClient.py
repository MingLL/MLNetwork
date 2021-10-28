import threading

from MLNetwork.Core.Network.MLNetworkPipline import MLNetworkPipline
 
class MLHttpClient(object):
    _instance_lock = threading.Lock()
    __array = list()

    @classmethod
    def instance(cls, *args, **kwargs):
        with MLHttpClient._instance_lock:
            if not hasattr(MLHttpClient, "_instance"):
                MLHttpClient._instance = MLHttpClient(*args, **kwargs)
        return MLHttpClient._instance

    def http_request(self, context):
        pipline = MLNetworkPipline(context)
        self.enqueue(pipline)
        pipline.execte()
        self.dequeue(pipline)


    def enqueue(self, pipline):
        with MLHttpClient._instance_lock:
            self.__array.append(pipline)

    def dequeue(self, pipline):
        with MLHttpClient._instance_lock:
            self.__array.remove(pipline)