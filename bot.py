import lightbulb
from hikari import Activity
import json
from os import listdir

with open('config.json') as config_file:
    config = json.load(config_file)

bot = lightbulb.Bot(
    token=config['tokens']['discord'],
    prefix=config['prefix']
)

if __name__ == '__main__':
    for plugin in listdir('plugins'):
        if plugin.endswith('.py'):
            plugin = f"plugins.{plugin.replace('.py', '')}"
            bot.load_extension(plugin)

bot.run(activity=Activity(name=f'(try {config["prefix"]}help)', type=3))