% Program 19: Student-Teacher-Subject-Code database.
% Facts: teaches(Teacher, Student, SubjectCode).
teaches(mr_kumar, arun, cs101).
teaches(mrs_priya, divya, cs102).
teaches(mr_kumar, rahul, cs103).
teaches(mrs_meena, arun, cs102).
teaches(mr_john, divya, cs101).

% Queries:
% ?- teaches(Teacher, arun, SubjectCode).
% ?- teaches(Teacher, Student, cs101).
% ?- teaches(mr_kumar, Student, SubjectCode).
