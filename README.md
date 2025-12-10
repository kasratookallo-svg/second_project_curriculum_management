This Python program is prepared to receive Study_related information while showing them in a list and formating them simultaneously, before saving them in a database.
Functions are based on Class_method.

<< Features of the Program >>

- 'Show in Table' Button regarding representing Lesson in a table.

( Database_related merits ) ---->> for future reference :

- 'Submit to Database'
- 'Edit databse'_ Based on Lesson_code
- 'Remove from Databse'

<< Additional Features >>

- Representing Lesson's detail in a format_style for printing.
- Through Window, there are some suggestions for all details displayed in respective Entry_Region, which can be selected by a click.

<< Structure and Folder >>

- Study_model file : Lesson class defines the structure of a Study record.
- Study_controller file : Handles validation and connects the GUI to the database.
- Study_dao file : CurriculumDataAccess manages database operations (save, edit, remove, find).
- Study_view file : Tkinter GUI for managing Lesson (add, edit, remove, view).
