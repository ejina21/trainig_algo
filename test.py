def convert_to_good_string(s1: str) -> str:
	def check_remove(sym1, sym2):
		if sym1.casefold() == sym2.casefold() and \
			(sym1.islower() and sym2.isupper() or sym1.isupper() and sym2.islower()):
			return True
		return False
	new_str = []
	i = 0
	while i < len(s1):
		first = i
		second = i + 1
		new_str.append(i)
		flag = True
		while first > -1 and second < len(s1) and check_remove(s1[first], s1[second]):
			i += 2 if flag else 1
			new_str.pop()
			first = new_str[-1] if new_str else -1
			second += 1
			flag = False
		if flag:
			i += 1
	return ''.join(s1[i] for i in new_str)

probably_bad_string = input()
print(convert_to_good_string(probably_bad_string))