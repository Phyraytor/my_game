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
		mag.Mag,
		knight.Knight,
		healer.Healer,
		scout.Scout,
	]
	for i in range(len(Percon) - 1):
		for j in range(i + 1, len(Percon)):

			person_one = Percon[i](persons[i])
			person_two = Percon[j](persons[j])
			#print(person_one.name, "VS", person_two.name)
			while person_one.live() and person_two.live():
				if person_two.time() <= person_one.time():
					person_two.get_enemy_skill( person_one.get_enemy_skill( person_two.activate() ) )
				else:
					person_one.get_enemy_skill( person_two.get_enemy_skill( person_one.activate() ) )
    
			#with open("debug.txt", "a") as file:
				#file.write(person_one.name + " " + person_one.debug_hp() + " " + person_two.name + " " + person_two.debug_hp() + "\n")
			if person_one.live():
				    #file.write(person_one.name + " WIN\n")
				Person_win[person_one.name ] += 1
				Person_table[ person_one.name ][ person_two.name ] += 1
			elif person_two.live():
					#file.write(person_two.name + " WIN\n")
				Person_win[person_two.name ] += 1
				Person_table[ person_two.name ][ person_one.name ] += 1

	fight += 1
	with open("test.txt", "a") as file:
		file.write("fight " + str(fight) + " \n")
		for key in Person_win:
			file.write(key + " " + str(Person_win[key]) + " "
					   + str(round(100 * Person_win[key] / ( (len(Percon) - 1) * fight) / 2, 2 ) ) + "% \n")
		#print(Person_table)
		file.write("\n")
		for key_i in Person_table:
			file.write(key_i + ": ")
			for key_j in Person_table:
				if key_i == key_j: continue
				file.write(key_j + " = " + str( round( (100 * Person_table[key_i][key_j] / fight), 2) ) + "% ")
			file.write("\n")
		file.write("\n")