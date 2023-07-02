# FIFA23-AutoRelist-WebApp
 A Selenium based Python script which automates the relisting of FIFA 23 items.
 
 This script requires FIFA 23 login data to be stored within a Chrome profile and the path to the profile added to the browser setup within the code.

 To access Chrome Profile path:
 ![image](https://github.com/EwanStewart/FIFA23-AutoRelist-WebApp/assets/80590593/fd7cb7b3-044d-4f57-b5aa-7d59a2f84053)

 This script is best utilised on a scheduler, such as Cron on a low-energy consumption micro-computer like a RPi.

 Cron Expression (Relist every 65mins):
 */65 * * * * export DISPLAY=:0 && /usr/bin/python3 ~/Documents/relist.py
 
 
 
 
