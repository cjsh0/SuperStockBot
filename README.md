# SuperStockBot
Simple inventory stock checker written in Python with Pushbullet notifications

Requirements:


A Pushbullet account and API Key
https://pypi.org/project/pushbullet.py/0.9.1/

Written with Ubuntu as the host, contains some Ubuntu specific commands like aplay, if running on another OS just leave audio notifications disabled


You'll need a configuration file (settings.conf)
```
LINUX_DESKTOP_NOTIFICATION_SOUND=0 (Enable or disable audio ping)
PUSHBULLET_API_KEY=o.xjkc893fAkE-KEY903jg (You will want to use your own pushbullet API key)
LIST_OF_URLS=url_list.txt (list of stock page URLs you want to monitor)
CHECK_INTERVAL=6 (How often you want to check the page for updates, be reasonable)
```

Scoring a GPU is hard right now, hopefully this will help. Remember, don't be evil.
