def stingy(total_lambs):
	stingyList = [1, 1]
	x, total = 2, 2
	while x <= total_lambs:
		value = stingyList[x-1] + stingyList[x-2]
		stingyList.append(value)
		total += int(stingyList[x])
		if total > total_lambs:
			break
		x+= 1
	return len(stingyList)


def generous(total_lambs):
	generousList = []
	x, total = 0, 0
	while x <= total_lambs:
		current = 2**x
		generousList.append(current)
		total += current
		if total > total_lambs:
			break
		x += 1
	return len(generousList)


def solution(total_lambs):
	return stingy(total_lambs) - generous(total_lambs)


if __name__ == "__main__":
	i1 = 143
	print(solution(i1))

	i2 = 10
	print(solution(i2))