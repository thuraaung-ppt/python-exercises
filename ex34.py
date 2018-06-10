
animals = ['bear','python3.6','peacock','kangaroo','whale']

places = {
	1 : "first(1st)",
	2 : "second(2nd)",
	3 : "third(3rd)",
	4 : "fourth(4th)",
	5 : "fifth(5th)",
}

positions = {
	1 : "1st",
	2 : "2nd",
	3 : "3rd",
	4 : "4th",
	5 : "5th",
}

is_valid = False

query_string = ''

query_string = input()

while query_string != '':

	for i in range(1,6):
		if str(i) in query_string:
			selected_index = i
			is_valid = True
			break


	if is_valid:
		print(f"The {places[selected_index]} animal is at {selected_index - 1} and is a {animals[selected_index - 1]}")
		print(f"The animal at {selected_index-1} is the {positions[selected_index]} animal and is a {animals[selected_index - 1]}\n")
		is_valid = False
		
	else: 
		print(f"Invalid position!\n")

	query_string = input()


print("Terminated!")