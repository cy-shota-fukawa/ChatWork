#!/usr/bin/python
# -*- coding: utf-8 -*-
import pycurl
import urllib
import json

class ChatWork():
    def __init__(self, api_token):
        self.api_token = api_token
        self.curl = pycurl.Curl()

    def show_rooms(self):
        url = "https://api.chatwork.com/v1/rooms"
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, ["X-ChatWorkToken:" + self.api_token])
        c.perform()

    def send_message(self, room_id, message):
        """
        テキストの送信
        :param room_id: 部屋ID
        :message: 送信するテキスト
        """
        # 送り先のURL作成
        url = "https://api.chatwork.com/v1/rooms/%s/messages" % room_id

        # オプションの設定
        options = {
            "thought":message,
            'description': 'Python test Room',
            'icon_preset': 'beer'
        }
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.HTTPHEADER, ['X-ChatWorkToken:' + self.api_token])
        self.curl.setopt(pycurl.POST, 1)
        self.curl.setopt(pycurl.POSTFIELDS, json.dumps(options))
        # self.curl.setopt(pycurl.POSTFIELDS, urllib.urlencode(option))
        self.curl.perform()

# me = 'https://api.chatwork.com/v1/me'
# status = 'https://api.chatwork.com/v1/my/status'
# tasks = 'https://api.chatwork.com/v1/my/tasks'
# room_message = 'https://api.chatwork.com/v1/rooms/{room_id}/messages'