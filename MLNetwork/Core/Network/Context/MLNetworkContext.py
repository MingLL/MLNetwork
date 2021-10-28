class MLNetworkContext(object) :
    """
        网络库内部类，保存成功，失败，取消回调
    """
    def __init__(self, request, successBlock: callable = None, failureBlock: callable = None, cancelBlock: callable = None) -> None:
        super().__init__()
        self.request = request
        self.successBlock = successBlock
        self.failureBlock = failureBlock
        self.cancelBlock = cancelBlock