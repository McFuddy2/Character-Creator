import random
from spells import *


# only level 1 feats are included here. 
# Fighting style feats are NOT here




class Feat:
    def __init__(self, feat_name, feat_features, level_req=1, additional_requirements=None):
        self.feat_name = feat_name
        self.feat_features = feat_features
        self.level_req = level_req
        self.additional_requirements = additional_requirements
        self.gain_skill_prof = None
        self.gain_hp = None
        self.gain_tool_prof = None
        self.gain_spells = {}
        self.gain_initiative = None
        self.gain_armor_training = None
        self.check_for_stat_changes()


    def __str__(self):
        return f"{self.feat_name}"


    def __repr__(self):
        return f"{self.feat_name}"


    def check_for_stat_changes(self):
        features_that_gain_skill_prof = (skilled_features_math)
        features_that_gain_hp = (tough_features_math)
        features_that_gain_tool_prof = (tool_prof, instrument_training)
        features_that_gain_spells = (two_arcane_cantrips, two_divine_cantrips, two_primal_cantrips, first_level_arcane_spell, first_level_divine_spell, first_level_primal_spell)
        features_that_gain_initiative = (initiative_proficency,)
        features_that_gain_armor_training = (lightly_armored_math,)
        
        
        for i in range(len(self.feat_features)):
            if self.feat_features[i] in features_that_gain_skill_prof:
                try:
                    num_skills_to_pick, skill_list = self.feat_features[i+1][1]
                    selected_skills = random.sample(skill_list, num_skills_to_pick)
                    if self.gain_skill_prof is None:
                        self.gain_skill_prof = selected_skills
                    else:
                        self.gain_skill_prof.extend(selected_skills)
                except (ValueError, TypeError):
                    pass
                
            if self.feat_features[i] in features_that_gain_tool_prof:
                try:
                    num_tools_to_pick, tool_list = self.feat_features[i][1]
                    selected_tools = random.sample(tool_list, num_tools_to_pick)
                    if self.gain_tool_prof is None:
                        self.gain_tool_prof = selected_tools
                    else:
                        self.gain_tool_prof.extend(selected_tools)
                except (ValueError, TypeError):
                    pass
            if self.feat_features[i] in features_that_gain_hp:
                
                try:
                    if self.gain_hp is None:
                        self.gain_hp = self.feat_features[i+1][1]
                    else:
                        # Make sure gain_hp is always a tuple
                        self.gain_hp = tuple(self.gain_hp) + tuple(self.feat_features[i+1][1])
                except (ValueError, TypeError):
                    pass
        
            if  self.feat_features[i] in features_that_gain_spells:
                try:
                    for key, value in self.feat_features[i][1].items():
                        if key in self.gain_spells:
                            self.gain_spells[key].append(value)
                        else:
                            self.gain_spells[key] = value
                except (ValueError, TypeError):
                    pass
            
            if  self.feat_features[i] in features_that_gain_initiative:
                try:
                    if self.gain_initiative is None:
                        self.gain_initiative = self.feat_features[i][1]
                    else:
                        self.gain_initiative.append(self.feat_features[i][1])
                except (ValueError, TypeError):
                    pass

            if  self.feat_features[i] in features_that_gain_armor_training:
                try:
                    if self.gain_armor_training is None:
                        self.gain_armor_training = self.feat_features[i][1]
                    else:
                        self.gain_armor_training.append(self.feat_features[i][1])
                except (ValueError, TypeError):
                    pass
            
    


two_arcane_cantrip_list = {"Cantrip":[random.sample(arcane_cantrips_list, 2)]}
two_divine_cantrip_list = {"Cantrip":[random.sample(divine_cantrips_list, 2)]}
two_primal_cantrip_list = {"Cantrip":[random.sample(primal_cantrips_list, 2)]}
first_level_arcane_list = {"1st":[random.choice(arcane_first_level_list)]}
first_level_divine_list = {"1st":[random.choice(divine_first_level_list)]}
first_level_primal_list = {"1st":[random.choice(primal_first_level_list)]}


initiative_proficency = ("When you roll Initiative, you can add your Proficiency Bonus to the roll", "Proficency Bonus")
initiative_swap = ("Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can’t make this swap if you or the ally is Incapacitated.")
tool_prof = ("You gain Tool Proficiency with three different Artisan’s Tools of your choice", (3, ("Alchemist’s supplies", "Brewer’s supplies", "Calligrapher's", "Carpenter’s tools", "Cartographer’s tools", "Cobbler’s tools", "Cook’s utensils", "Glassblower’s tools", "Jeweler’s tools", "Leatherworker’s tools", "Mason’s tools", "Painter’s supplies", "Potter’s tools", "Smith’s tools", "Tinker’s tools", "Weaver’s tools", "Woodcarver’s tools", "Navigator’s tools", "Thieves’ tools")))
discount = ("Whenever you buy a nonmagical item, you receive a 20 percent discount on it")
faster_crafting = ("When you craft an item using a tool with which you have Tool Proficiency, the required crafting time is reduced by 20 percent.")
battle_medic = ("If you have a Healer’s Kit, you can expend one use of it and tend to a creature within 5 feet of you as an Action. That creature can expend one of its Hit Dice, and you then roll that die. The creature regains a number of Hit Points equal to the roll plus your Proficiency Bonus")
healing_rerolls = ("Whenever you roll a die to determine the number of Hit Points you restore with a spell or with this feat’s Battle Medic benefit, you can reroll the die if it rolls a 1, and you must use the new roll.")
luck_points = ("You have a number of Luck Pointsequal to your Proficiency Bonus. You can spend the points on the benefits below, and you regain your expended Luck Points when you finish a Long Rest.")
advantage = ("Immediately after you roll a d20 for a d20 Test, you can spend 1 Luck Point to give yourself Advantage on the roll")
disadvantage = ("When a creature rolls a d20 for an attack roll against you, you can spend 1 Luck Point to impose Disadvantage on that roll.")
two_arcane_cantrips = ("You learn two cantrips of your choice from the Spell arcane list.", two_arcane_cantrip_list)
two_divine_cantrips = ("You learn two cantrips of your choice from the Spell divine list.", two_divine_cantrip_list)
two_primal_cantrips = ("You learn two cantrips of your choice from the Spell primal list.", two_primal_cantrip_list)
first_level_arcane_spell = ("Choose one 1st-level Spell from the Arcane Spell list. You always have that Spell prepared. You can cast it once without a SpellSlot, and you regain the ability to cast it in that way when you finish a Long Rest. You can also cast the Spell using any Spell Slots you have.", first_level_arcane_list)
first_level_divine_spell = ("Choose one 1st-level Spell from the Divine Spell list. You always have that Spell prepared. You can cast it once without a SpellSlot, and you regain the ability to cast it in that way when you finish a Long Rest. You can also cast the Spell using any Spell Slots you have.", first_level_divine_list)
first_level_primal_spell = ("Choose one 1st-level Spell from the Primal Spell list. You always have that Spell prepared. You can cast it once without a SpellSlot, and you regain the ability to cast it in that way when you finish a Long Rest. You can also cast the Spell using any Spell Slots you have.", first_level_primal_list)
instrument_training = ("You gain Tool Proficiency with three Musical Instrumentsof your choice.", (3, ("Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan flute", "Shawm", "Viol")))
inspiring_song = ("As you finish a Short Rest or a Long Rest, you can play a song on a Musical Instrument with which you have Tool Proficiency and give Inspiration to allies who hear the song. The number of allies you can affect in this way equals your Proficiency Bonus.")
enhanced_unarmed_strike = ("When you hit with your Unarmed Strike and deal damage, you can deal Bludgeoning Damage equal to 1d4 + your Strength modifier, instead of the normal damage of an Unarmed Strike")
damage_rerolls = ("Whenever you roll a damage die for your Unarmed Strike, you can reroll the die if it rolls a 1, and you must use the new roll")
shove = ("When you hit a creature with an Unarmed Strike as part of the Attack Actionon your turn, you can deal damage to the target and also push it 5 feet away. You can use this benefit only once per turn")
furniture_as_weapons = ("You can wield furniture as a Weapon, using the rules of the Greatclub for Small or Medium furniture and the rules of the Club for Tiny furniture.")
lightly_armored_math = ("You gain the following Armor Training: Light Armor, Medium Armor, and Shield.", ("Light", "Medium", "Sheild"))
tough_features_math = ("Your Hit Point Maximum increases by an amount equal to twice your character level when you gain this Feat. Whenever you gain a level thereafter, your Hit Point Maximum increases by an additional 2 Hit Points.", (2,1))
skilled_features_math = ("You have exceptionally broad learning. Choose three Skills in which you lack Proficiency. You gain Proficiency in those Skills", (1, ("Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival")))





alert_features = ("Always on the lookout for danger, you gain the following benefits:", initiative_proficency, initiative_swap)
crafter_features = ("You are adept at crafting things and bargaining with merchants, granting you the following benefits:", tool_prof, discount, faster_crafting)
healer_features = ("You have the training and intuition to administer first aid and other care effectively, granting you the following benefits:", battle_medic, healing_rerolls)
lightly_armored_features = ("You gain the following Armor Training: Light Armor, Medium Armor, and Shield.", lightly_armored_math)
lucky_features = ("You have inexplicable luck that can kick in at just the right moment, granting you the following benefits:", luck_points, advantage, disadvantage)
magic_initiate_arcane_features = ("You have learned the basics of a particular magical tradition. You gain the following benefits related to that to be selected from the Arcane spell list: Two Cantrips and a 1st Level spell.Intelligence, Wisdom, or Charisma is your spellcasting ability for these Spells (choose when you select this Feat). Consult the Player’s Handbook for the rules on spellcasting.Whenever you gain a new level, you can replace one of the Spells you chose for this Featwith a different Spell of the same level from the chosen Spell list.", two_arcane_cantrips, first_level_arcane_spell)
magic_initiate_divine_features = ("You have learned the basics of a particular magical tradition. You gain the following benefits related to that to be selected from the Divine spell list: Two Cantrips and a 1st Level spell.Intelligence, Wisdom, or Charisma is your spellcasting ability for these Spells (choose when you select this Feat). Consult the Player’s Handbook for the rules on spellcasting.Whenever you gain a new level, you can replace one of the Spells you chose for this Featwith a different Spell of the same level from the chosen Spell list.", two_divine_cantrips, first_level_divine_spell)
magic_initiate_primal_features = ("You have learned the basics of a particular magical tradition. You gain the following benefits related to that to be selected from the Primal spell list: Two Cantrips and a 1st Level spell.Intelligence, Wisdom, or Charisma is your spellcasting ability for these Spells (choose when you select this Feat). Consult the Player’s Handbook for the rules on spellcasting.Whenever you gain a new level, you can replace one of the Spells you chose for this Featwith a different Spell of the same level from the chosen Spell list.", two_primal_cantrips, first_level_primal_spell)
musician_features = ("You are a practiced musician, granting you the following benefits:", instrument_training, inspiring_song)
savage_attacker_features = ("You have trained to deal particularly damaging strikes. When you take the Attack Action and hit a target with a Weapon as part of that Action, you can roll the Weapon’s damage dice twice and use either roll against the target. You can use this benefit only once per turn.")
skilled_features = ("You have exceptionally broad learning. Choose three Skills in which you lack Proficiency. You gain Proficiency in those Skills", skilled_features_math)
tavern_brawler_features = ("Accustomed to brawling, you gain the following benefits:", enhanced_unarmed_strike, damage_rerolls, shove, furniture_as_weapons)
tough_features = ("Your Hit Point Maximum increases by an amount equal to twice your character level when you gain this Feat. Whenever you gain a level thereafter, your Hit Point Maximum increases by an additional 2 Hit Points.", tough_features_math)


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

fs_feats = ()

fs_feat = random.choice=(fs_feats)


