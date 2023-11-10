def grade_calculator(assignments: list, bonus_assignment: int, exam: int) -> tuple[bool, int]:
    final_grade = 5
    assignments = [0 if score is None else score for score in assignments]
    if bonus_assignment is None:
        bonus_assignment = 0
    if exam is None:
        exam = 0
    assignments.append(bonus_assignment)
    ass = assignments
    passed_assignments = [i for i in assignments if i >= 25]
    if len(passed_assignments) < 8:
        return False, final_grade
    else:
        assignments_sum = sum(assignments)
        total_points = assignments_sum + exam
        grade = total_points / 1100 * 100
        if total_points < 0.5 * 1100 or assignments_sum < 0.5 * 1000 or exam <= 0.5 * 100:
            return False, final_grade
        else:
            if grade >= 87.5:
                final_grade = 1
            elif 75 <= grade < 87.5:
                final_grade = 2
            elif 62.5 <= grade < 75:
                final_grade = 3
            elif grade >= 50:
                final_grade = 4
            return True, final_grade


# print(grade_calculator([0, 100, 100, 13, 100, 100, None, 100, 100, 100], 100, 100))
# print(grade_calculator([95, 100, 39, 13, 86, 71, 20, 100, 83, 100], None, 82))
# print(grade_calculator([95, 100, 39, 13, 86, 71, 20, 100, 83, 100], 51, 82))
# print(grade_calculator([0, 100, 100, 13, 100, 100, 20, 100, 100, 100], 0, 100))
# print(grade_calculator([0, 100, 100, 13, 100, 100, 20, 100, 100, 100], 100, 100))
# print(grade_calculator([0, 100, 100, 13, 100, 100, None, 100, 100, 100], 100, 100))
# print(grade_calculator([100, 100, 100, 100, 100, 100, 100, 100, 100, 100], 100, 49))
