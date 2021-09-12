from lightbulb import Bot
from core.config import load_config
from logging import getLogger

class Elderberry(Bot):
    def __init__(self):
        self.config = load_config()
        self.logger = getLogger('hikari.bot')

        super().__init__(
            token=self.config['tokens']['discord'],
            prefix=self.config['prefix']
        )