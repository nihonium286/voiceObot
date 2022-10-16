# voiceObot
Telegram bot that transcribe voice messeges

#How to run
1. Create a bot following this [guide]('https://core.telegram.org/bots') and get the bot auth key
2. Create an environmental variable called BOT_KEY='your_key'
3. Install dependencies
- pip install python-telegram-bot==20.0a4 --upgrade
- pip install git+https://github.com/openai/whisper.git
4. Run an application 
- python bot_main.py
