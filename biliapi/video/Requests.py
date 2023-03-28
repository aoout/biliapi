import requests

from .VideoFormat import VideoFormat
from .VideoQuality import VideoQuality

def getVideoInfo(
        avid:int = None,
        bvid:str = None
):
    return requests.get(
        url = 'https://api.bilibili.com/x/web-interface/view',
        params=dict(
            aid = avid,
            bvid = bvid
        )
    )

def getVideoUrl(
        cid:int,
        fnval:VideoFormat,
        avid:int = None,
        bvid:int = None,
        fnver:int = 0,
        fourk:int = 0,
        session=None,
        otype:str = "json",
        type:str = "",
        platform:str = "",
        qn:VideoQuality = VideoQuality._720P,
):
    return requests.get(
        url = 'https://api.bilibili.com/x/player/playurl',
        params=dict(
            avid = avid,
            bvid = bvid,
            cid = cid,
            qn = qn.value,
            fnval = fnval.value,
            fnver = fnver,
            fourk = fourk,
            session = session,
            otype = otype,
            type = type,
            platform = platform
        )
    )