import random
from hearthbreaker.engine import Player, Game
from tests.agents.testing_agents import SelfSpellTestingAgent
from tests.testing_utils import StackedDeck
from tests.agents.testing_agents import PlayAndAttackAgent, OneCardPlayingAgent, CardTestingAgent, \
    HeroPowerAndCardPlayingAgent
from tests.testing_utils import generate_game_for
from hearthbreaker.cards import *
from hearthbreaker.agents.basic_agents import PredictableAgent, DoNothingAgent
from hearthbreaker.cards.minions.testsets import *

def test_Sorcerer(self):
    game = generate_game_for(Sorcerer, IronbeakOwl, OneCardPlayingAgent, OneCardPlayingAgent)

    for i in range(0, 11):
        game.play_single_turn()

    self.assertEqual(3, len(game.current_player.minions))
    self.assertEqual(5, game.current_player.minions[0].health)
    self.assertEqual(5, game.current_player.minions[0].calculate_max_health())
    self.assertEqual(5, game.current_player.minions[0].calculate_attack())
    self.assertEqual(2, game.current_player.spell_damage)

    game.play_single_turn()

    self.assertEqual(3, len(game.other_player.minions))
    self.assertEqual(5, game.other_player.minions[0].health)
    self.assertEqual(5, game.other_player.minions[0].calculate_max_health())
    self.assertEqual(5, game.other_player.minions[0].calculate_attack())
    self.assertEqual(0, game.other_player.spell_damage)


def test_Necromancer(self):
    game = generate_game_for(Necromancer, Flamestrike, OneCardPlayingAgent, OneCardPlayingAgent)
    game.players[0].hero.health = 20
    for turn in range(0, 8):
        game.play_single_turn()
    self.assertEqual(21, game.players[0].hero.health)

    game.play_single_turn()

    self.assertEqual(22, game.players[0].hero.health)
    self.assertEqual(2, len(game.players[0].minions))
    self.assertEqual(6, game.players[0].minions[0].health)
    self.assertEqual(6, game.players[0].minions[1].health)

    game.play_single_turn()
    game.play_single_turn()

    self.assertEqual(23, game.players[0].hero.health)
    self.assertEqual(3, len(game.players[0].minions))
    self.assertEqual(6, game.players[0].minions[0].health)
    self.assertEqual(6, game.players[0].minions[1].health)
    self.assertEqual(6, game.players[0].minions[2].health)

    game.play_single_turn()
    game.play_single_turn()
    # 3rd Necromancer
    self.assertEqual(24, game.players[0].hero.health)
    self.assertEqual(4, len(game.players[0].minions))
    self.assertEqual(6, game.players[0].minions[0].health)
    self.assertEqual(6, game.players[0].minions[1].health)
    self.assertEqual(6, game.players[0].minions[2].health)
    self.assertEqual(6, game.players[0].minions[3].health)

    game.play_single_turn()
    # Flamestrike
    self.assertEqual(24, game.players[0].hero.health)
    self.assertEqual(4, len(game.players[0].minions))
    self.assertEqual(2, game.players[0].minions[0].health)
    self.assertEqual(2, game.players[0].minions[1].health)
    self.assertEqual(2, game.players[0].minions[2].health)
    self.assertEqual(2, game.players[0].minions[3].health)

    game.play_single_turn()
    # 4th Necromancer
    self.assertEqual(25, game.players[0].hero.health)
    self.assertEqual(5, len(game.players[0].minions))
    self.assertEqual(6, game.players[0].minions[0].health)
    self.assertEqual(3, game.players[0].minions[1].health)
    self.assertEqual(3, game.players[0].minions[2].health)
    self.assertEqual(3, game.players[0].minions[3].health)
    self.assertEqual(3, game.players[0].minions[4].health)


def test_FireHydrant(self):
    game = generate_game_for(FireHydrant, BoulderfistOgre,
                             PlayAndAttackAgent, DoNothingAgent)

    for turn in range(0, 3):
        game.play_single_turn()

    self.assertEqual(3, game.current_player.weapon.durability)
    self.assertEqual(4, game.current_player.weapon.base_attack)
    self.assertEqual(27, game.other_player.hero.health)


def test_FreshwaterBass(self):
    game = generate_game_for(FreshwaterBass, ArgentSquire, OneCardPlayingAgent, OneCardPlayingAgent)
    for turn in range(0, 9):
        game.play_single_turn()
    self.assertEqual(2, len(game.players[0].minions))
    self.assertEqual(2, game.players[0].minions[0].calculate_attack())
    self.assertEqual(4, game.players[0].minions[0].health)
    self.assertEqual(1, game.players[0].minions[1].calculate_attack())
    self.assertEqual(3, game.players[0].minions[1].health)

    game.play_single_turn()
    game.play_single_turn()

    self.assertEqual(3, len(game.players[0].minions))
    self.assertEqual(3, game.players[0].minions[0].calculate_attack())
    self.assertEqual(5, game.players[0].minions[0].health)
    self.assertEqual(2, game.players[0].minions[1].calculate_attack())
    self.assertEqual(4, game.players[0].minions[1].health)
    self.assertEqual(1, game.players[0].minions[2].calculate_attack())
    self.assertEqual(3, game.players[0].minions[2].health)


def test_HeavenWater(self):
    game = generate_game_for(HeavenWater, SilverbackPatriarch, CardTestingAgent, OneCardPlayingAgent)
    for turn in range(0, 6):
        game.play_single_turn()
        # plays 1 Silverback Patriarch
    self.assertEqual(1, len(game.players[1].minions))
    self.assertEqual(28, game.players[0].hero.health)
    self.assertEqual(4, game.players[1].minions[0].health)
    self.assertEqual(28, game.players[1].hero.health)

    game.play_single_turn()
    # Plays Hellfire, 3 damage to all
    self.assertEqual(1, len(game.players[1].minions))
    self.assertEqual(2, game.players[1].minions[0].health)
    self.assertEqual(26, game.players[0].hero.health)
    self.assertEqual(26, game.players[1].hero.health)


def test_Sterilize(self):
    game = generate_game_for(Sterilize, StonetuskBoar, SelfSpellTestingAgent, DoNothingAgent)
    # triggers all four innervate cards the player is holding.
    game.play_single_turn()
    self.assertEqual(1, game.current_player.mana)

    for turn in range(0, 16):
        game.play_single_turn()

    # The mana should not go over 10 on turn 9 (or any other turn)
    self.assertEqual(9, game.current_player.mana)

    game.play_single_turn()
    game.play_single_turn()

    self.assertEqual(10, game.current_player.mana)


def test_FaradayCage(self):
    game = generate_game_for(BloodfenRaptor, FaradayCage, DoNothingAgent, OneCardPlayingAgent)

    raptor = BloodfenRaptor()
    raptor.summon(game.players[0], game, 0)
    # player 0 plays raptor
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(2, game.players[0].minions[0].health)
    self.assertEqual(5, len(game.players[1].hand))

    game.play_single_turn()
    game.play_single_turn()
    # mortal coils the 2hp raptor
    self.assertEqual(6, len(game.players[1].hand))
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(2, game.players[0].minions[0].health)


def test_Trigonometric(self):
    game = generate_game_for(MogushanWarden, Trigonometric, OneCardPlayingAgent, CardTestingAgent)

    for turn in range(0, 7):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertTrue(game.current_player.minions[0].taunt)
    self.assertEqual(1, game.current_player.minions[0].calculate_attack())
    self.assertEqual(7, game.current_player.minions[0].health)
    self.assertEqual("Mogu'shan Warden", game.current_player.minions[0].card.name)

    game.play_single_turn()
    self.assertEqual(1, len(game.other_player.minions))
    self.assertFalse(game.other_player.minions[0].taunt)
    self.assertEqual(1, game.other_player.minions[0].calculate_attack())
    self.assertEqual(1, game.other_player.minions[0].health)
    self.assertEqual("Sheep", game.other_player.minions[0].card.name)
    self.assertEqual(MINION_TYPE.BEAST, game.other_player.minions[0].card.minion_type)


def test_MedievalRaven(self):
    game = generate_game_for(MedievalRaven, StonetuskBoar, SelfSpellTestingAgent, DoNothingAgent)

    game.players[0].hero.health = 20

    for turn in range(5):
        game.play_single_turn()

    # Heal self
    self.assertEqual(23, game.players[0].hero.health)
    self.assertEqual(1, len(game.players[0].minions))


def test_CurlyTeddyDog(self):
    game = generate_game_for(CurlyTeddyDog, [Consecration, Silence], OneCardPlayingAgent, OneCardPlayingAgent)

    for turn in range(0, 7):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertEqual(4, game.current_player.minions[0].calculate_attack())

    game.play_single_turn()
    self.assertEqual(5, game.other_player.minions[0].calculate_attack())

    game.play_single_turn()
    self.assertEqual(2, len(game.current_player.minions))
    self.assertEqual(4, game.current_player.minions[0].calculate_attack())
    self.assertEqual(5, game.current_player.minions[1].calculate_attack())

    game.play_single_turn()
    self.assertEqual(5, game.other_player.minions[0].calculate_attack())
    self.assertEqual(6, game.other_player.minions[1].calculate_attack())


def test_FairyWand(self):
    game = generate_game_for([FairyWand, ClockworkGnome, Deathwing], DeadlyShot,
                             PlayAndAttackAgent, OneCardPlayingAgent)
    for turn in range(0, 6):
        game.play_single_turn()

    self.assertEqual(2, game.players[0].weapon.base_attack)
    self.assertEqual(28, game.players[1].hero.health)
    self.assertEqual(0, len(game.players[0].minions))

    # Plays Clockwork Gnome, buffing Wrench
    game.play_single_turn()

    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(25, game.players[1].hero.health)

    # Deadly Shot kills Clockwork Gnome, removing Wrench buff
    game.play_single_turn()
    game.play_single_turn()

    self.assertEqual(23, game.players[1].hero.health)

def test_SingularOptics(self):
    game = generate_game_for([NoviceEngineer, NoviceEngineer, GnomishInventor, GnomishInventor, SingularOptics], Wisp,
                             OneCardPlayingAgent, DoNothingAgent)
    for turn in range(0, 10):
        game.play_single_turn()

    # Plays first 4 "draw" minions
    self.assertEqual(8, len(game.players[0].hand))
    self.assertEqual(4, len(game.players[0].minions))

    game.play_single_turn()

    # Plays Echo and overflows
    self.assertEqual(10, len(game.players[0].hand))
    self.assertEqual(4, len(game.players[0].minions))
    self.assertEqual("Novice Engineer", game.players[0].hand[8].name)
    self.assertEqual("Novice Engineer", game.players[0].hand[9].name)


def test_FlyingGuard(self):
    game = generate_game_for(FlyingGuard, HeavenWater, HeroPowerAndCardPlayingAgent, OneCardPlayingAgent)

    for turn in range(11):
        game.play_single_turn()

    self.assertEqual(2, len(game.current_player.minions))
    self.assertEqual(14, game.current_player.hero.health)
    self.assertEqual(2, game.current_player.minions[0].calculate_attack())
    self.assertEqual(3, game.current_player.minions[0].calculate_max_health())
    self.assertEqual(4, game.current_player.minions[1].calculate_attack())
    self.assertEqual(4, game.current_player.minions[1].calculate_max_health())

    game.play_single_turn()
    self.assertEqual(1, len(game.other_player.minions))
    self.assertEqual(12, game.other_player.hero.health)
    self.assertEqual(2, game.other_player.minions[0].calculate_attack())
    self.assertEqual(3, game.other_player.minions[0].calculate_max_health())

    game.play_single_turn()
    self.assertEqual(2, len(game.current_player.minions))
    self.assertEqual(10, game.current_player.hero.health)
    self.assertEqual(2, game.current_player.minions[0].calculate_attack())
    self.assertEqual(3, game.current_player.minions[0].calculate_max_health())
    self.assertEqual(4, game.current_player.minions[1].calculate_attack())
    self.assertEqual(4, game.current_player.minions[1].calculate_max_health())


def test_ChickenPoultryizer(self):
    game = generate_game_for(ChickenPoultryizer, StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)

    for turn in range(5):
        game.play_single_turn()

    self.assertEqual("Chicken", game.current_player.hand[-1].name)
    self.assertEqual(1, game.current_player.hand[-1].mana)
    self.assertEqual(MINION_TYPE.BEAST, game.current_player.hand[-1].minion_type)
    self.assertEqual(6, len(game.current_player.hand))
    self.assertEqual(type(game.current_player.hand[-1].player), Player)


def test_CherryBomb(self):
    game = generate_game_for(CherryBomb, CircleOfHealing, OneCardPlayingAgent, PredictableAgent)
    for turn in range(9):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual("Cherry Bomb", game.players[0].minions[0].card.name)

    found_mine = False
    for card in game.players[1].deck.cards:
        if card.name == "Burrowing Mine":
            found_mine = True

    self.assertTrue(found_mine, "Did not find the burrowing mine in the opponent's deck")

    # Will draw multiple mines in a row
    self.assertEqual(30, game.players[1].hero.health)
    for turn in range(45):
        game.play_single_turn()
    self.assertEqual(0, game.players[1].hero.health)


def test_WanderingBird(self):
    game = generate_game_for(WanderingBird, StonetuskBoar, OneCardPlayingAgent, OneCardPlayingAgent)
    for turn in range(0, 22):
        game.play_single_turn()

    self.assertEqual(4, len(game.players[1].minions))
    self.assertEqual(26, game.players[0].hero.health)
    self.assertEqual(20, game.players[1].hero.health)

    game.play_single_turn()
    self.assertEqual(2, len(game.players[1].minions))  # 2 hits boar
    self.assertEqual(3, game.players[0].minions[0].health)
    self.assertEqual(25, game.players[0].hero.health)  # 3 hits us
    self.assertEqual(20, game.players[1].hero.health)  # 0 hits him


def test_GoldenSnitch(self):
    game = generate_game_for(GoldenSnitch, Assassinate, OneCardPlayingAgent, OneCardPlayingAgent)

    for turn in range(0, 11):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertEqual("Golden Snitch", game.current_player.minions[0].card.name)

    # The assassinate will kill the golem, and leave the other player with a 4 mana card
    game.play_single_turn()

    self.assertLessEqual(1, len(game.other_player.minions))
    self.assertEqual(3, game.other_player.minions[0].card.mana)


def test_VioletPolarizer(self):
    game = generate_game_for([LootHoarder, VioletPolarizer], [StonetuskBoar, NerubianEgg],
                             CardTestingAgent, CardTestingAgent)

    for turn in range(5):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertEqual(2, len(game.other_player.minions))

    self.assertEqual("Violet Polarizer", game.current_player.minions[0].card.name)
    self.assertEqual("Nerubian Egg", game.other_player.minions[0].card.name)
    self.assertEqual("Stonetusk Boar", game.other_player.minions[1].card.name)


def test_SkylineKeeper(self):
    game = generate_game_for([MurlocTidecaller, MurlocTidehunter, SkylineKeeper, Deathwing],
                             [MurlocTidecaller, Hellfire, BaneOfDoom], OneCardPlayingAgent, OneCardPlayingAgent)

    for turn in range(4):
        game.play_single_turn()

    self.assertEqual(3, len(game.other_player.minions))
    self.assertEqual(1, len(game.current_player.minions))

    # Play Siltfin

    game.play_single_turn()

    self.assertEqual(4, len(game.current_player.minions))
    self.assertEqual(1, len(game.other_player.minions))

    self.assertEqual(3, len(game.current_player.hand))
    self.assertEqual(6, len(game.other_player.hand))

    # Hellfire will kill all the murlocs but the siltfin.
    for turn in range(3):
        game.play_single_turn()

    self.assertEqual(0, len(game.other_player.minions))
    self.assertEqual(7, len(game.other_player.hand))
    self.assertEqual(0, len(game.current_player.minions))
    self.assertEqual(7, len(game.current_player.hand))


def test_SleepwalkingPhysician(self):
    game = generate_game_for([SleepwalkingPhysician, SpiderTank], Wisp, OneCardPlayingAgent, DoNothingAgent)

    for turn in range(0, 14):
        game.play_single_turn()

    self.assertEqual(2, len(game.players[0].minions))
    self.assertEqual("Spider Tank", game.other_player.minions[0].card.name)
    self.assertEqual(3, game.players[0].minions[0].calculate_attack())
    self.assertEqual(3, game.players[0].minions[0].calculate_attack())

    # 2nd Tinker gets buff and draws
    game.play_single_turn()

    self.assertEqual(3, len(game.players[0].minions))
    self.assertEqual("Sleepwalking Physician", game.current_player.minions[0].card.name)
    self.assertEqual("Spider Tank", game.current_player.minions[1].card.name)
    self.assertEqual("Sleepwalking Physician", game.current_player.minions[2].card.name)
    self.assertEqual(6, game.players[0].minions[0].calculate_attack())
    self.assertEqual(3, game.players[0].minions[1].calculate_attack())
    self.assertEqual(4, game.players[0].minions[2].calculate_attack())

    self.assertEqual("Rusty Horn", game.players[0].hand[-1].name)


def test_Sonata(self):
    game = generate_game_for(Sonata, ChillwindYeti, OneCardPlayingAgent, OneCardPlayingAgent)
    for turn in range(9):
        game.play_single_turn()

    self.assertEqual(3, len(game.current_player.minions))
    self.assertEqual(1, len(game.other_player.minions))
    self.assertEqual(5, game.current_player.minions[0].calculate_max_health())
    self.assertEqual(5, game.current_player.minions[0].health)
    self.assertEqual(4, game.other_player.minions[0].calculate_max_health())
    self.assertEqual(4, game.other_player.minions[0].health)


def test_MorningCall(self):
    game = generate_game_for([IronfurGrizzly, MorningCall], Deathlord,
                             PlayAndAttackAgent, OneCardPlayingAgent)

    for turn in range(0, 7):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertIsNotNone(game.current_player.weapon)
    self.assertEqual(4, game.other_player.minions[0].health)

    for turn in range(0, 4):
        game.play_single_turn()

    # The Death's Bite attacks the new Deathlord, triggering the weapon's deathrattle
    # This finishes off the other deathlord and the first friendly Grizzly
    self.assertEqual(2, len(game.other_player.minions))
    self.assertEqual(5, game.other_player.minions[0].health)
    self.assertEqual(2, len(game.current_player.minions))
    self.assertEqual(1, game.current_player.minions[0].health)
    self.assertEqual(3, game.current_player.minions[1].health)


def test_Melania(self):
    game = generate_game_for(Melania, [Melania, WarGolem, Gruul],
                             PlayAndAttackAgent, PlayAndAttackAgent)

    for turn in range(0, 9):
        game.play_single_turn()

    self.assertEqual(0, len(game.other_player.minions))
    self.assertEqual(1, len(game.current_player.minions))

    game.play_single_turn()
    game.play_single_turn()

    self.assertEqual(0, len(game.other_player.minions))
    self.assertEqual(2, len(game.current_player.minions))

    game.play_single_turn()
    game.play_single_turn()

    self.assertEqual(0, len(game.other_player.minions))
    self.assertEqual(3, len(game.current_player.minions))


def test_ScotlandCockroach(self):
    game = generate_game_for(ScotlandCockroach, Fireball, OneCardPlayingAgent, OneCardPlayingAgent)

    for turn in range(0, 9):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertTrue(game.current_player.minions[0].taunt)
    self.assertEqual(5, game.current_player.minions[0].health)

    game.play_single_turn()

    self.assertEqual(1, len(game.other_player.minions))
    self.assertTrue(game.other_player.minions[0].taunt)
    self.assertEqual(2, game.other_player.minions[0].health)


def test_Nullpointer(self):
    game = generate_game_for(Assassinate, [Nullpointer, FlameImp, ArgentSquire, BoulderfistOgre, StonetuskBoar],
                             CardTestingAgent, OneCardPlayingAgent)

    for turn in range(0, 4):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertEqual(2, game.current_player.minions[0].health)
    self.assertEqual("Nullpointer", game.current_player.minions[0].card.name)

    for turn in range(0, 3):
        game.play_single_turn()

    self.assertEqual(2, len(game.other_player.minions))
    self.assertEqual("Flame Imp", game.other_player.minions[0].card.name)


def test_Lacertidae(self):
    game = generate_game_for(Lacertidae, StonetuskBoar, SelfSpellTestingAgent, DoNothingAgent)
    for turn in range(0, 15):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(20, game.players[0].hero.health)
    self.assertEqual(30, game.players[1].hero.health)


def test_CrystalBall(self):
    game = generate_game_for(CrystalBall, StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)
    for turn in range(0, 8):
        game.play_single_turn()

    self.assertEqual(5, game.players[1].max_mana)
    self.assertEqual(1, len(game.players[0].minions))

    game.play_single_turn()

    self.assertEqual(6, game.players[1].max_mana)
    self.assertEqual(2, len(game.players[0].minions))


def test_FloppyFur(self):
    game = generate_game_for(Shieldbearer, FloppyFur, OneCardPlayingAgent, PredictableAgent)

    for turn in range(0, 11):
        game.play_single_turn()

    self.assertEqual(6, len(game.players[0].minions))
    self.assertEqual(30, game.players[0].hero.health)
    self.assertEqual(4, game.players[0].minions[0].health)
    self.assertEqual(3, game.players[0].minions[1].health)
    self.assertEqual(3, game.players[0].minions[2].health)
    self.assertEqual(3, game.players[0].minions[3].health)
    self.assertEqual(3, game.players[0].minions[4].health)
    self.assertEqual(4, game.players[0].minions[5].health)

    # An attack with our knife should first happen, and then should Blade Flurry be played, destroying our knife
    # and dealing 1 damage to all enemy minions
    game.play_single_turn()
    self.assertEqual(6, len(game.players[0].minions))
    self.assertEqual(29, game.players[0].hero.health)
    self.assertEqual(2, game.players[0].minions[0].health)
    self.assertEqual(2, game.players[0].minions[1].health)
    self.assertEqual(2, game.players[0].minions[2].health)
    self.assertEqual(2, game.players[0].minions[3].health)
    self.assertEqual(2, game.players[0].minions[4].health)
    self.assertEqual(3, game.players[0].minions[5].health)


def test_Kenka(self):
    game = generate_game_for(Kenka, StonetuskBoar, CardTestingAgent, DoNothingAgent)

    game.players[0].mana = 100

    shield = Shieldbearer()
    shield.player = game.players[0]
    shield.use(game.players[0], game)
    shield.use(game.players[0], game)
    golem = HarvestGolem()
    golem.player = game.players[0]
    golem.use(game.players[0], game)
    shield.use(game.players[1], game)
    shield.use(game.players[1], game)
    shield.use(game.players[1], game)

    for turn in range(0, 4):
        game.play_single_turn()

    self.assertEqual(3, len(game.players[0].minions))
    self.assertEqual(3, len(game.players[1].minions))

    # Brawl should be played, leaving one minion behind and Damaged Golem should have spawned for first player
    game.play_single_turn()
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual("Damaged Golem", game.players[0].minions[0].card.name)
    self.assertEqual(1, len(game.players[1].minions))


def test_Reveal(self):
    game = generate_game_for([StonetuskBoar, Reveal, MogushanWarden], StonetuskBoar, CardTestingAgent,
                             DoNothingAgent)

    for turn in range(0, 3):
        game.play_single_turn()

    # Stonetusk and Conceal should have been played
    self.assertEqual(1, len(game.players[0].minions))
    self.assertTrue(game.players[0].minions[0].stealth)

    game.play_single_turn()
    # Conceal should fade off
    game.play_single_turn()
    self.assertEqual(1, len(game.players[0].minions))
    self.assertFalse(game.players[0].minions[0].stealth)


def test_Sheepfold(self):
    game = generate_game_for(Sheepfold, StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)
    for turn in range(0, 6):
        game.play_single_turn()

    self.assertEqual(0, len(game.players[0].minions))
    self.assertEqual(6, len(game.players[0].hand))

    game.play_single_turn()
    # Plays Sheepfold, discards once
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(5, len(game.players[0].hand))


def test_CrustalMovement(self):
    game = generate_game_for(CrustalMovement, StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)

    # Earth Elemental should be played
    for turn in range(0, 11):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual("Crustal Movement", game.players[0].minions[0].card.name)
    self.assertTrue(game.players[0].minions[0].taunt)
    self.assertEqual(3, game.players[0].upcoming_overload)


def test_Retaliate(self):
    game = generate_game_for(Retaliate, StonetuskBoar, CardTestingAgent, PlayAndAttackAgent)

    for turn in range(0, 7):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.secrets))
    self.assertEqual(7, len(game.other_player.minions))

    game.play_single_turn()

    self.assertEqual(0, len(game.other_player.secrets))
    self.assertEqual(0, len(game.current_player.minions))
    self.assertEqual(27, game.current_player.hero.health)
    self.assertEqual(19, game.other_player.hero.health)

    random.seed(1857)
    game = generate_game_for(ExplosiveTrap, Frostbolt, CardTestingAgent, CardTestingAgent)

    for turn in range(0, 4):
        game.play_single_turn()

    self.assertEqual(1, len(game.other_player.secrets))
    self.assertEqual(30, game.current_player.hero.health)
    self.assertEqual(27, game.other_player.hero.health)


def test_StarLight(self):
    game = generate_game_for(StonetuskBoar, StarLight, DoNothingAgent, CardTestingAgent)

    for turn in range(0, 11):
        game.play_single_turn()

    self.assertEqual(30, game.players[0].hero.health)
    game.play_single_turn()
    # Star Light should be played that will draw Holy Wrath that costs 6 mana, thus dealing 6 damage
    self.assertEqual(24, game.players[0].hero.health)


def test_InfinitoDeLaufraut(self):
    game = generate_game_for([InfinitoDeLaufraut, Vaporize, Spellbender], StonetuskBoar,
                             CardTestingAgent, DoNothingAgent)
    for turn in range(0, 7):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.secrets))
    self.assertEqual("Vaporize", game.current_player.secrets[0].name)
    self.assertEqual(1, len(game.current_player.minions))
    self.assertEqual("Infinito De Laufraut", game.current_player.minions[0].card.name)
    self.assertEqual(3, game.current_player.hand[0].mana_cost())
    self.assertEqual("Spellbender", game.current_player.hand[0].name)

    random.seed(1857)
    game = generate_game_for([KirinTorMage, Vaporize], StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)
    for turn in range(0, 5):
        game.play_single_turn()

    self.assertEqual(0, len(game.current_player.secrets))
    self.assertEqual(1, len(game.current_player.minions))
    self.assertEqual("Kirin Tor Mage", game.current_player.minions[0].card.name)
    self.assertEqual(3, game.current_player.hand[2].mana_cost())
    self.assertEqual("Vaporize", game.current_player.hand[2].name)


def test_DarkKnight(self):
    game = generate_game_for([DarkKnight, MindControl],
                             [StonetuskBoar, BoulderfistOgre, BoulderfistOgre, BoulderfistOgre, BoulderfistOgre],
                             PredictableAgent, PredictableAgent)

    for turn in range(0, 6):
        game.play_single_turn()

    self.assertEqual(1, game.players[0].minions[0].calculate_attack())
    self.assertEqual(1, game.players[0].minions[0].health)

    game.play_single_turn()  # Heal Lightwarden

    self.assertEqual(2, game.players[0].minions[0].calculate_attack())
    self.assertEqual(2, game.players[0].minions[0].health)

    game.players[0].hero.health = 28
    game.players[0].hero.heal(2, None)

    self.assertEqual(3, game.players[0].minions[0].calculate_attack())


def test_MoonlightDemon(self):
    game = generate_game_for([MoonlightDemon, Silence], StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)
    for turn in range(0, 4):
        game.play_single_turn()

    self.assertEqual(0, game.players[0].hand[0].mana_cost())
    self.assertEqual(3, game.players[0].hand[1].mana_cost())
    self.assertEqual(2, game.players[1].hand[0].mana_cost())

    game.play_single_turn()

    self.assertEqual(2, game.players[0].hand[0].mana_cost())
    self.assertEqual(0, game.players[0].hand[1].mana_cost())
    self.assertEqual(1, game.players[1].hand[0].mana_cost())


def test_Manifestation(self):
    game = generate_game_for(Manifestation, StonetuskBoar, CardTestingAgent, PlayAndAttackAgent)

    for turn in range(0, 4):
        game.play_single_turn()

    self.assertEqual(28, game.other_player.hero.health)
    self.assertEqual(1, len(game.current_player.minions))  # The boar has been misdirected into another boar
    self.assertEqual(30, game.current_player.hero.health)


def test_CubicRoom(self):
    game = generate_game_for(CubicRoom, StonetuskBoar, CardTestingAgent, PlayAndAttackAgent)

    game.play_single_turn()  # NobleSacrifice should be played
    self.assertEqual(1, len(game.players[0].secrets))
    self.assertEqual("Cubic Room", game.players[0].secrets[0].name)

    game.play_single_turn()
    # Attack with Stonetusk should happen, and the secret should trigger. Both minions should die.
    self.assertEqual(0, len(game.players[0].secrets))
    self.assertEqual(0, len(game.players[0].minions))
    self.assertEqual(0, len(game.players[1].minions))
    self.assertEqual(30, game.players[0].hero.health)

    # Test with 7 minions
    game = playback(Replay("tests/replays/card_tests/NobleSacrifice.hsreplay"))
    game.start()
    self.assertEqual(7, len(game.players[0].minions))
    self.assertEqual(29, game.players[0].hero.health)
    self.assertEqual(1, len(game.players[0].secrets))
    self.assertEqual("Cubic Room", game.players[0].secrets[0].name)


def test_VoiceOfTheLand(self):
    deck1 = StackedDeck([StonetuskBoar(), StonetuskBoar(), VoiceOfTheLand()], CHARACTER_CLASS.DRUID)
    deck2 = StackedDeck([StonetuskBoar()], CHARACTER_CLASS.MAGE)

    # This is a test of the +1/+1 option of the Power Of the Wild Card
    game = Game([deck1, deck2], [OneCardPlayingAgent(), OneCardPlayingAgent()])
    game.current_player = game.players[1]

    game.play_single_turn()
    game.play_single_turn()
    game.play_single_turn()
    game.play_single_turn()
    game.play_single_turn()
    self.assertEqual(2, game.current_player.minions[0].calculate_attack())
    self.assertEqual(2, game.current_player.minions[0].health)
    self.assertEqual(2, game.current_player.minions[0].calculate_max_health())
    self.assertEqual(2, game.current_player.minions[1].calculate_attack())
    self.assertEqual(2, game.current_player.minions[1].calculate_max_health())

    # This is a test of the "Summon Panther" option of the Power of the Wild Card

    agent = OneCardPlayingAgent()
    agent.choose_option = lambda options, player: options[1]

    deck1 = StackedDeck([StonetuskBoar(), StonetuskBoar(), PowerOfTheWild()], CHARACTER_CLASS.DRUID)
    deck2 = StackedDeck([StonetuskBoar()], CHARACTER_CLASS.MAGE)
    game = Game([deck1, deck2], [agent, OneCardPlayingAgent()])
    game.current_player = game.players[1]

    game.play_single_turn()
    game.play_single_turn()
    game.play_single_turn()
    game.play_single_turn()
    game.play_single_turn()
    game.play_single_turn()

    self.assertEqual("Panther", game.current_player.minions[2].card.__class__.__name__)
    self.assertEqual(3, game.current_player.minions[2].calculate_attack())
    self.assertEqual(2, game.current_player.minions[2].calculate_max_health())


def test_Detention(self):
    game = generate_game_for([Detention, SilvermoonGuardian], WarGolem, CardTestingAgent, PredictableAgent)

    # Redemption and Silvermoon Guardian should be played
    for turn in range(0, 7):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].secrets))
    self.assertEqual("Detention", game.players[0].secrets[0].name)
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(3, game.players[0].minions[0].calculate_max_health())
    self.assertEqual(3, game.players[0].minions[0].health)
    self.assertTrue(game.players[0].minions[0].divine_shield)

    # Mage hero power should have been used
    for turn in range(0, 6):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].secrets))
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(3, game.players[0].minions[0].calculate_max_health())
    self.assertEqual(1, game.players[0].minions[0].health)
    self.assertFalse(game.players[0].minions[0].divine_shield)

    game.play_single_turn()
    # Silvermoon Guardian should be killed by the mage hero power, that will trigger the secret
    self.assertEqual(0, len(game.players[0].secrets))
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(3, game.players[0].minions[0].calculate_max_health())
    self.assertEqual(2, game.players[0].minions[0].health)
    self.assertTrue(game.players[0].minions[0].divine_shield)


def test_CornerCreature(self):
    game = generate_game_for([MagmaRager, MogushanWarden, WarGolem],
                             [CornerCreature, CornerCreature, Silence], OneCardPlayingAgent,
                             PlayAndAttackAgent)

    # Magma Rager should be played
    for turn in range(0, 5):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual("Magma Rager", game.players[0].minions[0].card.name)
    self.assertEqual(7, len(game.players[1].hand))

    # Shadow Madness shouldn't be played, since Magma Rager has attack > 3
    game.play_single_turn()
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(8, len(game.players[1].hand))

    # Mogu'shan Warden should be played
    game.play_single_turn()
    self.assertEqual(2, len(game.players[0].minions))
    self.assertEqual("Mogu'shan Warden", game.players[0].minions[0].card.name)

    # Shadow Madness should be played, targeting the Mogu'shan that will attack the Magma.
    # Results in killing the Magma, and Mogu'shan takes 5 damage before being returned to the owner.
    game.play_single_turn()
    self.assertEqual(0, len(game.players[1].minions))
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual("Mogu'shan Warden", game.players[0].minions[0].card.name)
    self.assertEqual(2, game.players[0].minions[0].health)

    # Nothing should happen, no mana for War Golem
    game.play_single_turn()

    # Shadow Madness should be played again targeting the damaged Mogu'shan. Silence should follow after, that
    # target the "mind controlled" Mogu'shan, immediately causing it to switch to our side, before it can attack.
    game.play_single_turn()
    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(0, len(game.players[1].minions))
    self.assertEqual("Mogu'shan Warden", game.players[0].minions[0].card.name)
    self.assertEqual(2, game.players[0].minions[0].health)
    self.assertEqual(30, game.players[0].hero.health)


def test_LucratiousDeal(self):
    game = generate_game_for(MindBlast, LucratiousDeal, OneCardPlayingAgent, CardTestingAgent)
    for turn in range(0, 11):
        game.play_single_turn()
        # Uses Mindblast for 5 turns
    self.assertEqual(5, game.players[1].hero.health)
    boar = StonetuskBoar()
    boar.summon(game.players[0], game, 0)

    game.play_single_turn()
    # Siphon Soul on the Boar
    self.assertEqual(10, game.players[1].hero.health)


def test_Troublemaker(self):
    game = generate_game_for([Troublemaker, Wisp], Moonfire, CardTestingAgent, CardTestingAgent)

    for turn in range(0, 8):
        game.play_single_turn()

    # The moonfire should have been re-directed to the Spellbender, which should have taken one damage
    self.assertEqual(2, len(game.other_player.minions))
    self.assertEqual(3, game.other_player.minions[1].health)
    self.assertEqual(2, game.other_player.minions[1].calculate_attack())
    self.assertEqual("Troublemaker", game.other_player.minions[1].card.name)

    # Now make sure it won't work when the hero is targeted
    random.seed(1857)
    game = generate_game_for(Troublemaker, Moonfire, CardTestingAgent, CardTestingAgent)

    for turn in range(0, 8):
        game.play_single_turn()

    self.assertEqual(0, len(game.other_player.minions))
    self.assertEqual(1, len(game.other_player.secrets))
    self.assertEqual(22, game.other_player.hero.health)

    # Now make sure it doesn't activate when a non-targeted spell is used
    random.seed(1857)
    game = generate_game_for(Troublemaker, ArcaneIntellect, CardTestingAgent, CardTestingAgent)

    for turn in range(0, 8):
        game.play_single_turn()

    # The arcane intellect should not have caused the Spellbender to activate
    self.assertEqual(0, len(game.other_player.minions))
    self.assertEqual(1, len(game.other_player.secrets))


def test_ActionPeguintial(self):
    game = generate_game_for([ActionPeguintial, Wisp], StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)
    for turn in range(0, 5):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual('Wisp', game.players[0].hand[0].name)
    self.assertEqual(0, game.players[0].hand[0].mana_cost())


def test_Sublimate(self):
    game = generate_game_for(Sublimate, StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)

    for turn in range(0, 4):
        game.play_single_turn()

    self.assertEqual(1, game.players[0].weapon.base_attack)
    self.assertEqual(3, game.players[0].weapon.durability)

    game.play_single_turn()

    self.assertEqual(4, game.players[0].weapon.base_attack)
    self.assertEqual(4, game.players[0].weapon.durability)


def test_Castellan(self):
    game = generate_game_for([Castellan, IronbeakOwl], Moonfire, OneCardPlayingAgent, CardTestingAgent)
    game.players[0].max_mana = 3

    for turn in range(3):
        game.play_single_turn()

    self.assertEqual(1, len(game.current_player.minions))
    self.assertEqual(4, game.current_player.minions[0].health)
    self.assertEqual(4, game.current_player.minions[0].calculate_max_health())
    self.assertEqual(2, game.current_player.minions[0].calculate_attack())

    game.play_single_turn()
    self.assertEqual(1, len(game.other_player.minions))
    self.assertEqual(5, game.other_player.minions[0].health)
    self.assertEqual(6, game.other_player.minions[0].calculate_max_health())
    self.assertEqual(3, game.other_player.minions[0].calculate_attack())

    game.play_single_turn()
    self.assertEqual(2, len(game.current_player.minions))
    self.assertEqual(4, game.current_player.minions[1].health)
    self.assertEqual(4, game.current_player.minions[1].calculate_max_health())
    self.assertEqual(2, game.current_player.minions[1].calculate_attack())


def test_AngryBird(self):
    game = generate_game_for(AngryBird, StonetuskBoar, OneCardPlayingAgent, DoNothingAgent)

    for turn in range(5):
        game.play_single_turn()

    self.assertEqual(1, len(game.players[0].minions))
    self.assertEqual(1, len(game.players[1].minions))
    self.assertEqual(3, game.players[1].minions[0].card.mana)


def test_WutheringHills(self):
    game = generate_game_for(Wisp, [Consecration, WutheringHills], CardTestingAgent, CardTestingAgent)
    for turn in range(7):
        game.play_single_turn()

    self.assertEqual(7, len(game.players[0].minions))
    self.assertEqual(8, len(game.players[1].hand))

    game.play_single_turn()

    self.assertEqual(0, len(game.players[0].minions))
    self.assertEqual(10, len(game.players[1].hand))
