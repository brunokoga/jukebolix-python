import nxppy
import time
import subprocess
mifare = nxppy.Mifare()

# Print card UIDs as they are detected
card001 = "04E9AD6A835C80"
card002 = "04E4AC6A835C80"
card003 = "04DEAC6A835C80"
card004 = "04ABA66A835C80"
card005 = "04C6AA6A835C80"
card006 = "04D9AB6A835C80"
card007 = "047C9D6A835C80"
card008 = "04829D6A835C80"
card009 = "04869F6A835C80"
card010 = "04769D6A835C80"
card011 = "048FA26A835C80"
card012 = "0499A46A835C80"
card013 = "049FA66A835C80"
card014 = "04D3AB6A835C80"
card015 = "04BBA86A835C80"
card016 = "04B0A76A835C80"
card017 = "04B5A86A835C80"
card018 = "04CBAB6A835C80"
card019 = "0435996A835C80"
card020 = "04099A6A835C80"
card021 = "042F996A835C80"
card022 = "0411996A835C80"
card023 = "040B996A835C80"
card024 = "040F9A6A835C80"
card025 = "04159A6A835C80"
card026 = "041B9A6A835C80"
card027 = "04279A6A835C80"
card028 = "042D9A6A835C80"
card029 = "04339A6A835C80"
card030 = "04399A6A835C80"
card031 = "043F9A6A835C80"
card032 = "045E9D6A835C80"
card033 = "04459A6A835C80"
card034 = "044A996A835C80"
card035 = "0450996A835C80"
card036 = "04599C6A835C80"
card037 = "04559A6A835C80"
card038 = "04649D6A835C80"
card039 = "04709D6A835C80"
card040 = "046A9D6A835C80"
card041 = "044C986A835C80"
card042 = "0493A16A835C80"
card043 = "0497A36A835C80"
card044 = "049CA46A835C80"
card045 = "04A1A56A835C80"
card046 = "04ADA56A835C80"
card047 = "04C2A86A835C80"
card048 = "04B2A66A835C80"
card049 = "04BDA76A835C80"
card050 = "04C7A96A835C80"
card051 = "04CEAA6A835C80"
card052 = "04D4AA6A835C80"
card053 = "04DAAA6A835C80"
card054 = "04E5AB6A835C80"
card055 = "04EAAC6A835C80"
card056 = "04F6AC6A835C80"
card057 = "0409AD6A835C81"
card058 = "0403AD6A835C81"
card059 = "04FCAC6A835C80"
card060 = "040FAD6A835C81"
card061 = "0415AD6A835C81"
card062 = "041BAD6A835C81"
card063 = "0421AD6A835C81"
card064 = "0427AD6A835C81"
card065 = "0439AF6A835C81"
card066 = "044AB06A835C81"
card067 = "0445AF6A835C81"
card068 = "0433AF6A835C81"
card069 = "042CAE6A835C81"
card070 = "0423996A835C80"
card071 = "04219A6A835C80"
card072 = "0417996A835C80"
card073 = "041D996A835C80"
card074 = "048BA06A835C80"
card075 = "043B996A835C80"
card076 = "04A5A66A835C80"
card077 = "043FAF6A835C81"
card078 = "0450B06A835C81"
card079 = "0429996A835C80"
card080 = "04F0AC6A835C80"
card081 = "04B7A76A835C80"
card082 = "04A7A56A835C80"
card083 = "048EA06A835C80"
card084 = "04899F6A835C80"
card085 = "047A9C6A835C80"
card086 = "04809C6A835C80"
card087 = "04869C6A835C80"
card088 = "045C9B6A835C80"
card089 = "04619C6A835C80"
card090 = "04679C6A835C80"
card091 = "046D9C6A835C80"
card092 = "04739C6A835C80"
card093 = "0441996A835C80"
card094 = "0453986A835C80"
card095 = "0458996A835C80"
card096 = "0494A36A835C80"
card097 = "04C1A96A835C80"
card098 = "0456B06A835C81"
card099 = "04DFAB6A835C80"
card100 = "0447996A835C80"

def nameForCard(cardId):
    return {
            card001: "001",
            card002: "002",
            card003: "003",
            card004: "004",
            card005: "005",
            card006: "006",
            card007: "007",
            card008: "008",
            card009: "009",
            card010: "010",
            card011: "011",
            card012: "012",
            card013: "013",
            card014: "014",
            card015: "015",
            card016: "016",
            card017: "017",
            card018: "018",
            card019: "019",
            card020: "020",
            card021: "021",
            card022: "022",
            card023: "023",
            card024: "024",
            card025: "025",
            card026: "026",
            card027: "027",
            card028: "028",
            card029: "029",
            card030: "030",
            card031: "031",
            card032: "032",
            card033: "033",
            card034: "034",
            card035: "035",
            card036: "036",
            card037: "037",
            card038: "038",
            card039: "039",
            card040: "040",
            card041: "041",
            card042: "042",
            card043: "043",
            card044: "044",
            card045: "045",
            card046: "046",
            card047: "047",
            card048: "048",
            card049: "049",
            card050: "050",
            card051: "051",
            card052: "052",
            card053: "053",
            card054: "054",
            card055: "055",
            card056: "056",
            card057: "057",
            card058: "058",
            card059: "059",
            card060: "060",
            card061: "061",
            card062: "062",
            card063: "063",
            card064: "064",
            card065: "065",
            card066: "066",
            card067: "067",
            card068: "068",
            card069: "069",
            card070: "070",
            card071: "071",
            card072: "072",
            card073: "073",
            card074: "074",
            card075: "075",
            card076: "076",
            card077: "077",
            card078: "078",
            card079: "079",
            card080: "080",
            card081: "081",
            card082: "082",
            card083: "083",
            card084: "084",
            card085: "085",
            card086: "086",
            card087: "087",
            card088: "088",
            card089: "089",
            card090: "090",
            card091: "091",
            card092: "092",
            card093: "093",
            card094: "094",
            card095: "095",
            card096: "096",
            card097: "097",
            card098: "098",
            card099: "099",
            card100: "100"
            }.get(cardId, "stop")

def stopAllPlayers():
    global player
    try:
        player.stdin.write('q')
    except:
        pass

def plim():
    subprocess.call(['omxplayer', 'pop.mp3'])

def play(filename):
    global player
    player = subprocess.Popen(['omxplayer', filename], stdin=subprocess.PIPE)

while True:
    try:
        uid = mifare.select()
        name = nameForCard(uid)
        plim()
        stopAllPlayers()
        if name != "stop":
            filename = "songs/" + name + ".mp3"
            play(filename)
        time.sleep(2)
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass
