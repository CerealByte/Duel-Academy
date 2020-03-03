import random
import asyncio
import discord
from gsheet import *


client = discord.Client()

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Unassigned')
    await member.add_roles(role)

@client.event
async def on_message(message):
    sheet = gsheet()
    SAMPLE_SPREADSHEET_ID = '1oaN40EjGcCfqMVZlHuXZMI8avsDdO5Oelca0k-OjEJA'
    SAMPLE_RANGE_NAME = 'Table!A2:B9'
    colourr = 0x000000
    roles = message.author.roles
    SPREADSHEET_ID = '1oaN40EjGcCfqMVZlHuXZMI8avsDdO5Oelca0k-OjEJA' 
    RANGE_NAME = 'A11:F'
    FIELDS = 1
    msg = message.content[3:]
    result = [x.strip() for x in msg.split(',')]
    
    if "holactie white" in [y.name.lower() for y in roles]:
        colourr = 0xdadada
    elif "obelisk blue" in [i.name.lower() for i in roles]:
        colourr = 0x5656ec
    elif "slifer red" in [i.name.lower() for i in roles]:
        colourr = 0xff0000
    elif "ra yellow" in [i.name.lower() for i in roles]:
        colourr = 0xffff00
    
    if message.author == client.user:
        return
    prefix = "!sb"
    ##AUTO POINTS FOR HOUSE WARS
    if message.channel == client.get_channel(668558378636673031):
        if len(message.attachments) == 1:
            words = message.content.lower().split(" ")
            if words[1] == "win" and "vs" in words[2] and words[4] == "lose":
                def check(r, u ):
                    return "moderator" in [i.name.lower() for i in u.roles] and r.emoji.name == "Tick"
                winhouse = words[0]
                losehouse = words[3]
                r, u  = await client.wait_for("reaction_add", check = check)
                if winhouse == "holactie":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [message.content]
                elif winhouse == "obelisk":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [message.content]
                elif winhouse == "slifer":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0]+ [message.content]
                elif winhouse == "ra":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [message.content]
                else:
                    e = await message.channel.send(f"sorry, i couldn't find house: {winhouse}, check your spelling and try again. NO POINTS AWARDED.")
                    await message.delete()
                    await e.delete()
                    return
                sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
                mesg = await message.channel.send(f'{winhouse} has won 10 points!')
                if losehouse == "holactie":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [message.content]
                elif losehouse == "obelisk":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [message.content]
                elif losehouse == "slifer":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0]+ [message.content]
                elif losehouse == "ra":
                    DATA = DATA = ["autobot"] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [message.content]
                else:
                    await message.channel.send(f"sorry, i couldn't find house: {losehouse}, check your spelling and try again. <@&668442198370418698> please take points from: {losehouse}.")
                    await message.delete()
                    return
                sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
                mes = await message.channel.send(f'{losehouse} has lost 5 points!')
                
                await message.delete()
                await asyncio.sleep(3)
                await mes.delete()
                await mesg.delete()
            else:
                mesg = await message.channel.send("you have sent this in the wrong format. therefore no points will be awarded. try again in the format \{house\} win vs \{house\} lose")
                await message.delete()
            
        
   
    

                            
    if message.content.lower().startswith(prefix):
        

        cmd = message.content.split(" ")[1].lower()
        if cmd == "scoreboard":
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])
            embed = discord.Embed(title = "!S Scoreboard", colour = colourr)
            
            for row in values:
                embed.add_field(name=f"{row[0]}", value=f"`{row[1]}`", inline=False)
            sb = await message.channel.send(embed = embed)
            await asyncio.sleep(60)
            await sb.delete()
            return
        if cmd == "help":
            embed = discord.Embed(title = "!S Help",colour = colourr)
            commands = {
                #slifer
                "sliferwin": "gives Slifer 10 points", #
                "sliferlose": "takes 5 points from slifer", #
                "sliferbonus": "gives slifer 50 points",#
                "slifercup": "gives slifer the House Cup",#
                #ra
                "rawin": "gives ra 10 points",#
                "ralose": "takes 5 points from ra",#
                "rabonus": "gives ra 50 points",#
                "racup": "gives ra the House Cup",#
                #obelisk
                "obeliskwin": "gives obelisk 10 points",#
                "obelisklose": "takes 5 points from obelisk",#
                "obeliskbonus": "gives obelisk 50 points",#
                "obeliskcup": "gives obelisk the House Cup",#
                #holactie
                "holactiewin": "gives holactie 10 points",#
                "holactielose": "takes 5 points from holactie",#
                "holactiebonus": "gives holactie 50 points",#
                "holactiecup": "gives holactie the House Cup",#
                #other commands
                "scoreboard": "displays scoreboard",#
                "help": "displays help display",#
                "kaiba":"displays an invite to Kaiba Corp",#
                "staff": "displays staff list",#
                "affiliates": "displays our affiliates",#
                "info": "displays information about this server",#
                "whois": "displays important people"#
                }
            for i, j in commands.items():
                embed.add_field(name = f"`{prefix} {i}`", value = j, inline = True)
            embed.set_footer(text = "`all commands are moderator only, ask a mod to help if required`")
            await message.channel.send(embed = embed)
            return
        if not discord.utils.get(message.author.roles, name="Moderator"):
            mesg = await message.channel.send('You don\'t have the required role!')
            return
        #SLIFERSTUFF
        if cmd == "sliferwin":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0]+ result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg  = await message.channel.send('Slifer Red Won +10 Points!')
            
            
        if cmd == "sliferlose":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Slifer Red Lost -5 Points')
        if cmd == "sliferbonus":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Slifer Red, Bonus +50 Points!')
        if cmd == "slifercup":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Slifer Red Wins The House Cup! Congratulations!')

        #RASTUFF
        if cmd == "rawin":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Ra Yellow Won +10 Points!')
        if cmd == "ralose":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Ra Yellow Lost -5 Points')
        if cmd == "rabonus":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Ra Yellow, Bonus +50 Points!')
        if cmd == "racup":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Ra Yellow Wins The House Cup! Congratulations!')

        #OBELISKSTUFF
        if cmd == "obeliskwin":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Obelisk Blue Won +10 Points!')
        if cmd == "obelisklose":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Obelisk Blue Lost -5 Points')
        if cmd == "obeliskbonus":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Obelisk Blue, Bonus +50 Points')
        if cmd == "obeliskcup":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Obelisk Blue Wins The House Cup! Congratulations!')

        #HOLACTIESTUFF
        if cmd == "holactiewin":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Holactie White Won +10 Points!')
        if cmd == "holactielose":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Holactie White Lost -5 Points')
        if cmd == "holactiebonus":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Holactie White Bonus +50 Points!')
        if cmd == "holactiecup":
            DATA = DATA = [message.author.name] + [str(message.created_at)] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [0] + [1] + [0] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            mesg = await message.channel.send('Holactie White Wins The House Cup! Congratulations!')

        #SCOREBOARDCOMMAND
        
        #HELPCOMMAND
        

        #WHOISCOMMAND
        if cmd == "whois" or cmd == "who":
            embed = discord.Embed(name = "Important People!", colour = colourr)
            people = {
                "MauiMallard":"Created `Duel Academy (Discord Server)`, `GSheet (Database)`, and was instrumental in the creation of this bot",
                "EmoDigestive":"Was instrumental in the creation of this bot.",
                "Seto Kaiba, Malcolm Merlyn": "Created \nTDOANE: https://ygopro.org/ and \nYGOPRO2: https://www.ygopro2.org/ Forums: \nhttp://ygopro.club/ Discord: \nhttps://discord.gg/FTPcGg6'",
                "hugonun": "created the main body of the bot's Discord - GSheets input. github:https://github.com/hugonun/ and \nSource code: https://github.com/hugonun/discord2sheet-bot'"
                }
            for i, j in people.items():
                embed.add_field(name = i, value = j, inline = False)
            await message.channel.send(embed = embed)
            
        #STAFFCOMMAND
        if cmd == "staff":
            embed = discord.Embed(title = "!S Staff",colour = colourr)
            embed.add_field(name = "Administrator", value = "Maui Mallard#3619", inline = True)
            embed.add_field(name = "Coder", value = "EmoDigestive#7345", inline = True)
            embed.add_field(name = "Moderator", value = "Gremuar#8888", inline = True)
            embed.add_field(name = "Moderator", value = "Psycho_Kitteh (ﾉ◕ヮ◕)ﾉ*･ﾟ✧#8525", inline = True)
            embed.add_field(name = "Moderator", value = "VendeTTa-123#1428", inline = True)
            embed.add_field(name = "Moderator", value = "Zane Truesdale#9199", inline = True)
            embed.add_field(name = "Moderator", value = "Open Position", inline = True)
            embed.add_field(name = "Moderator", value = "Open Position", inline = True)
            embed.add_field(name = "Moderator", value = "Open Position", inline = True)
            embed.add_field(name = "Moderator", value = "Open Position", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position.", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position", inline = True)
            embed.add_field(name = "Prefect", value = "Open Position", inline = True)
            embed.set_footer(text = "ONLY Prefects may apply for the position of Moderator, Prefects are Chosen on MERIT! Be good and Don't Ask!")
            await message.channel.send(embed = embed)

        #KAIBAINFO
        if cmd == "kaiba":
            embed=discord.Embed(title="Kaiba Corp. (TDOANE/YGOPRO2)", url="https://discord.gg/FTPcGg6", color=colourr)
            embed=discord.Embed(title = "***___Click HERE to accept Invitation!___***", url="https://discord.gg/FTPcGg6", description="**Attention Duelists!** You have been invited to Kaiba Corp. the Home of TDOANE & YGOPRO2... Don't worry, there's no wimps here, Only the most Premium of Duelists... Think you've got what it takes to be one of us? just click the link if you're Brave enough!",)
            embed.set_author(name="Seto Kaiba", url="https://discord.gg/FTPcGg6", icon_url="https://cdn.discordapp.com/attachments/680273056173916260/680280733314711552/unnamed.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/680273056173916260/680280202395516969/caeb3790947d1ae8391274dafb32b3aa.jpeg")
            embed.add_field(name="PvP Duels", value="Ranked, Un-Ranked, Tournaments", inline=False)
            embed.add_field(name="Puzzles", value="AI DuelBots, Endless Duel Puzzles", inline=False)
            embed.add_field(name="Great Community", value="Built in Chat UI, Forums & Discord", inline=False)
            embed.add_field(name="Customizable Themes", value="Customise all that you see and Hear!", inline=False)
            embed.set_footer(text="TDOANE-https://ygopro.org/, YGOPRO2-https://www.ygopro2.org/, Forums-http://ygopro.club/")
            await message.channel.send(embed = embed)

        #AFFILIATES
        if cmd == "affiliates":
            embed = discord.Embed(title = "!S Affiliates",colour = colourr)
            embed.add_field(name = "Duel Academy", value = "`Maui Mallard#3619`, \nhttps://discord.gg/wFuBc5S", inline = True)
            embed.add_field(name = "Kaiba Corp", value = "`Seto Kaiba#9040`, `Malcolm Merlyn#8130`, \nhttps://discord.gg/FTPcGg6, use `!S Kaiba Corp.` for an Invite.", inline = True)
            embed.add_field(name = "Open Position", value = "Contact Staff for More Info", inline = True)
            embed.set_footer(text = "If you are interested in Affilation, please contact an Admin.")    
            await message.channel.send(embed = embed)
        if cmd == "info":
            embed=discord.Embed(title="Duel Academy Open-Beta", url="https://discord.gg/CjpvExt", color=colourr)
            embed=discord.Embed(title = "***___Click HERE to accept Invitation!___***", url="https://discord.gg/wFuBc5S", description="**Attention Duelists!** You have been invited to attend Duel Academy... Don't worry, there's no long interview Process, just click the link and you'll be able to join a House and begin your adventure at Duel Academy.  We Have 4 Houses to choose from;",)
            embed.set_author(name="Maui Mallard", url="http://ygopro.club/index.php?/user/855497-maui-mallard/", icon_url="https://cdn.discordapp.com/attachments/668444703485591552/680256433643847890/maui-mallard-in-cold-shadow.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/680273056173916260/680273188034445332/duel_academy_wallpaper_by_duel_academy_dg9hrx-fullview.jpg")
            embed.add_field(name="Slifer Red", value="Head of House: Pharaoh", inline=False)
            embed.add_field(name="Ra Yellow", value="Head of House: Proffessor Satyr", inline=False)
            embed.add_field(name="Obelisk Blue", value="Head of House: Dr. Villian Crowler", inline=False)
            embed.add_field(name="Holactie White", value="Head of House: Chancellor Sheppard", inline=False)
            embed.set_footer(text="All Beta-Access members will get a Special Prize for TDOANE!  Good Luck, and we hope you enjoy yourselves.  It's Time to Duel!")
            await message.channel.send(embed = embed)



        await message.delete()
        try:
            await asyncio.sleep(3)
            await mesg.delete()
        except:
            pass
client.run('Njc4NTIwMjU5NDQyOTAwOTky.XlCQgA.qql3w65yF6d8_1CvzCoT9GsQYBI')
            
            
