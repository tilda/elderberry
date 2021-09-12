from lightbulb import Plugin, command, owner_only
import lightbulb

class Core(Plugin):

    @command()
    async def ping(self, ctx):
        """Check if I am alive at this present moment"""
        return await ctx.respond('the')

    @owner_only()
    @command()
    async def reload(self, ctx, *plugins: str):
        """Quick reload command for debugging purposes"""
        for plugin in plugins:
            try:
                ctx.bot.reload_extension(plugin)
            finally:
                return await ctx.respond(f':white_check_mark: Reloaded plugin {plugin} successfully.')

    @owner_only()
    @command()
    async def load(self, ctx, *plugins: str):
        """Quick load command for debugging purposes"""
        for plugin in plugins:
            try:
                ctx.bot.load_extension(plugin)
            finally:
                return await ctx.respond(f':white_check_mark: Loaded plugin {plugin} successfully.')
    
    @owner_only()
    @command()
    async def unload(self, ctx, *plugins: str):
        """Quick unload command for debugging purposes"""
        for plugin in plugins:
            try:
                ctx.bot.unload_extension(plugin)
            finally:
                return await ctx.respond(f':white_check_mark: Unloaded plugin {plugin} successfully.')

    @owner_only()
    @command()
    async def shutdown(self, ctx):
        """Shut down the bot"""
        await ctx.message.add_reaction("👋")
        return await ctx.bot.close()

def load(bot):
    bot.add_plugin(Core())

def unload(bot):
    bot.remove_plugin("Core")