from quotexpy.new import Quotex
from telegram import Bot

# Login credentials
email = "arhimanshya@gmail.com"
password = "12345678an"

TELEGRAM_BOT_TOKEN = "7413469925:AAHd7Hi2g3609KoT15MSdrJSeqF1-YlCC54"
TELEGRAM_CHAT_ID = "6065493589"

q = Quotex()
q.login(email=email, password=password)

if q.check_connection():
    token = q.token
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f"Your Quotex Token:\n\n`{token}`", parse_mode="Markdown")
    print("✅ Token sent to Telegram")
else:
    print("❌ Login Failed!")
