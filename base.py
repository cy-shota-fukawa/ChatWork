#!/usr/bin/python
# -*- coding: utf-8 -*-
import pycurl
import urllib

class ChatWork():
    def __init__(self, api_token):
        self.api_token = api_token
        self.curl = 

    def show_rooms(self):
        """
        ルーム一覧
        """
        url = "https://api.chatwork.com/v1/rooms"
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.HTTPHEADER, ["X-ChatWorkToken:" + self.api_token])
        curl.perform()

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
            "body":message
        }
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.HTTPHEADER, ['X-ChatWorkToken:' + self.api_token])
        self.curl.setopt(pycurl.POST, 1)
        self.curl.setopt(pycurl.POSTFIELDS, urllib.urlencode(options))
        self.curl.perform()