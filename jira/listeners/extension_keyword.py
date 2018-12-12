# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 12.12.2018 """
import base64
import json
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
import urllib
import urllib2
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

__author__ = 'safaariman'


class ExtensionKeywordListener(EventListener):

    def __init__(self, icon_file):
        self.icon_file = icon_file

    def on_event(self, event, extension):

        query = event.get_argument()

        url = extension.preferences.get('url')
        user = extension.preferences.get('username')
        password = extension.preferences.get('password')

        token = base64.b64encode(str('%s:%s' % (user, password)).encode()).decode()
        get_url = "%s?%s" % (url, urllib.urlencode({'q': query}))

        req = urllib2.Request(get_url, headers={'Authorization': 'Basic %s' % token})

        results = []

        response = urllib2.urlopen(req)
        result_types = json.loads(response.read())
        for rtype in result_types:
            for item in rtype.get('items', []):
                key = item.get('subtitle')
                title = item.get('title')
                res_name = rtype.get('name')
                url = item.get('url')
                results.append(
                    ExtensionResultItem(name=key, description=title if not key else '%s - %s' % (key, title),
                        icon=self.icon_file, on_enter=OpenUrlAction(url=url))
                )

        return RenderResultListAction(results)
