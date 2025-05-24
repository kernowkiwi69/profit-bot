import os
import asyncio
from web3 import Web3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive
from eth_account import Account
from datetime import datetime

# Enable HD wallet feature
Account.enable_unaudited_hdwallet_features()

# Load env variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_CHAT_ID = int(os.getenv("OWNER_CHAT_ID"))
WALLET_SEED = os.getenv("METAMASK_SEED")

# Create wallet
wallet = Account.from_mnemonic(WALLET_SEED)
wallet_address = wallet.address

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == OWNER_CHAT_ID:
        await update.message.reply_text("Bot is live and listening.")
    else:
        await update.message.reply_text("Access denied.")

# /wallet command
async def wallet_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == OWNER_CHAT_ID:
        await update.message.reply_text(f"Wallet address: {wallet_address}")
    else:
        await update.message.reply_text("Access denied.")

# Main function
async def main():
    keep_alive()
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("wallet", wallet_info))

    print("Bot is polling...")
    await app.run_polling()

# Run
if __name__ == "__main__":
    asyncio.run(main())
