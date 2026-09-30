# words = "KOWKAK"
# lines = []
# length = 4

# for i in range(0, len(words), length):
#     lines.append(words[i:i+length])
    
# print("\n".join(lines))
import itertools
import collections
import re 

def zipGrades(total_grades, total_students):
    list_grades = []
    for i in range(total_students):
        student_grades = []
        for j in range(total_grades):
            grade = float(input(f"Masukkan nilai ke-{j + 1}: "))
            student_grades.append(grade)
        list_grades.append(student_grades)
    averages = [sum(grade_per_test) / total_grades for grade_per_test in zip(*list_grades)]
    print(averages)
    


# zipGrades(3, 3)

data = [1, 2, 3, 1, 2, 3]

sortedData = sorted(data)
for key, group in itertools.groupby(sortedData):
    print(list(group))


companyData = "aabbiawoskdcsalwaakkkkk"
sortedCompany = sorted(companyData)
countedData = collections.Counter(sortedCompany)

for key, value in countedData.items():
    print(key, value)

def validate_card(card_number):
    pattern_format = r"^[456](\d{15}|\d{3}(-\d{4}){3})$"

    if not re.match(pattern_format, card_number):
        return "Invalid"
    
    clean_card = card_number.replace("-", "")

    pattern_repeat = r"(\d)\1{3,}"

    if re.search(pattern_repeat, clean_card):
        return "Invalid"

    return "Valid"

test_cards = [
    "4123456789123456",      # Valid (16 digit)
    "5123-4567-8912-3456", # Valid (kelompok 4 digit)
    "6123333789123456",    # Invalid (ada 3333)
    "5133-3367-8912-3456", # Invalid (33-33 jika dilepas strip jadi 3333)
    "41234567891234567"    # Invalid (17 digit)
]

for card in test_cards:
    print(f"{card}: {validate_card(card)}")



