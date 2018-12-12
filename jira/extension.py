# -*- coding: utf-8 -*-
""" Created by Safa Arıman on 12.12.2018 """
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent

from jira.listeners.extension_keyword import ExtensionKeywordListener

__author__ = 'safaariman'


class JiraExtension(Extension):
    ICON_FILE = 'images/jira.png'

    timer = None

    def __init__(self):
        super(JiraExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, ExtensionKeywordListener(self.ICON_FILE))
