def solution(answers):
	p1 = [1, 2, 3, 4, 5]
	p2 = [2, 1, 2, 3, 2, 4, 2, 5]
	p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	score = [0, 0, 0]
	for i in range(len(answers)):
		if p1[i%5] == answers[i]:
			score[0] += 1
		if p2[i%8] == answers[i]:
			score[1] += 1
		if p3[i%10] == answers[i]:
			score[2] += 1
	answer = list()
	max_score = max(score)
	for i in range(3):
		if score[i] == max_score:
			answer.append(i+1)
	return answer