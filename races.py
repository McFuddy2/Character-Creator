


# so far only Dwarf and human have been added


class Race:
    def __init__(self, race_name, creature_type, size, speed_in_feet, life_span_in_years, special_traits):
        self.race_name = race_name
        self.creature_type = creature_type
        self.size  = size
        self.speed_in_feet = speed_in_feet
        self.life_span_in_years =  life_span_in_years
        self.special_traits = special_traits

    def __str__(self):
        return f"{self.race_name}"
    

resourceful = "You gain Inspiration whenever you finish a Long Rest"
skillfull = "You gain Proficiency in one Skill of your choice "
versatile = "You gain the Skilled Feat or another 1st-level Feat of your choice"
darkvision = "You have Darkvision with a range of 60 feet."
dwarven_resilience = "You have Resistance to Poison Damage. You also have Advantage on saving throws you make to avoid or end the Poisoned Condition on yourself."
dwarven_toughness = "Your Hit Point Maximum increases by 1, and it increases by 1 again whenever you gain a level"
forge_wise = "Your divine creator gave you an uncanny affinity for working with stone or metal. You gain Tool Proficiency with two of the following options of your choice: Jeweler’s Tools, Mason’s Tools, Smith’s Tools, or Tinker’s Tools"
stonecunning = "As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes. You must be on a stone surface or touching such a surface to use this Tremorsense. The stone can be natural or worked. You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."
elven_lineage = "You are part of an elven lineage that grants you supernatural abilities. Choose a lineage from the Elven Lineages table: Drow, the lineage of the Underdark; High Elf, the lineage of fey crossings and other magical locations; or Wood Elf, the lineage of primeval forests. You gain the 1st-level benefit of that lineage. Starting at 3rd level and again at 5th level, you also gain the ability to cast a Spell with this trait. Once you cast the Spell with this trait, you can’t cast that Spell with it again until you finish a Long Rest*; however, you can cast the Spell using any Spell Slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage)."
fey_ancestry = "You have Advantage on saving throws you make to avoid or end the Charmed Condition on yourself."
keen_senses = "You have Proficiency in the Perception Skill."
trance = "You don’t need to sleep, and magic can’t put you to sleep. You can finish a Long Rest* in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness."
gnomish_cunning = "You have Advantage on Intelligence, Wisdom, and Charisma saving  throws."
gnomish_lineage = "You are part of a gnomish lineage that grants you supernatural abilities. Choose a lineage from the Gnomish Lineages table: Forest Gnome, the lineage of magic-filled forests, or Rock Gnome, the lineage of primeval mountains. You gain the benefits of that lineage. Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage)."
brave = "You have Advantage on saving throws you make to avoid or end the Frightened Condition on yourself."
halfling_nimbleness = "You can move through the space of any creature that is of a Size larger than yours, but you can’t stop there."
luck = "When you roll a 1 on the d20 of a d20 Test,* you can reroll the die, and you must use  the new roll."
naturally_stealthy = "You have Proficiency in the Stealth Skill."
adrenaline_rush = "You can take the Dash  Action as a Bonus Action. When you do so, you gain a number of Temporary Hit Points equal to  your Proficiency Bonus. You can use this trait a number of times equal to your Proficiency Bonus, and you regain all  expended uses when you finish a Long Rest."
powerful_build = "You count as one Size larger when determining your carrying capacity and  the weight you can push, drag, or lift."
relentless_endurance = "When you are reduced to 0 Hit Points but not killed outright, you can drop to 1 Hit Point instead. Once you use this trait, you can’t do so again until you finish a Long Rest."
fiendish_legacy = "You are the recipient of a fiendish legacy that grants you supernatural abilities. Choose a legacy from the FiendishLegacies table: Abyssal, associated with Chaotic Evil planes; Chthonic, associated with Neutral Evil planes; or Infernal, associated with Lawful Evil planes. You gain the 1st-level benefit of the chosen legacy.Starting at 3rd level and again at 5th level, you gain the ability to cast a higher-level Spellwith this trait, as shown on the table. Once you cast the Spell with this trait, you can’t cast that Spell with it again until you finish a Long Rest;however, you can cast the Spell using any SpellSlots you have of the appropriate level.Intelligence, Wisdom, or Charisma is your spellcasting ability for the Spells you cast with this trait (choose the ability when you select the lineage)."
otherworldly_presence = "You know the Thaumaturgy cantrip. When you cast it with this trait, the Spell uses the same spellcasting ability you use for your Fiendish Legacy trait."
draconic_ancestry = "Your lineage stems from a dragon progenitor. Choose the kind of dragon from the Draconic Ancestor table. Your choice affects your Breath Weapon and Damage Resistance traits, as well as the look of your Draconic Flight. The chosen dragon also affects your appearance, with you displaying coloration and other features reminiscent of that dragon."
breath_weapon = "When you take the Attack Action on your turn, you can replace one of your attacks with an exhalation of magical energy in either a 15-foot cone or a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity Saving Throw against a DC equal to 8 + your Constitution modifier + your Proficiency Bonus. On a failed save, a creature takes 1d10 damage of the type determined by your Draconic Ancestry trait. On a successful save, a creature takes half as much damage. This damage increases by 1d10 when you reach the following character levels: 5th level (2d10), 11th level (3d10), and 17th level (4d10).You can use this Breath Weapon a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."
damage_resistance = "You have Resistance to the damage type determined by your Draconic Ancestry trait."
draconic_flight = "When you reach 5th level, you learn how to channel the magical energy of your Draconic Ancestry to give yourself temporary flight. As a Bonus Action, you sprout spectral wings on your back that last for 10 minutes or until you are Incapacitated or you retract the wings as a Bonus Action. During that time, you have a Fly Speed equal to your Speed. Your wings appear to be made of the energy used by your Breath Weapon. Once you use this trait, you can’t use it again until you finish a Long Rest."
giant_ancestry = "You are descended from Giants. Choose one of the following benefits—a supernatural boon from your ancestry; you can use the chosen benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest:"
large_form = ". Starting at 5th level, you gain the ability to supernaturally grow. As a Bonus Action, you change your Size to Large, provided you’re in a big enough space. This transformation lasts for 10 minutes or until you end it as a Bonus Action. During that duration, you have Advantage on Strength Checks, and your Sped increases by 10 feet. Once you use this trait, you can’t use it again until you finish a Long Rest."









# choices need to be added and made: elven_lineage, gnomish lineage, fiendish legacy, drconic ancestry, giant ancestry
# need to find a way to make all these strings turn into appropriate meta data

human_special_traits = (resourceful, skillfull, versatile)
dwarf_special_traits = (darkvision, dwarven_resilience, dwarven_toughness, forge_wise, stonecunning)
elf_special_traits = (darkvision, elven_lineage, fey_ancestry, keen_senses, trance)
gnome_special_traits = (darkvision, gnomish_cunning, gnomish_lineage)
halfling_special_traits = (brave, halfling_nimbleness, luck, naturally_stealthy)
orc_special_traits = (adrenaline_rush, darkvision, powerful_build, relentless_endurance)
tiefling_special_traits = (darkvision, fiendish_legacy, otherworldly_presence)
dragonborn_special_traits = (draconic_ancestry, breath_weapon, damage_resistance, darkvision, draconic_flight)
goliath_special_traits = (giant_ancestry, large_form, powerful_build)



human = Race("Human", "humanoid", ("medium", "small"), 30, 80, human_special_traits)
dwarf = Race("Dwarf", "humanoid", "medium", 30, 350, dwarf_special_traits)
elf = Race("Elf", "Humanoid", "Medium", 30, 750, elf_special_traits)
gnome = Race("Gnome", "Humanoid", "small", 30, 425, gnome_special_traits)
halfling = Race("Halfling", "Humanoid", "Small", 30, 150, halfling_special_traits)
orc = Race("Orc", "humanoid", "Medium", 30, 80, orc_special_traits)
tiefling = Race("Tiefling","Humanoid", ("Medium", "Small"), 30, 100, tiefling_special_traits)
dragonborn = Race("Dragonborn", "Humanoid", "Medium", 30, 80, dragonborn_special_traits)
goliath = Race("Goliath", "Humanoid", "Medium", 35, 80, goliath_special_traits)




race_list = (human, dwarf, elf, gnome, halfling, orc, tiefling, dragonborn, goliath)


