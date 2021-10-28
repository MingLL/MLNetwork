from MLNetwork.Core.BaseModel.MLBaseModel import *
@dataclass
class MLOneWordModel(MLBaseModel):
    id: int = 0
    uuid: str = ''
    hitokoto: str = ''
    type: str = ''
    _from: str = ''
    creator: str = ''
    creator_uid: int = 0
    reviewer: int = 0
    commit_from: str = ''
    created_at: str = ''
    length: int = 0
