import random
from feats import *



class Race:
    def __init__(self, race_name, creature_type, size, speed_in_feet, life_span_in_years, special_traits):
        self.race_name = race_name
        self.creature_type = creature_type
        self.size  = size
        self.speed_in_feet = speed_in_feet
        self.life_span_in_years =  life_span_in_years
        self.special_traits = special_traits
        self.gain_skill_prof = None
        self.gain_feat = None
        self.gain_hp = None
        self.gain_tool_prof = None
        self.gain_spells = None
        self.check_for_stat_changes()

    def __str__(self):
        return f"{self.race_name}"
    
    def check_for_stat_changes(self):
        features_that_gain_skill_prof = (skillfull, keen_senses, naturally_stealthy)
        features_that_gain_feat = (versatile,)
        features_that_gain_hp = (dwarven_toughness,)
        features_that_gain_tool_prof = (forge_wise,)
        features_that_gain_spells = (otherworldly_presence, drow_elven_lineage, high_elven_lineage, wood_elven_lineage, rock_gnomish_lineage, forest_gnomish_lineage, abyssal_fiendish_legacy, chthonic_fiendish_legacy, infernal_fiendish_legacy)

        for trait in self.special_traits:
            if trait in features_that_gain_skill_prof and isinstance(trait, tuple) and len(trait) == 2 and isinstance(trait[1], tuple):
                try:
                    num_skills_to_pick, skill_list = trait[1]
                    selected_skills = random.sample(skill_list, num_skills_to_pick)

                    if self.gain_skill_prof is None:
                        self.gain_skill_prof = selected_skills
                    else:
                        self.gain_skill_prof.extend(selected_skills)
                except (ValueError, TypeError):
                    pass
                
            if trait in features_that_gain_tool_prof and isinstance(trait, tuple) and len(trait) == 2 and isinstance(trait[1], tuple):
                try:
                    num_tools_to_pick, tool_list = trait[1]
                    selected_tools = random.sample(tool_list, num_tools_to_pick)

                    if self.gain_tool_prof is None:
                        self.gain_tool_prof = selected_tools
                    else:
                        self.gain_tool_prof.extend(selected_tools)
                except (ValueError, TypeError):
                    pass
            if trait in features_that_gain_hp and isinstance(trait, tuple) and len(trait) == 2 and isinstance(trait[1], tuple):
                try:
                    if self.gain_hp is None:
                        self.gain_hp = trait[1]
                    else:
                        # Make sure gain_hp is always a tuple
                        self.gain_hp = tuple(self.gain_hp) + tuple(trait[1])
                except (ValueError, TypeError):
                    pass
            if trait in features_that_gain_feat and isinstance(trait, tuple) and len(trait) == 2 and isinstance(trait[1], tuple):
                try:
                    if self.gain_feat is None:
                        self.gain_feat = [(trait[1][1])]
                    else:
                        self.gain_feat.extend([(trait[1][1])])
                except (ValueError, TypeError):
                    pass    
            if isinstance(trait, tuple) and trait in features_that_gain_spells:
                try:
                    if self.gain_spells is None:
                        self.gain_spells = [trait[1]]
                    else:
                        self.gain_spells.extend([trait[1]])
                except (ValueError, TypeError):
                    pass
            
           


drow_elf_spells = {"Cantrip":["Dancing Lights"], "1st":["Farie Fire"], "2nd":["Darkness"]}
high_elf_spells = {"Cantrip":["Prestidigitation"], "1st":["Detect Magic"], "2nd":["Misty Step"]}
wood_elf_spells = {"Cantrip":["Druidcraft"], "1st":["Longstrider"], "2nd":["Pass without Trace"]} 
tiefling_spells = {"Cantrip":["Thaumaturgy"]}
abyssal_tiefling_spells = {"Cantrip":["Poison Spray"], "1st":["Ray of Sickness"], "2nd":["Hold Person"]} 
chthonic_tiefling_spells = {"Cantrip":["Chill Touch"], "1st":["False Life"], "2nd":["Ray of Enfeeblement"]} 
infernal_tiefling_spells = {"Cantrip":["Fire Bolt"], "1st":["Hellish Rebuke"], "2nd":["Darkness"]} 
rock_gnome_spells = {"Cantrip":["Mending","Prestidigitation"]} 
forest_gnome_spells = {"Cantrip":["Minor Illusion"], "1st":["Speak with Animals"]} 




# if you add new traits, and those traits have an effect on the math. please add that trait to the list in "check_for_stat_changes(self):" above.

resourceful = "You gain Inspiration whenever you finish a Long Rest"
skillfull = ("You gain Proficiency in one Skill of your choice", (1, ("Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival")))
versatile = ("You gain the Skilled Feat", (1, skilled))
darkvision = "You have Darkvision with a range of 60 feet."
dwarven_resilience = "You have Resistance to Poison Damage. You also have Advantage on saving throws you make to avoid or end the Poisoned Condition on yourself."
dwarven_toughness = ("Your Hit Point Maximum increases by 1, and it increases by 1 again whenever you gain a level", (1, 1))
forge_wise = ("Your divine creator gave you an uncanny affinity for working with stone or metal. You gain Tool Proficiency with two of the following options of your choice: Jeweler’s Tools, Mason’s Tools, Smith’s Tools, or Tinker’s Tools", (2, ("Jeweler’s Tools", "Mason’s Tools", "Smith’s Tools", "Tinker’s Tools")))
stonecunning = "As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes. You must be on a stone surface or touching such a surface to use this Tremorsense. The stone can be natural or worked. You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."
drow_elven_lineage = ("You are part of an elven lineage that grants you supernatural abilities. You are a Drow, the lineage of the Underdark. Starting at 1st level The range of your Darkvision increases to 120 feet. At 1st level you also know the Dancing Lights cantrip. Starting at 3rd level you know the spell Faerie Fire. Starting at 5th level you also know the Darkness spell. Once you cast either Farie Fire or Darkness with this trait, you can’t cast that Spell with it again until you finish a Long Rest; however, you can cast the Spell using any Spell Slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", drow_elf_spells)
high_elven_lineage = ("You are part of an elven lineage that grants you supernatural abilities. You are a High Elf, the lineage of fey crossings and other magical locations. Starting at 1st level You know the Prestidigitation cantrip. Whenever you finish a Long Rest, you can replace that cantrip with a different cantrip from the Arcane Spell List. Starting at 3rd level you know the Detect Magic spell. Starting at 5th level you know the Misty Step spell.Once you cast either Detect Magic or Misty Step with this trait, you can’t cast that Spell with it again until you finish a Long Rest; however, you can cast the Spell using any Spell Slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", high_elf_spells)
wood_elven_lineage = ("You are part of an elven lineage that grants you supernatural abilities. You are a Wood Elf, the lineage of primeval forests. Starting t 1st level your Speed increases to 35 feet. You also know the Druidcraft cantrip. Starting at 3rd level you know the Longstrider spell. Starting at 5th level you know the Pass without Trace spell. Once you cast either Longstrider or Pass without Trace with this trait, you can’t cast that Spell with it again until you finish a Long Rest; however, you can cast the Spell using any Spell Slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", wood_elf_spells)
fey_ancestry = "You have Advantage on saving throws you make to avoid or end the Charmed Condition on yourself."
keen_senses = ("You have Proficiency in the Perception Skill.", (1, ("Perception", "Perception")))
trance = "You don’t need to sleep, and magic can’t put you to sleep. You can finish a Long Rest* in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness."
gnomish_cunning = "You have Advantage on Intelligence, Wisdom, and Charisma saving  throws."
forest_gnomish_lineage = ("You are part of a gnomish lineage that grants you supernatural abilities. You are a Forest Gnome, the lineage of magic-filled forests. You know the Minor Illusion cantrip. You can also cast the Speak with Animals Spell with this trait. You can cast it with the trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest. You can also use any Spell Slots you have to cast the Spell. Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", forest_gnome_spells)
rock_gnomish_lineage = ("You are part of a gnomish lineage that grants you supernatural abilities. You are a Rock Gnome, the lineage of primeval mountains. You know the Mending and Prestidigitation cantrips. In addition, you can spend 10 minutes casting Prestidigitation to create a Tiny clockwork device (AC 5, 1 HP), such as a toy, a fire starter, or a music box. Casting the Spell in this way consumes 10 GP worth of raw material (string, gears, and the like), which you provide during the casting. When you create the device, you determine its function by choosing one effect from Prestidigitation; the device produces that effect whenever you or another creature takes a Bonus Action to touch the device and activate it. If the chosen effect has options within it, you choose one of those options for the device when you create it. For example, if you choose the spell’s ignite-extinguish effect, you determine whether the device ignites or extinguishes fire; the device doesn’t do both. You can have three such devices in existence at a time, and each one dismantles itself 8 hours after its creation. You can also touch one of your devices and dismantle it as an Action. After a device is dismantled, the 10 GP of materials used to create it can be reclaimed. Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", rock_gnome_spells)
brave = "You have Advantage on saving throws you make to avoid or end the Frightened Condition on yourself."
halfling_nimbleness = "You can move through the space of any creature that is of a Size larger than yours, but you can’t stop there."
luck = "When you roll a 1 on the d20 of a d20 Test, you can reroll the die, and you must use  the new roll."
naturally_stealthy = ("You have Proficiency in the Stealth Skill.", (1, ("Stealth", "Stealth")))
adrenaline_rush = "You can take the Dash  Action as a Bonus Action. When you do so, you gain a number of Temporary Hit Points equal to  your Proficiency Bonus. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all  expended uses when you finish a Long Rest."
powerful_build = "You count as one Size larger when determining your carrying capacity and  the weight you can push, drag, or lift."
relentless_endurance = "When you are reduced to 0 Hit Points but not killed outright, you can drop to 1 Hit Point instead. Once you use this trait, you can’t do so again until you finish a Long Rest."
abyssal_fiendish_legacy = ("You are the recipient of a fiendish legacy that grants you supernatural abilities. You are Abyssal, associated with Chaotic Evil planes. Starting at 1st level You have Resistance to Poison Damage. You also know the Poison Spray cantrip. Starting at 3rd level you know the Ray of Sickness spell. Starting at 5th level you know the Hold Person spell. Once you cast the Spell with this trait, you can’t cast that Spell with it again until you finish a Long Rest;however, you can cast the Spell using any SpellSlots you have of the appropriate level.Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", abyssal_tiefling_spells)
chthonic_fiendish_legacy = ("You are the recipient of a fiendish legacy that grants you supernatural abilities. You are Abyssal, associated with Chaotic Evil planes; Chthonic, associated with Neutral Evil planes; or Infernal, associated with Lawful Evil planes. Starting at 1st level You have Resistance to Necrotic Damage. You also know the Chill Touch cantrip. Starting at 3rd level you know the False Life spell. Starting at 5th level you know the Ray of Enfeeblement spell. Once you cast the Spell with this trait, you can’t cast that Spell with it again until you finish a Long Rest;however, you can cast the Spell using any SpellSlots you have of the appropriate level.Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", chthonic_tiefling_spells)
infernal_fiendish_legacy = ("You are the recipient of a fiendish legacy that grants you supernatural abilities. You are Abyssal, associated with Chaotic Evil planes; Chthonic, associated with Neutral Evil planes; or Infernal, associated with Lawful Evil planes. Starting at 1st level You have Resistance to Fire Damage. You also know the Fire Bolt cantrip. Starting at 3rd level you know the Hellish Rebuke spell. Starting at 5th level you know the Darkness spell. Once you cast the Spell with this trait, you can’t cast that Spell with it again until you finish a Long Rest;however, you can cast the Spell using any SpellSlots you have of the appropriate level.Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage).", infernal_tiefling_spells)
otherworldly_presence = ("You know the Thaumaturgy cantrip. When you cast it with this trait, the Spell uses the same spellcasting ability you use for your Fiendish Legacy trait.", (tiefling_spells))
black_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a black dragon which is connected to acid damage. You display coloration and other features reminiscent of that dragon type."
blue_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a blue dragon which is connected to lightning damage. You display coloration and other features reminiscent of that dragon type."
brass_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a brass dragon which is connected to fire damage. You display coloration and other features reminiscent of that dragon type."
bronze_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a bronze dragon which is connected to lightning damage. You display coloration and other features reminiscent of that dragon type."
copper_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a copper dragon which is connected to acid damage. You display coloration and other features reminiscent of that dragon type."
gold_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a gold dragon which is connected to fire damage. You display coloration and other features reminiscent of that dragon type."
green_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a green dragon which is connected to poison damage. You display coloration and other features reminiscent of that dragon type."
red_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a red dragon which is connected to fire damage. You display coloration and other features reminiscent of that dragon type."
silver_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a silver dragon which is connected to cold damage. You display coloration and other features reminiscent of that dragon type."
white_draconic_ancestry = "Your lineage stems from a dragon progenitor. You Draconic ancestor was a white dragon which is connected to cold damage. You display coloration and other features reminiscent of that dragon type."
breath_weapon = "When you take the Attack Action on your turn, you can replace one of your attacks with an exhalation of magical energy in either a 15-foot cone or a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity Saving Throw against a DC equal to 8 + your Constitution modifier + your Proficiency Bonus. On a failed save, a creature takes 1d10 damage of the type determined by your Draconic Ancestry trait. On a successful save, a creature takes half as much damage. This damage increases by 1d10 when you reach the following character levels: 5th level (2d10), 11th level (3d10), and 17th level (4d10).You can use this Breath Weapon a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."
damage_resistance = "You have Resistance to the damage type determined by your Draconic Ancestry trait."
draconic_flight = "When you reach 5th level, you learn how to channel the magical energy of your Draconic Ancestry to give yourself temporary flight. As a Bonus Action, you sprout spectral wings on your back that last for 10 minutes or until you are Incapacitated or you retract the wings as a Bonus Action. During that time, you have a Fly Speed equal to your Speed. Your wings appear to be made of the energy used by your Breath Weapon. Once you use this trait, you can’t use it again until you finish a Long Rest."
large_form = "Starting at 5th level, you gain the ability to supernaturally grow. As a Bonus Action, you change your Size to Large, provided you’re in a big enough space. This transformation lasts for 10 minutes or until you end it as a Bonus Action. During that duration, you have Advantage on Strength Checks, and your Sped increases by 10 feet. Once you use this trait, you can’t use it again until you finish a Long Rest."
clouds_jaunt = "You are descended from Cloud Giants. As a Bonus Action, you magically Teleport up to 30 feet to an unoccupied space you can see. You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest"
fires_burn = "You are descended from Fire Giants. When you hit a target with an Attack Roll and deal damage to it, you can also deal 1d10 Fire Damage to that target. You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest"
frosts_chill = "You are descended from Frost Giants. When you hit a target with an Attack Roll and deal damage to it, you can also deal 1d6 Cold Damage to that target and reduce its Speed by 10 feet until the start of your next turn. You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest"
hills_tumble = "You are descended from Hill Giants. When you hit a Large or smaller creature with an Attack Roll and deal damage to it, you can knock thattarget Prone. You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest"
stones_endurance = "You are descended from Stone Giants. When you take damage, you can use your Reaction to roll a d12. Add your Constitution modifier to the number rolled and reduce the damage by that total. You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest"
storms_thunder = "You are descended from Storm Giants. When you take damage from a creature within 60 feet of you, you can use your Reaction to deal 1d8 Thunder Damage to that creature. You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest"







# still need to figure out how to deal with spells



human_special_traits = [resourceful, skillfull, versatile]

dwarf_special_traits = (darkvision, dwarven_resilience, dwarven_toughness, forge_wise, stonecunning)
drow_elf_special_traits = (darkvision, drow_elven_lineage, fey_ancestry, keen_senses, trance)
high_elf_special_traits = (darkvision, high_elven_lineage, fey_ancestry, keen_senses, trance)
wood_elf_special_traits = (darkvision, wood_elven_lineage, fey_ancestry, keen_senses, trance)
forest_gnome_special_traits = (darkvision, gnomish_cunning, forest_gnomish_lineage)
rock_gnome_special_traits = (darkvision, gnomish_cunning, rock_gnomish_lineage)
halfling_special_traits = (brave, halfling_nimbleness, luck, naturally_stealthy)
orc_special_traits = (adrenaline_rush, darkvision, powerful_build, relentless_endurance)
abyssal_tiefling_special_traits = (darkvision, abyssal_fiendish_legacy, otherworldly_presence)
chthonic_tiefling_special_traits = (darkvision, chthonic_fiendish_legacy, otherworldly_presence)
infernal_tiefling_special_traits = (darkvision, infernal_fiendish_legacy, otherworldly_presence)
black_dragonborn_special_traits = (black_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
blue_dragonborn_special_traits = (blue_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
brass_dragonborn_special_traits = (brass_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
bronze_dragonborn_special_traits = (bronze_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
copper_dragonborn_special_traits = (copper_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
gold_dragonborn_special_traits = (gold_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
green_dragonborn_special_traits = (green_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
red_dragonborn_special_traits = (red_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
silver_dragonborn_special_traits = (silver_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
white_dragonborn_special_traits = (white_draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
cloud_goliath_special_traits = (clouds_jaunt, large_form, powerful_build)
fire_goliath_special_traits = (fires_burn, large_form, powerful_build)
frost_goliath_special_traits = (frosts_chill, large_form, powerful_build)
hill_goliath_special_traits = (hills_tumble, large_form, powerful_build)
stone_goliath_special_traits = (stones_endurance, large_form, powerful_build)
storm_goliath_special_traits = (storms_thunder, large_form, powerful_build)



human = Race("Human", "humanoid", ("medium", "small"), 30, 80, human_special_traits)
dwarf = Race("Dwarf", "humanoid", "medium", 30, 350, dwarf_special_traits)
drow_elf = Race("Drow (Elf)", "Humanoid", "Medium", 30, 750, drow_elf_special_traits)
high_elf = Race("High Elf", "Humanoid", "Medium", 30, 750, high_elf_special_traits)
wood_elf = Race("Wood Elf", "Humanoid", "Medium", 35, 750, wood_elf_special_traits)
forest_gnome = Race("Forest Gnome", "Humanoid", "small", 30, 425, forest_gnome_special_traits)
rock_gnome = Race("Rock Gnome", "Humanoid", "small", 30, 425, rock_gnome_special_traits)
halfling = Race("Halfling", "Humanoid", "Small", 30, 150, halfling_special_traits)
orc = Race("Orc", "humanoid", "Medium", 30, 80, orc_special_traits)
abyssal_tiefling = Race("Tiefling (Abyssal)","Humanoid", ("Medium", "Small"), 30, 100, abyssal_tiefling_special_traits)
chthonic_tiefling = Race("Tiefling (Chthonic)","Humanoid", ("Medium", "Small"), 30, 100, chthonic_tiefling_special_traits)
infernal_tiefling = Race("Tiefling (Infernal)","Humanoid", ("Medium", "Small"), 30, 100, infernal_tiefling_special_traits)
black_dragonborn = Race("Dragonborn (Black)", "Humanoid", "Medium", 30, 80, black_dragonborn_special_traits)
blue_dragonborn = Race("Dragonborn (Blue)", "Humanoid", "Medium", 30, 80, blue_dragonborn_special_traits)
brass_dragonborn = Race("Dragonborn (Brass)", "Humanoid", "Medium", 30, 80, brass_dragonborn_special_traits)
bronze_dragonborn = Race("Dragonborn (Bronze)", "Humanoid", "Medium", 30, 80, bronze_dragonborn_special_traits)
copper_dragonborn = Race("Dragonborn (Copper)", "Humanoid", "Medium", 30, 80, copper_dragonborn_special_traits)
gold_dragonborn = Race("Dragonborn (Gold)", "Humanoid", "Medium", 30, 80, gold_dragonborn_special_traits)
green_dragonborn = Race("Dragonborn (Green)", "Humanoid", "Medium", 30, 80, green_dragonborn_special_traits)
red_dragonborn = Race("Dragonborn (Red)", "Humanoid", "Medium", 30, 80, red_dragonborn_special_traits)
silver_dragonborn = Race("Dragonborn (Silver)", "Humanoid", "Medium", 30, 80, silver_dragonborn_special_traits)
white_dragonborn = Race("Dragonborn (White)", "Humanoid", "Medium", 30, 80, white_dragonborn_special_traits)
cloud_goliath = Race("Goliath (Cloud)", "Humanoid", "Medium", 35, 80, cloud_goliath_special_traits)
fire_goliath = Race("Goliath (Fire)", "Humanoid", "Medium", 35, 80, fire_goliath_special_traits)
frost_goliath = Race("Goliath (Frost)", "Humanoid", "Medium", 35, 80, frost_goliath_special_traits)
hill_goliath = Race("Goliath (Hill)", "Humanoid", "Medium", 35, 80, hill_goliath_special_traits)
stone_goliath = Race("Goliath (Stone)", "Humanoid", "Medium", 35, 80, stone_goliath_special_traits)
storm_goliath = Race("Goliath (Storm)", "Humanoid", "Medium", 35, 80, storm_goliath_special_traits)


elf = random.choice([drow_elf, high_elf, wood_elf])
gnome = random.choice([rock_gnome, forest_gnome])
tiefling = random.choice([abyssal_tiefling, chthonic_tiefling, infernal_tiefling])
dragonborn = random.choice([black_dragonborn, blue_dragonborn, brass_dragonborn, bronze_dragonborn, copper_dragonborn, gold_dragonborn, green_dragonborn, red_dragonborn, silver_dragonborn, white_dragonborn])
goliath = random.choice([cloud_goliath, fire_goliath, frost_goliath, hill_goliath, stone_goliath, storm_goliath])




race_list = (human, dwarf, elf, gnome, halfling, orc, tiefling, dragonborn, goliath)


