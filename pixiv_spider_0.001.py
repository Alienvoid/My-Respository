import requests
import re
s=requests.Session()
class pixiv_spider():
    def __init__(self):
        self.origin_url='https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
        self.login_url='https://accounts.pixiv.net/login?lang=zh'
        self.login_header={'Host':'accounts.pixiv.net','Origin':'https://accounts.pixiv.net',
                           'Referer':'https://accounts.pixiv.net/login?lang=zh',
                           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
                           'X-Requested-With':"XMLHttpRequest"}
        self.login_id='xxxxx'#Enter your Pixiv ID here.
        self.login_password='xxxxx'#Enter your Pixiv password here.
        self.return_page_url='https://www.pixiv.net/member.php?id=3640500'
    def login(self):
        login_page=s.get(self.origin_url)
        self.post_key=re.findall(r'<input type="hidden" name="post_key" value="(.*?)">',login_page.text,re.S)
        login_data={'pixiv_id':self.login_id, 'password':self.login_password, 'post_key':self.post_key}
        s.post(self.login_url,data = login_data, headers = self.login_header)
        return s.get(self.return_page_url)
a=pixiv_spider()
print(a.login().text)
