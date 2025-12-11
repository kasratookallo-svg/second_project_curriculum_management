
#--------------------------------------------------------------------------------------------------

#                               Curriculum Application
#                <<<<<<         Made by Kasra Tookallo           >>>>>>
#                                   2025 the year
#                                    12/6/2025
#--------------------------------------------------------------------------------------------------
import sqlite3

#                                             Database_related Functions
with sqlite3.connect("Curriculum_backup_db") as connection:
    cursor = connection.cursor()

    cursor.execute("""
        create table if not exists lessons_backup (
            lesson_name text,
    lesson_code integer primary key,
    teacher_name text,
    lesson_credits integer
        )
    """)

    connection.commit()
# Submit Button reference
class LessonDataAccess:
    def save(self, lesson):
        with  sqlite3.connect("Curriculum_backup_db") as connection:
            cursor = connection.cursor()
            cursor.execute("insert into lessons_backup ("
                           "lesson_name,"
                           "lesson_code,"
                           "teacher_name,"
                           "lesson_credits)"
                           " values (?, ?, ?, ?)",
                           [
                            lesson.lesson_name,
                            lesson.lesson_code,
                            lesson.teacher_name,
                            lesson.lesson_credits]
                           )
            connection.commit()

    # Edit Button reference
    def edit(self, lesson):
        with  sqlite3.connect("Curriculum_backup_db") as connection:
            cursor = connection.cursor()
            cursor.execute("update lessons_backup set lesson_name=?, teacher_name=?, lesson_credits=? where lesson_code=?",
                           [
                            lesson.lesson_name,
                            lesson.teacher_name,
                            lesson.lesson_credits ,
                            lesson.lesson_code]
                           )
            connection.commit()

    # Remove Button reference

    def remove(self, lesson_code):
        with  sqlite3.connect("Curriculum_backup_db") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from lessons_backup where lesson_code=?", [lesson_code])
            connection.commit()

    def find_all(self):
        with  sqlite3.connect("Curriculum_backup_db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from lessons_backup order by lesson_code")
            return cursor.fetchall()
