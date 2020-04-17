
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pyowm
import requests
tokens = []


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text("I'm a bot, Nice to meet you!"
    "\nEnter /help to know what all can I do")

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "\n/weather (Just type, for example, /weather hyderabad)"
        "\n/getmeme"
        "\n/bop (get random images)"
        "\n/hey"
        "\n/start"
        "\n/help"
        "\n/developer"
        "\n/about"
        "\n/projects"
    )

def weather(bot, update, args):
    """Define weather at certain location"""
    owm = pyowm.OWM('6a764e45b29de0c6b9b7b374576c82df')
    text_location = "".join(str(x) for x in args)
    observation = owm.weather_at_place(text_location)
    w = observation.get_weather()
    humidity = w.get_humidity()
    wind = w.get_wind()
    temp = w.get_temperature('celsius')
    convert_temp = temp.get('temp')
    convert_wind = wind.get('speed')
    convert_humidity = humidity
    text_temp = str(convert_temp)
    text_wind = str(convert_wind)
    text_humidity = str(convert_humidity)
    update.message.reply_text("Temperature, celsius:")
    update.message.reply_text(text_temp)
    update.message.reply_text("Wind speed, m/s:")
    update.message.reply_text(text_wind)
    update.message.reply_text("Humidity, %:")
    update.message.reply_text(text_humidity) 

def developer(bot, update):
    update.message.reply_text("\nI was Developed by AnuragTekale"
    "\nEnter /about to get info about him")  

def about(bot, update):
    update.message.reply_text("Please open='http://anurag2402.herokuapp.com/'  \nto know about me")

def projects(bot, update):
    update.message.reply_text("Please open='https://github.com/anurag-tekale'   \n to get info about my projects")

def hey(bot, update):
    update.message.reply_text("Hey..! How are you..?")    

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
        
def get_url():
    contents = requests.get('https://meme-api.herokuapp.com/gimme').json()
    url = contents['url']
    return url

def getmeme(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():

    """Start the bot."""
    updater = Updater('1132161922:AAFqWkWStkENcNd8cL6TNe3EgrP2lOjo7Hw')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("weather", weather, pass_args=True))
    dp.add_handler(CommandHandler("hey",hey))
    dp.add_handler(CommandHandler("bop",bop))
    dp.add_handler(CommandHandler("getmeme",getmeme))
    dp.add_handler(CommandHandler("developer",developer))
    dp.add_handler(CommandHandler("about",about))
    dp.add_handler(CommandHandler("projects",projects))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()