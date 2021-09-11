import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

app = commands.Bot(command_prefix='.')
token = "ODY2MzI1MTIxNzQ5MDkwMzE0.YPQ6JA.GTgxbrfd9OeWeR6PN60N2vUoRs8"


@app.event
async def on_ready():
    print('Login to: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)


@app.command()
async def q(ctx, champName):
    pass
    url = 'https://poro.gg/champions/' + champName + '/aram?hl=ko-KR'
    uuu = '#wrapper > div > div > div > div:nth-child(7) > div.row.row-small > '
    url_r = (uuu
    + 'div.col-lg-8.col-xl-7 > div.champion-box.champion-box--rune-build '
    + '> div.champion-box__content > div > div.champion-rune__content '
    + '> div.champion-rune-tab-content.active.h-auto > div:nth-child(1)')
    url_s = (uuu
    + 'div.col-lg-4.col-xl-5 > div > div.champion-box__content '
    + '> div.champion-build.champion-build--spells > div.champion-build'
    + '__content > div:nth-child(1) > div.champion-build__icons')
    response = requests.get(url)

    if response.status_code == 200:
        # basic settings
        # --------------------------------------------------------------
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # open Rune page
        # --------------------------------------------------------------
        sample = soup.select_one(url_r)
        runes_html = sample.find_all('img', {'class': 'active'})

        # rune_img_urls = [str(a.attrs['src']) for a in runes_html]

        main_r = [str(a.attrs['alt']) for a in runes_html[:5]]  # primary rune
        second_r = [str(a.attrs['alt']) for a in runes_html[5:8]]  # secondary rune
        other_r = [str(a.attrs['alt']) for a in runes_html[8:]]  # adapt ability

        await ctx.send('[ ' + main_r[0] + ' ]')  # print main runes
        for i in range(1, len(main_r)):
            await ctx.send(' ' + main_r[i])
        await ctx.send('- ' * 10)
        await ctx.send('[ ' + second_r[0] + ' ]')  # print second runes
        for i in range(1, len(second_r)):
            await ctx.send(' ' + second_r[i])
        await ctx.send('- ' * 10)
        for item in other_r:
            await ctx.send(' ' + item)

        # open Spell page
        # --------------------------------------------------------------
        sample = soup.select_one(url_s)
        spells_html = sample.find_all('img')

        # spell_img_urls = [str(a.attrs['src']) for a in spells_html]
        spells = [str(a.attrs['alt']) for a in spells_html]

        # for item in spell_img_urls:
        #    print(item)
        await ctx.send('\n< ' + spells[0] + ' ' + spells[1] + ' >')

        # make embed
        # --------------------------------------------------------------
        embed = discord.Embed(title='MyEmbed', description='This is my embed')
        embed.add_field(name='This is my field 1', value='Value of embed field 1', inline=True)
        # embed.set_image(url=rune_img_urls[1])
        # embed.set_thumbnail(url=rune_img_urls[0])
        embed.set_footer(text='footer text')

        await ctx.send(embed=embed(embed))


app.run(token)
