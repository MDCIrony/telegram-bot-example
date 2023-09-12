from src.config.app import config
from telegram.ext import Application, ApplicationBuilder, CommandHandler,MessageHandler, filters
from src.commands.no_auth import start_command, help_command, custom_command
from src.responses.response import handle_message, error


class App:
    def __init__(self) -> None:
        self.config = config
        self.bot = Application.builder().token(self.config.API_KEY).build()
        
        # Commands        
        self.bot.add_handler(CommandHandler('start', start_command))
        self.bot.add_handler(CommandHandler('help', help_command))
        self.bot.add_handler(CommandHandler('custom', custom_command))

        # Messages
        
        self.bot.add_handler(MessageHandler(filters.TEXT, handle_message))
        
        # Errors
        self.bot.add_error_handler(error)
        
    def run(self) -> None:
        self.bot.run_polling(poll_interval=1, timeout=30)