
def get_employees(id, personals):
    for personal in personals:
        if personal['id'] == id:
            return personal['surname']
