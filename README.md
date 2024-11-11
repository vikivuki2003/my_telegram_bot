# My Telegram Bot  

This is a simple Telegram bot created using [Python](https://www.python.org/) and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). The bot is designed to perform various tasks and interact with users on Telegram.  

## Features  

- Command handling  
- Responses to text messages  
- Integration with various APIs (if applicable)  
- Easy configuration and extensibility  

## Installation  

1. Clone the repository:  
   git clone https://github.com/vikivuki2003/my_telegram_bot.git  
   cd my_telegram_bot  

Create a virtual environment (optional):
python -m venv venv  
source venv/bin/activate  # On Windows, use: venv\Scripts\activate  

Install the dependencies:
pip install -r requirements.txt  

Obtain your bot token from BotFather on Telegram.
Create a .env file and add your token:
dotenv
TG_BOT_TOKEN=your_token_here  
Running the Bot
Run the bot using the following command:

bash
python bot.py  
Usage
Once the bot is running, you can interact with it via Telegram. Simply find it by its username and send a command or message.
