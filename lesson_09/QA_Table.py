from sqlalchemy import create_engine
from sqlalchemy.sql import text


class QA_Table:
    __scripts = {
        # Скрипты для таблицы subject
        "insert_subject": text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        "select_subject": text(
            "SELECT subject_title FROM subject "
            "WHERE subject_id = :id"
        ),
        "update_subject": text(
            "UPDATE subject SET subject_title = :new_title "
            "WHERE subject_id = :id"
        ),
        "delete_subject": text(
            "DELETE FROM subject WHERE subject_id = :id"
        ),

        # Скрипты для таблицы teacher
        "insert_teacher": text(
            "INSERT INTO teacher (teacher_id, email, group_id) "
            "VALUES (:id, :email, :group_id)"
        ),
        "select_teacher": text(
            "SELECT teacher_id, email, group_id FROM teacher "
            "WHERE teacher_id = :id"
        ),
        "update_teacher": text(
            "UPDATE teacher SET email = :new_email, group_id = :new_group_id "
            "WHERE teacher_id = :id"
        ),
        "delete_teacher": text(
            "DELETE FROM teacher WHERE teacher_id = :id"
        ),

        # Скрипты для таблицы student
        "insert_student": text(
            "INSERT INTO student (user_id, level, education_form, subject_id) "
            "VALUES (:user_id, :level, :education_form, :subject_id)"
        ),
        "select_student": text(
            "SELECT user_id, level, education_form, subject_id FROM student "
            "WHERE user_id = :user_id"
        ),
        "update_student": text(
            "UPDATE student SET level = :new_level, "
            "education_form = :new_form, "
            "subject_id = :new_subject_id WHERE user_id = :user_id"
        ),
        "delete_student": text(
            "DELETE FROM student WHERE user_id = :user_id"
        ),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    # Методы для subject
    def insert_subject(self, subject_id, subject_title):
        self.__db.execute(
            self.__scripts["insert_subject"],
            {"id": subject_id, "title": subject_title}
        )

    def get_subject_by_id(self, subject_id):
        row = self.__db.execute(
            self.__scripts["select_subject"],
            {"id": subject_id}
        ).fetchall()
        return row[0] if row else None

    def update_subject(self, subject_id, new_title):
        self.__db.execute(
            self.__scripts["update_subject"],
            {"id": subject_id, "new_title": new_title}
        )

    def delete_subject(self, subject_id):
        self.__db.execute(
            self.__scripts["delete_subject"],
            {"id": subject_id}
        )

    # Методы для teacher
    def insert_teacher(self, teacher_id, email, group_id):
        self.__db.execute(
            self.__scripts["insert_teacher"],
            {"id": teacher_id, "email": email, "group_id": group_id}
        )

    def get_teacher_by_id(self, teacher_id):
        return self.__db.execute(
            self.__scripts["select_teacher"],
            {"id": teacher_id}
        ).fetchall()

    def update_teacher(self, teacher_id, new_email, new_group_id):
        self.__db.execute(
            self.__scripts["update_teacher"],
            {"id": teacher_id, "new_email": new_email,
             "new_group_id": new_group_id}
        )

    def delete_teacher(self, teacher_id):
        self.__db.execute(
            self.__scripts["delete_teacher"],
            {"id": teacher_id}
        )

    # Методы для student
    def insert_student(self, user_id, level, education_form, subject_id):
        self.__db.execute(
            self.__scripts["insert_student"],
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            }
        )

    def get_student_by_id(self, user_id):
        return self.__db.execute(
            self.__scripts["select_student"],
            {"user_id": user_id}
        ).fetchone()

    def update_student(self, user_id, new_level, new_form, new_subject_id):
        self.__db.execute(
            self.__scripts["update_student"],
            {
                "user_id": user_id,
                "new_level": new_level,
                "new_form": new_form,
                "new_subject_id": new_subject_id
            }
        )

    def delete_student(self, user_id):
        self.__db.execute(
            self.__scripts["delete_student"],
            {"user_id": user_id}
        )
