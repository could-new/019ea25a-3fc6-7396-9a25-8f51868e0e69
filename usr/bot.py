import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up intents (required for reading message content in newer discord.py versions)
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with a prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Triggered when the bot successfully connects to Discord."""
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('Ready to receive commands!')
    print('------')

@bot.command(name='ping')
async def ping(ctx):
    """A simple ping command that replies with Pong! and the bot's latency."""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 ({latency}ms)')

@bot.command(name='hello')
async def hello(ctx):
    """Says hello to the user."""
    await ctx.send(f'Hello {ctx.author.mention}! How can I help you today?')

@bot.command(name='echo')
async def echo(ctx, *, message: str):
    """Repeats whatever the user says."""
    await ctx.send(message)

# Error handling example
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You are missing a required argument for this command.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use `!help` to see available commands.")
    else:
        print(f"Error: {error}")

if __name__ == '__main__':
    # Retrieve the token from the environment variable
    token = os.getenv('DISCORD_TOKEN')
    
    if token:
        bot.run(token)
    else:
        print("Error: DISCORD_TOKEN not found. Please set it in your .env file.")
