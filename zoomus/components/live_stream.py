from __future__ import absolute_import

from zoomus import util
from zoomus.components import base

class LiveStreamComponentV2(base.BaseComponent):

    def update(self, **kwargs):
        util.require_keys(kwargs, "meeting_id")
        return self.patch_request(
            "/meetings/{}/liveStream".format(kwargs.get("meeting_id")), params=kwargs
        )
