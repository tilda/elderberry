from lightbulb import Plugin, command
import wolframalpha

class Wolfram(Plugin):
    def __init__(self, bot):
        self.bot = bot
        self.wolfram = wolframalpha.Client(self.bot.config['tokens']['wolfram'])
        super().__init__()

    def plugin_remove(self) -> None:
        self.wolfram.session.close()
        return super().plugin_remove()

    @command(aliases=['wolfram', 'wolframalpha'])
    async def wa(self, ctx, *, query: str):
        return await ctx.respond('piss shit and cum and also balls')

def load(bot):
    bot.add_plugin(Wolfram(bot))

def unload(bot):
    bot.remove_plugin("Wolfram")