
from telegram import Update
from telegram.ext import ContextTypes
from src.config.app import config


def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hello!'
    
    if 'help' in processed:
        return 'Help!'
    
    if 'i love python' in processed:
        return 'Check me out on GitHub!'
    
    return 'Custom!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    message_text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type} said: "{message_text}"')
    
    
    # This is because on groups all messages sended to bot are preceded by the bot username
    if message_type == 'group':
        if config.USERNAME in message_text:
            new_text: str = message_text.replace(config.BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        
        else:
            return

    # On private chats, the bot username is not included
    else:
        response: str = handle_response(message_text)
    
    print(f'Bot Response: "{response}"')
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')