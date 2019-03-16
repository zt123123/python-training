import ssl
import urllib
import json
import urllib.request


class DingRobot(object):
    webhook = ''

    def __init__(self, webhook):
        super(DingRobot, self).__init__()
        self.webhook = webhook

    def sendText(self, msg, isAtAll=False, atMobiles=[]):
        data = {
            "msgtype": "text",
            "text": {
                "content": msg
            },
            "at": {
                "atMobiles": atMobiles,
                "isAtAll": isAtAll
            }
        }
        res = self.post(data)
        print(res)
        return res

    def sendMarkdown(self, title, text, isAtAll=False, atMobiles=[]):
        data = {
            "msgtype": "markdown",
            "markdown": {"title": title,
                         "text": text
                         },
            "at": {
                "atMobiles": atMobiles,
                "isAtAll": isAtAll
            }
        }

        return self.post(data)

    def post(self, data):
        post_data = str.encode(json.dumps(data))
        print(data)

        ssl._create_default_https_context = ssl._create_unverified_context

        req = urllib.request.Request(self.webhook, post_data)
        req.add_header('Content-Type', 'application/json')
        content = urllib.request.urlopen(req).read()
        return content


wh = 'https://oapi.dingtalk.com/robot/send?access_token=65d0871c16f8f4cb9bca82dc7bddbc54ceba909a703b05863c1786a658d93483'

if __name__ == "__main__":
    robot = DingRobot(wh)
    robot.sendMarkdown("Hello World!!!",
                       "#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) ",
                       False, ['13125066078'])
