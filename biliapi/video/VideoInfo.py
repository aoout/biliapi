import time

from .Requests import getVideoInfo

from ..utils import *


class VideoInfo:
    def __init__(self,id_:str or int) -> None:
        result = extend_id(id_)
        if result:
            for key, value in result.items():
                setattr(self, key, value)
        else:
            raise Exception(
                "It's not a bvid, av or url that can be used to link to a bilibili video.")
        self._getinfo()
        
    def _getinfo(self) -> None:
        try:
            response = getVideoInfo(self.av, self.bvid)
            data = response.json()['data']
        except Exception as exception:
            raise Exception('some network porblems happended.') from exception

        if not self.av:
            self.av = data['aid']
        if not self.bvid:
            self.bvid = data['bvid']

        self.info = dict(
            title=data['title'],
            publisher=data['owner']['name'],
            publisherUrl=mid2url(data['owner']['mid']),
            releaseDate=time.strftime(
                '%Y-%m-%d', time.localtime(data['pubdate'])),
            copyright='自制' if data['copyright'] == 1 else '转载'
        )

        self.imageUrl = data['pic']

        self.cids = [a['cid'] for a in data['pages']]