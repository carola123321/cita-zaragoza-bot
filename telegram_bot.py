from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)

async def enviar_aviso(texto):
    await bot.send_message(
        chat_id=CHAT_ID,
        text=texto
    )
