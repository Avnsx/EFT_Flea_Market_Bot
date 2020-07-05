################### Credits ###############################

#master: https://github.com/yagamiraku/tarkov_flea_bot_toTherapis
#	└──fork: https://github.com/astron4ik/tarkov_flea_bot_toTherapis
#		└──this fork: https://github.com/Avnsx/EFT_Flea_Market_Bot

#Master: yagamiraku | fork: astron4ik | this fork: Avn

#Read file READ_Me.md for assistance

############# MAIN CODE BELOW DO NOT EDIT UNLESS YOU KNOW WHAT YOU ARE DOING##############################

import requests
import zlib
import hashlib
import json
import datetime
import traceback
import os
import sys
import time, threading
from multiprocessing.pool import ThreadPool
import random
import getToken as token
import UnityPy
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import configparser
import subprocess
config = configparser.ConfigParser()

if os.path.exists('config.ini'):
    config.read_file(open('config.ini'))
    pass
else:
	print('[ERROR:] Did not find config.ini inside installation folder! Running getPath.py now, to create a config.ini file.')
	time.sleep(3)
	exec(open('./getPath.py').read())
	pass

def get_version_number(filename):
    try:
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        print('[ERROR:] Failed to fetch EFT Client version! Does getPath.py & config.ini exist in your installation folder?')
        time.sleep(10)
        exit()
        return

if __name__ == "__main__":
   ClientVersion = ".".join([str (i) for i in get_version_number (config['DEFAULT']['clientpath'])])
   UnityVersion = UnityPy.load(config['DEFAULT']['unitypath']).objects[0].assets_file.unity_version

cookies = {}
headers = {'User-Agent': 'UnityPlayer/'+str(UnityVersion)+' (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
           'Content-Type': 'application/json',
           'App-Version': 'EFT Client '+str(ClientVersion),
           'X-Unity-Version': str(UnityVersion)
           }

print('                                                ▄')
print('                                              ╓▀▀▄')
print('              ╓▐▌▒█▒▌▀▀▄╖                   ╓▀▀▀▀╢')
print('            ┌▀▀▀▀▒█▌▄▄▐▄▀╠                ╓╢▀▀▀▀▀▀▄')
print('           ╒╓▄▄▄▌██▌▐▒█▌▄▄▄             ╓╢▀▀▀▀▀▀▀▀▀')
print('           ▄▌▌▌▒███▌▄░▄╢▌░╠            ╙╨╝╢╢▀▀▀▀▀▀▀▄')
print('           ▒████████▌▌▌▄▌▐▀               ╒▀▀▀▀▀╠╨╝╝')
print('           ▐███▓▓▓▓█▒▌▒█▒█   READY TO     ╢▀▀▀▀▀')
print('            ██▓▓▓▓▓▓█▒▌▒░    DO SOME     ╒▀▀▀▀▀╠')
print('            ▐███▓▓▓▓▓▓▀▀     STONKS?     ▀▀▀▀▀▀')
print('           ▄▓▓█████▓▓           B)      ▐▀▀▀▀▀╛')
print('      ▄▄▓▓▓▓▓▓▓▓▀▒█▒▀╙█▄▄               ▀▀▀▀╢▀')
print(' ▄█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▄▄▄▐▓▓▓▓▓▓█▄▄        ▐▀▀▀▀╢╛')
print(' ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌▀▒▓▓▓▓▓▓▓▓▓▓▓      ▀▀▀▀▀▀')
print(' ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▄▓▓▓▓▓▓▓▓▓▓▓▄    ╠▀▀▀▀▀╛')
print('  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ╒▀▀▀▀▀▀')
print('  ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▐▀▀▀▀╢')
print('  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄ ╨╝╝▀▀▀')
print('                                                                                                            ')
print('███████╗██╗     ███████╗ █████╗     ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗███████╗████████╗    ██████╗  ██████╗ ████████╗')
print('██╔════╝██║     ██╔════╝██╔══██╗    ████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝')
print('█████╗  ██║     █████╗  ███████║    ██╔████╔██║███████║██████╔╝█████╔╝ █████╗     ██║       ██████╔╝██║   ██║   ██║   ')
print('██╔══╝  ██║     ██╔══╝  ██╔══██║    ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝     ██║       ██╔══██╗██║   ██║   ██║   ')
print('██║     ███████╗███████╗██║  ██║    ██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗███████╗   ██║       ██████╔╝╚██████╔╝   ██║   ')
print('╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   ')
print('[INFO:] Welcome to Developer Version 0.3 for Game Client Version ' + str(ClientVersion)+ ' on Unity Engine Version ' + str(UnityVersion))
print('[INFO:] This github fork was developed by Avn @ unknowncheats. Additionaly huge thanks to yagamiraku & astron4ik!')
print('[INFO:] The last manual update to this code was on 07/01/2020 by Avn unknowncheats.me/forum/members/2564688.html')

RUBLES = '5449016a4bdc2d6f028b456f'
PMC = {}
Balance = 0
oldBalance = 0
moneyStacks = {}
all_item_list = {}
NPC = ""
use_full_list = True
min_price = 1287 #Minimum Price to profit in Rubles, price also changes speed of income and spent value on therapist
NPC_name = 'Терапевт' #Therapist in russian

WishList = ['5ad7247386f7747487619dc3', '5a0ee34586f774023b6ee092', '5c127c4486f7745625356c13',
            '5c1e2a1e86f77431ea0ea84c', '5a13ef0686f7746e5a411744', '5a0f08bc86f77478f33b84c2',
            '5a1452ee86f7746f33111763', '5a0eecf686f7740350630097', '5a0ee76686f7743698200d5c',
            '5913915886f774123603c392', '5a0ee4b586f7743698200d22', '5a144bdb86f7741d374bbde0',
            '5a0ee37f86f774023657a86f', '5a0eeb1a86f774688b70aa5c', '5c052f6886f7746b1e3db148',
            '5a0eedb386f77403506300be', '5addaffe86f77470b455f900', '5c052e6986f7746b207bc3c9',
            '5da5cdcd86f774529238fb9b', '5b43575a86f77424f443fe62', '5ad7217186f7746744498875',
            '5ad7242b86f7740a6a3abd43', '5a13ee1986f774794d4c14cd', '5a0ee72c86f77436955d3435',
            '5d1b327086f7742525194449', '5c1e2d1f86f77431e9280bee', '5c1f79a086f7746ed066fb8f',
            '5ad5d64486f774079b080af8', '5d1b2f3f86f774252167a52c', '5a0eebed86f77461230ddb3d',
            '5d0377ce86f774186372f689', '5780cf942459777df90dcb72', '5bc9bc53d4351e00367fbcee',
            '5d80c93086f7744036212b41', '5a0ee62286f774369454a7ac', '5a0f006986f7741ffd2fe484',
            '5d1b32c186f774252167a530', '5bc9b9ecd4351e3bac122519', '5a0ec70e86f7742c0b518fba',
            '5bc9c049d4351e44f824d360', '5a0ea69f86f7741cd5406619', '5a0eeb8e86f77461257ed71a',
            '590de7e986f7741b096e5f32', '5d0378d486f77420421a5ff4', '59e3647686f774176a362507',
            '5d03784a86f774203e7e0c4d', '5bc9bdb8d4351e003562b8a1', '5bc9b720d4351e450201234b',
            '5bc9c377d4351e3bac12251b', '5a0f045e86f7745b0f0d0e42', '59e3658a86f7741776641ac4',
            '5d403f9186f7743cac3f229b', '590de71386f774347051a052', '5ad5d20586f77449be26d877',
            '5d0375ff86f774186372f685', '5d1b304286f774253763a528', '5734758f24597738025ee253',
            '5d235b4d86f7742e017bc88a', '59136e1e86f774432f15d133', '5d80cb8786f774405611c7d9',
            '5c0e534186f7747fa1419867', '5a0f075686f7745bcc42ee12', '5c1265fc86f7743f896a21c2',
            '5ad5ccd186f774446d5706e9', '5c0e531286f7747fa54205c2', '5bc9be8fd4351e00334cae6e',
            '5d1b385e86f774252167b98a', '5af0561e86f7745f5f3ad6ac', '5c0e533786f7747fa23f4d47',
            '5d40407c86f774318526545a', '5734773724597737fd047c14', '5c10c8fd86f7743d7d706df3',
            '590a3b0486f7743954552bdb', '5d1b39a386f774252339976f', '5c0e530286f7747fa1419862',
            '5af04b6486f774195a3ebb49', '5a8036fb86f77407252ddc02', '573477e124597737dd42e191',
            '590a3efd86f77437d351a25b', '590c5c9f86f77477c91c36e7', '590a391c86f774385a33c404',
            '59faf98186f774067b6be103', '5780d0532459777a5108b9a2', '590a3c0a86f774385a33c450',
            '590a358486f77429692b2790', '56742c324bdc2d150f8b456d', '591383f186f7744a4c5edcf3',
            '590c35a486f774273531c822', '5913877a86f774432f15d444', '593aa4be86f77457f56379f8',
            '5a0eb38b86f774153b320eb0', '5751496424597720a27126da', '544fb3f34bdc2d03748b456a',
            '574eb85c245977648157eec3', '57347baf24597738002c6178', '59e3556c86f7741776641ac2',
            '5d1b3f2d86f774253763b735', '590c5bbd86f774785762df04', '59136a4486f774447a1ed172',
            '590c2d8786f774245b1f03f3', '5939a00786f7742fe8132936', '57347c77245977448d35f6e2',
            '5798a2832459774b53341029', '5751435d24597720a27126d1', '5d40412b86f7743cb332ac3a',
            '5c13cef886f774072e618e82', '590c5a7286f7747884343aea', '59e361e886f774176c10a2a5',
            '5900b89686f7744e704a8747', '5c13cd2486f774072c757944', '5bc9c29cd4351e003562b8a3',
            '5d40425986f7743185265461', '57505f6224597709a92585a9', '5d4042a986f7743185265463',
            '5937ee6486f77408994ba448', '57347d7224597744596b4e72', '5d1b3a5d86f774252167ba22',
            '593962ca86f774068014d9af', '590c695186f7741e566b64a2', '5938504186f7740991483f30',
            '5672cb304bdc2dc2088b456a', '5d1c819a86f774771b0acd6c', '59e358a886f7741776641ac3',
            '59e366c186f7741778269d85', '5780cf692459777de4559321', '59148f8286f7741b951ea113',
            '57347cd0245977445a2d6ff1', '57347d692459774491567cf1', '57347d3d245977448f7b7f61',
            '5d4041f086f7743cac3f22a7', '5780d0652459777df90dcb74', '59e3596386f774176c10a2a2',
            '5780d0652459777df90dcb74', '57347d3d245977448f7b7f61', '59e3596386f774176c10a2a2',
            '57347d692459774491567cf1', '5d1b309586f77425227d1676', '590a3d9c86f774385926e510',
            '5734781f24597737e04bf32a', '590c595c86f7747884343ad7', '59148c8a86f774197930e983',
            '5673de654bdc2d180f8b456d', '5be4038986f774527d3fae60', '590c2b4386f77425357b6123',
            '5913611c86f77479e0084092', '5938603e86f77435642354f4', '544fb62a4bdc2dfb738b4568',
            '5a80a29286f7742b25692012', '575062b524597720a31c09a1', '57347d5f245977448b40fa81',
            '5913651986f774432f15d132', '5448ff904bdc2d6f028b456e', '590a3cd386f77436f20848cb',
            '5780cf9e2459777df90dcb73', '5780d07a2459777de4559324', '544fb6cc4bdc2d34748b456e',
            '573476f124597737e04bf328', '5c06782b86f77426df5407d2', '590c2c9c86f774245b1f03f2',
            '5780cda02459777b272ede61', '573474f924597738002c6174', '5b7c710788a4506dec015957',
            '5734779624597737e04bf329', '5914578086f774123569ffa4', '57a349b2245977762b199ec7',
            '573476d324597737da2adc13', '591382d986f774465a6413a7', '5672c92d4bdc2d180f8b4567',
            '57347c1124597737fb1379e3', '5783c43d2459774bbe137486', '57a349b2245977762b199ec7',
            '5d1b31ce86f7742523398394', '5672cb124bdc2d1a0f8b4568', '5938994586f774523a425196',
            '5780cf722459777a5108b9a1', '57347c93245977448d35f6e3', '544fb3364bdc2d34748b456a',
            '573475fb24597737fb1379e1', '5909e99886f7740c983b9984', '5734770f24597738025ee254',
            '544fb25a4bdc2dfb738b4567', '59136f6f86f774447a1ed173', '56742c284bdc2d98058b456d',
            '57347b8b24597737dd42e192', '591ae8f986f77406f854be45']
print('[LOG:] Loaded List: Wishlist')

# Full List
if use_full_list:
    print('[LOG:] Loaded List: Complete Entry')
    WishList = ['5c1d0efb86f7744baf2e7b7b', '5c0a840b86f7742ffa4f2482', '59fb042886f7746c5005a7b2',
                '5b6d9ce188a4501afc1b2b25', '5c1d0c5f86f7744bb2683cf0', '5c1d0dc586f7744baf2e7b79',
                '5d235bb686f77443f4331278', '5c1e495a86f7743109743dfb', '59fb023c86f7746d0d4b423c',
                '5c0530ee86f774697952d952', '59fafd4b86f7745ca07e1232', '5d03794386f77420415576f5',
                '5ad5d7d286f77450166e0a89', '5d95d6fa86f77424484aa5e9', '5d80cb5686f77440545d1286',
                '5c093db286f7740a1b2617e3', '5c1d0f4986f7744bb01837fa', '5a0ee30786f774023b6ee08f',
                '5d8e3ecc86f774414c78d05e', '5d80cab086f77440535be201', '590c60fc86f77412b13fddcf',
                '5a0dc95c86f77452440fc675', '5aafbcd986f7745e590fff23', '5a13ef7e86f7741290491063',
                '5c093e3486f77430cb02e593', '5ad7247386f7747487619dc3', '5da743f586f7744014504f72',
                '5a13f46386f7741dd7384b04', '5d80cbd886f77470855c26c2', '5d1b376e86f774252519444e',
                '5a0ee34586f774023b6ee092', '59fb016586f7746d0d4b423a', '5d947d4e86f774447b415895',
                '5d80c8f586f77440373c4ed0', '5ad5cfbd86f7742c825d6104', '5d03775b86f774203e7e0c4b',
                '5c127c4486f7745625356c13', '59e3639286f7741777737013', '5c1e2a1e86f77431ea0ea84c',
                '5a13ef0686f7746e5a411744', '5d8e0db586f7744450412a42', '57347ca924597744596b4e71',
                '5aafbde786f774389d0cbc0f', '5a1452ee86f7746f33111763', '5a0f08bc86f77478f33b84c2',
                '5ad5db3786f7743568421cce', '5733279d245977289b77ec24', '5a0eecf686f7740350630097',
                '5a0ee76686f7743698200d5c', '5a13f35286f77413ef1436b0', '5d9f1fa686f774726974a992',
                '5d80ccdd86f77474f7575e02', '5a13f24186f77410e57c5626', '5913915886f774123603c392',
                '5a0ee4b586f7743698200d22', '5d80c78786f774403a401e3e', '5d8e0e0e86f774321140eb56',
                '5da46e3886f774653b7a83fe', '5d1b33a686f7742523398398', '59e3606886f77417674759a5',
                '5d80c6c586f77440351beef1', '5c12620d86f7743f8b198b72', '5a13eebd86f7746fd639aa93',
                '5a144bdb86f7741d374bbde0', '5c1267ee86f77416ec610f72', '5c94bbff86f7747ee735c08f',
                '5a0ee37f86f774023657a86f', '5a0eeb1a86f774688b70aa5c', '5a0f0f5886f7741c4e32a472',
                '5c052f6886f7746b1e3db148', '5addaffe86f77470b455f900', '5a0dc45586f7742f6b0b73e3',
                '59faf7ca86f7740dbe19f6c2', '5a0eee1486f77402aa773226', '5a0eedb386f77403506300be',
                '5d80c88d86f77440556dbf07', '5c052e6986f7746b207bc3c9', '5d947d3886f774447b415893',
                '59e35cbb86f7741778269d83', '5d80c66d86f774405611c7d6', '590c2e1186f77425357b6124',
                '5c05308086f7746b2101e90b', '5a0ea64786f7741707720468', '5d80cb3886f77440556dbf09',
                '5d8e15b686f774445103b190', '5af0534a86f7743b6f354284', '5da5cdcd86f774529238fb9b',
                '5b43575a86f77424f443fe62', '5ad7242b86f7740a6a3abd43', '5ad7217186f7746744498875',
                '5a0ee72c86f77436955d3435', '5d80ca9086f774403a401e40', '5a13ee1986f774794d4c14cd',
                '5d95d6be86f77424444eb3a7', '5a0eb6ac86f7743124037a28', '5d80c95986f77440351beef3',
                '5c1f79a086f7746ed066fb8f', '567143bf4bdc2d1a0f8b4567', '5d0377ce86f774186372f689',
                '5c1e2d1f86f77431e9280bee', '5d1b327086f7742525194449', '5d0376a486f7747d8050965c',
                '5a145d4786f7744cbb6f4a12', '5780cfa52459777dfb276eb1', '5bc9bc53d4351e00367fbcee',
                '5d80cd1a86f77402aa362f42', '5d6fc78386f77449d825f9dc', '5751a89d24597722aa0e8db0',
                '5a0eebed86f77461230ddb3d', '5d1b2f3f86f774252167a52c', '5ad5d64486f774079b080af8',
                '5c05300686f7746dce784e5d', '5a0ee62286f774369454a7ac', '5d80c93086f7744036212b41',
                '5d1b32c186f774252167a530', '5bc9b9ecd4351e3bac122519', '5a0f006986f7741ffd2fe484',
                '5ad5d20586f77449be26d877', '5a0eec9686f77402ac5c39f2', '5bc9c049d4351e44f824d360',
                '5d235a5986f77443f6329bc6', '59fafb5d86f774067a6f2084', '5d80c6fc86f774403a401e3c',
                '5a0ea69f86f7741cd5406619', '5a0eeb8e86f77461257ed71a', '5c12688486f77426843c7d32',
                '590de7e986f7741b096e5f32', '5780cf942459777df90dcb72', '5d1b313086f77425227d1678',
                '5a145d7b86f7744cbb6f4a13', '5a0ea79b86f7741d4a35298e',
                '5d1b2fa286f77425227d1674', '59e3647686f774176a362507', '5a0eed4386f77405112912aa',
                '5d0378d486f77420421a5ff4', '5d03784a86f774203e7e0c4d', '5c0e531d86f7747fa23f4d42',
                '5a0ec70e86f7742c0b518fba', '5bc9bdb8d4351e003562b8a1', '5d80ccac86f77470841ff452',
                '5d0379a886f77420407aa271', '5bc9b720d4351e450201234b', '5bc9c377d4351e3bac12251b',
                '59e3658a86f7741776641ac4', '5a0f068686f7745b0d4ea242', '5b4335ba86f7744d2837a264',
                '57347c2e24597744902c94a1', '5d1b2ffd86f77425243e8d17', '5d40419286f774318526545f',
                '59e35de086f7741778269d84', '5d403f9186f7743cac3f229b', '5c052fb986f7746b2101e909',
                '590de71386f774347051a052', '590a373286f774287540368b', '5a0ec6d286f7742c0b518fb5',
                '5d235b4d86f7742e017bc88a', '5a0f045e86f7745b0f0d0e42', '590c346786f77423e50ed342',
                '5734758f24597738025ee253', '59e36c6f86f774176c10a2a7', '5d0375ff86f774186372f685',
                '5938144586f77473c2087145', '5d1b304286f774253763a528', '5734795124597738002c6176',
                '5d1b392c86f77425243e98fe', '5af04b6486f774195a3ebb49', '5d80cb8786f774405611c7d9',
                '591afe0186f77431bd616a11', '5bc9be8fd4351e00334cae6e', '59136e1e86f774432f15d133',
                '59faf98186f774067b6be103', '5a144dfd86f77445cb5a0982', '5ad5ccd186f774446d5706e9',
                '590c5f0d86f77413997acfab', '5c0e534186f7747fa1419867',
                '5c1265fc86f7743f896a21c2', '59e35ef086f7741777737012', '5d1c774f86f7746d6620f8db',
                '59e35abd86f7741778269d82', '590c311186f77424d1667482', '5c0e531286f7747fa54205c2',
                '5a0f075686f7745bcc42ee12', '5af0454c86f7746bf20992e8', '57347c5b245977448d35f6e1',
                '57347d8724597744596b4e76', '5af0561e86f7745f5f3ad6ac', '5c0e533786f7747fa23f4d47',
                '5be4038986f774527d3fae60', '5d1b39a386f774252339976f', '57347d9c245977448b40fa85',
                '59387a4986f77401cc236e62', '5734773724597737fd047c14',
                '5a145ebb86f77458f1796f05', '590c5d4b86f774784e1b9c45', '593aa4be86f77457f56379f8',
                '5751487e245977207e26a315', '5c10c8fd86f7743d7d706df3', '5d1b385e86f774252167b98a',
                '575146b724597720a27126d5', '5d6fc87386f77449db3db94e', '5d63d33b86f7746ea9275524',
                '5c0e530286f7747fa1419862', '57347da92459774491567cf5', '5a0eff2986f7741fd654e684',
                '590c35a486f774273531c822', '590c5c9f86f77477c91c36e7', '57514643245977207f2c2d09',
                '59e3556c86f7741776641ac2', '5c06779c86f77426e00dd782', '59e358a886f7741776641ac3',
                '5939a00786f7742fe8132936', '5af0484c86f7740f02001f7f', '5751435d24597720a27126d1',
                '590a3b0486f7743954552bdb', '590a391c86f774385a33c404', '5780d0532459777a5108b9a2',
                '590a3efd86f77437d351a25b', '590a358486f77429692b2790', '56742c324bdc2d150f8b456d',
                '57347d3d245977448f7b7f61', '590a386e86f77429692b27ab', '573477e124597737dd42e191',
                '5913877a86f774432f15d444', '5672cb724bdc2dc2088b456b', '544fb3f34bdc2d03748b456a',
                '591383f186f7744a4c5edcf3', '574eb85c245977648157eec3', '57347baf24597738002c6178',
                '57347d692459774491567cf1', '59e3556c86f7741776641ac2', '5d1c819a86f774771b0acd6c',
                '5937ee6486f77408994ba448', '59136a4486f774447a1ed172', '544fb62a4bdc2dfb738b4568',
                '5d1b3f2d86f774253763b735', '5ad5d49886f77455f9731921', '590c5bbd86f774785762df04',
                '5d1b309586f77425227d1676', '5bc9c29cd4351e003562b8a3', '57347c77245977448d35f6e2',
                '5a8036fb86f77407252ddc02', '5a8036fb86f77407252ddc02', '5d1b3a5d86f774252167ba22',
                '59148c8a86f774197930e983', '5d4042a986f7743185265463', '5c06782b86f77426df5407d2',
                '5c13cd2486f774072c757944', '5a0eb38b86f774153b320eb0', '5d40412b86f7743cb332ac3a',
                '590a3d9c86f774385926e510', '5a80a29286f7742b25692012', '5900b89686f7744e704a8747',
                '57347d7224597744596b4e72', '5d40425986f7743185265461', '59e3596386f774176c10a2a2',
                '5751496424597720a27126da', '590c5a7286f7747884343aea', '5780cf692459777de4559321',
                '59148f8286f7741b951ea113', '5673de654bdc2d180f8b456d', '5938504186f7740991483f30',
                '577e1c9d2459773cd707c525', '590c2d8786f774245b1f03f3', '59e366c186f7741778269d85',
                '5780d0652459777df90dcb74', '5672cb304bdc2dc2088b456a', '590a3c0a86f774385a33c450',
                '59e361e886f774176c10a2a5', '5798a2832459774b53341029', '5448ff904bdc2d6f028b456e',
                '590c595c86f7747884343ad7', '590a3cd386f77436f20848cb', '590c695186f7741e566b64a2',
                '57505f6224597709a92585a9', '5c13cef886f774072e618e82', '5938603e86f77435642354f4',
                '5913611c86f77479e0084092', '5913651986f774432f15d132', '5783c43d2459774bbe137486',
                '593962ca86f774068014d9af', '57347c1124597737fb1379e3', '5734781f24597737e04bf32a',
                '590c2b4386f77425357b6123', '5909e99886f7740c983b9984', '575062b524597720a31c09a1',
                '5780cf9e2459777df90dcb73', '573476f124597737e04bf328', '5b7c710788a4506dec015957',
                '5672cb124bdc2d1a0f8b4568', '590c2c9c86f774245b1f03f2', '544fb6cc4bdc2d34748b456e',
                '5780d07a2459777de4559324', '5b7c710788a4506dec015957', '57a349b2245977762b199ec7',
                '5d4041f086f7743cac3f22a7', '57347d5f245977448b40fa81', '573474f924597738002c6174',
                '5914578086f774123569ffa4', '5734779624597737e04bf329', '5780cda02459777b272ede61',
                '5672c92d4bdc2d180f8b4567', '591382d986f774465a6413a7', '57a349b2245977762b199ec7',
                '573475fb24597737fb1379e1', '57347cd0245977445a2d6ff1', '57347c93245977448d35f6e3',
                '544fb3364bdc2d34748b456a', '5d1b31ce86f7742523398394', '5938994586f774523a425196',
                '5734770f24597738025ee254', '544fb25a4bdc2dfb738b4567', '5780cf722459777a5108b9a1',
                '57347b8b24597737dd42e192', '573476d324597737da2adc13', '59136f6f86f774447a1ed173',
                '591ae8f986f77406f854be45', '56742c284bdc2d98058b456d']

print("[LOG:] Launching and waiting for the Escape from Tarkov Client...")

startlauncher = config['DEFAULT']['launcherpath']
subprocess.Popen(startlauncher)

def _keep_alive(): #keep session token alive
    while True:
        get_api_result('https://prod.escapefromtarkov.com/client/game/keepalive', '')
        time.sleep(5 * 60)

def goto(linenum): #do not judge
    global line
    line = linenum
    line == 1

def remove_white_space(s): #filter to raw input only
    return s.replace(' ', '').replace('\n', '')

def get_api_result(url, data): #read api request
    global cookies
    try:
        data = zlib.compress(remove_white_space(data).encode())
        res = requests.post(url,
                            data=data,
                            cookies=cookies,
                            headers=headers,
                            timeout=5
                            )
        if res.status_code == 200:
            if 'PHPSESSID' in res.cookies:
                cookies = res.cookies.get_dict()
            content = zlib.decompress(res.content).decode()
            return json.loads(content)
        else:
            print("%d" % res.status_code)
            raise Exception(res.status_code)
    except:
        print('[ERROR:] ... Token Requests Fail')


def buy(offer): #purchase item function
    print('\n[LOG:] Bought ' + offer['items'][0]['_tpl'] + ' [ ' + all_item_list[offer['items'][0]['_tpl']]['_props'][
        'Name'] + ' ]' + ' at ' + str(offer['requirementsCost']) + ' / ' + str(int(offer['itemsCost'] * 0.75)))
    offer_id = offer['_id']
    offer_count = offer['items'][0]['upd']['StackObjectsCount']
    offer_price = offer['items'][0]['upd']['StackObjectsCount'] * offer['summaryCost']
    start_time = offer['startTime']
    start_from = 56 #wait alteast for 56
    spent_time = time.time() - start_time
    if spent_time < start_from:
        to_wait = start_from - spent_time
        time.sleep(to_wait / 100) #division equals random wait timer
        print('  Waited ' + str(to_wait / 100) +' Seconds before purchase')

    data = {
        "data": [
            {
                "Action": "RagFairBuyOffer",
                "offers":
                    [
                        {
                            "id": offer_id,
                            "count": offer_count,
                            "items": []
                        }
                    ]
            }
        ]
    }

    items = []
    for (id, value) in moneyStacks.items():
        if value >= offer_price:
            items.append((id, offer_price))
            break
        else:
            offer_price -= value
            items.append((id, value))

    for item in items:
        stack_info = dict()
        stack_info['id'] = item[0]
        stack_info['count'] = item[1]
        data['data'][0]['offers'][0]['items'].append(stack_info)

    result_data = get_api_result(
        'https://prod.escapefromtarkov.com/client/game/profile/items/moving',
        json.dumps(data))

    if result_data['err'] in (228, 1512, 1514):
        return

    if result_data['err'] == 1505:
        print("[ERROR:] Purchase Failed ... OUT OF SPACE")
        exit()

    if result_data['err'] == 0:
        # offer was sold out
        if len(result_data['data']['badRequest']) > 0:
            print('[ERROR:] Purchase Failed ... ITEM WAS SOLD')
            todo = {}
        # added new item to inventory
        elif len(result_data['data']['items'].keys()) > 0:
            print('   Purchase Success ... ADDED ITEM')
            print('    | Stonks: + ' + format(int(offer['itemsCost'] * 0.75) - offer['summaryCost'],
                                                 ',') + ' ₽ |')
            for item in result_data['data']['items']['new']:
                data = {
                    "data": [
                        {
                            "Action": "TradingConfirm",
                            "type": "sell_to_trader",
                            "tid": NPC['_id'],  #NPC Identifier
                            "items":
                                [
                                    {"id": item['_id'], "count": item['upd']['StackObjectsCount'],
                                     "scheme_id": 0}
                                ]
                        }
                    ],
                    "tm": 0,
                }
                result_data = get_api_result(
                    'https://prod.escapefromtarkov.com/client/game/profile/items/moving',
                    json.dumps(data))
                # print(result_data)

            update_profile()

    else:
        print('[ERROR:] ' + str(result_data['err']) + '')

def update_profile():
    global PMC
    global Balance
    global oldBalance
    global all_item_list
    # get_profiles
    profile_list = get_api_result('https://prod.escapefromtarkov.com/client/game/profile/list', '{}')
    if profile_list is None:
        print('profile_list is None.')
    if profile_list['err'] != 0:
        print(profile_list['errmsg'])
        exit()
    # print(profile_list)

    # get PMC ID
    for item in profile_list['data']:
        if item['Info']['LastTimePlayedAsSavage'] == 0:
            PMC = item

    # get items
    _inventory = dict()
    for item in PMC['Inventory']['items']:
        _inventory[item['_id']] = item
    oldBalance = Balance
    Balance = 0
    for item_id, item in _inventory.items():
        if item['_tpl'] == RUBLES:
            count = item['upd']['StackObjectsCount']
            Balance += count
            moneyStacks[item_id] = count

    timeStr = str(time.strftime("%H:%M:%S", time.localtime(time.time())))
    if Balance - oldBalance > 0:
        print('[' + timeStr + '] Balance: ' + format(Balance, ',') + ' ₽')
    else:
        print('[' + timeStr + '] Balance: ' + format(Balance, ',') + ' ₽')


if __name__ == '__main__':
    PHPSESSID = token.getToken()
    print('\n[INFO:] Starting with token:', PHPSESSID)
    cookies = {'PHPSESSID': PHPSESSID}
    pool = ThreadPool(2)

    keep_alive_thread = threading.Thread(target=_keep_alive)
    keep_alive_thread.daemon = True
    keep_alive_thread.start()

    update_profile()

    # select_profiles
    get_api_result('https://prod.escapefromtarkov.com/client/game/profile/select', json.dumps({'uid': PMC['_id']}))

    all_item_list = get_api_result('https://prod.escapefromtarkov.com/client/items', '{}')['data']

    traders_list = get_api_result('https://trading.escapefromtarkov.com/client/trading/api/getTradersList', '{}')[
        'data']
    # print(traders_list)
    for trader in traders_list:
        # print(trader)
        if trader['nickname'] == NPC_name:
            NPC = trader  # Therapist
    if NPC == "":
        print('Can not find Trader')

    if NPC['working'] is not True:
        print('Trader is off duty')
        exit()

    while 1:
        print('\n[INFO:] Next Iteration with token: ' + cookies['PHPSESSID'] + '')
        # WishList = PMC['WishList']:
        print('     Wishlist currently includes: ' + str(len(WishList)) + ' items!')
        for wish in WishList:
            try:
                data = {
                    "page": 0,
                    "limit": 15,
                    "sortType": 5,
                    "sortDirection": 0,
                    "currency": 0,
                    "priceFrom": 0,
                    "priceTo": 0,
                    "quantityFrom": 0,
                    "quantityTo": 0,
                    "conditionFrom": 0,
                    "conditionTo": 100,
                    "oneHourExpiration": False,
                    "onlyPrioritized": False,
                    "removeBartering": True,
                    "removeMerchantOffers": True,
                    "onlyFunctional": True,
                    "updateOfferCount": True,
                    "handbookId": wish,
                    "linkedSearchId": "",
                    "neededSearchId": ""
                }
                req = get_api_result('https://ragfair.escapefromtarkov.com/client/ragfair/search', json.dumps(data))
                # print(req)
                if req is not None:
                    offers = req['data']['offers']
                    # print('Search ' + str(len(offers)) + ' items with ' + wish + ' ( ' + all_item_list[wish]['_props']['Name'] + ' )')
                    if len(offers) == 0:
                        # print('\n... No items found.')
                        todo = {}
                    for offer in offers:
                        if int(offer['itemsCost'] * 0.60) - offer['summaryCost'] > min_price:  # price check originally 75
                            buy(offer)

            except:
                #traceback.print_exc()
                print('\n[ERROR:]: Offers returned NullType, restarting routine...')
                goto(1) #do not judge eZ bugfix
