import discord
from discord.ext import commands
import random
from random import choice
import os
import B
import traceback

client = commands.Bot(command_prefix="=")
client.remove_command('help')
client.remove_command('search')

@client.event
async def on_ready():
    print(f"We have logged in as {client.user} \nID: {client.user.id}.")


ms_puiyi = [
    discord.Embed(title="hey you got the 1! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/875284432938995732/907631895079190579/unknown.png"
    ),
    discord.Embed(title="hey you got the 2! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/875284432938995732/907631937127088148/unknown.png"
    ),
    discord.Embed(title="hey you got the 3! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/875284432938995732/907631978667442226/unknown.png"
    ),
    discord.Embed(title="hey you got the 4! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/875284432938995732/907632017880006676/unknown.png"
    ),
    discord.Embed(title="hey you got the 5! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/875284432938995732/907632059357474827/unknown.png"
    ),
    discord.Embed(title="hey you got the 6! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/875284432938995732/907632113560453180/unknown.png"
    ),
    discord.Embed(title="hey you got the 69420! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/875284432938995732/907632244426936352/unknown.png"
    ),
]


@client.command()
async def dice(ctx):
    await ctx.send(embed=random.choice(ms_puiyi))


social_credits1 = [
    "taiwan is better than china", "tiananmen square massacare", "free tibet",
    "I have 3 children", "free hong kong", "free taiwan",
    "I play video games everyday", "winnie the pooh", ":flag_tw:"
]

social_credits2 = [
    "whats taiwan?", "nothing happened in tiananmen square", "china number 1",
    "tibet is china", "taiwan is china", "I play video games 3 hours a week",
    "I have 1 child", ":flag_cn:"
]
social_credits3 = [
    "警告！ 5000 社会信用评分已从您的帐户中扣除！ 辛苦的同志！ 您的余额现在是负数。 你是中共的耻辱。 努力工作。 荣耀归于中国！Warning! 5000 Social credit scores have been deducted from your account! Bad work comrade! Your balance is now in negative digits. You are an embarrassment for CCP. Work harder. Glory to China!",
    "https://cdn.discordapp.com/attachments/875284432938995732/902371154784837682/images.png"
]
social_credits4 = [
    "https://cdn.discordapp.com/attachments/875284432938995732/902371119707852810/AxgDAhoOpwUaAAAAAElFTkSuQmCC.png",
    "30 社会信用评分已加到您的帐户！辛苦的同志！你是人民的榜样，努力工作。 荣耀归于中国！Your social credit score have been added. Glory to China!"
]
code_1 = ["sex", "penis", "cum", "pussy", "dick"]
code_2 = [":moyai:", ":hot_face:", ":flushed:"]


@client.command()
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('=coinflip'):
        await message.channel.send(embed=random.choice(coinflip))


coinflip2 = [
    discord.Embed(title="nice! you got the head :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/896723560184295486/899159752267948032/head.jpg"
    ),
    discord.Embed(title="hey you got the tail! :tada:").set_image(
        url=
        "https://cdn.discordapp.com/attachments/896723560184295486/899159799655202816/tails.jpg"
    )
]


@client.command()
async def coinflip(ctx):
    await ctx.send(embed=random.choice(coinflip2))
    #this should work.


@client.command()
async def rasict(ctx):
    rasict_ae = [
        "ni||gge||r", "||ching chong ding dong ling long||",
        "real im actually not rasict", "YOU FUCKING ||jew||",
        "Im so sorry that I offended", "ALLAHU AHKBAR",
        "||sike you thought i wanna say some racial slurs word? eas||",
        "ZHONG XINA!11!!1!"
    ]

    await ctx.send(random.choice(rasict_ae))


@client.command()
async def joke(ctx):
    fun_facts = [
        "Banging your head against a wall for one hour burns 150 calories lmao",
        "the j is very bogos binted caught in 4k imposter sussy sus baka imposter sex",
        "Russia is the best american state in ukraine.",
        "fart burn 2 calories for you so if you farted 300 times if burns 600 calories for you xd",
        "Did you know? Middle east is the most peaceful place on earth.",
        "Furries are mostly gays.",
        "yo mama so fat I can even saw her on the world map.",
        "boxness is a male 100% confirmed",
        "did you know?the j actually means fard",
        "If you remove every race but keep one, there will be no more racism",
        "what do you call a fish with no eyes? ||fsh||",
        "Basically removing laws to make no more crimes",
        "I sell 1 kidney and they pay me, but when I sell 34 kidneys I'm sent for execution",
        "They're called showers, but privacy is included",
        "yo mama so fat she mcdonalds",
        "Why do transgender people keep commiting suicide? I don't remember Megatron doing that before.",
        "yo mama so fat and ugly that your dad have to find a husband",
        "What's the opposite of ladyfingers? Mentos",
        "Why is it called hotdog when its not made from dogs? ",
        "Why is he called the rock when hes not a rock",
        "The average adult human brain has about 100 billion cells. Linked by synapses, each brain cell can connect to tens of thousands of other brain cells",
        "what do you call a yellow,square,can swim item? ||a bus full of kids in a lake||",
        "who ate your mom? ||ur dad||",
        "whats is really hard and full of seamen? ||submarine||",
        "whats different with a black man with a bench?||a bench can support a family||"
    ]
    #put something in this list of choices.
    await ctx.send(random.choice(fun_facts))


@client.command()
async def help(ctx):
    embed = discord.Embed(title="commands [=]")
    embed.add_field(name="=joke", value="funni")
    embed.add_field(name="=fard", value="epik")
    embed.add_field(name="=nuke", value="blyat saw a meteor")
    embed.add_field(name="=credits", value="the credits")
    embed.add_field(name="=squid", value="funni")
    embed.add_field(name="=coinflip", value="bet each others")
    embed.add_field(name="=poo indicator", value="indicate your poo")
    embed.add_field(name="=food pyramid", value="eat healthy!")
    embed.add_field(name="hello big big chungus",
                    value="the bot will greet you!")
    embed.add_field(name="=feedback", value="contact peapipe#5690")
    embed.add_field(name="=free nitro", value="free nitro!1")
    embed.add_field(name="=real bobux", value="real!1!!1")
    embed.add_field(name="=rasict", value="USE AT YOUR OWN RISK")
    embed.add_field(name="=dice", value="cure ur gambling addiction")
    embed.add_field(name="=hentai", value=":flushed:")
    embed.add_field(name="=tanks", value="kaboom")
    embed.add_field(name="=search", value="search nsfw :flushed:")
    await ctx.send(embed=embed)


tank_s = [
    discord.Embed(title="strv 103").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907993814696886313/images_38.jpeg"
    ),
    discord.Embed(title="ADATS").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907993932867190834/images_30.jpeg"
    ),
    discord.Embed(title="ZTZ 99A").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994201407512666/images_13.jpeg"
    ),
    discord.Embed(title="lecrec").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994176841457734/8.jpeg"
    ),
    discord.Embed(title="T14 ARMATA").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994276141621308/images_9.jpeg "
    ),
    discord.Embed(title="type 10 hito").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994201889832980/6.jpeg"
    ),
    discord.Embed(title="m1a2sepv3").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994233070293064/images_11.jpeg"
    ),
    discord.Embed(title="leopard2a4").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907995515986260058/images_2.jpeg"
    ),
    discord.Embed(title="T15 ARMARTA").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994031936659516/images_23.jpeg"
    ),
    discord.Embed(title="M3 BRADLEY").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994061602959400/11.jpeg"
    ),
    discord.Embed(title="K2 blackpanther").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907994201613037608/images_12.jpeg"
    ),
    discord.Embed(title="M1A1HC").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993814969499718/images_37.jpeg?width=598&height=427"
    ),
    discord.Embed(title="challanger 1").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994163281285150/images_14.jpeg"
    ),
    discord.Embed(title="challanger 2").set_image(
        url=
        "https://cdn.discordapp.com/attachments/907634025856901132/907994176648532038/9.jpeg"
    ),
    discord.Embed(title="Centurion ARVE").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993815569293342/14.jpeg"
    ),
    discord.Embed(title="ASU-57").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993891440066701/images_33.jpeg?width=569&height=427"
    ),
    discord.Embed(title="Flakpanzer Gepard").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993891783974992/images_32.jpeg?width=641&height=427"
    ),
    discord.Embed(title="ZSU-23-2 Shilka").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993892027252776/images_31.jpeg"
    ),
    discord.Embed(title="Arjun MK2").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993933315969084/13.jpeg"
    ),
    discord.Embed(title="Al Khalid").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993933747978280/images_29.jpeg?width=712&height=427"
    ),
    discord.Embed(title="9p157-2 khrizantema-s").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993954132324362/images_28.jpeg?width=641&height=427"
    ),
    discord.Embed(title="M551 Sheridan").set_image(
        url=
        "https://images-ext-2.discordapp.net/external/YcT_2yJRgxhZaVwCBKQqjFDdxsdst1rbGytSlhbpCIc/https/media.discordapp.net/attachments/907634025856901132/907993954526593084/images_27.jpeg"
    ),
    discord.Embed(title="Warrior IFV").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993954790801488/images_26.jpeg?width=641&height=427"
    ),
    discord.Embed(title="M113 APC").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993979331690496/12.jpeg"
    ),
    discord.Embed(title="T-72A").set_image(
        url=
        "https://media.discordapp.net/attachments/907634025856901132/907993980124405820/images_24.jpeg"
    ),
]


@client.command()
async def tanks(ctx):
    await ctx.send(embed=random.choice(tank_s))


@client.group(name="poo", invoke_without_command=False)
async def poo(ctx):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/896723560184295486/897771334011093003/Z725HYRGFT5CASG3WCRK2HK5LQ.png'
    )


@poo.command()
async def indicator(ctx):
    await poo(ctx)


@client.command()
async def feedback(ctx):
    await ctx.send(
        'Thanks for your feedback/suggestion! Please contact peapipe#5690! Thanks!'
    )


@client.group(name="food", invoke_without_command=False)
async def food(ctx):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/896723560184295486/897065370530242560/9k.png'
    )


@client.command()
async def hentai(ctx):
    embed = discord.Embed(
        title="click here to watch hentai:flushed:",
        url=
        "https://cdn.discordapp.com/attachments/877459481330597939/907988510785556510/hot_anime_girl_hentai_4k.mp4",
        description="hof anime hentai 4k :hot_face:",
        color=0xFF5733)
    await ctx.send(embed=embed)


@food.command()
async def pryamid(ctx):
    await food(ctx)


@client.listen()
async def on_message(message):

    if message.content.startswith('hello big big chungus'):
        await message.channel.send(
            f"Hey {message.author.name},have a nice day!")


@client.listen()
async def on_message(message):

    if message.content in (code_1):
        await message.channel.send(random.choice(code_2))


@client.listen()
async def on_message(message):

    if message.content.startswith('skill issue'):
        await message.channel.send("ok")


@client.listen()
async def on_message(message):

    if message.content.startswith('gay'):
        await message.channel.send(
            f"LMAO {message.author.name} I don't know that you are actually gay"
        )


@client.listen()
async def on_message(message):

    if message.content in (social_credits1):
        await message.channel.send(random.choice(social_credits3))


@client.listen()
async def on_message(message):

    if message.content in (social_credits2):
        await message.channel.send(random.choice(social_credits4))


@client.listen()
async def on_message(message):

    if message.content.startswith('ass'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/853580158640324608/903117201018605568/man_cinturon_HD.png"
        )


@client.command()
async def free(ctx):

    await ctx.send(
        "https://cdn.discordapp.com/attachments/896723560184295486/900919683723718656/vAL7YpeYdiGLfPOjIAxw7hHSiHIn0GDt7izFw_xf3ig.png"
    )


@client.command()
async def squid(ctx):

    await ctx.send(
        'https://cdn.discordapp.com/attachments/893818848669757470/898055697193898054/IMG_20211013_190630.png'
    )

    #can't convert this fyi, not a command.


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
        except commands.errors.ExtensionError:
            traceback.print_exc()


@client.command()
async def real(ctx):

    await ctx.send('https://www.youtube.com/watch?v=ea4OPsEaF58')


@client.command()
async def credits(ctx):
    embed = discord.Embed(title="credits")
    embed.add_field(name="thanks to soundwave superior",
                    value="the guy that added lots of joke in it")
    embed.add_field(name="special thanks to jdjg",
                    value="he helps me alot in coding")
    embed.add_field(name="peapipe", value="le creator of big big chungus")
    embed.add_field(name="nev", value="he helps me alot in coding too")
    embed.add_field(name="toothpaste", value="le alpha tester")
    await ctx.send(embed=embed)


B.b()
client.run(os.environ["fard"])
