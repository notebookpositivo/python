import discord
from discord.ext import commands
import random
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Variáveis para controle
last_everyone_time = {}
victim_count = {}  # Contagem de vítimas
bot_active = True  # Estado do bot (ligado/desligado)
allowed_user_id = 1109190627763171459  # Substitua pelo ID do usuário _.notebook

respostas_normais = [
    "disse pra você se fuder",
    "disse que vai te abusar",
    # ... (mantenha suas outras respostas)
]

respostas_everyone = [
    "Irei abusar de todos cronicamente",
    "Todos serão minhas vitimas",
    "Eu sou o abusador supremo desse servidor"
]

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Vigiando o @everyone"))

@bot.command()
async def fuder(ctx, member: str):
    if not bot_active:
        return
    
    # Verifica se é menção especial
    if member.lower() in ['@here', '@everyone', 'here', 'everyone']:
        await handle_everyone_mention(ctx)
        return
    
    try:
        # Tenta converter para Member
        member_obj = await commands.MemberConverter().convert(ctx, member)
        
        if ctx.author.id == member_obj.id:
            await ctx.send(f"{ctx.author.mention} Quer se fuder, bate punheta")
            return
            
        if member_obj.id == ctx.guild.id:  # ID do @everyone
            await handle_everyone_mention(ctx)
        else:
            resposta = random.choice(respostas_normais)
            await ctx.send(f"{ctx.author.mention} {resposta} {member_obj.mention}")
            
            # Atualiza contador de vítimas
            if ctx.author.id not in victim_count:
                victim_count[ctx.author.id] = 0
            victim_count[ctx.author.id] += 1
    
    except commands.MemberNotFound:
        await ctx.send(f"{ctx.author.mention} Sei quem é esse merda não")

@bot.command()
async def vitimas(ctx):
    """Mostra quantas vezes você usou o comando !fuder"""
    count = victim_count.get(ctx.author.id, 0)
    await ctx.send(f"{ctx.author.mention} Você já abusou de {count} {'pessoa' if count == 1 else 'pessoas'}!")

@bot.command()
async def off(ctx):
    """Desativa o bot (apenas para _.notebook)"""
    if ctx.author.id == allowed_user_id:
        global bot_active
        bot_active = False
        await ctx.send("Bot desativado. Não vou mais responder a comandos.")
        await bot.change_presence(activity=discord.Game(name="Desativado ⛔"))
    else:
        await ctx.send("Você não tem permissão para desativar o bot.")

@bot.command()
async def on(ctx):
    """Ativa o bot (apenas para _.notebook)"""
    if ctx.author.id == allowed_user_id:
        global bot_active
        bot_active = True
        await ctx.send("Bot ativado. Pronto para o abuso!")
        await bot.change_presence(activity=discord.Game(name="Vigiando o @everyone"))
    else:
        await ctx.send("Você não tem permissão para ativar o bot.")

async def handle_everyone_mention(ctx):
    if not bot_active:
        return
        
    now = datetime.now()
    author_id = ctx.author.id
    
    # Verifica cooldown (1 minuto)
    if author_id in last_everyone_time:
        remaining = (timedelta(minutes=1)) - (now - last_everyone_time[author_id])
        if remaining > timedelta(0):
            await ctx.send(f"{ctx.author.mention} Calma ai precoce, ainda faltam {remaining.seconds} pra você usar o comando de novo")
            return
    
    last_everyone_time[author_id] = now
    resposta = random.choice(respostas_everyone)
    
    # Envia a mensagem principal primeiro
    await ctx.send(f"{ctx.author.mention} {resposta}")
    
    # 100% de chance de enviar um GIF em mensagem separada
    if random.random() < 1:
        gifs = [
            "https://tenor.com/view/funny-gif-8376507566099409182",
            "https://tenor.com/view/sonic-gif-2410389723882233984",
            "https://tenor.com/view/freaky-freaky-smile-sukuna-sukuna-smile-freaky-sukuna-gif-4852549280133734300"
        ]
        await ctx.send(random.choice(gifs))

@bot.event
async def on_message(message):
    if not bot_active:
        return
        
    if not message.author.bot:
        if "@everyone" in message.content or "@here" in message.content:
            if not message.author.guild_permissions.mention_everyone:
                await handle_everyone_mention(await bot.get_context(message))
                await message.delete()
    
    await bot.process_commands(message)

# Substitua pelo seu token real
bot.run('')