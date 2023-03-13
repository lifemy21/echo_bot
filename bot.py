# 6153048734:AAEqUS7RhMo6lJ5idyfdJAPWUYx2EVICIDk DostavkaEd_bot
# 6293433229:AAFFP_N0xqJwj2slYyxKWrK8VJAWPgvEtr8 yarasoff_bot

from config_data.config import load_config


config = load_config('C:\Project\Telegram_bot\.env')

bot_token = config.tg_bot.token           # Сохраняем токен в переменную bot_token
superadmin = config.tg_bot.admin_ids[0]   # Сохраняем ID админа в переменную superadmin

print(superadmin)