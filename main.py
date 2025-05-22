import time
import threading
from web3 import Web3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive
import os
import pytz
from datetime import datetime
from eth_account import Account

Account.enable_unaudited_hdwallet_features()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_CHAT_ID = os.getenv("OWNER_CHAT_ID")
WALLET_SEED = os.getenv("METAMASK_SEED")

wallet = Account.from_mnemonic(WALLET_SEED)
wallet_address = wallet.address

def get_uk_time():
    return datetime.now(pytz.timezone("Europe/London")).strftime('%Y-%m-%d %H:%M:%S')

def scan_airdrops():
    while True:
        print(f"[{get_uk_time()}] Scanning airdrops for {wallet_address}")
        time.sleep(1800)

def run_sniper():
    while True:
        print(f"[{get_uk_time()}] Sniper active - monitoring token listings")
        time.sleep(60)

def scan_casino_bonuses():
    while True:
        print(f"[{get_uk_time()}] Checking casino bonus loops")
        time.sleep(600)

def evolve_bot():
    while True:
        print(f"[{get_uk_time()}] Evaluating growth strategy...")
        time.sleep(3600)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) == OWNER_CHAT_ID:
        await update.message.reply_text(f"Bot running. Wallet: {wallet_address}\nUK Time: {get_uk_time()}")
    else:
        await update.message.reply_text("Unauthorized.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    keep_alive()

    threading.Thread(target=scan_airdrops, daemon=True).start()
    threading.Thread(target=run_sniper, daemon=True).start()
    threading.Thread(target=scan_casino_bonuses, daemon=True).start()
    threading.Thread(target=evolve_bot, daemon=True).start()
    threading.Thread(target=app.run_polling, daemon=True).start()

    while True:
        time.sleep(100)
