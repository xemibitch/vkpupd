import vk_api, time, colorama
import time
import os
import sys
from colorama import Fore, Back, Style
from vk_api import VkUpload
colorama.init()

banner = [
"""
  updated script
       ___.    __  .__     
___  __\_ |___/  |_|  |__  
\  \/  /| __ \   __\  |  \ 
 >    < | \_\ \  | |   Y  \\
/__/\_ \|___  /__| |___|  /
      \/    \/          \/ 
              by @xemibitch
"""
]

warning = [
"""
начать выполнение скрипта? (y/n)
"""
]

abort = [
"""

"""
]

print(Fore.CYAN + banner[0])
print(Fore.CYAN + warning[0])
choose = input('--> ')
if choose == "y":
	login1 = input("логин от страницы: ")
	password1 = input("пароль от страницы: ")
	album = input("id альбома: ")
	def auth_handler():
    		key = input("код двухфакторки: ")
    		remember_device = True
    		return key, remember_device
	vk_session = vk_api.VkApi(login=login1, password=password1, auth_handler=auth_handler, app_id='6287487')
	vk_session.auth(token_only=True)
	vks = vk_session
	upload = VkUpload(vk_session)
	while True:
		upload.photo(photos="photo.jpg", album_id=album)

else:
	print(Fore.CYAN + abort[0])
