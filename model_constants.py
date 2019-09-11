
"""Keeping things simple for now - can divide into tackles/baits"""
BAIT_TYPE = ("Baitbug", "Balloon Bug", "Blue Bobbit", "Bream Lure", "Fruit Worm", "Giant Crane Fly", "Goblin Jig", "Live Shrimp", "Magma Worm", "Midge Larva", "Moyebi Shrimp", "Nightcrawler", "Pill Bug", "Robber Ball", "Salmon Roe", "Sand Leech", "Short Bill Minnow", "Silkworm", "Spoon Worm", "Stonefly Larva", "Suspending Minnow")

"""There are three weather intervals a day - one from 12am-8am, 8am-4pm, 4pm-12am"""
WEATHER_INTERVALS = {
    first = {
        start: "00:00", 
        end: "08:00"
    },
    second = {
        start: "16:00", 
        end: "00:00"
    },
    third = {
        start: "08:00", 
        end: "16:00"
    }
}

# WEATHER_INTERVALS = {
#         start1: "00:00", 
#         end1: "08:00",
#         start2: "16:00", 
#         end2: "00:00",
#         start3: "08:00", 
#         end3: "16:00"
# }

# WEATHER_CONDITIONS = ("Blizzard", "Clear Skies", "Clouds", "Dust Storms", 
#     "Fair Skies", "Fog", "Gales", "Heat Waves", "Rain", "Sandstorms", "Showers", 
#     "Snow", "Thunder", "Thunderstorms", "Umbral Static", "Umbral Wind", "Wind")

REGIONS = ("Thanalan", "The Black Shroud", "La Noscea", "Mor Dhona", "Coerthas", "Abalathia", "Dravania", "Gyr Abania")


SUBREGIONS = 

# Dravania

"Idyllshire", "The Dravanian Forelands", "The Dravanian Hinterlands", "The Churning Mists"

# Gyr Abania

"Rhalgr's Reach", "The Fringes", "The Lochs", "The Peaks"

# Othard

"Kugane", "The Azim Steppe", "The Ruby Sea", "Yanxia"

# Norvandt

"Crystarium", "Lakeland", "Eulmore", "Kholusia", "Amh Araeng", "Il Mheg", "The Rak'tika Greatwood", "The Tempest"

FISHING_HOLES = 


# Eventually add spearfishing?
# FISHING_TYPE = ("Fishing", "Spearfishing")
# JIG_TYPES = ("Small", "Medium", "Large")