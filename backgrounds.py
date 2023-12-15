
from feats import *



class Background:
    def __init__(self, background_name, ability_improvements, skill_prof, tool_prof, language, feat, equipment):
        self.background_name = background_name
        self.ability_improvements = ability_improvements
        self.skill_prof = skill_prof
        self.tool_prof = tool_prof
        self.language = language
        self.feat = [feat]
        self.equipment = equipment

    def __str__(self):
        return f"{self.background_name}"

acolyte_equipment = {"Book (Prayers)":1, "Calligrapher’s Supplies":1, "Holy Symbol":1, "Parchment":10, "Robe":1, "GP":3}
artisan_equipment = {"Abacus":1, "Artisan’s Tools (you chose)":1, "Merchant’s Scale":1, "Pouch":2, "Traveler’s Clothes":1, "GP":25}
charlatan_equipment = {"Costume":1, "Fine Clothes":1, "Forgery Kit":1, "GP":15}
criminal_equipment = {"Crowbar":1, "Dagger":2, "Pouch":2, "Thieves’ Tools":1, "Traveler’s Clothes":1, "GP":16}
cultist_equipment = {"Bell":1, "Common Clothes":1, "Dagger":1, "Disguise Kit":1, "Lamp":1, "Robe":1, "GP":19}
entertainer_equipment = {"Costume":2, "Musical Instrument (you chose)":1, "Perfume":1, "Steel Mirror":1, "Traveler’s Clothes":1, "GP":8}
farmer_equipment = {"Carpenter’s Tools":1, "Healer’s Kit (uses)": 10, "Iron Pot":1, "Shovel":1, "Sickle":1, "Traveler’s Clothes":1, "GP":23}
gladiator_equipment = {"Chain":1, "Costume":1, "Healer’s Kit":1, "Javelin":6, "Smith’s Tools":1, "Traveler’s Clothes":1, "GP":15}
guard_euipment = {"Crossbow Bolt":20, "Gaming Set (you choice)":1, "Hooded Lantern":1, "Light Crossbow":1, "Manacles":1, "Quiver":1, "Spear":1, "Traveler’s Clothes":1, "GP":12}
guide_equipment = {"Arrow":20, "Bedroll":1, "Cartographer’s Tools":1, "Fishing Tackle":1, "Quiver":1, "Shortbow":1, "Tent":1, "Traveler’s Clothes":1, "GP":2}
hermit_equipment = {"Bedroll":1, "Book (Philosophy)":1, "Fishing Tackle":1, "Herbalism Kit":1, "Lamp":1, "Oil (flasks)":3, "Quarterstaff":1, "Traveler’s Clothes":1, "GP":15}
laborer_equipment = {"Bullseye Lantern":1, "Common Clothes":1, "Handaxe":1, "Light Hammer":1, "Mason’s Tools":1, "Mess Kit":1, "Oil (flask)":1, "Shovel":1, "Waterskin":1, "GP":15}
noble_equipment = {"Fine Clothes":1, "Gaming Set":1, "Perfume":1, "Signet Ring":1, "GP":24}
pilgrim_equipment = {"Bedroll":1, "Healer’s Kit":1, "Holy Symbol":1, "Musical Instrument":1, "Daily Rations":2, "Traveler’s Clothes":1, "GP":16}
sage_equipment = {"Book (History)":1, "Calligrapher’s Supplies":1, "Parchment":8, "Quarterstaff":1, "Robe":1, "GP":8}
sailor_equipment = {"Dagger":1, "Fishing Tackle":1, "Navigator’s Tools":1, "Silk Rope":1, "Traveler’s Clothes":1, "GP":30}
soldier_equipmnet = {"Arrow":20, "Gaming Set (you chose)":1, "Healer’s Kit":1, "Quiver":1, "Shortbow":1, "Spear":1, "Traveler’s Clothes":1, "GP":14}
urchin_equipment = {"Bedroll":1, "Common Clothes":1, "Dagger":2, "Gaming Set":1}



acolyte = Background("Acolyte", ("Wisdom", "Intelligence"), ("Insight", "Religon"), "calligrapher's supplies", "Celestial", magic_initiate_divine, acolyte_equipment)
artisan = Background("Artisan", ("Intelligence", "Charisma"), ("Investigation", "Persuasion"), "Artisans's Tools(your choice)", "Gnomish", crafter, artisan_equipment)
charlatan = Background("Charlatan", ("Charisma", "Dexterity"),("Deception", "Sleight of Hand"), "Forgery Kit", "Infernal", skilled, charlatan_equipment)
criminal = Background("Criminal", ("Dexterity", "Intelligence"), ("Slight of Hand", "Stealth"), "Thieves' Tools", "Thieves' Cant", alert, criminal_equipment)
cultist = Background("Cultist", ("Intelligence", "Charisma"), ("Arcana", "Religion"), "Disguise Kit", "Abyssal", magic_initiate_arcane, cultist_equipment)
entertainer = Background("Entertainer", ("Charisma", "Dexterity"), ("Acrobatics", "Performance"), "Musical Instrument (your choice)", "Elvish", musician, entertainer_equipment)
farmer = Background("Farmer", ("Constitution", "Wisdom"), ("Animal Handling", "Nature"), "Carpernter's Tools", "Halfling", tough, farmer_equipment)
gladiator = Background("Gladiator", ("Strength", "Charisma"), ("Athletics", "Performance"), "Smith's Tools", "Orc", savage_attacker, gladiator_equipment)
guard = Background("Guard", ("Strength", "Wisdom"), ("Athletics", "Perception"), "Gaming Set (you chose)", "Dwarvish", alert, guard_euipment)
guide = Background("Guide", ("Wisdom", "Dexterity"), ("Stealth", "Survival"), "Cartographer's Tools", "Giant", magic_initiate_primal, guide_equipment)
hermit = Background("Hermit", ("Wisdom", "Constitution"), ("Medicine", "Religion"), "Herbalism Kit", "Sylvan", magic_initiate_primal, hermit_equipment)
laborer = Background("Laborer", ("Constitution", "Strength"), ("Athletics", "Survival"), "Mason's Tools", "Dwarvish", tough, laborer_equipment)
noble = Background("Noble", ("Charisma", "Intelligence"), ("History", "Persuasion"), "Gaming Set (you chose)", "Draconic", skilled, noble_equipment)
pilgrim = Background("Pilgrim", ("Wisdom", "Constitution"), ("Religion", "Survival"), "Musical Instrument (your choice)", "Halfling", healer, pilgrim_equipment)
sage = Background("Sage", ("Intelligence", "Wisdom"), ("Arcana", "History"), "Calligrapher's Supplies", "Elvish", magic_initiate_arcane, sage_equipment)
sailor = Background("Sailor", ("Dexterity", "Wisdom"), ("Acrobatics", "Perception"), "Navogator's Tools", "Primordial", tavern_brawler, sailor_equipment)
soldier = Background("Soldier", ("Strength", "Constitution"), ("Athletics", "Intimidation"), "Gaming Set (your choice)", "Goblin", savage_attacker, soldier_equipmnet)
urchin = Background("Urchin", ("Dexterity", "Wisdom"), ("Insight", "Stealth"), "Thieves' Tools", "Common Sign Language", lucky, urchin_equipment)


all_backgrounds = (acolyte, artisan, charlatan, criminal, cultist, entertainer, farmer, gladiator, guard, guide, hermit, laborer, noble, pilgrim, sage, sailor, soldier, urchin)



