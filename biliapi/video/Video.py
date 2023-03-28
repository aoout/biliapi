import requests

from .VideoFormat import VideoFormat
from .VideoQuality import VideoQuality


def getVideoUrl(
        avid:int,
        bvid:int,
        cid:int,
        qn:VideoQuality,
        fnval:VideoFormat,
        fnver:int = 0,
        fourk:int = 0,
        session=None,
        otype:str = "json",
        type:str = "",
        platform:str = "",
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