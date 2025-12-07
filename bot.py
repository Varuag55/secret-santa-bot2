import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен беремо з Render Environment Variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Учасники (потім заміниш на своїх)
participants = [
    "Аня",
    "Богдан",
    "Віра",
    "Гліб",
    "Діана",
    "Соня"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 Дізнатися кому я дарую", callback_data='draw')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Привіт! Натисни кнопку ↓ щоб дізнатися кому ти даруєш подарунок 🎁",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    recipient = random.choice(participants)
    
    await query.edit_message_text(f"✨ Ти даруєш подарунок: **{recipient}** 🎁")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()
