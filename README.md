# Telegram2FB

Telegram Bot for publish in Facebook
(Español: http://blog.desdelinux.net/python-publicar-redes-sociales-telegram/)

# INSTALLATION

Simply clone the GitHub repository:

`git clone https://github.com/XTickXIvanX/Telegram2FB.git`

Install requirements:

`pip install requests DictObject facebook-sdk`

Create the Bot and get the token: https://core.telegram.org/bots

Create a new Facebook app: https://developers.facebook.com/apps/

We get our access token in: https://developers.facebook.com/tools/explorer/

We grant the following permissions to generate:

![](http://blog.desdelinux.net/wp-content/uploads/2015/08/Captura-de-pantalla-79.png)![](http://blog.desdelinux.net/wp-content/uploads/2015/08/Captura-de-pantalla-80.png)

Run.py modify the program file and remplasamos three points of the variable API_KEY=”…” by the token Telegram and three points of the variable graph = facebook.GraphAPI(access_token=’…’) by the token of Facebook.

We link our Twitter account Facebook to tweet what we publish on Facebook.

We run the program:

`python Run.py`

It is done!

Telegram is now only open and send a message (s) to our Bot: '/publicar "Insert here what you want to publish."'
