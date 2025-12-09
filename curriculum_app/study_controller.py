
#--------------------------------------------------------------------------------------------------

#                               Curriculum Application
#                <<<<<<         Made by Kasra Tookallo           >>>>>>
#                                   2025 the year
#                                    12/6/2025
#--------------------------------------------------------------------------------------------------
from study_dao import LessonDataAccess
from study_model import Curriculum

# Since Database Controller is a Class_Method, therefore requires date.
class LessonController:
    @staticmethod

    @staticmethod
    def save(lesson_name, lesson_code, teacher_name, lesson_credits):
        try:
            lesson = Curriculum(
            lesson_name,
            lesson_code,
            teacher_name,
            lesson_credits
            )
            lesson_da = LessonDataAccess()
            lesson_da.save(lesson)
            return True, "Lesson saved successfully"
        except Exception as e:
            return False, f"Lesson saving product {e}"

    @staticmethod
    def edit(lesson_name, lesson_code, teacher_name, lesson_credits):
        try:
            lesson = Curriculum(
                lesson_name,
                lesson_code,
                teacher_name,
                lesson_credits
            )
            lesson_da = LessonDataAccess()
            lesson_da.edit(lesson)
            return True, "Lesson edited successfully"
        except Exception as e:
            return False, f"Lesson editing product {e}"

    @staticmethod
    def remove(lesson_code):
        try:
            lesson_da = LessonDataAccess()
            lesson_da.remove(lesson_code)
            return True, "Lesson removed successfully"
        except Exception as e:
            return False, f"Lesson removing product {e}"

    @staticmethod
    def find_all():
        try:
            lesson_da = LessonDataAccess()
            return True, lesson_da.find_all()
        except Exception as e:
            return False, f"Error find Lesson {e}"
