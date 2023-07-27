from hearthbreaker.cards.base import SecretCard
from hearthbreaker.cards.minions.neutral import *
from hearthbreaker.cards.spells.druid import LeaderOfThePack, SummonPanther
from hearthbreaker.game_objects import Hero
from hearthbreaker.tags.action import Heal, Summon, Draw, \
    Kill, Damage, ResurrectFriendly, Steal, Duplicate, Give, SwapWithHand, AddCard, Transform, ApplySecret, \
    Silence, Bounce, GiveManaCrystal, Equip, GiveAura, Replace, SetHealth, ChangeTarget, Discard, \
    RemoveDivineShields, DecreaseDurability, IncreaseDurability, IncreaseWeaponAttack, Destroy, GiveEffect, SwapStats, \
    Joust, RemoveFromDeck, RemoveSecret
from hearthbreaker.tags.base import Effect, Deathrattle, Battlecry, Aura, BuffUntil, Buff, AuraUntil, ActionTag
from hearthbreaker.tags.card_source import CardList, LastCard, DeckSource, Same, CollectionSource
from hearthbreaker.tags.condition import Adjacent, IsType, MinionHasDeathrattle, IsMinion, IsSecret, \
    MinionIsTarget, IsSpell, IsDamaged, InGraveyard, ManaCost, OpponentMinionCountIsGreaterThan, AttackGreaterThan, \
    IsWeapon, HasStatus, AttackLessThanOrEqualTo, OneIn, NotCurrentTarget, HasDivineShield, HasSecret, \
    BaseAttackEqualTo, GreaterThan, And, TargetAdjacent, Matches, HasBattlecry, Not, IsRarity, MinionIsNotTarget, \
    IsClass
from hearthbreaker.tags.event import TurnEnded, CardPlayed, MinionSummoned, TurnStarted, DidDamage, AfterAdded, \
    SpellCast, CharacterHealed, CharacterDamaged, MinionDied, CardUsed, Damaged, Attack, CharacterAttack, \
    MinionPlaced, CardDrawn, SpellTargeted, UsedPower
from hearthbreaker.tags.selector import MinionSelector, BothPlayer, SelfSelector, \
    PlayerSelector, TargetSelector, EnemyPlayer, CharacterSelector, WeaponSelector, \
    HeroSelector, OtherPlayer, UserPicker, RandomPicker, CurrentPlayer, Count, Attribute, CardSelector, \
    Difference, LastDrawnSelector, RandomAmount, DeadMinionSelector, FriendlyPlayer
from hearthbreaker.tags.status import ChangeAttack, ChangeHealth, Charge, Taunt, Windfury, CantAttack, \
    SpellDamage, DoubleDeathrattle, Frozen, ManaChange, DivineShield, MegaWindfury, CanAttack, Stealth
import hearthbreaker.targeting
import copy
from hearthbreaker.tags.base import Deathrattle, Effect, ActionTag, BuffUntil
from hearthbreaker.tags.action import Summon, Kill, Damage, Discard, DestroyManaCrystal, Give, Equip, \
    Remove, Heal, ReplaceHeroWithMinion
from hearthbreaker.tags.base import Effect, Aura, Deathrattle, Battlecry, Buff, ActionTag
from hearthbreaker.tags.card_source import HandSource
from hearthbreaker.tags.condition import IsType, MinionCountIs, Not, OwnersTurn, IsHero, And, Adjacent, IsMinion
from hearthbreaker.tags.event import TurnEnded, CharacterDamaged, DidDamage, Damaged
from hearthbreaker.tags.selector import MinionSelector, PlayerSelector, \
    SelfSelector, BothPlayer, HeroSelector, CharacterSelector, RandomPicker, Attribute, EventValue, CardSelector, \
    FriendlyPlayer
from hearthbreaker.tags.status import ChangeHealth, ManaChange, ChangeAttack, Immune
from hearthbreaker.cards.base import MinionCard, WeaponCard
from hearthbreaker.cards.spells.warrior import BurrowingMine
from hearthbreaker.game_objects import Weapon, Minion
from hearthbreaker.tags.action import IncreaseArmor, Damage, Give, Equip, AddCard
from hearthbreaker.tags.base import Effect, Battlecry, Buff, Aura, ActionTag
from hearthbreaker.tags.condition import AttackLessThanOrEqualTo, IsMinion, IsType, GreaterThan
from hearthbreaker.tags.event import MinionPlaced, CharacterDamaged, ArmorIncreased, Damaged
from hearthbreaker.tags.selector import BothPlayer, SelfSelector, TargetSelector, HeroSelector, MinionSelector, \
    PlayerSelector, EnemyPlayer, UserPicker, Count, CardSelector
from hearthbreaker.constants import CHARACTER_CLASS, CARD_RARITY, MINION_TYPE
from hearthbreaker.tags.status import ChangeAttack, Charge, ChangeHealth




# "Sorcerer NAME_END 5 ATK_END 5 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Spell Damage +2</b>"
class Sorcerer(MinionCard):
    def __init__(self):
        super().__init__("Sorcerer", 4, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(5, 5, spell_damage=2)

# "Misty Lake Butterfly NAME_END 3 ATK_END 5 DEF_END 7 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Taunt</b>"
class MistyLakeButterfly(MinionCard):
    def __init__(self):
        super().__init__("Misty Lake Butterfly", 7, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(3, 5, taunt=True)

# "Necromancer NAME_END 5 ATK_END 6 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Battlecry:</b> Restore 1 Health to all friendly characters."
class Necromancer(MinionCard):
    def __init__(self):
        super().__init__("Necromancer", 4, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON,
                         battlecry=Battlecry(Heal(1), CharacterSelector()))

    def create_minion(self, player):
        return Minion(5, 6)

# "Fire Hydrant NAME_END 4 ATK_END -1 DEF_END 3 COST_END 3 DUR_END Weapon TYPE_END Warrior PLAYER_CLS_END NIL RACE_END Free RARITY_END NIL"
class FireHydrant(WeaponCard):
    def __init__(self):
        super().__init__("Fire Hydrant", 3, CHARACTER_CLASS.WARRIOR, CARD_RARITY.FREE)

    def create_weapon(self, player):
        return Weapon(4, 3)

# "Freshwater Bass NAME_END 1 ATK_END 3 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Battlecry:</b> Gain +1/+1 for each other friendly minion on the battlefield."
class FreshwaterBass(MinionCard):
    def __init__(self):
        super().__init__("FreshwaterBass", 4, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON,
                         battlecry=Battlecry(Give([Buff(ChangeAttack(Count(MinionSelector()))),
                                                   Buff(ChangeHealth(Count(MinionSelector())))]),
                                             SelfSelector()))

    def create_minion(self, player):
        return Minion(1, 3)

# "Hellfire NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Warlock PLAYER_CLS_END NIL RACE_END Free RARITY_END Deal $2 damage to ALL characters."
class HeavenWater(SpellCard):
    def __init__(self):
        super().__init__("HeavenWater", 3, CHARACTER_CLASS.WARLOCK, CARD_RARITY.FREE)

    def use(self, player, game):
        super().use(player, game)
        targets = copy.copy(game.other_player.minions)
        targets.extend(game.current_player.minions)
        targets.append(game.other_player.hero)
        targets.append(game.current_player.hero)
        for minion in targets:
            minion.damage(player.effective_spell_damage(2), self)

# "Sterilize NAME_END -1 ATK_END -1 DEF_END 1 COST_END -1 DUR_END Spell TYPE_END Druid PLAYER_CLS_END NIL RACE_END Free RARITY_END Gain 1 Mana Crystals this turn only."
class Sterilize(SpellCard):
    def __init__(self):
        super().__init__("Sterilize", 1, CHARACTER_CLASS.DRUID, CARD_RARITY.FREE)

    def use(self, player, game):
        super().use(player, game)
        if player.mana < 9:
            player.mana += 1
        else:
            player.mana = 10

# "Fire Vampire NAME_END 2 ATK_END 6 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Free RARITY_END NIL"
class FireVampire(MinionCard):
    def __init__(self):
        super().__init__("Fire Vampire", 4, CHARACTER_CLASS.ALL, CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(2, 6)

# "Faraday Cage NAME_END -1 ATK_END -1 DEF_END 2 COST_END -1 DUR_END Spell TYPE_END Warlock PLAYER_CLS_END NIL RACE_END Common RARITY_END Deal $2 damage to a minion. If that kills it, draw a card."
class FaradayCage(SpellCard):
    def __init__(self):
        super().__init__("Faraday Cage", 2, CHARACTER_CLASS.WARLOCK, CARD_RARITY.COMMON,
                         target_func=hearthbreaker.targeting.find_minion_spell_target)

    def use(self, player, game):
        super().use(player, game)
        if self.target.health <= player.effective_spell_damage(2) and not self.target.divine_shield:
            self.target.damage(player.effective_spell_damage(2), self)
            player.draw()
        else:
            self.target.damage(player.effective_spell_damage(2), self)
            # not sure how necessary this is, making sure damage before
            # draw but need to compare health before dealing damage

# "Trigonometric NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Mage PLAYER_CLS_END NIL RACE_END Free RARITY_END Transform a minion into a 1/1 Sheep."
class Trigonometric(SpellCard):
    def __init__(self):
        super().__init__("Trigonometric", 3, CHARACTER_CLASS.MAGE, CARD_RARITY.FREE,
                         target_func=hearthbreaker.targeting.find_minion_spell_target)

    def use(self, player, game):
        super().use(player, game)
        from hearthbreaker.cards.minions.mage import Sheep
        sheep = Sheep()
        minion = sheep.create_minion(None)
        minion.card = sheep
        self.target.replace(minion)

# "Blazing Scarecrow NAME_END 2 ATK_END 3 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Shaman PLAYER_CLS_END Totem RACE_END Free RARITY_END NIL"
class BlazingScarecrow(MinionCard):
    def __init__(self):
        super().__init__("Blazing Scarecrow", 4, CHARACTER_CLASS.SHAMAN, CARD_RARITY.FREE, False, MINION_TYPE.TOTEM)

    def create_minion(self, player):
        return Minion(2, 3)

# "Black Sheepherder NAME_END 3 ATK_END 5 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Beast RACE_END Common RARITY_END <b>Taunt</b>"
class BlackSheepherder(MinionCard):
    def __init__(self):
        super().__init__("Black Sheepherder", 4, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON,
                         minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(3, 5, taunt=True)

# "Shadow Warrior NAME_END 1 ATK_END 3 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Charge</b>"
class ShadowWarrior(MinionCard):
    def __init__(self):
        super().__init__("Shadow Warrior", 3, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(1, 3, charge=True)

# "Medieval Raven NAME_END 1 ATK_END 3 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Free RARITY_END <b>Battlecry:</b> Restore 3 Health."
class MedievalRaven(MinionCard):
    def __init__(self):
        super().__init__("Medieval Raven", 3, CHARACTER_CLASS.ALL, CARD_RARITY.FREE,
                         battlecry=Battlecry(Heal(3), CharacterSelector(players=BothPlayer(), picker=UserPicker())))

    def create_minion(self, player):
        return Minion(1, 3)

# "Meek In The Rain NAME_END 1 ATK_END 1 DEF_END 2 COST_END -1 DUR_END Minion TYPE_END Shaman PLAYER_CLS_END Totem RACE_END Free RARITY_END <b>Spell Damage +2</b>"
class MeekInTheRain(MinionCard):
    def __init__(self):
        super().__init__("Meek In The Rain", 2, CHARACTER_CLASS.SHAMAN, CARD_RARITY.FREE, False, MINION_TYPE.TOTEM)

    def create_minion(self, player):
        return Minion(1, 1, spell_damage=2)

# "Meteor Shower NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Druid PLAYER_CLS_END NIL RACE_END Epic RARITY_END Gain 12 Mana Crystals. Discard your hand."
class MeteorShower(SpellCard):
    def __init__(self):
        super().__init__("Meteor Shower", 3, CHARACTER_CLASS.DRUID, CARD_RARITY.EPIC)

    def use(self, player, game):
        super().use(player, game)
        for card in player.hand:
            card.unattach()
            player.trigger("card_discarded", card)
        player.hand = []
        player.max_mana = 12
        player.mana = 12

# "Onion Head NAME_END 3 ATK_END 4 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Mech RACE_END Common RARITY_END <b>Taunt</b> NL <b>Divine Shield</b>"
class OnionHead(MinionCard):
    def __init__(self):
        super().__init__("Onion Head", 3, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON, minion_type=MINION_TYPE.MECH)

    def create_minion(self, player):
        return Minion(3, 4, divine_shield=True, taunt=True)

# "Curly Teddy Dog NAME_END 4 ATK_END 3 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END Whenever your opponent casts a spell, gain +1 Attack."
class CurlyTeddyDog(MinionCard):
    def __init__(self):
        super().__init__("Curly Teddy Dog", 3, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(4, 3, effects=[Effect(SpellCast(player=EnemyPlayer()), ActionTag(Give(ChangeAttack(1)),
                                                                                       SelfSelector()))])

# "Fairy Wand NAME_END 2 ATK_END -1 DEF_END 3 COST_END 4 DUR_END Weapon TYPE_END Rogue PLAYER_CLS_END NIL RACE_END Epic RARITY_END Has +1 Attack while you have a Mech."
class FairyWand(WeaponCard):
    def __init__(self):
        super().__init__("Fairy Wand", 3, CHARACTER_CLASS.ROGUE, CARD_RARITY.EPIC)

    def create_weapon(self, player):
        return Weapon(2, 4, buffs=[Buff(ChangeAttack(1), GreaterThan(Count(MinionSelector(IsType(MINION_TYPE.MECH))),
                                                                     value=0))])

# "Singular Optics NAME_END -1 ATK_END -1 DEF_END 2 COST_END -1 DUR_END Spell TYPE_END Mage PLAYER_CLS_END NIL RACE_END Epic RARITY_END Put a copy of each friendly minion into your hand."
class SingularOptics(SpellCard):
    def __init__(self):
        super().__init__("Singular Optics", 2, CHARACTER_CLASS.MAGE, CARD_RARITY.EPIC)

    def use(self, player, game):
        super().use(player, game)
        for minion in sorted(copy.copy(player.minions), key=lambda minion: minion.born):
            if len(player.hand) < 10:
                player.hand.append(minion.card)

# "Flying Guard NAME_END 2 ATK_END 2 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Warlock PLAYER_CLS_END Demon RACE_END Common RARITY_END Whenever your hero takes damage on your turn, gain +2/+1."
class FlyingGuard(MinionCard):
    def __init__(self):
        super().__init__("Flying Guard", 3, CHARACTER_CLASS.WARLOCK, CARD_RARITY.COMMON,
                         minion_type=MINION_TYPE.DEMON)

    def create_minion(self, player):
        return Minion(2, 3, effects=[Effect(CharacterDamaged(And(IsHero(), OwnersTurn())),
                                            ActionTag(Give([Buff(ChangeAttack(2)), Buff(ChangeHealth(1))]),
                                            SelfSelector()))])

# "Chicken Poultryizer NAME_END 2 ATK_END 3 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Rare RARITY_END <b>Battlecry:</b> Draw a card. If it's a minion, transform it into a Chicken."
class ChickenPoultryizer(MinionCard):
    def __init__(self):
        super().__init__("Chicken Poultryizer", 4, CHARACTER_CLASS.ALL, CARD_RARITY.RARE,
                         battlecry=(Battlecry(Draw(), PlayerSelector()), Battlecry(Transform(GnomishChicken()),
                                                                                   LastDrawnSelector(),
                                                                                   Matches(LastDrawnSelector(),
                                                                                           IsMinion()))))

    def create_minion(self, player):
        return Minion(2, 3)

# "Cherry Bomb NAME_END 4 ATK_END 6 DEF_END 5 COST_END -1 DUR_END Minion TYPE_END Warrior PLAYER_CLS_END Mech RACE_END Legendary RARITY_END <b>Battlecry:</b> Shuffle a Mine into your opponent's deck. When drawn, it explodes for 10 damage."
class CherryBomb(MinionCard):
    def __init__(self):
        super().__init__("Cherry Bomb", 5, CHARACTER_CLASS.WARRIOR, CARD_RARITY.LEGENDARY,
                         minion_type=MINION_TYPE.MECH,
                         battlecry=Battlecry(AddCard(BurrowingMine(), add_to_deck=True), PlayerSelector(EnemyPlayer())))

    def create_minion(self, player):
        return Minion(4, 6)

# "Wandering Bird NAME_END 2 ATK_END 3 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Rare RARITY_END <b>Battlecry:</b> Deal 4 damage randomly split between all other characters."
class WanderingBird(MinionCard):
    def __init__(self):
        super().__init__("Wandering Bird", 3, CHARACTER_CLASS.ALL, CARD_RARITY.RARE,
                         battlecry=Battlecry(Damage(1), CharacterSelector(players=BothPlayer(),
                                                                          picker=RandomPicker(4))))

    def create_minion(self, player):
        return Minion(2, 3)

# "Arcanist NAME_END 3 ATK_END 2 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Epic RARITY_END <b>Stealth</b> NL <b>Spell Damage +2</b>"
class Arcanist(MinionCard):
    def __init__(self):
        super().__init__("Arcanist", 3, CHARACTER_CLASS.ALL, CARD_RARITY.EPIC)

    def create_minion(self, player):
        return Minion(3, 2, stealth=True, spell_damage=2)

# "Golden Snitch NAME_END 1 ATK_END 3 DEF_END 6 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Mech RACE_END Epic RARITY_END <b>Deathrattle:</b> Summon a random 3-Cost minion."
class GoldenSnitch(MinionCard):
    def __init__(self):
        super().__init__("Golden Snitch", 6, CHARACTER_CLASS.ALL, CARD_RARITY.EPIC, minion_type=MINION_TYPE.MECH)

    def create_minion(self, player):
        return Minion(1, 3, deathrattle=Deathrattle(Summon(CollectionSource([ManaCost(3), IsMinion()])),
                                                    PlayerSelector()))

# "Violet Polarizer NAME_END 2 ATK_END 4 DEF_END 2 COST_END -1 DUR_END Minion TYPE_END Paladin PLAYER_CLS_END NIL RACE_END Rare RARITY_END <b>Battlecry</b>: Deal 1 damage to all minions with <b>Deathrattle</b>."
class VioletPolarizer(MinionCard):
    def __init__(self):
        super().__init__("Violet Polarizer", 2, CHARACTER_CLASS.PALADIN, CARD_RARITY.RARE,
                         battlecry=Battlecry(Damage(1), MinionSelector(MinionHasDeathrattle(), BothPlayer())))

    def create_minion(self, player):
        return Minion(2, 4)

# "Skyline Keeper NAME_END 2 ATK_END 3 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Shaman PLAYER_CLS_END Murloc RACE_END Epic RARITY_END Whenever another friendly Murloc dies, draw a card. <b>Overload</b>: (1)"
class SkylineKeeper(MinionCard):
    def __init__(self):
        super().__init__("Skyline Keeper", 3, CHARACTER_CLASS.SHAMAN, CARD_RARITY.EPIC,
                         minion_type=MINION_TYPE.MURLOC, overload=1)

    def create_minion(self, player):
        return Minion(2, 3, effects=[Effect(MinionDied(IsType(MINION_TYPE.MURLOC)),
                                            ActionTag(Draw(), PlayerSelector()))])


# "Sleepwalking Physician NAME_END 4 ATK_END 3 DEF_END 6 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Battlecry:</b> If you have a Mech, gain +2/+2 and add a <b>Spare Part</b> to your hand."
class SleepwalkingPhysician(MinionCard):
    def __init__(self):
        from hearthbreaker.cards.spells.neutral import spare_part_list
        super().__init__("Sleepwalking Physician", 6, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON,
                         battlecry=(Battlecry(Give([Buff(ChangeAttack(2)), Buff(ChangeHealth(2))]), SelfSelector(),
                                              GreaterThan(Count(MinionSelector(IsType(MINION_TYPE.MECH))), value=0)),
                                    Battlecry(AddCard(CardList(spare_part_list)), PlayerSelector(),
                                              GreaterThan(Count(MinionSelector(IsType(MINION_TYPE.MECH))), value=0))))

    def create_minion(self, player):
        return Minion(4, 3)

# "Sonata NAME_END 3 ATK_END 4 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Priest PLAYER_CLS_END NIL RACE_END Legendary RARITY_END <b>Battlecry:</b> Swap Health with another minion."
class Sonata(MinionCard):
    def __init__(self):
        super().__init__("Sonata", 3, CHARACTER_CLASS.PRIEST, CARD_RARITY.LEGENDARY,
                         battlecry=Battlecry(SwapStats("health", "health", True), MinionSelector(players=BothPlayer(),
                                                                                                 picker=UserPicker())))

    def create_minion(self, player):
        return Minion(3, 4)

# "Morning Call NAME_END 1 ATK_END -1 DEF_END 2 COST_END 2 DUR_END Weapon TYPE_END Warrior PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Deathrattle:</b> Deal 2 damage to all minions."
class MorningCall(WeaponCard):
    def __init__(self):
        super().__init__("Morning Call", 2, CHARACTER_CLASS.WARRIOR, CARD_RARITY.COMMON)

    def create_weapon(self, player):
        return Weapon(1, 2, deathrattle=Deathrattle(Damage(2), MinionSelector(players=BothPlayer())))

# "Melania NAME_END 3 ATK_END 6 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Beast RACE_END Legendary RARITY_END Destroy any minion damaged by this minion."
class Melania(MinionCard):
    def __init__(self):
        super().__init__("Melania", 4, CHARACTER_CLASS.ALL, CARD_RARITY.LEGENDARY, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(3, 6, effects=[Effect(DidDamage(), ActionTag(Kill(), TargetSelector(IsMinion())))])

# "Scotland Cockroach NAME_END 3 ATK_END 6 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Rare RARITY_END <b>Taunt. NL Deathrattle:</b> Summon a 1/2 Slime with <b>Taunt</b>."
class ScotlandCockroach(MinionCard):
    def __init__(self):
        super().__init__("Scotland Cockroach", 3, CHARACTER_CLASS.ALL, CARD_RARITY.RARE)

    def create_minion(self, player):
        return Minion(3, 6, taunt=True, deathrattle=Deathrattle(Summon(Slime()), PlayerSelector()))

# "Nullpointer NAME_END 5 ATK_END 2 DEF_END 2 COST_END -1 DUR_END Minion TYPE_END Warlock PLAYER_CLS_END Demon RACE_END Common RARITY_END <b>Deathrattle:</b> Put a random Demon from your hand into the battlefield."
class Nullpointer(MinionCard):
    def __init__(self):
        super().__init__("Nullpointer", 2, CHARACTER_CLASS.WARLOCK, CARD_RARITY.COMMON, minion_type=MINION_TYPE.DEMON)

    def create_minion(self, player):
        return Minion(5, 2, deathrattle=Deathrattle(Summon(HandSource(FriendlyPlayer(), [IsType(MINION_TYPE.DEMON)])),
                                                    PlayerSelector()))

# "Lacertidae NAME_END 5 ATK_END 7 DEF_END 8 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Dragon RACE_END Legendary RARITY_END <b>Battlecry:</b> Set a hero's remaining Health to 20."
class Lacertidae(MinionCard):
    def __init__(self):
        super().__init__("Lacertidae", 8, CHARACTER_CLASS.ALL, CARD_RARITY.LEGENDARY, minion_type=MINION_TYPE.DRAGON,
                         battlecry=Battlecry(SetHealth(20), HeroSelector(players=BothPlayer(), picker=UserPicker())))

    def create_minion(self, player):
        return Minion(5, 7)

# "Crystal Ball NAME_END 2 ATK_END 3 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Rare RARITY_END <b>Charge</b>. <b>Battlecry:</b> Give your opponent a Mana Crystal."
class CrystalBall(MinionCard):
    def __init__(self):
        super().__init__("Crystal Ball", 4, CHARACTER_CLASS.ALL, CARD_RARITY.RARE,
                         battlecry=Battlecry(GiveManaCrystal(), PlayerSelector(players=EnemyPlayer())))

    def create_minion(self, player):
        return Minion(2, 3, charge=True)

# "Bunny Woodland NAME_END 6 ATK_END 4 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Legendary RARITY_END NIL"
class BunnyWoodland(MinionCard):
    def __init__(self):
        super().__init__("Bunny Woodland", 3, CHARACTER_CLASS.ALL, CARD_RARITY.LEGENDARY, False)

    def create_minion(self, player):
        return Minion(6, 4)

# "FloppyFur NAME_END -1 ATK_END -1 DEF_END 4 COST_END -1 DUR_END Spell TYPE_END Rogue PLAYER_CLS_END NIL RACE_END Rare RARITY_END Destroy your weapon and deal its damage to all enemies."
class FloppyFur(SpellCard):
    def __init__(self):
        super().__init__("Floppy Fur", 4, CHARACTER_CLASS.ROGUE, CARD_RARITY.RARE)

    def use(self, player, game):
        super().use(player, game)

        if player.weapon is not None:
            # Yes, this card is affected by spell damage cards.
            # Source: http://www.hearthhead.com/card=1064/blade-flurry#comments:id=1927317
            attack_power = player.effective_spell_damage(player.hero.calculate_attack())
            player.weapon.destroy()

            for minion in copy.copy(game.other_player.minions):
                minion.damage(attack_power, self)

            game.other_player.hero.damage(attack_power, self)

# "Kenka NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Warrior PLAYER_CLS_END NIL RACE_END Epic RARITY_END Destroy all minions except one. <i>(chosen randomly)</i>"
class Kenka(SpellCard):
    def __init__(self):
        super().__init__("Kenka", 3, CHARACTER_CLASS.WARRIOR, CARD_RARITY.EPIC)

    def can_use(self, player, game):
        return super().can_use(player, game) and len(player.minions) + len(player.opponent.minions) >= 2

    def use(self, player, game):
        super().use(player, game)

        minions = copy.copy(player.minions)
        minions.extend(game.other_player.minions)

        if len(minions) > 1:
            survivor = game.random_choice(minions)
            for minion in minions:
                if minion is not survivor:
                    minion.die(self)

# "Reveal NAME_END -1 ATK_END -1 DEF_END 2 COST_END -1 DUR_END Spell TYPE_END Rogue PLAYER_CLS_END NIL RACE_END Common RARITY_END Give your minions <b>Stealth</b> until your next turn."
class Reveal(SpellCard):
    def __init__(self):
        super().__init__("Reveal", 2, CHARACTER_CLASS.ROGUE, CARD_RARITY.COMMON)

    def use(self, player, game):
        super().use(player, game)
        for minion in player.minions:
            if not minion.stealth:
                minion.add_buff(BuffUntil(Stealth(), TurnStarted()))

# "Carbuncle NAME_END 1 ATK_END 3 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Paladin PLAYER_CLS_END NIL RACE_END Common RARITY_END NIL"
class Carbuncle(MinionCard):
    def __init__(self):
        super().__init__("Carbuncle", 3, CHARACTER_CLASS.PALADIN, CARD_RARITY.COMMON)

    def create_minion(self, p):
        return Minion(1, 3)

# "Sheepfold NAME_END 3 ATK_END 6 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Warlock PLAYER_CLS_END Demon RACE_END Rare RARITY_END <b>Charge</b>. <b>Battlecry:</b> Discard one random cards."
class Sheepfold(MinionCard):
    def __init__(self):
        super().__init__("Sheepfold", 4, CHARACTER_CLASS.WARLOCK, CARD_RARITY.RARE, minion_type=MINION_TYPE.DEMON,
                         battlecry=Battlecry(Discard(amount=1), PlayerSelector()))

    def create_minion(self, player):
        return Minion(3, 6, charge=True)

# "Crustal Movement NAME_END 8 ATK_END 8 DEF_END 6 COST_END -1 DUR_END Minion TYPE_END Shaman PLAYER_CLS_END NIL RACE_END Epic RARITY_END <b>Taunt</b>. <b>Overload:</b> (3)"
class CrustalMovement(MinionCard):
    def __init__(self):
        super().__init__("Crustal Movement", 6, CHARACTER_CLASS.SHAMAN, CARD_RARITY.EPIC, overload=3)

    def create_minion(self, player):
        return Minion(8, 8, taunt=True)

# "Retaliate NAME_END -1 ATK_END -1 DEF_END 4 COST_END -1 DUR_END Spell TYPE_END Hunter PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Secret:</b> When your hero is attacked, deal $3 damage to all enemies."
class Retaliate(SecretCard):
    def __init__(self):
        super().__init__("Retaliate", 4, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON)

    def activate(self, player):
        player.opponent.bind("character_attack", self._reveal)

    def deactivate(self, player):
        player.opponent.unbind("character_attack", self._reveal)

    def _reveal(self, attacker, target):
        if isinstance(target, Hero):
            game = attacker.player.game
            enemies = copy.copy(game.current_player.minions)
            enemies.append(game.current_player.hero)
            for enemy in enemies:
                enemy.damage(3, None)
            game.check_delayed()
            super().reveal()

# "Rain of Chaos NAME_END 2 ATK_END 1 DEF_END 1 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END NIL RARITY_END NIL"
class RainOfChaos(MinionCard):
    def __init__(self):
        super().__init__("Rain of Chaos", 2, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON, False)

    def create_minion(self, player):
        return Minion(2, 3)

# "Gnoll NAME_END 1 ATK_END 3 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END NIL RARITY_END <b>Taunt</b>"
class Goblin(MinionCard):
    def __init__(self):
        super().__init__("Goblin", 3, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON, False)

    def create_minion(self, player):
        return Minion(1, 3, taunt=True)

# "Star Light NAME_END -1 ATK_END -1 DEF_END 6 COST_END -1 DUR_END Spell TYPE_END Paladin PLAYER_CLS_END NIL RACE_END Rare RARITY_END Draw a card and deal damage equal to its cost."
class StarLight(SpellCard):
    def __init__(self):
        super().__init__("Star Light", 6, CHARACTER_CLASS.PALADIN,
                         CARD_RARITY.RARE, target_func=hearthbreaker.targeting.find_spell_target)

    def use(self, player, game):
        super().use(player, game)

        fatigue = False
        if player.deck.left == 0:
            fatigue = True

        player.draw()
        if not fatigue:
            cost = player.hand[-1].mana
            self.target.damage(player.effective_spell_damage(cost), self)

# "Goldfish NAME_END 4 ATK_END 3 DEF_END 5 COST_END -1 DUR_END Minion TYPE_END Warlock PLAYER_CLS_END Demon RACE_END Common RARITY_END NIL"
class Goldfish(MinionCard):
    def __init__(self):
        super().__init__("Goldfish", 5, CHARACTER_CLASS.WARLOCK, CARD_RARITY.COMMON, False,
                         minion_type=MINION_TYPE.DEMON)

    def create_minion(self, player):
        return Minion(4, 3)

# "Infinito De Laufraut NAME_END 2 ATK_END 3 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Mage PLAYER_CLS_END NIL RACE_END Rare RARITY_END <b>Battlecry:</b> The next <b>Secret</b> you play this turn costs (0)."
class InfinitoDeLaufraut(MinionCard):
    def __init__(self):
        super().__init__("Infinito De Laufraut", 4, CHARACTER_CLASS.MAGE, CARD_RARITY.RARE,
                         battlecry=Battlecry(GiveAura([AuraUntil(ManaChange(-100), CardSelector(condition=IsSecret()),
                                                                 CardPlayed(IsSecret()))]), PlayerSelector()))

    def create_minion(self, player):
        return Minion(2, 3)

# "Dark Knight NAME_END 2 ATK_END 3 DEF_END 2 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Rare RARITY_END Whenever a character is healed, gain +1 Attack."
class DarkKnight(MinionCard):
    def __init__(self):
        super().__init__("Dark Knight", 2, CHARACTER_CLASS.ALL, CARD_RARITY.RARE)

    def create_minion(self, player):
        return Minion(2, 3, effects=[Effect(CharacterHealed(player=BothPlayer()),
                                            ActionTag(Give(ChangeAttack(1)), SelfSelector()))])


# "Moonlight Demon NAME_END 1 ATK_END 4 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Rare RARITY_END ALL minions cost (1) more."
class MoonlightDemon(MinionCard):
    def __init__(self):
        super().__init__("Moonlight Demon", 3, CHARACTER_CLASS.ALL, CARD_RARITY.RARE)

    def create_minion(self, player):
        return Minion(1, 4, auras=[Aura(ManaChange(1), CardSelector(BothPlayer(), IsMinion()))])


# "Manifestation NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Hunter PLAYER_CLS_END NIL RACE_END Rare RARITY_END <b>Secret:</b> When a character attacks your hero, instead he attacks another random character."
class Manifestation(SecretCard):
    def __init__(self):
        super().__init__("Manifestation", 2, CHARACTER_CLASS.HUNTER, CARD_RARITY.RARE)

    def activate(self, player):
        player.opponent.bind("character_attack", self._reveal)

    def deactivate(self, player):
        player.opponent.unbind("character_attack", self._reveal)

    def _reveal(self, character, target):
        if isinstance(target, Hero) and not character.removed:
            game = character.player.game
            possibilities = copy.copy(game.current_player.minions)
            possibilities.extend(game.other_player.minions)
            possibilities.append(game.current_player.hero)
            possibilities.append(game.other_player.hero)
            possibilities.remove(character.current_target)
            character.current_target = game.random_choice(possibilities)

            super().reveal()

# "Cubic Room NAME_END -1 ATK_END -1 DEF_END 2 COST_END -1 DUR_END Spell TYPE_END Paladin PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Secret:</b> When an enemy attacks, summon a 2/1 Defender as the new target."
class CubicRoom(SecretCard):
    def __init__(self):
        super().__init__("Cubic Room", 2, CHARACTER_CLASS.PALADIN, CARD_RARITY.COMMON)

    def _reveal(self, attacker, target):
        player = attacker.player.game.other_player
        if len(player.minions) < 7 and not attacker.removed:
            from hearthbreaker.cards.minions.paladin import DefenderMinion
            defender = DefenderMinion()
            defender.summon(player, player.game, len(player.minions))
            attacker.current_target = player.minions[-1]
            super().reveal()

    def activate(self, player):
        player.opponent.bind("character_attack", self._reveal)

    def deactivate(self, player):
        player.opponent.unbind("character_attack", self._reveal)

# "Voice of The Land NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Druid PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Choose One</b> - Give your minions +1/+1; or Summon a 3/2 Panther."
class VoiceOfTheLand(SpellCard):
    def __init__(self):
        super().__init__("Voice Of The Land", 3, CHARACTER_CLASS.DRUID, CARD_RARITY.COMMON)

    def use(self, player, game):
        super().use(player, game)
        option = player.agent.choose_option([LeaderOfThePack(), SummonPanther()], player)
        option.use(player, game)

# "Redemption NAME_END -1 ATK_END -1 DEF_END 1 COST_END -1 DUR_END Spell TYPE_END Paladin PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Secret:</b> When one of your minions dies, return it to life with 2 Health."
class Detention(SecretCard):
    def __init__(self):
        super().__init__("Detention", 1, CHARACTER_CLASS.PALADIN, CARD_RARITY.COMMON)

    def _reveal(self, minion, by):
        resurrection = minion.card.summon(minion.player, minion.game, min(minion.index, len(minion.player.minions)))
        if resurrection:
            resurrection.health = 2
            super().reveal()

    def activate(self, player):
        player.bind("minion_died", self._reveal)

    def deactivate(self, player):
        player.unbind("minion_died", self._reveal)

# "Corner Creature NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Priest PLAYER_CLS_END NIL RACE_END Rare RARITY_END Gain control of an enemy minion with 3 or less Attack until end of turn."
class CornerCreature(SpellCard):
    def __init__(self):
        super().__init__("Corner Creature", 3, CHARACTER_CLASS.PRIEST,
                         CARD_RARITY.RARE,
                         target_func=hearthbreaker.targeting.find_enemy_minion_spell_target,
                         filter_func=lambda target: target.calculate_attack() <= 3 and target.spell_targetable())

# "Lucratious Deal NAME_END -1 ATK_END -1 DEF_END 3 COST_END -1 DUR_END Spell TYPE_END Warlock PLAYER_CLS_END NIL RACE_END Rare RARITY_END Destroy a minion. Restore #5 Health to your hero."
class LucratiousDeal(SpellCard):
    def __init__(self):
        super().__init__("Lucratious Deal", 3, CHARACTER_CLASS.WARLOCK, CARD_RARITY.RARE,
                         target_func=hearthbreaker.targeting.find_minion_spell_target)

    def use(self, player, game):
        super().use(player, game)
        self.target.die(self)
        player.hero.heal(player.effective_heal_power(5), self)

# "Troublemaker NAME_END 2 ATK_END 4 DEF_END 0 COST_END -1 DUR_END Minion TYPE_END Mage PLAYER_CLS_END NIL RACE_END Epic RARITY_END NIL"
class Troublemaker(SecretCard):
    def __init__(self):
        super().__init__("Troublemaker", 4, CHARACTER_CLASS.MAGE, CARD_RARITY.EPIC)
        self.player = None

    def _reveal(self, card, index):
        # According to http://us.battle.net/hearthstone/en/forum/topic/10070927066, Spellbender
        # will not activate if there are too many minions
        if card.is_spell() and len(self.player.minions) < 7 and card.target and card.target.is_minion():
            TroublemakerMinion().summon(self.player, self.player.game, len(self.player.minions))
            card.target = self.player.minions[-1]
            super().reveal()

    def activate(self, player):
        player.game.current_player.bind("card_played", self._reveal)
        self.player = player

    def deactivate(self, player):
        player.game.current_player.unbind("card_played", self._reveal)
        self.player = None

class TroublemakerMinion(MinionCard):
    def __init__(self):
        super().__init__("Troublemaker", 0, CHARACTER_CLASS.MAGE, CARD_RARITY.EPIC, False,
                         ref_name="Troublemaker (minion)")

    def create_minion(self, p):
        return Minion(2, 4)

# "Action Peguintial NAME_END 1 ATK_END 3 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Warlock PLAYER_CLS_END NIL RACE_END Common RARITY_END Your minions cost (2) less, but not less than (1)."
class ActionPeguintial(MinionCard):
    def __init__(self):
        super().__init__("Action Peguintial", 3, CHARACTER_CLASS.WARLOCK, CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(1, 3, auras=[Aura(ManaChange(-2, 1, minimum=1), CardSelector(condition=IsMinion()))])

# "Roaring Windmill NAME_END 4 ATK_END 5 DEF_END 4 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END <b>Windfury</b>"
class RoaringWindmill(MinionCard):
    def __init__(self):
        super().__init__("Roaring Windmill", 4, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(4, 5, windfury=True)

# "Sublimate! NAME_END -1 ATK_END -1 DEF_END 2 COST_END -1 DUR_END Spell TYPE_END Warrior PLAYER_CLS_END NIL RACE_END Rare RARITY_END If you have a weapon, give it +1/+3. Otherwise equip a 1/3 weapon."
class Sublimate(SpellCard):
    def __init__(self):
        super().__init__("Sublimate!", 2, CHARACTER_CLASS.WARRIOR, CARD_RARITY.RARE)

    def use(self, player, game):
        super().use(player, game)
        from hearthbreaker.cards.weapons.warrior import HeavyAxe
        if player.weapon:
            player.weapon.durability += 1
            player.weapon.base_attack += 3
        else:
            heavy_axe = HeavyAxe().create_weapon(player)
            heavy_axe.equip(player)

# "Blow NAME_END 1 ATK_END 2 DEF_END 1 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END NIL RACE_END Common RARITY_END NIL"
class Blow(MinionCard):
    def __init__(self):
        super().__init__("Blow", 1, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(1, 2)

# "Stray Dog NAME_END 3 ATK_END 4 DEF_END 2 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Dragon RACE_END Common RARITY_END NIL"
class StrayDog(MinionCard):
    def __init__(self):
        super().__init__("Stray Dog", 2, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON, False, MINION_TYPE.DRAGON)

    def create_minion(self, player):
        return Minion(3, 4)

# "Castellan NAME_END 2 ATK_END 4 DEF_END 5 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Dragon RACE_END Common RARITY_END Whenever <b>you</b> target this minion with a spell, gain +1/+2."
class Castellan(MinionCard):
    def __init__(self):
        super().__init__("Castellan", 5, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON,
                         minion_type=MINION_TYPE.DRAGON)

    def create_minion(self, player):
        return Minion(2, 4, effects=[Effect(SpellTargeted(), [ActionTag(Give([Buff(ChangeAttack(1)),
                                                                              Buff(ChangeHealth(2))]),
                                                                        SelfSelector())])])

# "Angry Bird NAME_END 6 ATK_END 4 DEF_END 3 COST_END -1 DUR_END Minion TYPE_END Neutral PLAYER_CLS_END Dragon RACE_END Common RARITY_END <b>Battlecry:</b> Summon a random 3-Cost minion for your opponent."
class AngryBird(MinionCard):
    def __init__(self):
        super().__init__("Angry Bird", 3, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON, minion_type=MINION_TYPE.DRAGON,
                         battlecry=(Battlecry(Summon(CollectionSource([ManaCost(3), IsMinion()])),
                                              PlayerSelector(EnemyPlayer()))))

    def create_minion(self, player):
        return Minion(6, 4)

# "Wuthering Hills NAME_END -1 ATK_END -1 DEF_END 4 COST_END -1 DUR_END Spell TYPE_END Paladin PLAYER_CLS_END NIL RACE_END Common RARITY_END Draw 3 cards. Costs (1) less for each minion that died this turn."
class WutheringHills(SpellCard):
    def __init__(self):
        super().__init__("Wuthering Hills", 4, CHARACTER_CLASS.PALADIN, CARD_RARITY.COMMON,
                         buffs=[Buff(ManaChange(Count(DeadMinionSelector(players=BothPlayer())), -1))])

    def use(self, player, game):
        super().use(player, game)
        for n in range(0, 3):
            player.draw()

