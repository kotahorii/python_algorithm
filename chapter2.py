subject_score = [70, 98, 92, 88, 64]
total_score = 0
average_score = 0

for i, _ in enumerate(subject_score):
    total_score += subject_score[i]
    average_score = total_score / len(subject_score)

print(total_score, average_score)
