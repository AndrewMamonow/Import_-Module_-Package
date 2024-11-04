
def calculate_salary(id, personals):
    for personal in personals:
        if personal['id'] == id:
            return personal['salary']
