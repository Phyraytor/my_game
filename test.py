import mag
import knight
import healer
import scout

def count_fight(count_pers: int, fight:int) -> int:
	return (count_pers - 1) * fight 

def init__dist(persons: list, init):
	result = {}
	for person in  persons:
		result[person] = init
	return result

persons = [
	"Mag",
	"Knight",
	"Healer",
	"Scout",
]
Person_win = init__dist(persons, init=0)
Person_table = {
	"Mag": {},
	"Knight": {},
	"Healer": {},
	"Scout": {},
}

for key_i in persons:
	for key_j in persons:
		if key_i == key_j: continue
		Person_table[key_i][key_j] = 0

with open("test.txt", "w") as file:
	1 + 1

fight = 0
while(True):
	Percon = [
		mag.Mag("Mag"),
		knight.Knight("Knight"),
		healer.Healer("Healer"),
		scout.Scout("Scout"),
	]
	for i in range(len(Percon) - 1):
		for j in range(i + 1, len(Percon)):

			while Percon[i].live() and Percon[j].live():
				if Percon[j].time() <= Percon[i].time():
				    Percon[j].get_enemy_skill( Percon[i].get_enemy_skill( Percon[j].activate() ) )
				else:
				    Percon[i].get_enemy_skill( Percon[j].get_enemy_skill( Percon[i].activate() ) )

			#Person_table[Percon[i].name][Percon[i].name] += 1
			#Person_table[Percon[j].name][Percon[j].name] += 1
			if Percon[i].live():
				Person_win[Percon[i].name ] += 1
				Person_table[ Percon[i].name ][ Percon[j].name ] += 1
			elif Percon[j].live():
				Person_win[Percon[j].name ] += 1
				Person_table[ Percon[j].name ][ Percon[i].name ] += 1

	fight += 1
	with open("test.txt", "a") as file:
		file.write("fight " + str(fight) + " \n")
		for key in Person_win:
			file.write(key + " " + str(Person_win[key]) + " "
					   + str(round(100 * Person_win[key] / ( (len(Percon) - 1) * fight) / 2, 2 ) ) + "% \n")
		#print(Person_table)
		for key_i in Person_table:
			file.write(key_i + ": ")
			for key_j in Person_table:
				if key_i == key_j: continue
				file.write(key_j + " = " + str( round( (100 * Person_table[key_i][key_j] / fight), 2) ) + "% ")
			file.write("\n")