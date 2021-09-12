from lightbulb import Plugin, command, owner_only
from logging import getLogger

class Core(Plugin):
    def __init__(self):
        self.log = getLogger('hikari.bot')
        super().__init__()

    @command()
    async def ping(self, ctx):
        """Check if I am alive at this present moment"""
        return await ctx.respond('yo dipshit')

    @owner_only()
    @command()
    async def reload(self, ctx, *plugins: str):
        """Quick reload command for debugging purposes"""
        for plugin in plugins:
            try:
                plugin = f'plugins.{plugin}'
                ctx.bot.unload_extension(plugin)
                ctx.bot.load_extension(plugin)
            finally:
                return await ctx.respond(f':white_check_mark: Reloaded plugin {plugin} successfully.')

    @owner_only()
    @command()
    async def load(self, ctx, *plugins: str):
        """Quick load command for debugging purposes"""
        for plugin in plugins:
            try:
                plugin = f'plugins.{plugin}'
                ctx.bot.load_extension(plugin)
            finally:
                return await ctx.respond(f':white_check_mark: Loaded plugin {plugin} successfully.')
    
    @owner_only()
    @command()
    async def unload(self, ctx, *plugins: str):
        """Quick unload command for debugging purposes"""
        for plugin in plugins:
            try:
                plugin = f'plugins.{plugin}'
                ctx.bot.unload_extension(plugin)
            finally:
                return await ctx.respond(f':white_check_mark: Unloaded plugin {plugin} successfully.')

def load(bot):
    bot.add_plugin(Core())