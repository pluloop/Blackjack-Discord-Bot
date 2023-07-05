# random for random.choice, discord for @bot.command(), and api_keys_list for bot_token
import random
import discord
from discord.ext import commands
from apikeys import api_keys_list

# to have prefix for command
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


# print statements to know bot is ready
@bot.event
async def on_ready():
    print("Bot Initiated.")
    print("----------------")


@bot.command()
# function for functionality of blackjack
async def blackjack(ctx):
    deck = {
        2: "<:TwoCard:1124964958925500416>", 3: "<:ThreeCard:1125567259608350750>",
        4: "<:FourCard:1125567386716737536>", 5: "<:FiveCard:1125567529956417587>", 6: "<:SixCard:1125567708478582784>",
        7: "<:SevenCard:1125567800975560724>", 8: "<:EightCard:1125567907439587479>",
        9: "<:NineCard:1125568014750863360>", 10: "<:TenCard:1125568135408390235>",
        'Q': "<:QueenCard:1125568447875666001>", 'K': "<:KingCard:1125568346981675049>",
        'J': "<:JackCard:1125568275728842823>", 'A': "<:AceCard:1124944068246515794>"
    }

    player_hand = []
    dealer_hand = []

    # function to deal card to user or dealer upon call
    def deal_card(hand):
        card = random.choice(list(deck.keys()))
        hand.append(card)

    # function to figure out the score of deck and returns score upon call
    def calculate_deck(hand):
        score = 0
        for card in hand:
            if card == 'J' or card == 'Q' or card == 'K':
                score += 10
            elif card == 'A':
                score += 1
            else:
                score += card
        return score

    # function to displays player and dealer scores as well as player and dealer cards upon call
    def create_blackjack_embed(context, score_of_player, cards_of_player, score_of_dealer, cards_of_dealer):
        embed_message = discord.Embed(color=discord.Color.og_blurple(), title="Blackjack")
        embed_message.set_author(name=context.author.name)
        embed_message.add_field(name="Player Score: " + str(score_of_player), value="", inline=True)
        embed_message.add_field(name="", value=cards_of_player, inline=False)
        embed_message.add_field(name="Dealer Score: " + str(score_of_dealer), value="", inline=True)
        embed_message.add_field(name="", value=cards_of_dealer, inline=False)
        return embed_message

    deal_card(dealer_hand)
    dealer_score = calculate_deck(dealer_hand)
    dealer_cards = deck[dealer_hand[0]]

    deal_card(player_hand)
    deal_card(player_hand)
    player_score = calculate_deck(player_hand)
    player_cards = deck[player_hand[0]] + " " + deck[player_hand[1]]

    embed = create_blackjack_embed(ctx, player_score, player_cards, dealer_score, dealer_cards)

    class MyView(discord.ui.View):
        clicked = None

        # function to disable buttons
        async def disable_all_items(self):
            for item in self.children:
                item.disabled = True
            await message.edit(view=self)

        # function to disable buttons if not clicked
        async def on_timeout(self):
            if self.clicked is None:
                await message.edit(embed=discord.Embed(color=discord.Color.og_blurple(), title="Timed out"))
                await self.disable_all_items()

        @discord.ui.button(label="Hit", style=discord.ButtonStyle.success, emoji="<:Hit:1125923390637740064>",
                           disabled=False)
        # function to simulate functionality of hit
        async def hit(self, interaction: discord.Interaction, button: discord.ui.Button):
            _ = button
            deal_card(player_hand)
            score_of_player = calculate_deck(player_hand)
            cards_of_player = " ".join(deck[card] for card in player_hand)
            embed_message = create_blackjack_embed(ctx, score_of_player, cards_of_player, dealer_score, dealer_cards)
            if score_of_player > 21:
                embed_message.add_field(name="You Lost! D:", value="", inline=False)
                await self.disable_all_items()
                await interaction.response.edit_message(embed=embed_message, view=self)
            else:
                await interaction.response.edit_message(embed=embed_message, view=self)
            self.clicked = True

        @discord.ui.button(label="Stand", style=discord.ButtonStyle.red, emoji="<:Stand:1125923235876323429>",
                           disabled=False)
        # function to simulate functionality of stand
        async def stand(self, interaction: discord.Interaction, button: discord.ui.Button):
            _ = button
            await self.disable_all_items()
            score_of_dealer = calculate_deck(dealer_hand)
            score_of_player = calculate_deck(player_hand)
            while score_of_dealer < 17:
                deal_card(dealer_hand)
                score_of_dealer = calculate_deck(dealer_hand)
            cards_of_dealer = " ".join(deck[card] for card in dealer_hand)
            cards_of_player = " ".join(deck[card] for card in player_hand)
            embed_message = create_blackjack_embed(ctx, score_of_player, cards_of_player, score_of_dealer,
                                                   cards_of_dealer)
            if score_of_dealer > 21:
                embed_message.add_field(name="You Win! :D", value="", inline=False)
                await interaction.response.edit_message(embed=embed_message, view=self)
            elif score_of_dealer > score_of_player:
                embed_message.add_field(name="You lose! :(", value="", inline=False)
                await interaction.response.edit_message(embed=embed_message, view=self)
            elif score_of_dealer < score_of_player:
                embed_message.add_field(name="You Win! :)", value="", inline=False)
                await interaction.response.edit_message(embed=embed_message, view=self)
            else:
                embed_message.add_field(name="Tie! :I", value="", inline=False)
                await interaction.response.edit_message(embed=embed_message, view=self)
            self.clicked = True

    view = MyView(timeout=8)
    message = await ctx.send(embed=embed, view=view)
    view.message = message


bot.run(api_keys_list[0])
