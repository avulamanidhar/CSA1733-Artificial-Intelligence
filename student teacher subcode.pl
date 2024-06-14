student(john, cs).
student(sarah, math).
student(tom, physics).

teacher(alice, cs).
teacher(bob, math).
teacher(charlie, physics).

sub_code(cs, csci101).
sub_code(math, math101).
sub_code(physics, phys101).

student_info(Student, Code, Teacher) :-
    student(Student, Subject),
    sub_code(Subject, Code),
    teacher(Teacher, Subject).

teacher_info(Teacher, Code, Students) :-
    teacher(Teacher, Subject),
    sub_code(Subject, Code),
    findall(Student, student(Student, Subject), Students).

