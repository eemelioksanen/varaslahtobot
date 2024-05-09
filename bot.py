import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import datetime
import random

with open("token.txt", "r") as file:
    token = file.read()

varaslahto_date = datetime(2024, 8, 18)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

emojis = ["😱", "😀", "🤣", "👌", "🗿", "🤨", "💀", "😤", "🙈"]


async def milloin_varaslahto(update: Update, context: ContextTypes.DEFAULT_TYPE):

    current_date = datetime.now()
    time_until_varaslahto = varaslahto_date - current_date
    days = time_until_varaslahto.days
    hours = time_until_varaslahto.seconds // 3600

    msg_text = f"Tietokillan varaslähtö järjestetään tänä vuonna 18.8.2024!!!! Varaslähtöön on siis aikaa {days} päivää ja {hours} tuntia! "
    emoji_number = random.randint(0, 10)
    for i in range(emoji_number):
        msg_text += emojis[random.randint(0, len(emojis) - 1)]

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg_text)


async def when_headstart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    current_date = datetime.now()
    time_until_varaslahto = varaslahto_date - current_date
    days = time_until_varaslahto.days
    hours = time_until_varaslahto.seconds // 3600

    msg_text = f"The headstart of Tietokilta will be held on 18.8.2024!!!! There are {days} days and {hours} hours left! "
    emoji_number = random.randint(0, 10)
    for i in range(emoji_number):
        msg_text += emojis[random.randint(0, len(emojis) - 1)]

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg_text)


if __name__ == "__main__":
    application = ApplicationBuilder().token(token).build()

    varaslahto_handler = CommandHandler("milloin_varaslahto", milloin_varaslahto)
    headstart_handler = CommandHandler("when_headstart", when_headstart)

    application.add_handler(varaslahto_handler)
    application.add_handler(headstart_handler)

    application.run_polling()
