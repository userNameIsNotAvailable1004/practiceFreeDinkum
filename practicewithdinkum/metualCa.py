# sprinkler = {"Copper Bar":5, "Quartz Crystal":4, "Old Spring":4, "Old Gear":4}
import re
# r'\d+'
sprinkler = {"mat":["Copper Bar","Quartz Crystal","Old Spring","Old Gear"]
            ,"num":[5,4,4,4]
            ,"output":1
            ,"name":"Sprinkler"}

# locaDataSear =[{'mat': ['Copper Bar', 'Quartz Crystal', 'Old Spring', 'Old Gear'], 'num': [5, 4, 4, 4], 'output': 1, 'name': 'Sprinkler'}, {'name': 'Advanced Sprinkler', 'output': 1, 'mat': ['Sprinkler', 'Iron Bar', 
# 'Old Gear', 'Old Spring', 'Hot Cylinder'], 'num': [1, 5, 4, 4, 1]}, {'name': 'Animal Collection Point', 'output': 1, 'mat': ['Palm Wood Plank', 'Hard Wood Plank', 'Nails'], 'num': [2, 2, 1]}, {'name': 'Animal Den', 'output': 1, 'mat': ['Bag of Cement', 'Stone', 'Palm Wood Plank', 'Copper Bar', 'Iron Ore'], 'num': [10, 10, 6, 4, 4]}, {'name': 'Animal Feeder', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [2, 2]}, {'name': 'Animal Stall', 'output': 1, 'mat': ['Iron Bar', 'Spinifex Tuft', 'Hard Wood Plank', 'Tin Sheet', 'Nails'], 'num': [3, 2, 8, 2, 8]}, {'name': 'Animal Trap', 'output': 1, 
# 'mat': ['Iron Bar', 'Hard Wood Plank', 'Old Spring'], 'num': [1, 1, 2]}, {'name': 'Arrow Light', 'output': 2, 'mat': ['Quartz Crystal', 'Glass Bulb', 'Ruby Shard'], 'num': [5, 3, 1]}, {'name': 'Basic Hammer', 'output': 1, 'mat': ['Gum Wood Plank', 'Tin Bar'], 'num': [1, 3]}, {'name': 'Basic Spear', 'output': 1, 'mat': ['Gum Wood Plank', 'Tin Bar'], 'num': [1, 1]}, {'name': 'Beach Bar', 'output': 1, 'mat': ['Spinifex Tuft', 'Palm Wood Plank', 'Nails'], 'num': [4, 4, 4]}, {'name': 'Bee House', 'output': 1, 'mat': ['Iron Bar', 'Spinifex Resin', 'Hard Wood Plank', 'Queen Bee'], 'num': [2, 2, 4, 1]}, {'name': 'Billy Can Kit', 'output': 1, 'mat': ['Campfire', 'Tin Bar'], 'num': [1, 2]}, {'name': 'Bird Coop', 'output': 1, 'mat': ['Copper Bar', 'Spinifex Tuft', 'Tin Sheet', 'Gum Wood Plank', 'Nails'], 'num': [4, 4, 2, 3, 4]}, {'name': 'Black Tile Path', 'output': 16, 'mat': ['Black Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Blue Floor Light', 'output': 2, 'mat': ['Aquamarine Shard', 'Tin Sheet', 'Glass Bulb'], 'num': [1, 2, 1]}, {'name': 'Blue Tile Path', 'output': 16, 'mat': ['Blue Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Brick Bridge', 'output': 1, 'mat': ['Bag of Cement', 'Stone'], 'num': [4, 15]}, {'name': 'Brick Fence', 'output': 8, 'mat': ['Stone', 'Bag of Cement'], 'num': [2, 1]}]

locaDataSear = [{'mat': ['Copper Bar', 'Quartz Crystal', 'Old Spring', 'Old Gear'], 'num': [5, 4, 4, 4], 'output': 1, 'name': 'Sprinkler'}, {'name': 'Advanced Sprinkler', 'output': 1, 'mat': ['Sprinkler', 'Iron Bar', 
'Old Gear', 'Old Spring', 'Hot Cylinder'], 'num': [1, 5, 4, 4, 1]}, {'name': 'Animal Collection Point', 'output': 1, 'mat': ['Palm Wood Plank', 'Hard Wood Plank', 'Nails'], 'num': [2, 2, 1]}, {'name': 'Animal Den', 'output': 1, 'mat': ['Bag of Cement', 'Stone', 'Palm Wood Plank', 'Copper Bar', 'Iron Ore'], 'num': [10, 10, 6, 4, 4]}, {'name': 'Animal Feeder', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [2, 2]}, {'name': 'Animal Stall', 'output': 1, 'mat': ['Iron Bar', 'Spinifex Tuft', 'Hard Wood Plank', 'Tin Sheet', 'Nails'], 'num': [3, 2, 8, 2, 8]}, {'name': 'Animal Trap', 'output': 1, 
'mat': ['Iron Bar', 'Hard Wood Plank', 'Old Spring'], 'num': [1, 1, 2]}, {'name': 'Arrow Light', 'output': 2, 'mat': ['Quartz Crystal', 'Glass Bulb', 'Ruby Shard'], 'num': [5, 3, 1]}, {'name': 'Basic Hammer', 'output': 1, 'mat': ['Gum Wood Plank', 'Tin Bar'], 'num': [1, 3]}, {'name': 'Basic Spear', 'output': 1, 'mat': ['Gum Wood Plank', 'Tin Bar'], 'num': [1, 1]}, {'name': 'Beach Bar', 'output': 1, 'mat': ['Spinifex Tuft', 'Palm Wood Plank', 'Nails'], 'num': [4, 4, 4]}, {'name': 'Bee House', 'output': 1, 'mat': ['Iron Bar', 'Spinifex Resin', 'Hard Wood Plank', 'Queen Bee'], 'num': [2, 2, 4, 1]}, {'name': 'Billy Can Kit', 'output': 1, 'mat': ['Campfire', 'Tin Bar'], 'num': [1, 2]}, {'name': 'Bird Coop', 'output': 1, 'mat': ['Copper Bar', 'Spinifex Tuft', 'Tin Sheet', 'Gum Wood Plank', 'Nails'], 'num': [4, 4, 2, 3, 4]}, {'name': 'Black Tile Path', 'output': 16, 'mat': ['Black Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Blue Floor Light', 'output': 2, 'mat': ['Aquamarine Shard', 'Tin Sheet', 'Glass Bulb'], 'num': [1, 2, 1]}, {'name': 'Blue Tile Path', 'output': 16, 'mat': ['Blue Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Brick Bridge', 'output': 1, 'mat': ['Bag of Cement', 'Stone'], 'num': [4, 15]}, {'name': 'Brick Fence', 'output': 8, 'mat': ['Stone', 'Bag of Cement'], 'num': [2, 1]}, {'name': 'Stone', 'output': 5, 'mat': ['Sprinkler', 'Bag of Cement'], 'num': [1, 5]}, {'name': 'Brick Path', 'output': 8, 'mat': ['Stone'], 'num': [2]}, {'name': 'Stone Steps', 'output': 4, 'mat': ['Stone', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Brick Well', 'output': 1, 'mat': ['Stone', 'Bag of Cement', 'Gum Wood Plank'], 'num': [10, 5, 5]}, {'name': 'Bulletin Board', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [6, 8]}, {'name': 'Bunting Festoon', 'output': 1, 'mat': ['Hard Wood Plank', 'Cloth'], 'num': [3, 4]}, {'name': 'Bus Stop', 'output': 1, 'mat': ['Tin Sheet', 'Iron Bar'], 'num': [2, 1]}, {'name': 'Campfire', 'output': 1, 'mat': ['Gum Log', 'Stone', 'Palm Wood', 'Stone', 'Hard Wood Log', 'Stone'], 'num': [2, 3, 2, 3, 2, 3]}, {'name': 'Cement Bird Bath', 'output': 1, 'mat': ['Bag of Cement'], 'num': [5]}, {'name': 'Cement Bridge', 'output': 1, 'mat': ['Bag of Cement', 'Tin Bar'], 'num': [15, 1]}, {'name': 'Cement Fence', 'output': 8, 'mat': ['Bag of Cement'], 'num': [4]}, {'name': 'Cement Path', 'output': 8, 'mat': ['Bag of Cement'], 'num': [2]}, {'name': 'Cement Planter', 'output': 1, 'mat': ['Bag of Cement', 'Gum Wood Plank'], 'num': [3, 2]}, {'name': 'Cement Steps', 'output': 4, 'mat': ['Bag of Cement'], 'num': [2]}, {'name': 'Cheese Maker', 'output': 1, 'mat': ['Milking Bucket', 'Iron Bar', 'Old Gear'], 'num': [1, 2, 4]}, {'name': 'Cobblestone Fence', 'output': 8, 'mat': ['Stone', 'Bag of Cement'], 'num': [2, 1]}, {'name': 'Cobblestone Path', 'output': 8, 
'mat': ['Stone', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Cobblestone Road', 'output': 8, 'mat': ['Stone', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Cobblestone Road Lines', 'output': 8, 'mat': ['Stone', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Compost Bin', 'output': 1, 'mat': ['Hard Wood Plank', 'Copper Bar', 'Tin Sheet', 'Nails'], 'num': [8, 3, 1, 15]}, {'name': 'Cooking Table', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails', 'Tin Bar', 'Tin Sheet'], 'num': [5, 2, 1, 1]}, {'name': 'Copper Axe', 'output': 1, 'mat': ['Basic Axe', 'Copper Bar'], 'num': [1, 2]}, {'name': 'Copper Bulb Lamp', 
'output': 1, 'mat': ['Quartz Crystal', 'Copper Bar', 'Glass Bulb'], 'num': [1, 1, 1]}, {'name': 'Copper Fishing Rod', 'output': 1, 'mat': ['Fishing Rod', 'Copper Bar'], 'num': [1, 2]}, {'name': 'Copper Flower Pot', 'output': 1, 'mat': ['Copper Bar'], 'num': [2]}, {'name': 'Copper Hammer', 'output': 1, 'mat': ['Gum Wood Plank', 'Copper Bar'], 'num': [1, 3]}, {'name': 'Copper Hoe', 'output': 1, 'mat': ['Hoe', 'Copper Bar'], 'num': [1, 2]}, {'name': 'Copper Pickaxe', 'output': 1, 'mat': ['Basic Pickaxe', 'Copper Bar'], 'num': [1, 2]}, {'name': 'Copper Scythe', 'output': 1, 'mat': ['Scythe', 'Copper Bar'], 'num': [1, 1]}, {'name': 'Copper Spear', 'output': 1, 'mat': ['Palm Wood Plank', 'Copper Bar'], 'num': [1, 2]}, {'name': 'Copper Top Fence', 'output': 8, 'mat': ['Gum Wood Plank', 'Copper Bar'], 'num': [2, 1]}, {'name': 'Copper Watering Can', 'output': 1, 'mat': ['Watering Can', 'Copper Bar'], 'num': [1, 5]}, {'name': 'Crab Pot', 'output': 1, 'mat': ['Copper Bar', 'Iron Bar', 'Palm Wood Plank', 'Spinifex Resin'], 'num': [3, 1, 4, 2]}, {'name': 'Crafting Table', 'output': 1, 'mat': ['Gum Wood Plank', 'Tin Bar', 'Nails'], 'num': [3, 1, 3]}, {'name': 'Croc Teeth Bat', 'output': 1, 'mat': ['Copper Bar', 'Spinifex Resin', 'Crocodile Tooth', 'Hard Wood Plank'], 'num': [1, 2, 2, 2]}, {'name': 'Crude Fence', 'output': 8, 'mat': ['Gum Log', 'Spinifex Resin'], 'num': [2, 1]}, {'name': 'Crude Furnace', 'output': 1, 'mat': ['Stone', 'Campfire', 'Tin Ore'], 'num': [3, 1, 5]}, {'name': 'Crude Ladder', 'output': 1, 'mat': ['Mangrove Stick'], 'num': [8]}, {'name': 'Curtain Festoon', 'output': 1, 'mat': ['Hard Wood Plank', 'Cloth'], 'num': [3, 4]}, {'name': 'Dunny', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [5, 4]}, {'name': 'Festoon Lights', 'output': 1, 'mat': ['Gum Wood Plank', 'Bright Wire', 'Glass Bulb'], 'num': [2, 4, 3]}, {'name': 'Field Mushroom Lamp', 'output': 1, 'mat': ['Field Mushroom', 'Quartz Crystal', 'Glass Bulb'], 'num': [10, 2, 1]}, {'name': 'Fish Pond', 'output': 1, 'mat': ['Stone', 'Bag of Cement', 'Pearl', 'River Reed Seed', 'Seaweed', 'Crab Pot', 'Gold Fish Trophy', 'Stone', 'Bag of Cement', 'Pearl', 'River Reed Seed', 'Seaweed', 'Crab Pot', 'Silver Fish Trophy', 'Stone', 'Bag of Cement', 'Pearl', 'River Reed Seed', 'Seaweed', 'Crab Pot', 'Bronze Fish Trophy'], 'num': [25, 25, 10, 10, 10, 3, 1, 25, 25, 10, 10, 10, 3, 1, 25, 25, 10, 10, 10, 3, 1]}, {'name': 'Flaming Bat', 'output': 1, 'mat': ['Iron Bar', 'Spinifex Resin', 'Flame Sac', 'Hard Wood Plank'], 'num': [1, 2, 2, 2]}, {'name': 'Flat Top Fence', 'output': 8, 'mat': ['Iron Bar'], 'num': [2]}, {'name': 'Floor Light', 'output': 2, 'mat': ['Quartz Crystal', 'Tin Sheet', 'Glass Bulb'], 'num': [1, 2, 1]}, {'name': 'Flower Pot', 'output': 1, 'mat': ['Bag of Cement'], 'num': [3]}, {'name': 'Garden Light', 'output': 2, 'mat': ['Quartz Crystal', 'Tin Sheet', 'Glass Bulb'], 'num': [1, 2, 1]}, {'name': 'Glass Fence', 'output': 8, 'mat': ['Quartz Crystal', 'Iron Bar'], 'num': [4, 1]}, {'name': 'Grain Mill', 'output': 1, 'mat': ['Gum Wood Plank', 'Old Gear', 'Copper Bar', 'Old Wheel'], 'num': [4, 4, 2, 1]}, {'name': 'Gravel Pathway', 'output': 8, 'mat': ['Stone', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Green Floor Light', 'output': 2, 'mat': ['Emerald Shard', 'Tin Sheet', 'Glass Bulb'], 'num': [1, 2, 1]}, {'name': 'Green Tile Path', 'output': 16, 'mat': ['Green Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Gum Log Seat', 'output': 1, 'mat': ['Gum Log'], 'num': [3]}, {'name': 'Gum Wood Arch', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [4, 2]}, {'name': 'Gum Wood Bench', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [5, 4]}, {'name': 'Gum Wood Bridge', 'output': 1, 'mat': ['Nails', 'Gum Wood Plank'], 'num': [15, 15]}, {'name': 'Gum Wood Double Gate', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [2, 4]}, {'name': 'Gum Wood Entrance Sign', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails', 'Spinifex Resin'], 'num': [5, 4, 1]}, {'name': 'Gum Wood Fence', 'output': 8, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [3, 4]}, {'name': 'Gum Wood Flag Post', 'output': 1, 'mat': ['Gum Wood Fence', 'Nails', 'Cloth'], 'num': [1, 2, 1]}, {'name': 'Gum Wood Flower Bed', 'output': 2, 
'mat': ['Gum Wood Plank', 'Nails'], 'num': [2, 1]}, {'name': 'Gum Wood Gate', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [2, 4]}, {'name': 'Gum Wood Ladder', 'output': 1, 'mat': ['Gum Wood Plank'], 'num': [4]}, {'name': 'Gum Wood Lamp Post', 'output': 1, 'mat': ['Gum Wood Fence', 'Nails', 'Quartz Crystal', 'Wooden Torch'], 'num': [1, 1, 1, 1]}, {'name': 'Gum Wood Market Stall', 'output': 
1, 'mat': ['Cloth', 'Gum Wood Plank', 'Nails'], 'num': [1, 4, 4]}, {'name': 'Gum Wood Path', 'output': 8, 'mat': ['Gum Wood Plank'], 'num': [2]}, {'name': 'Gum Wood Pergola', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails', 'Copper Bar'], 'num': [8, 8, 2]}, {'name': 'Gum Wood Steps', 'output': 4, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [1, 1]}, {'name': 'Gum Wood Table', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [5, 4]}, {'name': 'Gum Wood Tool Rack', 'output': 1, 'mat': ['Gum Wood Plank', 'Iron Bar'], 'num': [10, 2]}, {'name': 'Hard Wood Arch', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails'], 'num': [4, 2]}, {'name': 'Hard Wood Bench', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails'], 'num': [5, 4]}, {'name': 'Hard Wood Bridge', 'output': 1, 'mat': ['Nails', 'Hard Wood Plank'], 'num': [15, 15]}, {'name': 'Hard Wood Double Gate', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails'], 'num': [2, 4]}, {'name': 'Hard Wood Entrance Sign', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails', 
'Spinifex Resin'], 'num': [5, 4, 1]}, {'name': 'Hard Wood Fence', 'output': 8, 'mat': ['Hard Wood Plank', 'Nails'], 'num': [3, 4]}, {'name': 'Hard Wood Flag Post', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails', 'Cloth'], 'num': [1, 2, 1]}, {'name': 'Hard Wood Flower Bed', 'output': 2, 'mat': ['Hard Wood Plank', 'Nails'], 'num': [2, 1]}, {'name': 'Hard Wood Gate', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails'], 'num': [2, 4]}, {'name': 'Hard Wood Ladder', 'output': 1, 'mat': ['Hard Wood Plank'], 'num': [4]}, {'name': 'Hard Wood Lamp Post', 'output': 1, 'mat': ['Hard Wood Fence', 'Nails', 'Quartz Crystal', 'Wooden Torch'], 'num': [1, 1, 1, 1]}, {'name': 'Hard Wood Market Stall', 'output': 1, 'mat': ['Cloth', 'Hard Wood Plank', 'Nails'], 'num': [1, 4, 4]}, {'name': 'Hard Wood Path', 'output': 8, 
'mat': ['Hard Wood Plank'], 'num': [2]}, {'name': 'Hard Wood Pergola', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails', 'Copper Bar'], 'num': [8, 8, 2]}, {'name': 'Hard Wood Steps', 'output': 4, 'mat': 
['Hard Wood Plank', 'Nails'], 'num': [1, 1]}, {'name': 'Hard Wood Table', 'output': 1, 'mat': ['Hard Wood Plank', 'Nails'], 'num': [5, 4]}, {'name': 'Hard Wood Tool Rack', 'output': 1, 'mat': ['Hard Wood Plank', 'Iron Bar'], 'num': [10, 2]},{'name': 'Hardwood Crude Fence', 'output': 8, 'mat': ['Hard Wood Log', 'Spinifex Resin'], 'num': [2, 1]}, {'name': 'Hay Bale', 'output': 1, 'mat': ['Spinifex Tuft'], 'num': [4]}, {'name': 'Hedge', 'output': 8, 'mat': ['Spinifex Tuft', 'Fern Seed', 'Bush Seed'], 'num': [2, 2, 2]}, {'name': 'Hedge Arch', 'output': 1, 'mat': ['Hedge', 'Palm Wood Plank', 'Spinifex Resin'], 'num': [2, 1, 2]}, {'name': 'Honey Comb Path', 'output': 16, 'mat': ['Honey', 'Bag of Cement'], 'num': [1, 2]}, {'name': 'Iron Axe', 'output': 1, 'mat': ['Copper Axe', 'Iron Bar', 'Basic Axe', 'Iron Bar', 'Copper Bar'], 'num': [1, 2, 1, 2, 2]}, {'name': 'Iron Bridge', 'output': 1, 'mat': ['Iron Bar'], 'num': [5]}, {'name': 'Iron Cement Fence', 'output': 8, 'mat': ['Bag of Cement', 'Iron Bar'], 'num': [1, 1]}, {'name': 'Iron Fishing Rod', 'output': 1, 'mat': ['Copper Fishing Rod', 'Iron Bar'], 'num': [1, 2]}, {'name': 'Iron Hammer', 'output': 1, 'mat': ['Hard Wood Plank', 'Iron Bar'], 'num': [2, 3]}, {'name': 'Iron Hoe', 'output': 1, 'mat': ['Copper Hoe', 'Iron Bar'], 'num': [1, 2]}, {'name': 'Iron Ladder', 'output': 1, 'mat': ['Iron Bar'], 'num': [1]}, {'name': 'Iron Path', 'output': 8, 'mat': ['Iron Bar'], 'num': [1]}, {'name': 'Iron Pickaxe', 'output': 1, 'mat': ['Copper Pickaxe', 'Iron Bar', 'Basic Pickaxe', 'Iron Bar', 'Copper Bar'], 'num': [1, 2, 1, 2, 2]}, {'name': 'Iron Scythe', 'output': 1, 'mat': ['Copper Scythe', 'Iron Bar'], 'num': [1, 1]}, {'name': 'Iron Spear', 'output': 1, 'mat': ['Palm Wood Plank', 'Iron Bar'], 'num': [1, 2]}, {'name': 'Iron Watering Can', 'output': 1, 'mat': ['Copper Watering Can', 'Iron Bar'], 'num': [1, 5]}, {'name': 'Iron Wood Bench', 'output': 1, 'mat': ['Palm Wood Plank', 'Iron Bar'], 'num': [5, 2]}, {'name': 'Keg', 'output': 1, 'mat': ['Palm Wood Plank', 'Copper Bar', 'Iron Bar'], 'num': [10, 3, 3]}, {'name': 'Large Cement Fountain', 'output': 1, 'mat': ['Bag of Cement', 'Advanced Sprinkler'], 'num': [15, 1]}, {'name': 'Lattice Fence', 'output': 8, 'mat': ['Palm Wood Plank', 'Mangrove Stick', 'Nails'], 'num': [2, 2, 4]}, {'name': 'Marble Bench', 'output': 1, 'mat': ['Marble'], 'num': [10]}, {'name': 'Marble Fence', 'output': 8, 'mat': ['Marble', 'Vine'], 'num': [5, 5]}, {'name': 
'Marble Path', 'output': 8, 'mat': ['Marble'], 'num': [4]}, {'name': 'Marble Pedestal', 'output': 1, 'mat': ['Marble'], 'num': [10]}, {'name': 'Marble Pillar', 'output': 1, 'mat': ['Marble'], 'num': [25]}, {'name': 'Melon Scarecrow', 'output': 1, 'mat': ['Watermelon', 'Gum Log', 'Spinifex Tuft'], 'num': [1, 2, 8]}, {'name': 'Milk Cap Lamp', 'output': 1, 'mat': ['Milk Cap', 'Quartz Crystal', 'Glass Bulb'], 'num': [10, 2, 1]}, {'name': 'Mushroom Lamp', 'output': 1, 'mat': ['Glowing Mushroom', 'Quartz Crystal', 'Glass Bulb'], 'num': [15, 2, 1]}, {'name': 'Mushroom Path', 'output': 16, 'mat': ['Glowing Mushroom', 'Bag of Cement'], 'num': [4, 2]}, {'name': 'Nails', 'output': 8, 'mat': ['Tin Bar'], 'num': [1]}, {'name': 'Natural Path', 'output': 8, 'mat': ['Stone'], 'num': [2]}, {'name': 'Orange Tile Path', 'output': 16, 'mat': ['Orange Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Palm Wood Arch', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [4, 2]}, {'name': 'Palm Wood Bench', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [5, 4]}, {'name': 'Palm Wood Bridge', 'output': 4, 'mat': ['Nails', 'Palm Wood'], 'num': [15, 15]}, {'name': 'Palm Wood Bridge', 'output': 1, 'mat': 
['Nails', 'Palm Wood Plank'], 'num': [15, 15]}, {'name': 'Palm Wood Double Gate', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [2, 4]}, {'name': 'Palm Wood Entrance Sign', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails', 'Spinifex Resin'], 'num': [5, 4, 1]}, {'name': 'Palm Wood Fence', 'output': 8, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [3, 4]}, {'name': 'Palm Wood Flag Post', 'output': 1, 'mat': ['Palm Wood Fence', 'Nails', 'Cloth'], 'num': [1, 2, 1]}, {'name': 'Palm Wood Gate', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [2, 4]}, {'name': 'Palm Wood Ladder', 'output': 1, 'mat': ['Palm Wood Plank'], 'num': [4]}, {'name': 'Palm Wood Market Stall', 'output': 1, 'mat': ['Cloth', 'Palm Wood Plank', 'Nails'], 'num': [1, 4, 4]}, {'name': 'Palm Wood Path', 'output': 8, 'mat': ['Palm Wood Plank'], 'num': [2]}, {'name': 'Palm Wood Pergola', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails', 'Copper Bar'], 'num': [8, 8, 2]}, {'name': 'Palm Wood Steps', 'output': 4, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [1, 1]}, {'name': 'Palm Wood Table', 'output': 1, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [5, 4]}, {'name': 'Palm Wood Tool Rack', 'output': 1, 'mat': ['Palm Wood Plank', 'Iron Bar'], 'num': [10, 2]}, {'name': 'Pattern Stone Path', 'output': 8, 'mat': ['Stone', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Pearl Path', 'output': 16, 'mat': ['Pearl', 'Bag of Cement'], 'num': [1, 2]}, {'name': 'Picket Fence', 'output': 8, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [3, 4]}, {'name': 'Picket Gate', 'output': 1, 'mat': ['Gum Wood Plank', 'Nails'], 'num': [2, 4]}, {'name': 'Pink Tile Path', 'output': 16, 'mat': ['Pink Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Post Box', 'output': 1, 'mat': ['Iron Bar'], 'num': [2]}, {'name': 'Purple Tile Path', 'output': 16, 
'mat': ['Purple Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Ramp', 'output': 4, 'mat': ['Bag of Cement', 'Palm Wood Plank'], 'num': [2, 2]}, {'name': 'Recycling Bin', 'output': 1, 'mat': ['Palm Wood Plank', 'Gum Wood Plank'], 'num': [1, 2]}, {'name': 'Red Cloth Path', 'output': 16, 'mat': ['Cloth'], 'num': [1]}, {'name': 'Red Floor Light', 'output': 2, 'mat': ['Ruby Shard', 'Tin Sheet', 'Glass Bulb'], 'num': [1, 2, 1]}, {'name': 'Red Roundhead Lamp', 'output': 1, 'mat': ['Red Roundhead', 'Quartz Crystal', 'Glass Bulb'], 'num': [10, 2, 1]}, {'name': 'Red Tile Path', 'output': 16, 'mat': ['Red Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Rock Edge Path', 'output': 8, 'mat': ['Stone'], 'num': [2]}, {'name': 'Rock Path', 'output': 8, 'mat': ['Stone'], 'num': [2]}, {'name': 'Rope Fence', 'output': 8, 'mat': ['Hard Wood Plank', 'Nails', 'Vine'], 'num': [3, 2, 3]}, {'name': 'Rope Ladder', 'output': 1, 'mat': ['Gum Wood Plank', 'Vine'], 'num': [2, 4]}, {'name': 'Rowboat', 'output': 1, 'mat': ['Gum Wood Plank', 'Palm Wood Plank', 'Tin Bar', 'Nails'], 'num': [10, 10, 2, 4]}, {'name': 'Sail Boat', 'output': 1, 'mat': ['Gum Wood Plank', 'Palm Wood Plank', 'Hard Wood Plank', 'Copper Bar', 'Iron Bar', 'Cloth', 'Wooden Chest'], 'num': [15, 15, 15, 10, 10, 10, 1]}, {'name': 'Sand Fence', 'output': 8, 'mat': ['Scallop Shell', 'Buccinidae Shell', 'Cassidae Shell'], 'num': [4, 4, 4]}, {'name': 'Scarecrow', 'output': 1, 'mat': ['Pumpkin', 'Gum Log', 'Spinifex Tuft'], 'num': [1, 2, 8]}, {'name': 'Scythe', 'output': 1, 'mat': ['Palm Wood Plank', 'Tin Bar'], 'num': [1, 1]}, {'name': 'Signwriting Table', 'output': 1, 'mat': ['Hard Wood Plank', 'Iron Bar', 'Copper Bar', 'Nails'], 'num': [5, 1, 1, 8]}, {'name': 'Silo', 'output': 1, 'mat': ['Stone', 'Tin Sheet', 'Bag of Cement', 'Quartz Crystal', 'Iron Bar'], 'num': [25, 15, 10, 8, 5]}, {'name': 'Simple Animal Trap', 'output': 1, 'mat': ['Tin Bar', 'Mangrove Stick', 'Old Spring'], 'num': [1, 8, 1]}, {'name': 'Slippery Jack Lamp', 'output': 1, 'mat': ['Slippery Jack', 'Quartz Crystal', 'Glass Bulb'], 'num': [10, 2, 1]}, {'name': 'Small Cement Fountain', 'output': 1, 'mat': ['Stone', 'Sprinkler', 'Bag of Cement'], 'num': [5, 1, 5]}, {'name': 'Smooth Cement Path', 'output': 8, 'mat': ['Bag of Cement'], 'num': [2]}, {'name': 'Spinning Wheel', 'output': 1, 'mat': ['Palm Wood Plank', 'Old Gear', 'Old Wheel'], 'num': [4, 4, 1]}, {'name': 'Sprinkler', 'output': 1, 'mat': ['Copper Bar', 'Quartz Crystal', 'Old Spring', 'Old Gear'], 'num': [5, 4, 4, 4]}, {'name': 'Storage Barrel', 'output': 1, 'mat': ['Palm Wood Plank', 'Gum Wood Plank', 'Iron Bar'], 'num': [5, 2, 1]}, {'name': 'Street Lamp', 'output': 1, 'mat': ['Quartz Crystal', 'Iron Bar', 'Glass Bulb'], 'num': [1, 1, 1]}, {'name': 'Tiki Torch', 'output': 1, 'mat': ['Palm Wood', 'Wooden Torch'], 'num': [1, 1]}, {'name': 'Tin Double Gate', 'output': 1, 'mat': ['Tin Sheet'], 'num': [2]}, {'name': 'Tin Fence', 'output': 8, 'mat': ['Tin Sheet'], 'num': [4]}, {'name': 'Tin Flower Bed', 'output': 2, 'mat': ['Tin Sheet'], 'num': [1]}, {'name': 'Tin Gate', 'output': 1, 'mat': ['Tin Sheet'], 'num': [2]}, {'name': 'Trash Bin', 'output': 1, 'mat': ['Iron Bar', 'Tin Sheet', 'Milking Bucket'], 'num': [5, 3, 1]}, {'name': 'Vine Fence', 'output': 8, 'mat': ['Palm Wood Plank', 'Vine', 'Nails'], 'num': [2, 2, 4]}, {'name': 'Vine Festoon', 'output': 1, 'mat': ['Hard Wood Plank', 'Vine'], 'num': [3, 15]}, {'name': 'Vine Lattice Ladder', 'output': 1, 'mat': ['Palm Wood Plank', 'Vine'], 'num': [2, 4]}, {'name': 'Vine Wall', 'output': 8, 'mat': ['Palm Wood Plank', 'Vine', 'Nails'], 'num': [2, 4, 4]}, {'name': 'Water Tank', 'output': 1, 'mat': ['Hard Wood Plank', 'Tin Sheet', 'Old Contraption', 'Iron Bar', 'Nails'], 'num': [15, 15, 1, 8, 8]}, {'name': 'Waterbed', 'output': 8, 'mat': ['Bag of Cement', 'Pearl', 
'Copper Bar'], 'num': [2, 1, 1]}, {'name': 'Wheelbarrow Flower Bed', 'output': 1, 'mat': ['Wheelbarrow', 'Tin Sheet'], 'num': [1, 1]}, {'name': 'White Tile Path', 'output': 16, 'mat': ['White Paint', 'Bag of Cement'], 'num': [1, 1]}, {'name': 'Wide Brick Bridge', 'output': 1, 'mat': ['Bag of Cement', 'Stone'], 'num': [4, 15]}, {'name': 'Wide Cement Bridge', 'output': 1, 'mat': ['Bag of Cement', 'Tin Bar'], 'num': [15, 1]}, {'name': 'Wide Gum Wood Bridge', 'output': 1, 'mat': ['Nails', 'Gum Wood Plank'], 'num': [15, 15]}, {'name': 'Wide Hard Wood Bridge', 'output': 1, 'mat': ['Nails', 'Hard Wood Plank'], 'num': [15, 15]}, {'name': 'Wide Iron Bridge', 'output': 1, 'mat': ['Iron Bar'], 'num': [5]}, {'name': 'Wide Palm Wood Bridge', 'output': 1, 'mat': ['Nails', 'Palm Wood Plank'], 'num': [15, 15]}, {'name': 'Windmill', 'output': 1, 'mat': ['Tin Sheet', 'Old Gear', 'Old Spring', 'Iron Bar', 'Old Wheel'], 'num': [20, 5, 5, 5, 2]}, {'name': 'Wooden Bat', 'output': 1, 'mat': ['Gum Wood Plank', 'Spinifex Resin'], 'num': [1, 2]}, {'name': 'Wooden Crate', 'output': 1, 'mat': ['Palm Wood Plank', 'Gum Wood Plank', 'Nails'], 'num': [1, 2, 1]}, {'name': 'Wooden Flower Bed', 'output': 2, 'mat': ['Palm Wood Plank', 'Nails'], 'num': [2, 1]}, {'name': 'Wooden Lamp Post', 'output': 1, 'mat': ['Palm Wood Fence', 'Nails', 'Quartz Crystal', 'Wooden Torch'], 'num': [1, 1, 1, 1]}, {'name': 'Wooden Torch', 'output': 8, 'mat': ['Mangrove Stick'], 'num': [1]}, {'name': 'Worm Farm', 'output': 1, 'mat': ['Roo Poo', 'Bone', 'Copper Bar', 'Iron Bar', 'Hard Wood Plank'], 'num': [25, 15, 5, 5, 15]}, {'name': 'Wrought Iron Bench', 'output': 1, 'mat': ['Iron Bar'], 'num': [2]}, {'name': 'Wrought Iron Fence', 'output': 8, 'mat': ['Iron Bar'], 'num': [2]}, {'name': 'Wrought Iron Gate', 'output': 1, 'mat': ['Iron Bar'], 'num': [2]}, {'name': 'Wrought Iron Lamp', 'output': 1, 'mat': ['Quartz Crystal', 'Iron Bar', 'Glass Bulb'], 'num': [1, 1, 1]}, {'name': 'Yellow Morel Lamp', 'output': 1, 'mat': ['Yellow Morel', 'Quartz Crystal', 'Glass Bulb'], 'num': [10, 2, 1]}, {'name': 'Yellow Tile Path', 'output': 16, 'mat': ['Yellow Paint', 'Bag of Cement'], 'num': [1, 1]}]

contin = True

def incomaouter():
    temp1 = """ 8  Hardwood Crude Fence	2  Hard Wood Log
1  Spinifex Resin	
Base Price
 56
Commerce 1
 59
Commerce 2
 62
Commerce 3
 64
1  Hay Bale	4  Spinifex Tuft	
Base Price
 50
Commerce 1
 52
Commerce 2
 55
Commerce 3
 58
8  Hedge	2  Spinifex Tuft
2  Fern Seed
2  Bush Seed	
Base Price
 18
Commerce 1
 19
Commerce 2
 20
Commerce 3
 21
1  Hedge Arch	2  Hedge
1  Palm Wood Plank
2  Spinifex Resin	
Base Price
 351
Commerce 1
 369
Commerce 2
 386
Commerce 3
 404
16  Honey Comb Path	1  Honey
2  Bag of Cement	
Base Price
 244
Commerce 1
 256
Commerce 2
 268
Commerce 3
 281
1  Iron Axe	1  Copper Axe
2  Iron Bar	1  Basic Axe
2  Iron Bar
2  Copper Bar	
Base Price
 8,906
Commerce 1
 9,351
Commerce 2
 9,797
Commerce 3
 10,242
1  Iron Bridge	5  Iron Bar	
Base Price
 12,500
Commerce 1
 13,125
Commerce 2
 13,750
Commerce 3
 14,375
8  Iron Cement Fence	1  Bag of Cement
1  Iron Bar	
Base Price
 314
Commerce 1
 330
Commerce 2
 345
Commerce 3
 361
1  Iron Fishing Rod	1  Copper Fishing Rod
2  Iron Bar	
Base Price
 9,110
Commerce 1
 9,566
Commerce 2
 10,021
Commerce 3
 10,476
1  Iron Hammer	2  Hard Wood Plank
3  Iron Bar	
Base Price
 8,125
Commerce 1
 8,531
Commerce 2
 8,937
Commerce 3
 9,344
1  Iron Hoe	1  Copper Hoe
2  Iron Bar	
Base Price
 8,750
Commerce 1
 9,188
Commerce 2
 9,625
Commerce 3
 10,062
1  Iron Ladder	1  Iron Bar	
Base Price
 2,500
Commerce 1
 2,625
Commerce 2
 2,750
Commerce 3
 2,875
8  Iron Path	1  Iron Bar	
Base Price
 312
Commerce 1
 328
Commerce 2
 343
Commerce 3
 359
1  Iron Pickaxe	1  Copper Pickaxe
2  Iron Bar	1  Basic Pickaxe
2  Iron Bar
2  Copper Bar	
Base Price
 9,062
Commerce 1
 9,515
Commerce 2
 9,968
Commerce 3
 10,421
1  Iron Scythe	1  Copper Scythe
1  Iron Bar	
Base Price
 5,478
Commerce 1
 5,752
Commerce 2
 6,026
Commerce 3
 6,300
1  Iron Spear	1  Palm Wood Plank
2  Iron Bar	
Base Price
 5,281
Commerce 1
 5,545
Commerce 2
 5,809
Commerce 3
 6,073
1  Iron Watering Can	1  Copper Watering Can
5  Iron Bar	
Base Price
 28,125
Commerce 1
 29,531
Commerce 2
 30,937
Commerce 3
 32,344
1  Iron Wood Bench	5  Palm Wood Plank
2  Iron Bar	
Base Price
 6,406
Commerce 1
 6,726
Commerce 2
 7,047
Commerce 3
 7,367
1  Keg	10  Palm Wood Plank
3  Copper Bar
3  Iron Bar	
Base Price
 14,062
Commerce 1
 14,765
Commerce 2
 15,468
Commerce 3
 16,171
1  Large Cement Fountain	15  Bag of Cement
1  Advanced Sprinkler	
Base Price
 46,172
Commerce 1
 48,481
Commerce 2
 50,789
Commerce 3
 53,098
8  Lattice Fence	2  Palm Wood Plank
2  Mangrove Stick
4  Nails	
Base Price
 146
Commerce 1
 153
Commerce 2
 161
Commerce 3
 168
1  Marble Bench	10  Marble	
Base Price
 125
Commerce 1
 131
Commerce 2
 137
Commerce 3
 144
8  Marble Fence	5  Marble
5  Vine	
Base Price
 26
Commerce 1
 27
Commerce 2
 29
Commerce 3
 30
8  Marble Path	4  Marble	
Base Price
 6
Commerce 1
 6
Commerce 2
 7
Commerce 3
 7
1  Marble Pedestal	10  Marble	
Base Price
 125
Commerce 1
 131
Commerce 2
 137
Commerce 3
 144
1  Marble Pillar	25  Marble	
Base Price
 312
Commerce 1
 328
Commerce 2
 343
Commerce 3
 359
1  Melon Scarecrow	1  Watermelon
2  Gum Log
8  Spinifex Tuft	
Base Price
 4,200
Commerce 1
 4,410
Commerce 2
 4,620
Commerce 3
 4,830
1  Milk Cap Lamp	10  Milk Cap
2  Quartz Crystal
1  Glass Bulb	
Base Price
 4,919
Commerce 1
 5,165
Commerce 2
 5,411
Commerce 3
 5,657
1  Mushroom Lamp	15  Glowing Mushroom
2  Quartz Crystal
1  Glass Bulb	
Base Price
 2,450
Commerce 1
 2,572
Commerce 2
 2,695
Commerce 3
 2,818
16  Mushroom Path	4  Glowing Mushroom
2  Bag of Cement	
Base Price
 12
Commerce 1
 13
Commerce 2
 13
Commerce 3
 14
8  Nails	1  Tin Bar	
Base Price
 78
Commerce 1
 82
Commerce 2
 86
Commerce 3
 90
8  Natural Path	2  Stone	
Base Price
 2
Commerce 1
 2
Commerce 2
 2
Commerce 3
 2
16  Orange Tile Path	1  Orange Paint
1  Bag of Cement	
Base Price
 16
Commerce 1
 17
Commerce 2
 18
Commerce 3
 18
1  Palm Wood Arch	4  Palm Wood Plank
2  Nails	
Base Price
 1,320
Commerce 1
 1,386
Commerce 2
 1,452
Commerce 3
 1,518
1  Palm Wood Bench	5  Palm Wood Plank
4  Nails	
Base Price
 1,796
Commerce 1
 1,886
Commerce 2
 1,976
Commerce 3
 2,065
4  Palm Wood Bridge	15  Nails
15  Palm Wood	
Base Price
 1,069
Commerce 1
 1,122
Commerce 2
 1,176
Commerce 3
 1,229
1  Palm Wood Bridge	15  Nails
15  Palm Wood Plank	
Base Price
 5,681
Commerce 1
 5,965
Commerce 2
 6,249
Commerce 3
 6,533
1  Palm Wood Double Gate	2  Palm Wood Plank
4  Nails	
Base Price
 952
Commerce 1
 1,000
Commerce 2
 1,047
Commerce 3
 1,095
1  Palm Wood Entrance Sign	5  Palm Wood Plank
4  Nails
1  Spinifex Resin	
Base Price
 1,809
Commerce 1
 1,899
Commerce 2
 1,990
Commerce 3
 2,080
8  Palm Wood Fence	3  Palm Wood Plank
4  Nails	
Base Price
 154
Commerce 1
 162
Commerce 2
 169
Commerce 3
 177
1  Palm Wood Flag Post	1  Palm Wood Fence
2  Nails
1  Cloth	
Base Price
 6,825
Commerce 1
 7,166
Commerce 2
 7,507
Commerce 3
 7,849
1  Palm Wood Gate	2  Palm Wood Plank
4  Nails	
Base Price
 952
Commerce 1
 1,000
Commerce 2
 1,047
Commerce 3
 1,095
1  Palm Wood Ladder	4  Palm Wood Plank	
Base Price
 1,125
Commerce 1
 1,181
Commerce 2
 1,237
Commerce 3
 1,294
1  Palm Wood Market Stall	1  Cloth
4  Palm Wood Plank
4  Nails	
Base Price
 7,952
Commerce 1
 8,350
Commerce 2
 8,747
Commerce 3
 9,145
8  Palm Wood Path	2  Palm Wood Plank	
Base Price
 70
Commerce 1
 74
Commerce 2
 77
Commerce 3
 80
1  Palm Wood Pergola	8  Palm Wood Plank
8  Nails
2  Copper Bar	
Base Price
 5,530
Commerce 1
 5,806
Commerce 2
 6,083
Commerce 3
 6,360
4  Palm Wood Steps	1  Palm Wood Plank
1  Nails	
Base Price
 94
Commerce 1
 99
Commerce 2
 103
Commerce 3
 108
1  Palm Wood Table	5  Palm Wood Plank
4  Nails	
Base Price
 1,796
Commerce 1
 1,886
Commerce 2
 1,976
Commerce 3
 2,065
1  Palm Wood Tool Rack	10  Palm Wood Plank
2  Iron Bar	
Base Price
 7,812
Commerce 1
 8,203
Commerce 2
 8,593
Commerce 3
 8,984
8  Pattern Stone Path	1  Stone
1  Bag of Cement	
Base Price
 2
Commerce 1
 2
Commerce 2
 2
Commerce 3
 2
16  Pearl Path	1  Pearl
2  Bag of Cement	
Base Price
 391
Commerce 1
 411
Commerce 2
 430
Commerce 3
 450
8  Picket Fence	3  Gum Wood Plank
4  Nails	
Base Price
 119
Commerce 1
 125
Commerce 2
 131
Commerce 3
 137
1  Picket Gate	2  Gum Wood Plank
4  Nails	
Base Price
 765
Commerce 1
 803
Commerce 2
 841
Commerce 3
 880
16  Pink Tile Path	1  Pink Paint
1  Bag of Cement	
Base Price
 16
Commerce 1
 17
Commerce 2
 18
Commerce 3
 18
1  Post Box	2  Iron Bar	
Base Price
 5,000
Commerce 1
 5,250
Commerce 2
 5,500
Commerce 3
 5,750
16  Purple Tile Path	1  Purple Paint
1  Bag of Cement	
Base Price
 16
Commerce 1
 17
Commerce 2
 18
Commerce 3
 18
4  Ramp	2  Bag of Cement
2  Palm Wood Plank	
Base Price
 146
Commerce 1
 153
Commerce 2
 161
Commerce 3
 168
1  Recycling Bin	1  Palm Wood Plank
2  Gum Wood Plank	
Base Price
 656
Commerce 1
 689
Commerce 2
 722
Commerce 3
 754
16  Red Cloth Path	1  Cloth	
Base Price
 401
Commerce 1
 421
Commerce 2
 441
Commerce 3
 461
2  Red Floor Light	1  Ruby Shard
2  Tin Sheet
1  Glass Bulb	
Base Price
 2,240
Commerce 1
 2,352
Commerce 2
 2,464
Commerce 3
 2,576
1  Red Roundhead Lamp	10  Red Roundhead
2  Quartz Crystal
1  Glass Bulb	
Base Price
 8,044
Commerce 1
 8,446
Commerce 2
 8,848
Commerce 3
 9,251
16  Red Tile Path	1  Red Paint
1  Bag of Cement	
Base Price
 16
Commerce 1
 17
Commerce 2
 18
Commerce 3
 18
8  Rock Edge Path	2  Stone	
Base Price
 2
Commerce 1
 2
Commerce 2
 2
Commerce 3
 2
8  Rock Path	2  Stone	
Base Price
 2
Commerce 1
 2
Commerce 2
 2
Commerce 3
 2
8  Rope Fence	3  Hard Wood Plank
2  Nails
3  Vine	
Base Price
 152
Commerce 1
 160
Commerce 2
 167
Commerce 3
 175
1  Rope Ladder	2  Gum Wood Plank
4  Vine	
Base Price
 500
Commerce 1
 525
Commerce 2
 550
Commerce 3
 575
1  Rowboat	10  Gum Wood Plank
10  Palm Wood Plank
2  Tin Bar
4  Nails	
Base Price
 6,328
Commerce 1
 6,644
Commerce 2
 6,961
Commerce 3
 7,277
1  Sail Boat	15  Gum Wood Plank
15  Palm Wood Plank
15  Hard Wood Plank
10  Copper Bar
10  Iron Bar
10  Cloth
1  Wooden Chest	
Base Price
 116,344
Commerce 1
 122,161
Commerce 2
 127,978
Commerce 3
 133,796
8  Sand Fence	4  Scallop Shell
4  Buccinidae Shell
4  Cassidae Shell	
Base Price
 14
Commerce 1
 15
Commerce 2
 15
Commerce 3
 16
1  Scarecrow	1  Pumpkin
2  Gum Log
8  Spinifex Tuft	
Base Price
 4,250
Commerce 1
 4,462
Commerce 2
 4,675
Commerce 3
 4,888
1  Scythe	1  Palm Wood Plank
1  Tin Bar	
Base Price
 906
Commerce 1
 951
Commerce 2
 997
Commerce 3
 1,042
1  Signwriting Table	5  Hard Wood Plank
1  Iron Bar
1  Copper Bar
8  Nails	
Base Price
 6,092
Commerce 1
 6,397
Commerce 2
 6,701
Commerce 3
 7,006
1  Silo	25  Stone
15  Tin Sheet
10  Bag of Cement
8  Quartz Crystal
5  Iron Bar	
Base Price
 20,094
Commerce 1
 21,099
Commerce 2
 22,103
Commerce 3
 23,108
1  Simple Animal Trap	1  Tin Bar
8  Mangrove Stick
1  Old Spring	
Base Price
 2,131
Commerce 1
 2,238
Commerce 2
 2,344
Commerce 3
 2,451
1  Slippery Jack Lamp	10  Slippery Jack
2  Quartz Crystal
1  Glass Bulb	
Base Price
 4,919
Commerce 1
 5,165
Commerce 2
 5,411
Commerce 3
 5,657
1  Small Cement Fountain	5  Stone
1  Sprinkler
5  Bag of Cement	
Base Price
 15,500
Commerce 1
 16,275
Commerce 2
 17,050
Commerce 3
 17,825
8  Smooth Cement Path	2  Bag of Cement	
Base Price
 2
Commerce 1
 2
Commerce 2
 2
Commerce 3
 2
1  Spinning Wheel	4  Palm Wood Plank
4  Old Gear
1  Old Wheel	
Base Price
 5,400
Commerce 1
 5,670
Commerce 2
 5,940
Commerce 3
 6,210
1  Sprinkler	5  Copper Bar
4  Quartz Crystal
4  Old Spring
4  Old Gear	
Base Price
 12,300
Commerce 1
 12,915
Commerce 2
 13,530
Commerce 3
 14,145
1  Storage Barrel	5  Palm Wood Plank
2  Gum Wood Plank
1  Iron Bar	
Base Price
 4,281
Commerce 1
 4,495
Commerce 2
 4,709
Commerce 3
 4,923
1  Street Lamp	1  Quartz Crystal
1  Iron Bar
1  Glass Bulb	
Base Price
 4,044
Commerce 1
 4,246
Commerce 2
 4,448
Commerce 3
 4,651
1  Tiki Torch	1  Palm Wood
1  Wooden Torch	
Base Price
 205
Commerce 1
 215
Commerce 2
 225
Commerce 3
 236
1  Tin Double Gate	2  Tin Sheet	
Base Price
 688
Commerce 1
 722
Commerce 2
 757
Commerce 3
 791
8  Tin Fence	4  Tin Sheet	
Base Price
 171
Commerce 1
 180
Commerce 2
 188
Commerce 3
 197
2  Tin Flower Bed	1  Tin Sheet	
Base Price
 171
Commerce 1
 180
Commerce 2
 188
Commerce 3
 197
1  Tin Gate	2  Tin Sheet	
Base Price
 688
Commerce 1
 722
Commerce 2
 757
Commerce 3
 791
1  Trash Bin	5  Iron Bar
3  Tin Sheet
1  Milking Bucket	
Base Price
 14,531
Commerce 1
 15,258
Commerce 2
 15,984
Commerce 3
 16,711
8  Vine Fence	2  Palm Wood Plank
2  Vine
4  Nails	
Base Price
 126
Commerce 1
 132
Commerce 2
 139
Commerce 3
 145
1  Vine Festoon	3  Hard Wood Plank
15  Vine	
Base Price
 1,406
Commerce 1
 1,476
Commerce 2
 1,547
Commerce 3
 1,617
1  Vine Lattice Ladder	2  Palm Wood Plank
4  Vine	
Base Price
 688
Commerce 1
 722
Commerce 2
 757
Commerce 3
 791
8  Vine Wall	2  Palm Wood Plank
4  Vine
4  Nails	
Base Price
 134
Commerce 1
 141
Commerce 2
 147
Commerce 3
 154
1  Water Tank	15  Hard Wood Plank
15  Tin Sheet
1  Old Contraption
8  Iron Bar
8  Nails	
Base Price
 49,486
Commerce 1
 51,960
Commerce 2
 54,435
Commerce 3
 56,909
8  Waterbed	2  Bag of Cement
1  Pearl
1  Copper Bar	
Base Price
 940
Commerce 1
 987
Commerce 2
 1,034
Commerce 3
 1,081
1  Wheelbarrow Flower Bed	1  Wheelbarrow
1  Tin Sheet	
Base Price
 19,094
Commerce 1
 20,049
Commerce 2
 21,003
Commerce 3
 21,958
16  White Tile Path	1  White Paint
1  Bag of Cement	
Base Price
 16
Commerce 1
 17
Commerce 2
 18
Commerce 3
 18
1  Wide Brick Bridge	4  Bag of Cement
15  Stone	
Base Price
 238
Commerce 1
 250
Commerce 2
 262
Commerce 3
 274
1  Wide Cement Bridge	15  Bag of Cement
1  Tin Bar	
Base Price
 812
Commerce 1
 853
Commerce 2
 893
Commerce 3
 934
1  Wide Gum Wood Bridge	15  Nails
15  Gum Wood Plank	
Base Price
 4,275
Commerce 1
 4,489
Commerce 2
 4,703
Commerce 3
 4,916
1  Wide Hard Wood Bridge	15  Nails
15  Hard Wood Plank	
Base Price
 6,150
Commerce 1
 6,458
Commerce 2
 6,765
Commerce 3
 7,072
1  Wide Iron Bridge	5  Iron Bar	
Base Price
 12,500
Commerce 1
 13,125
Commerce 2
 13,750
Commerce 3
 14,375
1  Wide Palm Wood Bridge	15  Nails
15  Palm Wood Plank	
Base Price
 5,681
Commerce 1
 5,965
Commerce 2
 6,249
Commerce 3
 6,533
1  Windmill	20  Tin Sheet
5  Old Gear
5  Old Spring
5  Iron Bar
2  Old Wheel	
Base Price
 28,988
Commerce 1
 30,437
Commerce 2
 31,887
Commerce 3
 33,336
1  Wooden Bat	1  Gum Wood Plank
2  Spinifex Resin	
Base Price
 212
Commerce 1
 223
Commerce 2
 233
Commerce 3
 244
1  Wooden Crate	1  Palm Wood Plank
2  Gum Wood Plank
1  Nails	
Base Price
 754
Commerce 1
 792
Commerce 2
 829
Commerce 3
 867
2  Wooden Flower Bed	2  Palm Wood Plank
1  Nails	
Base Price
 330
Commerce 1
 346
Commerce 2
 363
Commerce 3
 380
1  Wooden Lamp Post	1  Palm Wood Fence
1  Nails
1  Quartz Crystal
1  Wooden Torch	
Base Price
 558
Commerce 1
 586
Commerce 2
 614
Commerce 3
 642
8  Wooden Torch	1  Mangrove Stick	
Base Price
 14
Commerce 1
 15
Commerce 2
 15
Commerce 3
 16
1  Worm Farm	25  Roo Poo
15  Bone
5  Copper Bar
5  Iron Bar
15  Hard Wood Plank	
Base Price
 23,938
Commerce 1
 25,135
Commerce 2
 26,332
Commerce 3
 27,529
1  Wrought Iron Bench	2  Iron Bar	
Base Price
 5,000
Commerce 1
 5,250
Commerce 2
 5,500
Commerce 3
 5,750
8  Wrought Iron Fence	2  Iron Bar	
Base Price
 625
Commerce 1
 656
Commerce 2
 687
Commerce 3
 719
1  Wrought Iron Gate	2  Iron Bar	
Base Price
 5,000
Commerce 1
 5,250
Commerce 2
 5,500
Commerce 3
 5,750
1  Wrought Iron Lamp	1  Quartz Crystal
1  Iron Bar
1  Glass Bulb	
Base Price
 4,044
Commerce 1
 4,246
Commerce 2
 4,448
Commerce 3
 4,651
1  Yellow Morel Lamp	10  Yellow Morel
2  Quartz Crystal
1  Glass Bulb	
Base Price
 4,919
Commerce 1
 5,165
Commerce 2
 5,411
Commerce 3
 5,657
16  Yellow Tile Path	1  Yellow Paint
1  Bag of Cement	
Base Price
 16
Commerce 1
 17
Commerce 2
 18
Commerce 3
 18
"""
    if temp1 == "0":
        return False
    else:
        num2 = temp1.count("Commerce 3")
        for ii in range(num2):
            a, temp1 = temp1[:temp1.find("Base Price")] ,temp1[temp1.find("Commerce 3"):]
            a = a.strip()
            if(ii == num2-1):
                incoma(a)
                return True
            temp1 = temp1[temp1.find("\n",12):]
            incoma(a)

        

def incoma(mat):
    mat = mat.replace("\t","")
    listte = re.split(r'(\d+)', mat)
    listte = listte[1:]
    listte = [i.strip() for i in listte]
    
    temp1 = {"name":listte[1],"output":int(listte[0])}
    arr_r = int(len(listte)/2 - 1)
    mat_temp = []
    num_temp = []
    for i in range(arr_r):
        mat_temp.append(listte[i*2+3])
        num_temp.append(int(listte[i*2+2]))
    
    temp1["mat"] = mat_temp
    temp1["num"] = num_temp
    locaDataSear.append(temp1)
    return True
    
contin = incomaouter()


print("=======================================================")
print(locaDataSear)
print("=======================================================")


# dummy = []
# num = 5

# list(filter(lambda m : dummy.append(m*num), sprinkler["num"]))

# print(dummy)

