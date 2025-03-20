# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name                
        self.last_name = last_name                  
        self.age = age                              
        self.email = email                          
        self.can_teach_subjects = can_teach_subjects  # предмети, які викладач може викладати (множина)
        self.assigned_subjects = set()              # предмети, які йому призначать (спочатку пустий набір)


def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)  
    schedule = []  

    while uncovered_subjects:
        best_teacher = None     # обраний викладач на цьому кроці
        best_covered = set()    # предмети, які він покриває на цьому кроці

        for teacher in teachers:
            # перетин між тим, що викладач може викладати, і тим, що ще залишилося непокритим
            covered = teacher.can_teach_subjects & uncovered_subjects
            if not covered:
                continue

            # вибираємо викладача: або вперше, або кращого за кількістю предметів, або молодшого за віком
            if (best_teacher is None or
                len(covered) > len(best_covered) or
                (len(covered) == len(best_covered) and teacher.age < best_teacher.age)):
                best_teacher = teacher
                best_covered = covered

        if best_teacher is None:
            return None

        # призначаємо предмети обраному викладачу
        best_teacher.assigned_subjects = best_covered
        schedule.append(best_teacher)

        # оновлюємо список непокритих предметів
        uncovered_subjects -= best_covered

        # видаляємо викладача зі списку, щоб не обрати його повторно
        teachers.remove(best_teacher)

    return schedule

# Точка входу
if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
    ]

    # Виклик функції для створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення результату
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
