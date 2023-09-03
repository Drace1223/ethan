import discord
from discord.ext import commands, tasks
import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Over Frizzle Studios"))

@bot.event
async def on_member_join(member):
    # You can uncomment this part if you have a welcome message with attachments
    # channel_to_send = bot.get_channel(1142973112758050860)
    # welcome_attachment = discord.File("retroPlayStation.png", filename="retroPlayStation.png")
    # welcome_embed = discord.Embed(
    #     color=discord.Color.green(),
    #     description=f"Welcome {member.mention}!\n<:speechbubble_what:1145370733082583111> Go chat about things in <#1142973112758050860>, or join up in a VC <:blurple_voicechannel:1145371297090654289>"
    # ).set_author(name=member.display_name, icon_url=member.avatar_url)
    # await channel_to_send.send(content=f"Welcome {member}!", embed=welcome_embed, file=welcome_attachment)
    pass  # Uncomment and modify the welcome message if needed

@tasks.loop(seconds=1)
async def update_time():
    count_down_date = datetime.datetime(2023, 10, 3, 0, 0, 0)
    now = datetime.datetime.now()
    delta = count_down_date - now
    time = str(delta).split(".")[0]
    update_time.time = time if delta.total_seconds() > 0 else "GOING ON"

@update_time.before_loop
async def before_update_time():
    await bot.wait_until_ready()

update_time.start()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def info(ctx):
    info_embed = discord.Embed(
        title="Bot Info",
        color=discord.Color.green()
    )
    info_embed.add_field(name="Version", value="V0.0.0 ALPHA", inline=True)
    info_embed.add_field(name="Next Play Test", value=update_time.time, inline=True)
    info_embed.set_footer(text="This shows all the info for our game currently being made.")
    await ctx.send(embed=info_embed)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTE0MzI2NDQ2MDc3NDA2MDA5NA.GolD2O.HJfaaCp8XDbvglJL_EvxRhV_Hy6J9Uy8RkAzdI')
