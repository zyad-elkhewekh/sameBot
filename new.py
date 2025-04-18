# import os
# import asyncio
# import datetime
# from typing import List, Optional

# import discord
# from discord.ext import commands, tasks

# # Constants for image URLs
# RISING_TIDES = "https://wiki.conflictnations.com/images/thumb/c/c1/RisingTides_Frame_v2_%281%29.gif/380px-RisingTides_Frame_v2_%281%29.gif"
# WW3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9LAA9pTsrubSazo9vOP8cGzv7sMdx2WYSKA&s"
# OVERKILL = "https://wiki.conflictnations.com/images/thumb/f/fa/2020-05-30_Overkill.png/380px-2020-05-30_Overkill.png"
# CON = "https://i.ytimg.com/vi/zewB_SSL9WA/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBJRlOBTBD-fHhN3s0fDQktGLRkyA"
# FLASHPOINT = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/clans/31932263/83472e81d1f50bb516d7df4c41ce37cab04bb34b.png"
# ANTARCTICA = "https://preview.redd.it/the-making-of-antarctica-scenario-v0-2bwo8l15satd1.jpg?width=730&format=pjpg&auto=webp&s=5d50d4cbc5b3573bdba4323adc6587a589912d5a"

# class DiscordBot(commands.Bot):
#     def __init__(self):
#         intents = discord.Intents.default()
#         intents.message_content = True
#         super().__init__(command_prefix="!", intents=intents)
        
#         # State variables
#         self.match_creator_id: Optional[str] = None
#         self.description: str = ""
#         self.description1: str = ""
#         self.player: List[str] = []
#         self.player1: List[str] = []
#         self.photo: str = ""
#         self.embed_message_id: Optional[int] = None
#         self.embed_message_id1: Optional[int] = None
#         self.clist: str = ""
#         self.clist1: str = "-----------\n"
#         self.map: str = ""
        
#     async def on_ready(self):
#         print(f'Logged in as {self.user}')

#     async def on_message(self, message: discord.Message):
#         if message.author.bot:
#             return

#         if message.content.lower() == "!ava":
#             await self.reset_state()
#             await message.channel.send("Enter game description: match type and start date (Format: yyyy-MM-dd HH:mm)")
            
#             def check(m):
#                 return m.author == message.author and m.channel == message.channel
            
#             try:
#                 response = await self.wait_for('message', check=check, timeout=60.0)
#                 content = response.content
                
#                 first_space = content.find(" ")
#                 second_space = content.find(" ", first_space + 1)
                
#                 if first_space == -1 or second_space == -1:
#                     await message.channel.send("Invalid format! Please enter: `yyyy-MM-dd HH:mm description`")
#                     return
                
#                 date_time_string = content[:second_space]
#                 self.description = content[second_space + 1:]
                
#                 try:
#                     game_time = datetime.datetime.strptime(date_time_string, "%Y-%m-%d %H:%M")
#                     delay = (game_time - datetime.datetime.now()).total_seconds() * 1000  # in milliseconds
                    
#                     if delay < 0:
#                         await message.channel.send("The specified time has already passed. Please enter a future date.")
#                         return
                    
#                     await message.channel.send(f"Game scheduled for: {game_time.strftime('%Y-%m-%d %H:%M')}")
                    
#                     await asyncio.sleep(delay / 1000)
#                     await self.send_ava_embed(message.channel)
                    
#                 except ValueError:
#                     await message.channel.send("Invalid date format! Use `yyyy-MM-dd HH:mm description`")
                    
#             except asyncio.TimeoutError:
#                 await message.channel.send("You took too long to respond!")
                
#         elif message.content.lower() == "!pub":
#             await self.reset_state2()
#             self.match_creator_id = str(message.author.id)
#             await message.channel.send("Enter game description: match type and start date (Format: yyyy-MM-dd HH:mm)")
            
#             def check(m):
#                 return m.author == message.author and m.channel == message.channel
            
#             try:
#                 response = await self.wait_for('message', check=check, timeout=60.0)
#                 parts = response.content.split(" ", 2)
                
#                 if len(parts) < 2:
#                     await message.channel.send("Invalid format! Please enter: `yyyy-MM-dd HH:mm description`")
#                     return
                
#                 date_time_string = f"{parts[0]} {parts[1].split(' ')[0]}"
#                 self.description1 = parts[1][parts[1].find(" ") + 1:]
                
#                 try:
#                     game_time = datetime.datetime.strptime(date_time_string, "%Y-%m-%d %H:%M")
#                     delay = (game_time - datetime.datetime.now()).total_seconds() * 1000  # in milliseconds
                    
#                     if delay < 0:
#                         await message.channel.send("The specified time has already passed. Please enter a future date.")
#                         return
                    
#                     await message.channel.send(f"Game scheduled for: {game_time.strftime('%Y-%m-%d %H:%M')}")
                    
#                     await asyncio.sleep(delay / 1000)
#                     await self.send_game_embed(message.channel)
                    
#                 except ValueError:
#                     await message.channel.send("Invalid date format! Use `yyyy-MM-dd HH:mm`")
                    
#             except asyncio.TimeoutError:
#                 await message.channel.send("You took too long to respond!")

#     async def on_button_click(self, interaction: discord.Interaction):
#         user_id = str(interaction.user.id)
#         username = interaction.user.display_name
        
#         if interaction.custom_id == "sign-up-button":
#             if username not in self.player:
#                 self.player.append(username)
            
#             await interaction.message.edit(embed=self.create_updated_embed())
            
#             await interaction.response.send_message(
#                 f"{username}, pick a role:",
#                 view=discord.ui.View(
#                     discord.ui.Button(style=discord.ButtonStyle.primary, label="Ground", custom_id="(ground)"),
#                     discord.ui.Button(style=discord.ButtonStyle.primary, label="Air (Helis)", custom_id="(helis)"),
#                     discord.ui.Button(style=discord.ButtonStyle.primary, label="Air (SASF)", custom_id="(sasf)"),
#                     discord.ui.Button(style=discord.ButtonStyle.primary, label="Feeder", custom_id="(feeder)"),
#                 ),
#                 ephemeral=True
#             )
            
#         elif interaction.custom_id == "consider-button":
#             username1 = interaction.user.display_name
#             self.clist += f"{username1}\n"
#             await interaction.message.edit(embed=self.create_updated_embed())
            
#         elif interaction.custom_id == "turn-down-button":
#             username2 = interaction.user.display_name
#             self.player = [p for p in self.player if not p.startswith(username2)]
#             await interaction.message.edit(embed=self.create_updated_embed())
            
#         elif interaction.custom_id.startswith("(") and interaction.custom_id.endswith(")"):
#             role = interaction.custom_id
#             for i, p in enumerate(self.player):
#                 if p == username:
#                     self.player[i] = f"{username} - {role}"
#                     break
                    
#             await interaction.message.edit(embed=self.create_updated_embed())
            
#         elif interaction.custom_id == "sign-up-button1":
#             if username not in self.player1:
#                 self.player1.append(username)
                
#             await interaction.message.edit(embed=self.create_updated_game_embed())
            
#             view = discord.ui.View()
#             view.add_item(discord.ui.Button(style=discord.ButtonStyle.success, label="Sign Up", custom_id="sign-up-button1"))
#             view.add_item(discord.ui.Button(style=discord.ButtonStyle.danger, label="Forfeit", custom_id="turn-down-button1"))
#             view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Considering", custom_id="consider-button1"))
            
#             # Second row for map selection
#             view2 = discord.ui.View()
#             view2.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="WW3 4x", custom_id="ww3_4x"))
#             view2.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="WW3 1x", custom_id="ww3_1x"))
#             view2.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="WW3 Apocalypse 4x", custom_id="ww3_apocalypse_4x"))
#             view2.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Rising Tides 1x", custom_id="rising_tides_1x"))
#             view2.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Flashpoint 1x", custom_id="flashpoint_1x"))
            
#             # Third row
#             view3 = discord.ui.View()
#             view3.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Overkill 1x", custom_id="overkill_1x"))
#             view3.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Overkill 4x", custom_id="overkill_4x"))
            
#             # Combine all views
#             combined_view = discord.ui.View()
#             for item in view.children + view2.children + view3.children:
#                 combined_view.add_item(item)
                
#             await interaction.message.edit(embed=self.create_updated_game_embed(), view=combined_view)
            
#         elif interaction.custom_id == "consider-button1":
#             usernamex = interaction.user.display_name
#             self.clist1 += f"{usernamex}\n------\n"
#             await interaction.message.edit(embed=self.create_updated_game_embed())
            
#         elif interaction.custom_id == "turn-down-button1":
#             username2 = interaction.user.display_name
#             self.player1 = [p for p in self.player1 if not p.startswith(username2)]
#             await interaction.message.edit(embed=self.create_updated_game_embed())
            
#         elif interaction.custom_id.endswith("x"):
#             if user_id != self.match_creator_id:
#                 return
                
#             self.map = interaction.custom_id
            
#             if interaction.custom_id in ["ww3_1x", "ww3_4x"]:
#                 self.photo = WW3
#             elif interaction.custom_id in ["overkill_1x", "overkill_4x"]:
#                 self.photo = OVERKILL
#             elif interaction.custom_id == "rising_tides_1x":
#                 self.photo = RISING_TIDES
#             elif interaction.custom_id == "flashpoint_1x":
#                 self.photo = FLASHPOINT
                
#             await interaction.message.edit(embed=self.create_updated_game_embed())

#     def create_embed(self) -> discord.Embed:
#         embed = discord.Embed(
#             title="New AvA starting",
#             description=self.description,
#             color=discord.Color.orange(),
#             timestamp=datetime.datetime.now()
#         )
#         embed.set_footer(text="created on")
#         embed.set_image(url=ANTARCTICA)
#         embed.add_field(name="Player 1", value="ground", inline=True)
#         embed.add_field(name="Player 2", value="ground", inline=True)
#         embed.add_field(name="Player 3", value="ground", inline=True)
#         embed.add_field(name="Player 4", value="air(helis)", inline=True)
#         embed.add_field(name="Player 5", value="air(sasf)", inline=True)
#         embed.add_field(name="Player 6", value="feeder", inline=True)
#         embed.add_field(name="Player 7", value="feeder", inline=True)
#         return embed

#     def create_updated_embed(self) -> discord.Embed:
#         embed = discord.Embed(
#             title="New AvA starting",
#             description=self.description,
#             color=discord.Color.orange(),
#             timestamp=datetime.datetime.now()
#         )
#         embed.set_footer(text="created on")
#         embed.set_image(url=ANTARCTICA)
#         embed.add_field(name="Considering:", value=self.clist, inline=False)
        
#         for i, player in enumerate(self.player, start=1):
#             embed.add_field(name=f"Player {i}", value=player, inline=True)
            
#         return embed

#     def create_new_game_embed(self) -> discord.Embed:
#         embed = discord.Embed(
#             title="New pub match starting",
#             description=self.description1,
#             color=discord.Color.orange(),
#             timestamp=datetime.datetime.now()
#         )
#         embed.set_footer(text="created on")
#         embed.set_image(url=CON)
        
#         for i in range(1, 6):
#             embed.add_field(name=f"Player {i}", value="", inline=True)
            
#         return embed

#     def create_updated_game_embed(self) -> discord.Embed:
#         embed = discord.Embed(
#             title=f"New pub match starting: {self.map}",
#             description=self.description1,
#             color=discord.Color.orange(),
#             timestamp=datetime.datetime.now()
#         )
#         embed.set_footer(text="created on")
#         embed.set_image(url=self.photo)
#         embed.add_field(name="Considering:", value=self.clist1, inline=False)
        
#         for i, player in enumerate(self.player1, start=1):
#             embed.add_field(name=f"Player {i}", value=player, inline=True)
            
#         return embed

#     async def reset_state(self):
#         self.player.clear()
#         self.embed_message_id = None
#         self.clist = ""
#         self.description = ""

#     async def reset_state2(self):
#         self.player1.clear()
#         self.embed_message_id1 = None
#         self.clist1 = "-----------\n"
#         self.map = ""
#         self.description1 = ""

#     async def send_ava_embed(self, channel: discord.TextChannel):
#         embed = self.create_embed()
#         view = discord.ui.View()
#         view.add_item(discord.ui.Button(style=discord.ButtonStyle.success, label="Sign Up", custom_id="sign-up-button"))
#         view.add_item(discord.ui.Button(style=discord.ButtonStyle.danger, label="Forfeit", custom_id="turn-down-button"))
#         view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Considering", custom_id="consider-button"))
        
#         message = await channel.send(embed=embed, view=view)
#         self.embed_message_id = message.id

#     async def send_game_embed(self, channel: discord.TextChannel):
#         embed = self.create_new_game_embed()
#         view = discord.ui.View()
#         view.add_item(discord.ui.Button(style=discord.ButtonStyle.success, label="Sign Up", custom_id="sign-up-button1"))
#         view.add_item(discord.ui.Button(style=discord.ButtonStyle.danger, label="Forfeit", custom_id="turn-down-button1"))
#         view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Considering", custom_id="consider-button1"))
        
#         message = await channel.send(embed=embed, view=view)
#         self.embed_message_id1 = message.id

# if __name__ == "__main__":
#     token = os.getenv("BOT_TOKEN")
#     if not token:
#         raise ValueError("Bot token is missing! Set the BOT_TOKEN environment variable.")
        
#     bot = DiscordBot()
#     bot.run(token)





import os
import asyncio
import datetime
import sqlite3
from typing import Dict, List, Optional, Tuple

import discord
from discord.ext import commands, tasks
from discord import app_commands

# Constants for image URLs
RISING_TIDES = "https://wiki.conflictnations.com/images/thumb/c/c1/RisingTides_Frame_v2_%281%29.gif/380px-RisingTides_Frame_v2_%281%29.gif"
WW3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9LAA9pTsrubSazo9vOP8cGzv7sMdx2WYSKA&s"
OVERKILL = "https://wiki.conflictnations.com/images/thumb/f/fa/2020-05-30_Overkill.png/380px-2020-05-30_Overkill.png"
CON = "https://i.ytimg.com/vi/zewB_SSL9WA/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBJRlOBTBD-fHhN3s0fDQktGLRkyA"
FLASHPOINT = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/clans/31932263/83472e81d1f50bb516d7df4c41ce37cab04bb34b.png"
ANTARCTICA = "https://preview.redd.it/the-making-of-antarctica-scenario-v0-2bwo8l15satd1.jpg?width=730&format=pjpg&auto=webp&s=5d50d4cbc5b3573bdba4323adc6587a589912d5a"

class GameDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('games.db')
        self.create_tables()
        
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ava_games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                creator_id TEXT NOT NULL,
                game_type TEXT NOT NULL,
                map_name TEXT NOT NULL,
                game_speed TEXT NOT NULL,
                start_time TEXT NOT NULL,
                war_time TEXT NOT NULL,
                notes TEXT,
                max_ground INTEGER DEFAULT 0,
                max_air INTEGER DEFAULT 0,
                max_navy INTEGER DEFAULT 0,
                max_support INTEGER DEFAULT 0,
                current_ground INTEGER DEFAULT 0,
                current_air INTEGER DEFAULT 0,
                current_navy INTEGER DEFAULT 0,
                current_support INTEGER DEFAULT 0,
                channel_id TEXT,
                message_id TEXT,
                image_url TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pub_games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                creator_id TEXT NOT NULL,
                description TEXT NOT NULL,
                start_time TEXT NOT NULL,
                map_name TEXT,
                notes TEXT,
                channel_id TEXT,
                message_id TEXT,
                image_url TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_signups (
                game_id INTEGER NOT NULL,
                game_type TEXT NOT NULL,
                user_id TEXT NOT NULL,
                username TEXT NOT NULL,
                role TEXT NOT NULL,
                PRIMARY KEY (game_id, game_type, user_id)
            )
        ''')
        
        self.conn.commit()
    
    def add_ava_game(self, creator_id: str, map_name: str, game_speed: str, 
                    start_time: str, war_time: str, notes: str, image_url: str = ANTARCTICA) -> int:
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO ava_games (
                creator_id, game_type, map_name, game_speed, 
                start_time, war_time, notes, image_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (creator_id, "ava", map_name, game_speed, start_time, war_time, notes, image_url))
        self.conn.commit()
        return cursor.lastrowid
    
    def add_pub_game(self, creator_id: str, description: str, start_time: str, 
                    map_name: str = "", notes: str = "", image_url: str = CON) -> int:
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO pub_games (
                creator_id, description, start_time, map_name, notes, image_url
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', (creator_id, description, start_time, map_name, notes, image_url))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_game(self, game_id: int, game_type: str) -> Optional[Dict]:
        cursor = self.conn.cursor()
        if game_type == "ava":
            cursor.execute('SELECT * FROM ava_games WHERE id = ?', (game_id,))
        else:
            cursor.execute('SELECT * FROM pub_games WHERE id = ?', (game_id,))
        
        row = cursor.fetchone()
        if not row:
            return None
            
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, row))
    
    def get_upcoming_games(self, game_type: str = "ava") -> List[Dict]:
        cursor = self.conn.cursor()
        if game_type == "ava":
            cursor.execute('''
                SELECT * FROM ava_games 
                WHERE datetime(start_time) > datetime('now')
                ORDER BY datetime(start_time) ASC
            ''')
        else:
            cursor.execute('''
                SELECT * FROM pub_games 
                WHERE datetime(start_time) > datetime('now')
                ORDER BY datetime(start_time) ASC
            ''')
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def signup_user(self, game_id: int, game_type: str, user_id: str, username: str, role: str) -> bool:
        # First check if user is already signed up
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT 1 FROM game_signups 
            WHERE game_id = ? AND game_type = ? AND user_id = ?
        ''', (game_id, game_type, user_id))
        
        if cursor.fetchone():
            return False  # Already signed up
            
        # Add the signup
        cursor.execute('''
            INSERT INTO game_signups (game_id, game_type, user_id, username, role)
            VALUES (?, ?, ?, ?, ?)
        ''', (game_id, game_type, user_id, username, role))
        
        # Update the counts
        if game_type == "ava":
            cursor.execute(f'''
                UPDATE ava_games 
                SET current_{role} = current_{role} + 1
                WHERE id = ?
            ''', (game_id,))
        
        self.conn.commit()
        return True
    
    def remove_signup(self, game_id: int, game_type: str, user_id: str) -> bool:
        # First get the role to decrement the count
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT role FROM game_signups 
            WHERE game_id = ? AND game_type = ? AND user_id = ?
        ''', (game_id, game_type, user_id))
        
        result = cursor.fetchone()
        if not result:
            return False
            
        role = result[0]
        
        # Remove the signup
        cursor.execute('''
            DELETE FROM game_signups 
            WHERE game_id = ? AND game_type = ? AND user_id = ?
        ''', (game_id, game_type, user_id))
        
        # Update the counts
        if game_type == "ava":
            cursor.execute(f'''
                UPDATE ava_games 
                SET current_{role} = current_{role} - 1
                WHERE id = ?
            ''', (game_id,))
        
        self.conn.commit()
        return True
    
    def set_role_limits(self, game_id: int, game_type: str, **limits) -> bool:
        if game_type != "ava":
            return False
            
        cursor = self.conn.cursor()
        updates = []
        params = []
        
        for role, limit in limits.items():
            if role in ['ground', 'air', 'navy', 'support']:
                updates.append(f"max_{role} = ?")
                params.append(limit)
        
        if not updates:
            return False
            
        params.append(game_id)
        query = f"UPDATE ava_games SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.rowcount > 0
    
    def update_game(self, game_id: int, game_type: str, **updates) -> bool:
        cursor = self.conn.cursor()
        valid_fields = []
        params = []
        
        for field, value in updates.items():
            if field in ['map_name', 'game_speed', 'start_time', 'war_time', 'notes', 'image_url']:
                valid_fields.append(f"{field} = ?")
                params.append(value)
        
        if not valid_fields:
            return False
            
        params.append(game_id)
        if game_type == "ava":
            query = f"UPDATE ava_games SET {', '.join(valid_fields)} WHERE id = ?"
        else:
            query = f"UPDATE pub_games SET {', '.join(valid_fields)} WHERE id = ?"
        
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.rowcount > 0

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = GameDatabase()
    
    @commands.hybrid_command(name='schedule_ava', description='Schedule a new AvA game (admin only)')
    @app_commands.describe(
        map_name="The map name for the game",
        game_speed="The game speed (e.g., '1x', '4x')",
        start_time="Start time (YYYY-MM-DD HH:MM)",
        war_time="War time (YYYY-MM-DD HH:MM)",
        notes="Additional notes about the game",
        max_ground="Maximum ground players",
        max_air="Maximum air players",
        max_support="Maximum support players",
        max_navy="Maximum navy players"
    )
    @commands.has_permissions(administrator=True)
    async def schedule_ava(self, ctx: commands.Context, 
                         map_name: str,
                         game_speed: str,
                         start_time: str,
                         war_time: str,
                         notes: str = "",
                         max_ground: int = 3,
                         max_air: int = 2,
                         max_support: int = 2,
                         max_navy: int = 0):
        """Schedule a new AvA game with all details"""
        try:
            # Validate times
            start_dt = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")
            war_dt = datetime.datetime.strptime(war_time, "%Y-%m-%d %H:%M")
            
            if start_dt < datetime.datetime.now():
                await ctx.send("Start time must be in the future!")
                return
                
            if war_dt < start_dt:
                await ctx.send("War time must be after start time!")
                return
                
            # Create the game
            game_id = self.db.add_ava_game(
                creator_id=str(ctx.author.id),
                map_name=map_name,
                game_speed=game_speed,
                start_time=start_time,
                war_time=war_time,
                notes=notes
            )
            
            # Set role limits
            self.db.set_role_limits(
                game_id=game_id,
                game_type="ava",
                ground=max_ground,
                air=max_air,
                support=max_support,
                navy=max_navy
            )
            
            # Get the full game data
            game_data = self.db.get_game(game_id, "ava")
            
            # Create and send the embed
            embed = self.create_ava_embed(game_data)
            view = self.create_ava_view(game_id)
            
            message = await ctx.send(embed=embed, view=view)
            
            # Store message info in database
            self.db.update_game(
                game_id=game_id,
                game_type="ava",
                channel_id=str(ctx.channel.id),
                message_id=str(message.id)
            )
            
            await ctx.send(f"AvA game #{game_id} scheduled successfully!")
            
        except ValueError as e:
            await ctx.send(f"Invalid time format! Use YYYY-MM-DD HH:MM. Error: {e}")
    
    @commands.hybrid_command(name='set_roles', description='Set role limits for a game (admin only)')
    @app_commands.describe(
        game_id="The game ID to update",
        max_ground="Maximum ground players",
        max_air="Maximum air players",
        max_support="Maximum support players",
        max_navy="Maximum navy players"
    )
    @commands.has_permissions(administrator=True)
    async def set_roles(self, ctx: commands.Context, 
                       game_id: int,
                       max_ground: int,
                       max_air: int,
                       max_support: int,
                       max_navy: int = 0):
        """Update role limits for an existing game"""
        if not self.db.set_role_limits(
            game_id=game_id,
            game_type="ava",
            ground=max_ground,
            air=max_air,
            support=max_support,
            navy=max_navy
        ):
            await ctx.send("Failed to update role limits. Check the game ID.")
            return
            
        # Refresh the game message
        await self.refresh_game_message(game_id, "ava", ctx.channel)
        await ctx.send(f"Role limits updated for game #{game_id}")
    
    @commands.hybrid_command(name='edit_game', description='Edit a game (admin only)')
    @app_commands.describe(
        game_id="The game ID to edit",
        field="Field to edit (map_name, game_speed, start_time, war_time, notes)",
        value="New value for the field"
    )
    @commands.has_permissions(administrator=True)
    async def edit_game(self, ctx: commands.Context, 
                      game_id: int,
                      field: str,
                      value: str):
        """Edit a game's details"""
        valid_fields = ['map_name', 'game_speed', 'start_time', 'war_time', 'notes']
        if field not in valid_fields:
            await ctx.send(f"Invalid field! Choose from: {', '.join(valid_fields)}")
            return
            
        # For time fields, validate the format
        if field in ['start_time', 'war_time']:
            try:
                datetime.datetime.strptime(value, "%Y-%m-%d %H:%M")
            except ValueError:
                await ctx.send("Invalid time format! Use YYYY-MM-DD HH:MM")
                return
                
        if not self.db.update_game(
            game_id=game_id,
            game_type="ava",
            **{field: value}
        ):
            await ctx.send("Failed to update game. Check the game ID.")
            return
            
        # Refresh the game message
        await self.refresh_game_message(game_id, "ava", ctx.channel)
        await ctx.send(f"Game #{game_id} updated successfully!")
    
    @commands.hybrid_command(name='list_games', description='List all scheduled games')
    @app_commands.describe(
        game_type="Type of games to list (ava or pub)"
    )
    async def list_games(self, ctx: commands.Context, game_type: str = "ava"):
        """List all scheduled games of the specified type"""
        games = self.db.get_upcoming_games(game_type)
        
        if not games:
            await ctx.send(f"No upcoming {game_type} games scheduled.")
            return
            
        embed = discord.Embed(
            title=f"Upcoming {game_type.upper()} Games",
            color=discord.Color.blue()
        )
        
        for game in games:
            if game_type == "ava":
                value = (
                    f"**Map:** {game['map_name']}\n"
                    f"**Speed:** {game['game_speed']}\n"
                    f"**Start:** {game['start_time']}\n"
                    f"**War:** {game['war_time']}\n"
                    f"**Slots:** G({game['current_ground']}/{game['max_ground']}) "
                    f"A({game['current_air']}/{game['max_air']}) "
                    f"S({game['current_support']}/{game['max_support']})"
                    f"{f' N({game['current_navy']}/{game['max_navy']})' if game['max_navy'] > 0 else ''}\n"
                    f"**Notes:** {game['notes'] or 'None'}"
                )
            else:
                value = (
                    f"**Description:** {game['description']}\n"
                    f"**Start:** {game['start_time']}\n"
                    f"**Map:** {game['map_name'] or 'Not specified'}\n"
                    f"**Notes:** {game['notes'] or 'None'}"
                )
            
            embed.add_field(
                name=f"Game #{game['id']}",
                value=value,
                inline=False
            )
        
        await ctx.send(embed=embed)
    
    def create_ava_embed(self, game_data: Dict) -> discord.Embed:
        embed = discord.Embed(
            title=f"New AvA Game: {game_data['map_name']} ({game_data['game_speed']})",
            description=game_data['notes'],
            color=discord.Color.orange(),
            timestamp=datetime.datetime.strptime(game_data['start_time'], "%Y-%m-%d %H:%M")
        )
        
        # Add game times
        embed.add_field(
            name="Start Time",
            value=game_data['start_time'],
            inline=True
        )
        embed.add_field(
            name="War Time",
            value=game_data['war_time'],
            inline=True
        )
        
        # Add role availability
        roles = [
            ('Ground', 'ground'),
            ('Air', 'air'),
            ('Support', 'support')
        ]
        
        if game_data['max_navy'] > 0:
            roles.append(('Navy', 'navy'))
        
        for name, role in roles:
            current = game_data[f'current_{role}']
            max_ = game_data[f'max_{role}']
            status = "FULL" if current >= max_ else f"{current}/{max_}"
            
            embed.add_field(
                name=name,
                value=status,
                inline=True
            )
        
        # Set appropriate image
        image_url = game_data.get('image_url', ANTARCTICA)
        embed.set_image(url=image_url)
        
        embed.set_footer(text=f"Game ID: {game_data['id']}")
        
        return embed
    
    def create_ava_view(self, game_id: int) -> discord.ui.View:
        view = discord.ui.View()
        
        # Add role buttons if slots are available
        view.add_item(discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="Ground",
            custom_id=f"role_{game_id}_ground"
        ))
        view.add_item(discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="Air",
            custom_id=f"role_{game_id}_air"
        ))
        view.add_item(discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="Support",
            custom_id=f"role_{game_id}_support"
        ))
        
        # Navy button only if max_navy > 0
        game_data = self.db.get_game(game_id, "ava")
        if game_data and game_data['max_navy'] > 0:
            view.add_item(discord.ui.Button(
                style=discord.ButtonStyle.primary,
                label="Navy",
                custom_id=f"role_{game_id}_navy"
            ))
        
        # Add management buttons
        view.add_item(discord.ui.Button(
            style=discord.ButtonStyle.danger,
            label="Leave Game",
            custom_id=f"leave_{game_id}"
        ))
        
        return view
    
    async def refresh_game_message(self, game_id: int, game_type: str, channel: discord.TextChannel):
        game_data = self.db.get_game(game_id, game_type)
        if not game_data or not game_data.get('message_id'):
            return
            
        try:
            message = await channel.fetch_message(int(game_data['message_id']))
            embed = self.create_ava_embed(game_data) if game_type == "ava" else self.create_pub_embed(game_data)
            view = self.create_ava_view(game_id) if game_type == "ava" else self.create_pub_view(game_id)
            
            await message.edit(embed=embed, view=view)
        except discord.NotFound:
            pass

class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.db = GameDatabase()
        
    async def setup_hook(self):
        await self.add_cog(AdminCommands(self))
        
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type != discord.InteractionType.component:
            await super().on_interaction(interaction)
            return
            
        custom_id = interaction.data.get('custom_id', '')
        
        # Handle role selection
        if custom_id.startswith('role_'):
            parts = custom_id.split('_')
            if len(parts) != 3:
                return
                
            game_id = int(parts[1])
            role = parts[2]
            
            game_data = self.db.get_game(game_id, "ava")
            if not game_data:
                await interaction.response.send_message("Game not found!", ephemeral=True)
                return
                
            # Check if role is available
            current = game_data[f'current_{role}']
            max_ = game_data[f'max_{role}']
            
            if current >= max_:
                await interaction.response.send_message(
                    f"This role is already full! {current}/{max_} slots taken.",
                    ephemeral=True
                )
                return
                
            # Sign up the user
            if not self.db.signup_user(
                game_id=game_id,
                game_type="ava",
                user_id=str(interaction.user.id),
                username=interaction.user.display_name,
                role=role
            ):
                await interaction.response.send_message(
                    "You're already signed up for this game!",
                    ephemeral=True
                )
                return
                
            # Update the message
            game_data = self.db.get_game(game_id, "ava")
            embed = AdminCommands(self).create_ava_embed(game_data)
            view = AdminCommands(self).create_ava_view(game_id)
            
            await interaction.message.edit(embed=embed, view=view)
            await interaction.response.send_message(
                f"You've been signed up as {role}!",
                ephemeral=True
            )
        
        # Handle leaving game
        elif custom_id.startswith('leave_'):
            game_id = int(custom_id.split('_')[1])
            
            if not self.db.remove_signup(
                game_id=game_id,
                game_type="ava",
                user_id=str(interaction.user.id)
            ):
                await interaction.response.send_message(
                    "You weren't signed up for this game!",
                    ephemeral=True
                )
                return
                
            # Update the message
            game_data = self.db.get_game(game_id, "ava")
            embed = AdminCommands(self).create_ava_embed(game_data)
            view = AdminCommands(self).create_ava_view(game_id)
            
            await interaction.message.edit(embed=embed, view=view)
            await interaction.response.send_message(
                "You've been removed from the game.",
                ephemeral=True
            )

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Bot token is missing! Set the BOT_TOKEN environment variable.")
        
    bot = DiscordBot()
    bot.run(token)
