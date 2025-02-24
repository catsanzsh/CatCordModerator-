import discord
from discord.ext import commands
import openai
import os
import lmstudio
import ollama

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Set up OpenAI GPT-J
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up LM Studio
lmstudio.api_key = os.getenv("LMSTUDIO_API_KEY")

# Set up ollama/highvibes
ollama.api_key = os.getenv("OLLAMA_API_KEY")

async def generate_response(prompt):
    if os.getenv("USE_LMSTUDIO"):
        response = lmstudio.Completion.create(
            engine="lmstudio-engine",
            prompt=prompt,
            max_tokens=150
        )
    elif os.getenv("USE_OLLAMA"):
        response = ollama.Completion.create(
            engine="ollama-engine",
            prompt=prompt,
            max_tokens=150
        )
    else:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )
    return response.choices[0].text.strip()

# Define bot commands
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='meow')
async def meow(ctx):
    response = await generate_response("You are an anime cat. Respond with a cute and playful message.")
    await ctx.send(response)

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    response = await generate_response(f"You are an anime cat moderator. Explain why {member.name} was banned.")
    await ctx.send(response)

@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    response = await generate_response(f"You are an anime cat moderator. Explain why {member.name} was kicked.")
    await ctx.send(response)

@bot.command(name='mute')
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not mute_role:
        mute_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False)
    await member.add_roles(mute_role, reason=reason)
    response = await generate_response(f"You are an anime cat moderator. Explain why {member.name} was muted.")
    await ctx.send(response)

@bot.command(name='unmute')
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mute_role, reason=reason)
    response = await generate_response(f"You are an anime cat moderator. Explain why {member.name} was unmuted.")
    await ctx.send(response)

# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))
