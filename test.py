import mag
import knight
import healer
import scout

def count_fight(count_pers: int, fight:int) -> int:
	return (count_pers - 1) * fight 

Percon = [
			mag.Mag("Mag"), 
			knight.Knight("Knight"), 
			healer.Healer("Healer"), 
			scout.Scout("Scout")
		]
		
for pers in Percon:
	pers.win = 0

fight = 0
while(True):
	for i in range(len(Percon) - 1):
		for j in range(i + 1, len(Percon)):

			while Percon[i].live() and Percon[j].live():
				if Percon[j].time() <= Percon[i].time():
				    Percon[j].get_enemy_skill( Percon[i].get_enemy_skill( Percon[j].activate() ) )
				else:
				    Percon[i].get_enemy_skill( Percon[j].get_enemy_skill( Percon[i].activate() ) )

			if Percon[i].live():Percon[i].win += 1
			elif Percon[j].live():Percon[j].win += 1

	fight += 1
	with open("test.txt", "a") as file:
		file.write("fight" + str(fight) + "\n")
		for pers in Percon:
			file.write(pers.name + " " + str(pers.win) + " " + str(round(100 * pers.win / count_fight(len(Percon), fight) ), 2) + "% \n")