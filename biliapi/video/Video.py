from .Requests import getVideoUrl
from .VideoInfo import VideoInfo
from .VideoFormat import VideoFormat


class Video:
    def __init__(self,id_:str or int) -> None:
        self.info = VideoInfo(id_)

    def getAudioUrl(self,pageIndex:int = 0) -> str:
        response = getVideoUrl(
            avid = self.info.av, 
            bvid = self.info.bvid,
            cid = self.info.cids[pageIndex],
            fnval =  VideoFormat.DASH
        )
        return response.json()['data']['dash']['audio'][0]['baseUrl']