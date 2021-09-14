from core.client import Elderberry
from hikari import Activity
from os import listdir
from core.config import load_config

bot = Elderberry()
config = load_config() # TODO: figure out a way to get rid of this because this is stupid

if __name__ == '__main__':
    for plugin in listdir('plugins'):
        if plugin.endswith('.py'):
            plugin = f"plugins.{plugin.replace('.py', '')}"
            bot.load_extension(plugin)
    bot.load_extension('plugins.filament.superuser')

bot.run(activity=Activity(name=f'(try {config["prefix"]}help)', type=3))