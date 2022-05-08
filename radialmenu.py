#!/usr/bin/env python3

from os import system as s;

def clear():
    s("clear")

vocalCMD = {"0": "vocalize PlayerDeath", "1": "vocalize PlayerWarnBoomer", "2": "vocalize PlayerWarnHunter", "3": "vocalize PlayerWarnSmoker", "4": "vocalize PlayerWarnWitch", "5": "vocalize PlayerWarnTank", "6": "vocalize PlayerKillThatLight",
"7": "vocalize WitchGettingAngry", "8": "vocalize Playerspotpisto", "9": "vocalize PlayerSpotAmmo",
"10": "vocalize PlayerSpotFirstAid", "11": "vocalize PlayerSpotGrenade", "12": "vocalize PlayerSpotPill", "13": "vocalize PlayerIncoming", "14": "vocalize Playerlookout", "15": "vocalize PlayerStayTogether", "16": "vocalize PlayerFollowMe",
"17": "vocalize PlayerLookOut", "18": "vocalize PlayerLeadOn", "19": "vocalize PlayerMoveOn", "20": "vocalize EatPills",
"21": "vocalize PlayerVomitInFace", "22": "vocalize PlayerChoke", "23": "vocalize PlayerDeath", "24": "vocalize Playergrabbedbytongue", "25": "vocalize ResponseSoftDispleasureSwear",
"26": "vocalize ReviveMeInterrupted", "27": "vocalize PlayerFriendlyFire", "28": "vocalize PlayerIncapacitated", "29": "vocalize PlayerReviveFriend", "30": "Revivedbyfriend", "31": "PlayerLedgeHangStart", "32": "PlayerLedgeHangMiddle",
"33": "vocalize PlayerLedgeHangEnd", "34": "vocalize PlayerLedgeSave", "35": "vocalize CallForRescue",
"36": "vocalize PlayerHelp", "37": "vocalize SurvivorWasPounced", "38": "vocalize PlayerHealing", "39": "vocalize PlayerHealingOther", "40": "vocalize Askforhealth2", "41": "vocalize PlayerYouAreWelcome", "42": "PlayerAlertGiveItem"}

#       Minify when done https://steamcommunity.com/sharedfiles/filedetails/?id=1433254329

print("No spaces and text only")
menuName = str(input("Menu name: "))

def ask(pos):
    ui1 = input(f'''
{pos}:

0) *Scream*
1) WarnBoomer
2) WarnHunter
3) WarnSmoker
4) WarnWitch
5) WarnTank
6) Kill that light
7) Witch is angry
8) Spot pistol
9) Spot ammo
10) Spot first aid
11) Spot grenade
12) Spot pills
13) Incoming!
14) Look out!
15) Stay together
16) Follow me
17) Look out!
18) Lead on
19) Move on
20) Eat pills
21) Vomited on
22) *choking*
23) *death*
24) Grabbed by smoker tongue
25) Swear
26) Interupted revive
27) Friendly fire
28) Incapacitated
29) Revive friend
30) Revived by friend
31) Ledge hang on start
32) Ledge hang on middle
33) Ledge hang on end
34) Ledge save
35) Call for rescue
36) Call for help
37) Pounced by hunter
38) Healing
39) Healing other
40) Ask for health
41) You're welcome
42) Give item
''')
    return str(ui1)

q0 = ask("Center")
q0Name = str(input("Name: "))
clear()
q1 = ask("North")
q1Name = str(input("Name: "))
clear()
q2 = ask("North east")
q2Name = str(input("Name: "))
clear()
q3 = ask("East")
q3Name = str(input("Name: "))
clear()
q4 = ask("South east")
q4Name = str(input("Name: "))
clear()
q5 = ask("South")
q5Name = str(input("Name: "))
clear()
q6 = ask("South west")
q6Name = str(input("Name: "))
clear()
q7 = ask("West")
q7Name = str(input("Name: "))
clear()
q8 = ask("North west")
q8Name = str(input("Name: "))
clear()

vals = {"center": q0, "north": q1, "northeast": q2, "east": q3, "southeast": q4, "south": q5, "southwest": q6, "west": q7, "northwest": q8}

menuString = f'''
//--------------------------------------------------------------
	"{menuName},Survivor,Alive"
	{{
		"Center"
		{{
			"command"	"{vocalCMD[vals['center']]}"
			"text"		"{q0Name}"
		}}
		"North"
		{{
			"command"	"{vocalCMD[vals['north']]}"
			"text"		"{q1Name}"
		}}
		"NorthEast"
		{{
			"command"	"{vocalCMD[vals['northeast']]}"
			"text"		"{q2Name}"
		}}
		"East"
		{{
			"command"	"{vocalCMD[vals['east']]}"
			"text"		"{q3Name}"
		}}
		"SouthEast"
		{{
			"command"	"{vocalCMD[vals['southeast']]}"
			"text"		"{q4Name}"
		}}
		"South"
		{{
			"command"	"{vocalCMD[vals['south']]}"
			"text"		"{q5Name}"
		}}
		"SouthWest"
		{{
			"command"	"{vocalCMD[vals['southwest']]}"
			"text"		"{q6Name}"
		}}
		"West"
		{{
			"command"	"{vocalCMD[vals['west']]}"
			"text"		"{q7Name}"
		}}
		"NorthWest"
		{{
			"command"	"{vocalCMD[vals['northwest']]}"
			"text"		"{q8Name}"
		}}
	}}	
'''

print(menuString)
