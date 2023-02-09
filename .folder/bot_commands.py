from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime
from dateutil.relativedelta import relativedelta
import tic_tac_toe
from my_calc import calculator

_state_message_handler = ""

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет, я первый бот моего хозяина.\n Я научился немного новому.\nПоздароваться с тобой "/hi"\n Показать тебе сколько осталось до Нового Года! "/time"\n  Cчитать числа"/calc"\n Если нужна помощь нажми "/help"\n/Можем сыграть в х_о"/tic_tac"')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет,{update.effective_user.first_name}. Желаю тебе отличного дня!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/start\n/hi\n/time\n/help\n/calc\n/tic_tac')


# async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def time_to_new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    date_now = datetime.today()
    date_new_year = datetime(date_now.year + 1, 1, 1, 0, 0, 0)
    remained = relativedelta(date_new_year, date_now)
    await update.message.reply_text(
        text=f'До {str(datetime.today().year + 1)} осталось:\n'
            #  f'{str(remained.days)} days\n'
             f'{str(remained.months)} месяц(-ев)\n'
             f'{str(remained.days)} день(дней)\n'
             f'{str(remained.hours)} час(-ов)\n'
             f'{str(remained.minutes)} минут(-а)\n'
             f'{str(remained.seconds)} секунд(-а)')
    
async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "calc"
    await update.message.reply_text(text="Ввод для расчета или 'Выход' для закрытия калькулятора")
    # await update.message.reply_text(text=update.message.text)

async def tic_tac_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "tic_tac"
    await update.message.reply_text(text=tic_tac_toe.show_matrix())
    await update.message.reply_text(text="Введите число для игры или 'Выход' для закрытия игры")

async def selector(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global _state_message_handler
    if update.message.text == "Выход":
        _state_message_handler = ""
        await update.message.reply_text(text="Пока )")
    # await update.message.reply_text(text=_state_message_handler)
    if _state_message_handler == "calc":
        res = calculator(update.message.text)
        await update.message.reply_text(text=f"{update.message.text}={res}")
        await update.message.reply_text(text="Ввод для расчета или 'Выход' для закрытия калькулятора")
    if _state_message_handler == "tic_tac":
        await update.message.reply_text(tic_tac_toe.start_game(update.message.text))
        if tic_tac_toe.is_first:
            _state_message_handler = ""
            await update.message.reply_text(text="Пока )")