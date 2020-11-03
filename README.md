# multiple_choice_exams_tex

This is a Python code that takes as input a LaTeX exam file in the exam documentclass. The Python file will shuffle problems and answers within each problem. It will produce n_versions (set to 3 by default) exam versions. It will actually generate a tex file for each of the versions, and will produce the solutions keys, as a single text file for all the versions.

Instructions for shuffling LaTeX exams:

1) Copy the file "shuffling_exam_problems_tex_exam.py" to a folder having two subfolders:
"original_exam" and "shuffled_exams".
2) Edit the copied Python file accordingly: changing the exam filename, n_versions (set to 3 by default).
3) Run the python (3) file, using for instance:
python shuffling_exam_problems_tex_exam.py
or
python3 shuffling_exam_problems_tex_exam.py

Enjoy shuffling!