
#--------------------------------------------------------------------------------------------------

#                               Curriculum Application
#                <<<<<<         Made by Kasra Tookallo           >>>>>>
#                                   2025 the year
#                                    12/6/2025
#--------------------------------------------------------------------------------------------------
import re

# Molding Studies
class   Curriculum:

    #Donder _ Double Underlines or magic function
    # Method
    def __init__(self, lesson_name, lesson_code, teacher_name , lesson_credits):
        # Property
        self.lesson_name = lesson_name
        self.lesson_code = lesson_code
        self.teacher_name = teacher_name
        self.lesson_credits = lesson_credits

        self.lesson_list = []

    # Method_Show Result
    def save(self):
        print(f"STUDY INFO :   {self.lesson_name:10} , {self.lesson_code:} \t\t ,{self.teacher_name:10} , {self.lesson_credits}")

    # Method_function
    def validation(self ):

        if not re.match(r"^[a-zA-Z0-9\s\.]{3,40}$",self.lesson_name):
            raise NameError("Lesson Name Error!!!!")

        if not (type(self.lesson_code) == int and self.lesson_code > 0):
            raise NameError("Code Error!!!!")

        if not re.match(r"^[a-zA-Z\s\.]{3,30}$", self.teacher_name):
            raise NameError("Teacher Name Error!!!!")

        if not (type(self.lesson_credits) == int and self.lesson_credits > 0):
            raise NameError("Lesson Credits Error!!!!")

        return True

    # Representation
    def __repr__(self):
        return f" \n{self.lesson_name} (Code :{self.lesson_code:^5})\t--->>\t{self.lesson_credits}\t( Credits ) \nTeacher's Name :\t\t {self.teacher_name}\n "

    def to_tuple(self):
        return tuple((self.lesson_name, self.lesson_code, self.teacher_name, self.lesson_credits))
