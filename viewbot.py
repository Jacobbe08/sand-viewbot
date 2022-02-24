#pip install aiohttp
import asyncio
from os import system
import aiohttp
from warnings import filterwarnings
filterwarnings("ignore", category=DeprecationWarning)
global check
check = 0
class Checker:
    global check
    async def _check(self, session: aiohttp.ClientSession, vid) -> None:
        global check
        url = "https://api16-core-c-alisg.tiktokv.com:443/aweme/v1/aweme/stats/?iid=7067548501364328239&device_id=7066521892505486853&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220704&version_name=22.7.4&device_platform=android&ab_version=22.7.4&ssmix=a&device_type=SM-G975N&device_brand=samsung&language=en&os_api=22&os_version=5.1.1&openudid=17cebe5c0a72bb95&manifest_version_code=2022207040&resolution=1280*720&dpi=240&update_version_code=2022207040&_rticket=1645542295905&current_region=US&app_type=normal&sys_region=US&mcc_mnc=310410&timezone_name=Europe%2FChisinau&residence=US&ts=1645542295&timezone_offset=7200&build_number=22.7.4&region=US&carrier_region=US&uoo=0&app_language=en&locale=en&op_region=US&ac2=wifi&host_abi=x86&cdid=bf1de5ea-b016-464b-9934-aa42d9c2f57f"
        headers = {"X-Ss-Stub": "B7E9060C2C6546B554F8E598899D039B", "Accept-Encoding": "gzip, deflate",
                         "Passport-Sdk-Version": "19", "Sdk-Version": "2",
                         "X-Tt-Multi-Sids": "6944736496406922242%3A94c494cf975178480afd6f92c9915669",
                         "Multi_login": "1",
                         "X-Tt-Token": "0494c494cf975178480afd6f92c99156690098c931fd5b5cf11645d614c78e57e86441112269895c41c1a264195d1c267dbd43cef2481ee74647120ba9802e3d2f3cda3ac7b8f836faf4d44786b8c560b5c33db7168d1e9090c8a1462375b00ab1bdf-1.0.1",
                         "X-Ss-Req-Ticket": "1645542295910", "X-Vc-Bdturing-Sdk-Version": "2.2.1.i18n",
                         "X-Tt-Dm-Status": "login=1;ct=1;rt=1",
                         "X-Tt-Cmpl-Token": "AgQQAPOgF-RPsLBeR6v_NF07-HDNCw_Qv4fZYMHjXA", "X-Tt-Store-Region": "id",
                         "X-Tt-Store-Region-Src": "uid",
                         "User-Agent": "com.zhiliaoapp.musically/2022207040 (Linux; U; Android 5.1.1; en_US; SM-G975N; Build/LMY49I;tt-ok/3.10.0.2)",
                         "X-Ladon": "D6KBSCZxCgKU3xE4gOFz52serBfccfJz0edEtS69fu/rucs0", "X-Khronos": "1645542295",
                         "X-Gorgon": "0404406d400073ced1aea09e7d6b14f79a90845be7b3a1c11723",
                         "X-Argus": "39LdloW8VaYGIXzTm9/V/2D397YZ5NFKIma+WcWIn9A2e5KFQC29PJaJ07C+Kpv+4ZDqoFk/pZSBgsnl3Rk3rYesLZxI/82p/LzX1w/bvPeqd9CxOp9Vdj098qApL9FClLiceOJWUlRnznV9+5a0m4dJm+Xc9NwnjtfEkcOo9db4SqixYsonjN13jOWuKL94aqQ3jrGMy9ATImIRJlUKUIUZOq1BTzN/8ZvIvNx/Pkor5niEDE4ziEw3ELbziklB3LQ=",
                         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                         "Cookie": "sessionid=0c15a1c3c57075bd85f457ef7cda5273"} #dont touch ssid >:(
        data = {"order": '', "first_install_time": "1645302938", "request_id": '', "is_ad": "0",
                      "follow_status": "0", "tab_type": "3", "aweme_type": "0", "item_id": vid,
                      "sync_origin": "false", "pre_item_playtime": "2194", "follower_status": "0",
                      "pre_hot_sentence": '', "pre_item_id": vid, "play_delta": "1",
                      "action_time": "1645542295", "enter_from": "others_homepage"}
        await session.post(url=url, headers=headers, data=data)
        print(f'[{check}] Another view!', end="\r")
        check = check + 1
    async def start(self):
        print('''

   _____                 _   __      ___               _           _   
  / ____|               | |  \ \    / (_)             | |         | |  
 | (___   __ _ _ __   __| |   \ \  / / _  _____      _| |__   ___ | |_ 
  \___ \ / _` | '_ \ / _` |    \ \/ / | |/ _ \ \ /\ / / '_ \ / _ \| __|
  ____) | (_| | | | | (_| |     \  /  | |  __/\ V  V /| |_) | (_) | |_ 
 |_____/ \__,_|_| |_|\__,_|      \/   |_|\___| \_/\_/ |_.__/ \___/ \__|
                                                                                                                                                         
''')
        rang = int(input("How many views? "))
        vid = input("Video id? (in url) ")
        print("Loading...")
        async with aiohttp.ClientSession() as sess:
            return await asyncio.gather(*[self._check(sess, vid) for _ in range(rang)])
system('cls && title Sand Viewbot')
checker = Checker()
loop = asyncio.get_event_loop()
loop.run_until_complete(checker.start())