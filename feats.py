class Feat:
    def __init__(self, feat_name, feat_features):
        self.feat_name = feat_name
        self.feat_features = feat_features


    def __str__(self):
        return f"{self.feat_name}"



alert_features = ()
crafter_features = ()
healer_features = ()
lucky_features = ()
magic_initiate_arcane_features = ()
magic_initiate_divine_features = ()
magic_initiate_primal_features = ()
musician_features = ()
savage_attacker_features = ()
skilled_features = ()
tavern_brawler_features = ()
tough_features = ()


alert = Feat("Alert", alert_features)
crafter = Feat("Crafter", crafter_features)
healer = Feat("Healer", healer_features)
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

