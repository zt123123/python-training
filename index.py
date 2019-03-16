import urllib
import urllib.request
import ssl
import time
import json
import os.path


class BingDownloader(object):
    _bing_interface = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=%d&nc=%d&pid=hp'
    _bing_url = 'https://cn.bing.com'
    _img_filename = '[%s][%s][%s].%s'

    def __init__(self):
        super(BingDownloader, self).__init__()
        ssl.create_default_context = ssl._create_unverified_context

    def download(self, num=1, local_path='./'):
        if num < 1:
            num = 1
        url = self._bing_interface % (num, int(time.time()))
        img_info = self._get_img_info(url)
        for info in img_info:
            self._down_img(self._bing_url + self._get_imgurl(info),
                           self._get_img_name(info))

    def _get_img_info(self, url):
        request = urllib.request.urlopen(url).read()
        bgObjs = json.loads(bytes.decode(request))
        return bgObjs['images']

    def _get_img_name(slef, img_info):
        pos = img_info['copyright'].index(' (')
        if pos < 0:
            zh_name = 'copyright'
        else:
            zh_name = img_info['copyright'][0:pos]

        entmp = img_info['url']
        en_name = entmp[entmp.index('id=') + 3:entmp.rindex('_ZH')]
        ex_name = entmp[entmp.rindex('.') + 1:entmp.rindex('&')]
        pix = entmp[entmp.rindex('_') + 1:entmp.rindex('.')]
        img_name = BingDownloader._img_filename % (zh_name, en_name, pix, ex_name)
        return img_name

    def _get_imgurl(slef, img_info):
        return img_info['url']

    def _down_img(self, img_url, img_path):
        img_data = urllib.request.urlopen(img_url).read()
        f = open(img_path, "wb")
        f.write(img_data)
        f.close()
        print("success save file",img_path)


if __name__ == '__main__':
    dl = BingDownloader()
    dl.download(3)
