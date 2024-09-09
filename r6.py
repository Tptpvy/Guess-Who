import random
import math
from PIL import Image

gadgetsPath = ".../gadgets/" # your path
x = 24
# names not used
gadgetsList = ["V10 PANTHEON SHELLS", "DEATHMARK TRACKER", "ZOTO CANISTER", "BU-GI AUTO BREACHER", "F-NATT DREAD MINE", "KLUDGE DRONE", "SPEC-IO ELECTRO SENSOR", "KAWAN HIVE LAUNCHER", "R.O.U. PROJECTOR SYSTEM", "KIBA BARRIER", 
               "RAZORBLOOM SHELL", "TALON-8 CLEAR SHIELD", "KONA STATION", "RCE-RATERO CHARGE", "SURYA GATE", "ARGUS LAUNCHER", "S.E.L.M.A. AQUA BREACHER", "BANSHEE SONIC DEFENSE", "REMAH DASH", "GEMINI REPLICATOR", "MAG-NET SYSTEM", 
               "LV EXPLOSIVE LANCE", "GARRA HOOK", "VOLCAN CANISTER", "HEL PRESENSE REDUCTION", "GLANCE SMART GLASSES", "PEST LAUNCHER", "TRAX STINGERS", "AIRJAB LAUNCHER", "RTILA ELECTROCLAW", "CCE SHIELD", "BREACHING TORCH", 
               "EVIL EYE", "PRISMA", "EE-ONE-D", "ADRENAL SURGE", "ERC-7", "LOGIC BOMB", "KS79 LIFELINE", "GRZMOT MINE", "CANDELA", "GU", "BLACK MIRROR", "EYENOX MODEL III", "X-KAIROS", "YOKAI", "SILENT STEP", "TACTICAL CROSSBOW", 
               "RIFLE SHIELD", "BLACK EYE", "SKELETON KEY", "WELCOME MAT", "SIGNAL DISRUPTOR", "BREACHING HAMMER", "REMOTE GAS GRENADE", "EMP GRENADE", "BREACHING ROUND", "ARMOR PANEL", "CARDIAC SENSOR", "EXOTHERMIC CHARGE", 
               "LE ROC SHIELD", "SHOCK DRONE", "STIM PISTOL", "ARMOR PACK", "ACTIVE DEFENSE", "SHOCK WIRE", "G52-TACTICAL SHIELD", "ELECTRONICS DETECTOR", "CLUSTER CHARGE", "FLIP SIGHT", "SHUMIKHA LAUNCHER", "ENTRY DENIAL DEVICE"]
gadgetsArray = []
while len(gadgetsArray) < x:
    random_index = random.randint(0, len(gadgetsList) - 1)
    if random_index not in gadgetsArray:
        gadgetsArray.append(random_index)
height = 860
width = 600
new_image = Image.new('RGB', (width * 6, height * 4))
for i in range(x):
    image = Image.open(gadgetsPath + str(gadgetsArray[i]) + ".jpg")
    new_image.paste(image, (width * (i % 6), height * math.floor(i/6)))

new_image.show()
