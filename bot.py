import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import datetime
import random
import pytz

capy_api_url = "https://api.capy.lol/v1/capybara/"

with open("token.txt", "r") as file:
    token = file.read()

finland_timezone = "Europe/Helsinki"
timezone = pytz.timezone(finland_timezone)

varaslahto_date = datetime(2024, 8, 18, 12, tzinfo=timezone)  # August 18 2024 at 12

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

emojis = ["😊", "😀", "🤣", "👌", "🗿", "🤨", "💀", "😤", "🙈"]


# remove unprintable characters from token, causes problems in my raspberry pi for some reason :D
def sanitize_string(input_string):
    sanitized_string = input_string.strip()
    sanitized_string = "".join(char for char in sanitized_string if char.isprintable())
    return sanitized_string


def get_time_left():
    current_date = datetime.now(tz=timezone)
    time_until_varaslahto = varaslahto_date - current_date
    days = time_until_varaslahto.days
    hours = time_until_varaslahto.seconds // 3600
    return [days, hours]


async def milloin_varaslahto(update: Update, context: ContextTypes.DEFAULT_TYPE):

    time_left = get_time_left()

    msg_text = f"❗Tietokillan varaslähtö järjestetään tänä vuonna 18.8.2024!❗\nVaraslähtöön on siis aikaa {time_left[0]} päivää ja {time_left[1]} tuntia! "
    emoji_number = random.randint(0, 10)
    for i in range(emoji_number):
        msg_text += emojis[random.randint(0, len(emojis) - 1)]

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg_text)


async def when_headstart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    time_left = get_time_left()

    msg_text = f"❗The headstart of Tietokilta will be held on 18.8.2024!❗\nThere are {time_left[0]} days and {time_left[1]} hours left! "
    emoji_number = random.randint(0, 10)
    for i in range(emoji_number):
        msg_text += emojis[random.randint(0, len(emojis) - 1)]

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg_text)


async def daily_capybara(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_date = datetime.now(timezone)
    time_until_varaslahto = varaslahto_date - current_date
    idx = time_until_varaslahto.days
    image_url = capy_api_url + str(idx)
    if idx < 0 or idx >= 100:
        return
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)


if __name__ == "__main__":
    application = ApplicationBuilder().token(sanitize_string(token)).build()

    varaslahto_handler = CommandHandler("milloin_varaslahto", milloin_varaslahto)
    headstart_handler = CommandHandler("when_headstart", when_headstart)
    daily_capybara_handler = CommandHandler("daily_capybara", daily_capybara)

    application.add_handler(varaslahto_handler)
    application.add_handler(headstart_handler)
    application.add_handler(daily_capybara_handler)

    application.run_polling()
