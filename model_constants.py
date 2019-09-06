
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

WEATHER_CONDITIONS = ("Blizzard", "Clear Skies", "Clouds", "Dust Storms", 
    "Fair Skies", "Fog", "Gales", "Heat Waves", "Rain", "Sandstorms", "Showers", 
    "Snow", "Thunder", "Thunderstorms", "Umbral Static", "Umbral Wind", "Wind")

# Eventually add spearfishing?
# FISHING_TYPE = ("Fishing", "Spearfishing")
# JIG_TYPES = ("Small", "Medium", "Large")