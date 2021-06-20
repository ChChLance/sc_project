"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
word_lst = []
bog_lst = []
ans_lst = []
legal_edge = []
record_lst = []
look_up_dict = {}


def main():
	"""
	TODO:
	"""
	read_dictionary()
	legal_edge_setup()
	for i in range(1, 5):
		row = input(str(i) + " row of letters: ")
		row_lst = row.lower().split()
		if check_illegal(row_lst) is False:
			print('Illegal input')
			break
		bog_lst.append(row_lst)
	if i == 4:
		built_dict()
		boggle()


def boggle():
	for x in range(0, 4):  # Start from every point
		for y in range(0, 4):
			# Take out letter location and append into record_lst
			start_point = (y, x)
			record_lst.append(start_point)
			boggle_helper(y, x)
	print("There are " + str(len(ans_lst)) + " words in total.")


def boggle_helper(y, x):
	for i in range(-1, 2):  # Search toward all direction
		for j in range(-1, 2):
			if (y+i, x+j) not in record_lst:  # Check whether we already passed the location
				if legal_edge_check((y+i, x+j)):  # Check whether the location excess the edge
					record_lst.append((y+i, x+j))  # Append letter into the record list
					cur_word = take_record_lst_str(record_lst)  # Take out string in the record list
					if len(cur_word) >= 4:  # Check prefix & ans at the same time only if length of word >= 4
						if has_prefix_and_find_ans(cur_word) == 'with_ans':
							if cur_word not in ans_lst:  # Just keep a unique answer
								ans_lst.append(cur_word)
								print("Found: ", cur_word)
							boggle_helper(y + i, x + j)
						else:
							# No prefix -> no wat to go -> pop(go back to previous selected point)
							record_lst.pop()
					else:  # Only check prefix when length of word < 4
						if has_prefix(cur_word):
							boggle_helper(y + i, x + j)
						else:
							# No prefix -> no wat to go -> pop(go back to previous selected point)
							record_lst.pop()
	# Completed search for all direction -> no wat to go -> pop(go back to previous selected point)
	record_lst.pop()


def check_illegal(row_lst):
	for letter in row_lst:
		if len(letter) != 1:
			return False


def built_dict():
	for x in range(0, 4):
		for y in range(0, 4):
			look_up_dict[(y, x)] = bog_lst[y][x]


def take_record_lst_str(lst):
	"""
	:param lst: list, the record list
	:return: str, the string which is taken from the record list
	"""
	cur_word = ''
	for tpl in lst:
		cur_word = cur_word + look_up_dict[tpl]
	return cur_word


def legal_edge_setup():
	for i in range(0, 4):
		for j in range(0, 4):
			legal_edge.append((i, j))


def legal_edge_check(cur_point):
	if cur_point in legal_edge:
		return True
	else:
		return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.split()
			if len(line[0]) >= 4:
				word_lst.append(line[0])


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in word_lst:
		if i.startswith(sub_s):
			return True
	return False


def has_prefix_and_find_ans(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in word_lst:
		if i.startswith(sub_s):
			if sub_s == i:
				return "with_ans"
			else:
				return "no_ans"
	return False


if __name__ == '__main__':
	main()
