#!/usr/bin/env python3
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import json

resp = urlopen("https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/main/db.json.zip")
zipfile = ZipFile(BytesIO(resp.read()))
db = json.loads(zipfile.open("db.json").read())

tag_dictionary = {number:name for name, number in db["tag_dictionary"].items()}

banned_tags = {
	"essential",
	"scripts",
	"linux",

	"presets",

}
{
	"arcadearkanoid", # arcadecores
	"arcadeasteroidsdeluxe", # arcadecores
	"arcadeasteroids", # arcadecores
	"arcadeastrocade", # arcadecores
	"arcadeataritetris", # arcadecores
	"arcadebagman", # arcadecores
	"arcadeberzerk", # arcadecores
	"arcadeblackwidow", # arcadecores
	"arcadeblockade", # arcadecores
	"arcadebombjack", # arcadecores
	"arcadebreakout", # arcadecores
	"arcadeburgertime", # arcadecores
	"arcadeburningrubber", # arcadecores
	"arcadecanyonbomber", # arcadecores
	"arcadecave", # arcadecores
	"arcadecentipede", # arcadecores
	"arcadecomputerspace", # arcadecores
	"arcadecosmic", # arcadecores
	"arcadecrazyballoon", # arcadecores
	"arcadecrazyclimber", # arcadecores
	"arcadecrazykong", # arcadecores
	"arcadedefender", # arcadecores
	"arcadedigdug", # arcadecores
	"arcadedominos", # arcadecores
	"arcadedonkeykong3", # arcadecores
	"arcadedonkeykongjunior", # arcadecores
	"arcadedonkeykong", # arcadecores
	"arcadedottorikun", # arcadecores
	"arcadedruaga", # arcadecores
	"arcadefinalizer", # arcadecores
	"arcadefoodfight", # arcadecores
	"arcadefrenzy", # arcadecores
	"arcadegalaga", # arcadecores
	"arcadegalaxian", # arcadecores
	"arcadegaplus", # arcadecores
	"arcadegauntlet", # arcadecores
	"arcadegyruss", # arcadecores
	"arcadeiremm62", # arcadecores
	"arcadeironhorse", # arcadecores
	"arcadejackal", # arcadecores
	"arcadejailbreak", # arcadecores
	"arcadejoust2", # arcadecores
	"arcadeladybug", # arcadecores
	"arcadelunarlander", # arcadecores
	"arcademcr1", # arcadecores
	"arcademcr2", # arcadecores
	"arcademcr3mono", # arcadecores
	"arcademcr3scroll", # arcadecores
	"arcademcr3", # arcadecores
	"arcademariobros", # arcadecores
	"arcademoonpatrol", # arcadecores
	"arcademrdo", # arcadecores
	"arcademysticmarathon", # arcadecores
	"arcadeninjakun", # arcadecores
	"arcadepacman", # arcadecores
	"arcadepengo", # arcadecores
	"arcadephoenix", # arcadecores
	"arcadepleiads", # arcadecores
	"arcadepolyplay", # arcadecores
	"arcadepong", # arcadecores
	"arcadepooyan", # arcadecores
	"arcadepopeye", # arcadecores
	"arcadeqbert", # arcadecores
	"arcaderallyx", # arcadecores
	"arcaderiverpatrol", # arcadecores
	"arcaderobotron", # arcadecores
	"arcadershnatk", # arcadecores
	"arcadesegasys1", # arcadecores
	"arcadesms", # arcadecores
	"arcadescootershooter", # arcadecores
	"arcadescramble", # arcadecores
	"arcadesilverland", # arcadecores
	"arcadesolomonskey", # arcadecores
	"arcadespaceinvaders", # arcadecores
	"arcadespacerace", # arcadecores
	"arcadesprint1", # arcadecores
	"arcadesprint2", # arcadecores
	"arcadesubs", # arcadecores
	"arcadesuperbreakout", # arcadecores
	"arcadetiamc1", # arcadecores
	"arcadetecmo", # arcadecores
	"arcadetimepilot84", # arcadecores
	"arcadetimepilot", # arcadecores
	"arcadetraverseusa", # arcadecores
	"arcadeturkeyshoot", # arcadecores
	"arcadeultratank", # arcadecores
	"arcadevball", # arcadecores
	"arcadexevious", # arcadecores
	"arcadezaxxon", # arcadecores
	"arcadezigzag", # arcadecores

	"acornatom", # computercores
	"acornelectron", # computercores
	"alicemc10", # computercores
	"altair8800", # computercores
	"amstradpcw", # computercores
	"amstrad", # computercores
	"apogee", # computercores
	"appleii", # computercores
	"applei", # computercores
	"aquarius", # computercores
	"archie", # computercores
	"atari800", # computercores
	"atarist", # computercores
	"bbcmicro", # computercores
	"bk0011m", # computercores
	"c16", # computercores
	"c64", # computercores
	"coco2", # computercores
	"coco3", # computercores
	"edsac", # computercores
	"galaksija", # computercores
	"interact", # computercores
	"jupiter", # computercores
	"laser310", "laser", # computercores
	"lynx48", # computercores
	"msx", # computercores
	"macplus", # computercores
	"minimig", # computercores
	"multicomp", # computercores
	"orao", # computercores
	"ondraspo186", # computercores
	"oric", # computercores
	"pc88", "pc8801", # computercores
	"pdp1", # computercores
	"pet2001", # computercores
	"pmd85", # computercores
	"ql", # computercores
	"rx78", # computercores
	"samcoupe", # computercores
	"sharpmz", # computercores
	"sordm5", # computercores
	"specialist", # computercores
	"svi328", # computercores
	"trs80", # computercores
	"tsconf", # computercores
	"tatungeinstein", # computercores
	"ti994a", # computercores
	"uk101", # computercores
	"vic20", # computercores
	"vector06c", # computercores
	"x68000", # computercores
	"zxspectrum", "spectrum", # computercores
	"zx81", # computercores
	"zxnext", # computercores
	"ao486", # computercores

	"ay38500", # consolecores
	"adventurevision", # consolecores
	"arcadia", # consolecores
	"astrocade", # consolecores
	"atari5200", # consolecores
	"atari7800", # consolecores
	"atarilynx", # consolecores
	"channelf", # consolecores
	"colecovision", # consolecores
	"gba2p", # consolecores
	"gba", # consolecores
	"gameboy2p", #  consolecores
	"gameboy", # consolecores
	"megadrive", # consolecores
	"intellivision", # consolecores
	"segacd", # consolecores
	"nintendo", # consolecores
	"neogeo", # consolecores
	"odyssey2", # consolecores
	"s32x", # consolecores
	"sms", # consolecores
	"supernintendo", # consolecores
	"turbografx16", # consolecores
	"vc4000", # consolecores
	"vectrex", # consolecores
	"wonderswan", # consolecores

	"arduboy", # othercores
	"chess", # othercores
	"chip8", # othercores
	"epochgalaxyii", # othercores
	"flappybird", "flappy", # othercores
	"gameoflife", # othercores
	"slugcross", # othercores
	"tomyscramble", # othercores

	"adctest", # utility
	"inputtest", # utility
	"memtest", # utility
}

all_meta_tags = {"cores", "arcadecores", "computercores" ,"consolecores", "othercores", "utility"}

for name, contents in db["files"].items():
	tags = set(tag_dictionary[tag_id] for tag_id in contents['tags'])
	if banned_tags.intersection(tags): continue
	meta_tags = tags.intersection(all_meta_tags)
	tags -= meta_tags
	print(f"{name}: {', '.join(list(tags) + list(meta_tags))}")
