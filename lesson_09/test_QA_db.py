from QA_Table import QA_Table

db = QA_Table("postgresql://postgres:123@localhost:5432/QA")


# Тесты для subject
def test_insert_subject():
    test_id = 17
    test_title = "Geometry"

    db.delete_subject(test_id)

    try:
        db.insert_subject(test_id, test_title)
        result = db.get_subject_by_id(test_id)

        assert result is not None, "Запись не была добавлена в БД"
        assert result[0] == test_title, (f"Ожидалось '{test_title}', "
                                         f"получено '{result[0]}'")
    finally:
        db.delete_subject(test_id)


def test_update_subject():
    test_id = 18
    initial_title = "Old Subject"
    updated_title = "New Subject"

    db.delete_subject(test_id)
    db.insert_subject(test_id, initial_title)

    try:
        db.update_subject(test_id, updated_title)
        result = db.get_subject_by_id(test_id)

        assert result is not None, "Запись не найдена в БД"
        assert result[0] == updated_title, (f"Ожидалось '{updated_title}', "
                                            f"получено '{result[0]}'")
    finally:
        db.delete_subject(test_id)


def test_delete_subject():
    test_id = 19
    test_title = "Subject to Delete"

    db.delete_subject(test_id)
    db.insert_subject(test_id, test_title)

    try:
        db.delete_subject(test_id)
        result = db.get_subject_by_id(test_id)

        assert result is None, "Запись не была удалена из БД"
    finally:
        db.delete_subject(test_id)


# Тесты для teacher
def test_insert_teacher():
    test_id = 777
    test_email = "goncharov@test.ru"
    test_group_id = 99

    db.delete_teacher(test_id)

    try:
        db.insert_teacher(test_id, test_email, test_group_id)
        result = db.get_teacher_by_id(test_id)

        assert result is not None, "Преподаватель не был добавлен в БД"
        assert result[0] == test_id
        assert result[1] == test_email
        assert result[2] == test_group_id
    finally:
        db.delete_teacher(test_id)


def test_update_teacher():
    test_id = 778
    initial_email = "old_mail@test.ru"
    initial_group = 99
    updated_email = "new_mail@test.ru"
    updated_group = 101

    db.delete_teacher(test_id)
    db.insert_teacher(test_id, initial_email, initial_group)

    try:
        db.update_teacher(test_id, updated_email, updated_group)
        result = db.get_teacher_by_id(test_id)

        assert result is not None, "Запись преподавателя не найдена в БД"
        assert result[1] == updated_email, "Email не обновился"
        assert result[2] == updated_group, "Номер группы не обновился"
    finally:
        db.delete_teacher(test_id)


def test_delete_teacher():
    test_id = 779
    test_email = "delete_me@test.ru"
    test_group_id = 103

    db.delete_teacher(test_id)
    db.insert_teacher(test_id, test_email, test_group_id)

    try:
        db.delete_teacher(test_id)
        result = db.get_teacher_by_id(test_id)

        assert result is None, "Запись преподавателя не была удалена из БД"
    finally:
        db.delete_teacher(test_id)


# Тесты для student
def test_insert_student():
    test_user_id = 7
    test_level = "Elementary"
    test_form = "group"
    test_subject_id = 1

    db.delete_student(test_user_id)

    try:
        db.insert_student(test_user_id, test_level, test_form, test_subject_id)
        result = db.get_student_by_id(test_user_id)

        assert result is not None, "Студент не был добавлен в БД"
        assert result[0] == test_user_id
        assert result[1] == test_level
        assert result[2] == test_form
        assert result[3] == test_subject_id
    finally:
        db.delete_student(test_user_id)


def test_update_student():
    test_user_id = 8
    initial_level = "Beginner"
    initial_form = "personal"
    initial_subject_id = 1

    updated_level = "Intermediate"
    updated_form = "group"
    updated_subject_id = 2

    db.delete_student(test_user_id)
    db.insert_student(test_user_id,
                      initial_level,
                      initial_form,
                      initial_subject_id)

    try:
        db.update_student(test_user_id, updated_level,
                          updated_form,
                          updated_subject_id)
        result = db.get_student_by_id(test_user_id)

        assert result is not None, "Запись студента не найдена в БД"
        assert result[1] == updated_level, "Уровень студента не обновился"
        assert result[2] == updated_form, "Форма обучения не обновилась"
        assert result[3] == updated_subject_id, "ID предмета не обновился"
    finally:
        db.delete_student(test_user_id)


def test_delete_student():
    test_user_id = 9
    test_level = "Advanced"
    test_form = "group"
    test_subject_id = 1

    db.delete_student(test_user_id)
    db.insert_student(test_user_id, test_level, test_form, test_subject_id)

    try:
        db.delete_student(test_user_id)
        result = db.get_student_by_id(test_user_id)

        assert result is None, "Запись студента не была удалена из БД"
    finally:
        db.delete_student(test_user_id)
