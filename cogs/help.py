import discord
from discord.ext import commands
from utils import checks, parsing

class Help:
    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command(pass_context=True)
    async def help(self, ctx):
        """
        Display a useful list of commands
        """
        channel_name = ctx.message.channel.name
        allowed_channels = parsing.parse_json('config.json')['command_channels'][ctx.command.name]
        if channel_name not in allowed_channels:
            return

        desc = ""
        for key in self.bot.commands.keys():
            command = self.bot.get_command(key)
            if command.hidden and not checks.is_owner(ctx):
                continue

            if command.aliases:
                desc += "`${}`".format(command.name)+" - {}\nAliases: `{}`\n".format(command.short_doc,
                ",".join(command.aliases))
                desc += "\n"

            elif command.short_doc:
                desc += "`${}`".format(command.name)+" - {}\n".format(command.short_doc)
                desc += "\n"

            else:
                desc += "`${}`\n".format(command.name)
                desc += "\n"

        embed = discord.Embed(description=desc)
        embed.set_author(icon_url=self.bot.user.avatar_url, name="SCT-Bot commands!")
        try:
            await self.bot.send_message(ctx.message.author, embed=embed)
            if ctx.message.server is not None:
                await self.bot.say("{}, I PMed you some helpful info! Make sure to double check that it is from me! :envelope:".format(ctx.message.author.mention))
        except discord.HTTPException:
            await self.bot.say("I need the `Embed links` permission to send this!")


def setup(bot):
    bot.add_cog(Help(bot))
