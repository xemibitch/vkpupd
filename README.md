Скрипт на 10000 фотографий в альбом ВКонтакте

Как пользоваться?

Скачиваем Termux по ссылке
https://github.com/termux/termux-app/releases
ВЕРСИЯ ИЗ Google Play НЕ БУДЕТ РАБОТАТЬ
И еще скачиваем FX File Explorer, можно из Google Play

Далее вводим следующие команды:
apt update
apt install git -y
apt install python -y
apt upgrade
pip install colorama
pip install vk_api
termux-setup-storage
mkdir nakrutka
cd nakrutka
git clone https://github.com/xemibitch/vkpupd
cd vkpupd

Теперь самый пот:
Скачиваем вашу картинку, переименовываем в photo.jpg.

Открываем FX File Explorer, скипаем вступление, далее нажимаем три точки справа сверху и выбираем Connect to Storage. слева сверху нажимаем на три полоски и там находим Termux, используем эту папку.

Находим в проводнике photo.jpg, копируем в папку nakrutka/vkpupd/ 

Идем создавать альбом, делаем его публичным и запоминаем айди из ссылки

Ну и теперь пишем команду
python main.py
Если никаких ошибок нет, значит скрипт работает и делает свою работу
