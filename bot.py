import discord
from discord.ext import commands
from discord import app_commands
from config import TOKEN
import random

GUILD_ID = 1431924286070718488
CHANNEL_ID = 1431926967334342811

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ------------------------------
# Motivationsnachrichten
MOTIVATIONAL_MESSAGES = [
    "Du schaffst das! 💪",
    "Gib niemals auf! 🌟",
    "Jeder Tag ist eine neue Chance! ✨",
    "Kleiner Schritt, große Wirkung! 🚀",
    "Bleib stark, du bist großartig! 🏆",
    "Träume groß und arbeite hart! 🌈",
    "Dein Einsatz zahlt sich aus! 🔥",
    "Glaube an dich selbst! 💖",
    "Jede Herausforderung ist eine Gelegenheit! 🎯",
    "Du bist stärker als du denkst! 🦁",
    "Halte durch, der Erfolg wartet! 🏅",
    "Sei die beste Version von dir! 🌟",
    "Dein Potenzial ist grenzenlos! 🚀",
    "Mach weiter so, du bist auf dem richtigen Weg! 🛤️",
    "Erfolg ist die Summe kleiner Anstrengungen! 📈",
    "Du bist einzigartig und wertvoll! 💎",
    "Lass dich von Rückschlägen nicht entmutigen! 🌪️",
    "Jeder Schritt bringt dich näher zum Ziel! 🏁",
    "Du bist auf dem Weg zu Großartigem! 🌠",
    "Bleib positiv und fokussiert! 🎯",
    "Deine harte Arbeit wird belohnt! 🏆",
    "Glaube an deine Träume! 🌌",
    "Du bist fähig zu unglaublichen Dingen! 🌟",
    "Lass dein Licht hell leuchten! ✨",
    "Du bist stärker als jede Herausforderung! 🛡️",
    "Dein Einsatz macht den Unterschied! ⚡",
    "Bleib dran, du bist fast am Ziel! 🏃‍♂️",
    "Du bist ein Champion! 🥇",
    "Jeder Tag bringt neue Möglichkeiten! 🌅",
    "Du bist auf dem richtigen Weg! 🚶‍♀️",
    "Deine Entschlossenheit ist bewundernswert! 💥",
    "Gib niemals auf, du bist fast da! 🏆",
    "Du bist ein Gewinner! 🎉",
    "Dein Mut inspiriert andere! 🦸‍♂️",
    "Bleib stark, du bist nicht allein! 🤝",
    "Du bist ein Vorbild für viele! 🌟",
    "Deine Träume sind es wert, verfolgt zu werden! 🌠",
    "Du bist fähig, Großes zu erreichen! 🚀",
    "Lass dich von nichts aufhalten! 🛡️",
    "Du bist ein Leuchtturm der Hoffnung! 🌟",
    "Deine Reise ist einzigartig! 🛤️",
    "Du bist stärker als du denkst! 🦁",
    "Dein Einsatz wird sich auszahlen! 💰",
    "Bleib positiv, du bist auf dem richtigen Weg! 🌈",
    "Du bist ein Held in deinem eigenen Abenteuer! 🦸‍♀️",
    "Deine Stärke ist bewundernswert! 💪",
    "Glaube an dich, du bist großartig! 🌟",
    "Du bist auf dem Weg zu etwas Großartigem! 🚀",
    "Deine Entschlossenheit ist inspirierend! 🔥",
    "Bleib dran, du bist fast am Ziel! 🏁",
    "Du bist ein Champion! 🥇",
    "Jeder Tag bringt neue Chancen! 🌅",
    "Du bist auf dem richtigen Pfad! 🚶‍♂️",
    "Deine harte Arbeit zahlt sich aus! 🏆",
    "Gib niemals auf, du bist fast da! 🏆",
    "Du bist ein Gewinner! 🎉",
    "Dein Mut inspiriert viele! 🦸‍♂️",
    "Bleib stark, du bist nicht allein! 🤝",
    "Du bist ein Vorbild für viele! 🌟",
    "Deine Träume sind es wert, verfolgt zu werden! 🌠",
    "Du bist fähig, Großes zu erreichen! 🚀",
    "Lass dich von nichts aufhalten! 🛡️",
    "Du bist ein Leuchtturm der Hoffnung! 🌟",
    "Deine Reise ist einzigartig! 🛤️",
    "Du bist stärker als du denkst! 🦁",
    "Dein Einsatz wird sich auszahlen! 💰",
    "Bleib positiv, du bist auf dem richtigen Weg! 🌈",
    "Du bist ein Held in deinem eigenen Abenteuer! 🦸‍♀️",
    "Deine Stärke ist bewundernswert! 💪",
    "Glaube an dich, du bist großartig! 🌟",
    "Du bist auf dem Weg zu etwas Großartigem! 🚀",
    "Deine Entschlossenheit ist inspirierend! 🔥",
    "Bleib dran, du bist fast am Ziel! 🏁",
    "Du bist ein Champion! 🥇",
    "Jeder Tag bringt neue Chancen! 🌅",
    "Du bist auf dem richtigen Pfad! 🚶‍♂️",
    "Deine harte Arbeit zahlt sich aus! 🏆",
    "Gib niemals auf, du bist fast da! 🏆",
    "Du bist ein Gewinner! 🎉",
    "Dein Mut inspiriert viele! 🦸‍♂️",
    "Bleib stark, du bist nicht allein! 🤝",
    "Du bist ein Vorbild für viele! 🌟",
    "Deine Träume sind es wert, verfolgt zu werden! 🌠",
    "Du bist fähig, Großes zu erreichen! 🚀",
    "Lass dich von nichts aufhalten! 🛡️",
    "Du bist ein Leuchtturm der Hoffnung! 🌟",
    "Deine Reise ist einzigartig! 🛤️",
    "Du bist stärker als du denkst! 🦁",
    "Dein Einsatz wird sich auszahlen! 💰",
    "Bleib positiv, du bist auf dem richtigen Weg! 🌈",
    "Du bist ein Held in deinem eigenen Abenteuer! 🦸‍♀️",
    "Deine Stärke ist bewundernswert! 💪",
    "Glaube an dich, du bist großartig! 🌟",
    "Du bist auf dem Weg zu etwas Großartigem! 🚀",
    "Deine Entschlossenheit ist inspirierend! 🔥",
    "Bleib dran, du bist fast am Ziel! 🏁",
    "Du bist ein Champion! 🥇",
    "Jeder Tag bringt neue Chancen! 🌅",
    "Du bist auf dem richtigen Pfad! 🚶‍♂️",
    "Deine harte Arbeit zahlt sich aus! 🏆",
    "Gib niemals auf, du bist fast da! 🏆",
    ]

# ------------------------------
# Schere, Stein, Papier Optionen
CHOICES = ["🪨", "📄", "✂️"]

# ------------------------------
# Spiel-Logik: Best of 5
class RPSGame:
    def __init__(self):
        self.player_score = 0
        self.bot_score = 0
        self.rounds_played = 0
        self.max_rounds = 5

    def play_round(self, player_choice: str):
        bot_choice = random.choice(CHOICES)
        result = None

        if player_choice == bot_choice:
            result = "🤝 Unentschieden!"
        elif (player_choice == "🪨" and bot_choice == "✂️") or \
             (player_choice == "📄" and bot_choice == "🪨") or \
             (player_choice == "✂️" and bot_choice == "📄"):
            result = "🎉 Du gewinnst die Runde!"
            self.player_score += 1
        else:
            result = "😈 Lumos gewinnt die Runde!"
            self.bot_score += 1

        self.rounds_played += 1
        return bot_choice, result

    def is_finished(self):
        return self.player_score == 3 or self.bot_score == 3 or self.rounds_played >= self.max_rounds

# ------------------------------
# View (Buttons)
class RPSView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.game = RPSGame()

    async def play_round_and_update(self, interaction, player_choice):
        bot_choice, result = self.game.play_round(player_choice)
        score_text = f"📊 **Punkte:** Du {self.game.player_score} – {self.game.bot_score} Lumos"

        if self.game.is_finished():
            if self.game.player_score > self.game.bot_score:
                final_text = "🏆 **Du gewinnst das Spiel!** 🎉"
            elif self.game.player_score < self.game.bot_score:
                final_text = "💀 **Lumos gewinnt das Spiel!** 😈"
            else:
                final_text = "🤝 **Unentschieden nach 5 Runden!**"

            await interaction.response.edit_message(
                content=f"Du wählst {player_choice} – Lumos wählt {bot_choice}\n{result}\n{score_text}\n\n{final_text}",
                view=None
            )
        else:
            await interaction.response.edit_message(
                content=f"Du wählst {player_choice} – Lumos wählt {bot_choice}\n{result}\n{score_text}\n\nWähle erneut ⚔️",
                view=self
            )

    @discord.ui.button(label="🪨 Stein", style=discord.ButtonStyle.primary)
    async def rock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_round_and_update(interaction, "🪨")

    @discord.ui.button(label="📄 Papier", style=discord.ButtonStyle.primary)
    async def paper(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_round_and_update(interaction, "📄")

    @discord.ui.button(label="✂️ Schere", style=discord.ButtonStyle.primary)
    async def scissors(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_round_and_update(interaction, "✂️")

# ------------------------------
# Slash Command: say
@bot.tree.command(name="say", description="Testnachricht von Lumos", guild=discord.Object(id=GUILD_ID))
async def say(interaction: discord.Interaction, text: str):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(text)
    else:
        await interaction.response.send_message("❌ Kanal nicht gefunden", ephemeral=True)

# ------------------------------
# Slash Command: motivate
@bot.tree.command(name="motivate", description="Motivationsnachricht von Lumos", guild=discord.Object(id=GUILD_ID))
async def motivate(interaction: discord.Interaction):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        message = random.choice(MOTIVATIONAL_MESSAGES)
        await channel.send(message)
    else:
        await interaction.response.send_message("❌ Kanal nicht gefunden", ephemeral=True)

# ------------------------------
# Slash Command: rps
@bot.tree.command(name="rps", description="Spiele 5 Runden Schere, Stein, Papier gegen Lumos", guild=discord.Object(id=GUILD_ID))
async def rps(interaction: discord.Interaction):
    view = RPSView()
    await interaction.response.send_message("⚔️ **Best of 5** – Wähle deine Waffe!", view=view)

# ------------------------------
# Event: Bot bereit
@bot.event
async def on_ready():
    print(f"✅ Eingeloggt als {bot.user} ({bot.user.id})")

    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Slash-Befehle synchronisiert: {[cmd.name for cmd in synced]}")
    except Exception as e:
        print(f"❌ Fehler bei der Synchronisierung: {e}")

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("✨ Lumos ist online und bereit! ✨")

bot.run(TOKEN)

