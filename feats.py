# only level 1 feats are included here. 
# Fighting style feats are NOT here




class Feat:
    def __init__(self, feat_name, feat_features, level_req=1, additional_requirements=None):
        self.feat_name = feat_name
        self.feat_features = feat_features
        self.level_req = level_req
        self.additional_requirements = additional_requirements


    def __str__(self):
        return f"{self.feat_name}"


initiative_proficiency = ()
initiative_swap = ()
tool_prof = ()
discount = ()
faster_crafting = ()
battle_medic = ()
healing_rerolls = ()
luck_points = ()
advantage = ()
disadvantage = ()
two_cantrips = ()
first_level_spell = ()
instrument_training = ()
inspiring_song = ()
enhanced_unarmed_strike = ()
damage_rerolls = ()
shove = ()
furniture_as_weapons = ()






alert_features = ("Always on the lookout for danger, you gain the following benefits:", initiative_proficiency, initiative_swap)
crafter_features = ("You gain Tool Proficiency with three different Artisan’s Tools* of your choice", tool_prof, discount, faster_crafting)
healer_features = ("You have the training and intuition to administer first aid and other care effectively, granting you the following benefits:", battle_medic, healing_rerolls)
lightly_armored_features = ("You gain the following Armor Training: Light Armor, Medium Armor, and Shield.")
lucky_features = ("You have inexplicable luck that can kick in at just the right moment, granting you the following benefits:", luck_points, advantage, disadvantage)
magic_initiate_arcane_features = ("You have learned the basics of a particular magical tradition. You gain the following benefits related to that to be selected from the Arcane spell list:", two_cantrips, first_level_spell)
magic_initiate_divine_features = ("You have learned the basics of a particular magical tradition. You gain the following benefits related to that to be selected from the Divine spell list:", two_cantrips, first_level_spell)
magic_initiate_primal_features = ("You have learned the basics of a particular magical tradition. You gain the following benefits related to that to be selected from the Primal spell list:", two_cantrips, first_level_spell)
musician_features = ("You are a practiced musician, granting you the following benefits:", instrument_training, inspiring_song)
savage_attacker_features = ("You have trained to deal particularly damaging strikes. When you take the Attack Action and hit a target with a Weapon as part of that Action, you can roll the Weapon’s damage dice twice and use either roll against the target. You can use this benefit only once per turn.")
skilled_features = ("You have exceptionally broad learning. Choose three Skills in which you lack Proficiency. You gain Proficiency in those Skills")
tavern_brawler_features = ("Accustomed to brawling, you gain the following benefits:", enhanced_unarmed_strike, damage_rerolls, shove, furniture_as_weapons)
tough_features = ("Your Hit Point Maximum increases by an amount equal to twice your character level when you gain this Feat. Whenever you gain a level thereafter, your Hit Point Maximum increases by an additional 2 Hit Points.")


alert = Feat("Alert", alert_features)
crafter = Feat("Crafter", crafter_features)
healer = Feat("Healer", healer_features)
lightly_armored = Feat("Lightly Armored", lightly_armored_features)
lucky = Feat("Lucky", lucky_features)
magic_initiate_arcane = Feat("Magic_initiate", magic_initiate_arcane_features)
magic_initiate_divine = Feat("Magic_initiate", magic_initiate_divine_features)
magic_initiate_primal = Feat("Magic_initiate", magic_initiate_primal_features)
musician = Feat("Musician", musician_features)
savage_attacker = Feat("Savage_attacker", savage_attacker_features)
skilled = Feat("Skilled", skilled_features)
tavern_brawler = Feat("Tavern_brawler", tavern_brawler_features)
tough = Feat("Tough", tough_features)

all_feats = (alert, crafter, healer, lucky, magic_initiate_arcane, magic_initiate_divine, magic_initiate_primal, musician, savage_attacker, skilled, tavern_brawler, tough)

