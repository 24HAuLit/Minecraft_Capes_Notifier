import discord
import os
from discord.ext import commands

# --- CONFIGURATION ---
TOKEN = os.getenv('discord_token')
MOT_CIBLE = ['cape', 'capes']
ID_ROLE_A_PING = 1473425852284010739  # Remplace par l'ID du rôle
ID_CHANNEL_SPECIFIQUE = 1473425628219834593  # Remplace par l'ID du salon textuel

# Configuration des Intents
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté : {bot.user.name}')
    print(f'Surveillance active dans le salon ID: {ID_CHANNEL_SPECIFIQUE}')

@bot.event
async def on_message(message):
    # 1. On ignore les messages du bot lui-même
    if message.author == bot.user:
        return

    # 2. ON VÉRIFIE LE SALON : Le bot n'exécute la suite que si l'ID du salon est le bon
    if message.channel.id == ID_CHANNEL_SPECIFIQUE:

        words = message.content.lower().replace('.', ' ').replace('!', ' ').split()
        
        # 3. Analyse du mot (en minuscules pour être flexible)
        if any(mot in words for mot in MOT_CIBLE):
            role = message.guild.get_role(ID_ROLE_A_PING)
            
            if role:
                # On envoie le ping dans le salon
                await message.channel.send(f"Alerte {role.mention} ! Le mot '{MOT_CIBLE}' a été détecté.")
            else:
                print("Erreur : ID du rôle introuvable.")

    # Permet aux autres commandes de fonctionner si tu en ajoutes plus tard
    await bot.process_commands(message)

bot.run(TOKEN)