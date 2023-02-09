
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler
from bot_commands import *
from tic_tac_toe import *



app = ApplicationBuilder().token("5991643794:AAHkgbIus2PtQh-EZvq2GdYhy3JNti4YGpk").build()

app.add_handler(CommandHandler("start", start_command))
# app.add_handler(CommandHandler("game", game_command))
app.add_handler(CommandHandler("hi", hi_command))
# app.add_handler(CommandHandler("time", time_to_new_year_command))
app.add_handler(CommandHandler("help", help_command))
# app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler(command="tic_tac", callback=tic_tac_command))
app.add_handler(CommandHandler(command="time", callback=time_to_new_year_command))
app.add_handler(CommandHandler(command="calc", callback=calc_command))

mess_handler = MessageHandler(filters=filters.USER, callback=selector)
app.add_handler(mess_handler)

print("Server start")
app.run_polling()
print("Server stopped")

