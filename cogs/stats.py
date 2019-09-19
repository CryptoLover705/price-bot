import discord, os
from discord.ext import commands
from utils import checks, output, parsing
from aiohttp import ClientSession
import urllib.request
import json

class Stats:
    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def stats(self, ctx, amount=1):
        """
        Show stats about XUN
        """
        channel_name = ctx.message.channel.name
        allowed_channels = parsing.parse_json('config.json')['command_channels'][ctx.command.name]
        if channel_name not in allowed_channels:
            return

        headers={"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
        try:
            async with ClientSession() as session:
                async with session.get("https://api.coingecko.com/api/v3/coins/ultranote", headers=headers) as response:
                    responseRaw = await response.read()
                    priceData = json.loads(responseRaw)
                    
                    embed= discord.Embed(colour=0x00FF00)
                    embed.set_author(name='Ultranote Information', icon_url="https://i.imgur.com/Zb6uZmP.jpg")
                    embed.add_field(name="current_price", value="${}".format(item['usd']))
                    embed.add_field(name="Price (BTC)", value="{} BTC".format(item['btc']))
                    embed.add_field(name="Price (LTC)", value="{} LTC".format(item['ltc']))
                    embed.add_field(name="Price (ETH)", value="{} ETH".format(item['eth']))
                    embed.add_field(name='\u200b',value='\u200b')
                    embed.add_field(name="Volume (BTC)", value="{} BTC".format(priceData['tickers'][0]['converted_volume']['btc']))
                    embed.add_field(name="Volume (USD)", value="${}".format(priceData['market_data']['total_volume']['usd']))
                    embed.add_field(name="Volume (XUN)", value="{} XUN".format(priceData['tickers'][0]['volume']))
                    embed.add_field(name="% 24h", value="{}%".format(priceData['market_data']['price_change_percentage_24h']))
                    embed.add_field(name="% 7d", value="{}%".format(priceData['market_data']['price_change_percentage_7d']))
                    embed.add_field(name="% 30d", value="{}%".format(priceData['market_data']['price_change_percentage_30d']))
                    embed.add_field(name="Market Cap", value="${}".format(priceData['market_data']['market_cap']['usd']))
                    embed.add_field(name="Circulating Supply", value="{} XUN".format(priceData['market_data']['circulating_supply']))
                    embed.add_field(name="Total Supply", value="{} XUN".format(priceData['market_data']['total_supply']))
                    embed.set_footer(text="https://www.coingecko.com/en/coins/ultranote", icon_url="https://i.imgur.com/Zb6uZmP.jpg")
                    await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(str(e))
#           await self.bot.say(":warning: Error fetching prices!")


def setup(bot):
    bot.add_cog(Stats(bot))