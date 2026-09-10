STUDENTS_COUNT = 5
total_score = 0
passed_count = 0

print("Введите баллы для 5 студентов:")

for i in range(1, STUDENTS_COUNT + 1):
    score = float(input(f"Введите балл студента №{i}: "))
    total_score += score
    if score >= 50:
        passed_count += 1

average_score = total_score / STUDENTS_COUNT

print("---------------------------------")
print(f"Средний балл по группе: {average_score:.2f}")
print(f"Количество студентов с баллом >= 50: {passed_count}")
