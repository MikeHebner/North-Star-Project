
INSERT INTO Course(description,course_ID,credits) VALUES
("Beginning Studio Art Adv. Dramatic","ART101",3),
("Expression","DRM350",3),
("Intro. To Stage Acting Voice-Over for","DRM150",4),
("Animation", "ANI330",2),
("Performing in Stand- Up Comedy","COM210",3);


INSERT INTO Instructor(instructor_ID,instructor_name) VALUES
(0045, "Tom Hanks"),
(0060, "Robin Williams"),
(0035, "Vincent VanGogh"),
(0010, "Martin Scorsese"),
(0040, "Judi Dench"),
(0055, "Mickey Mouse"),
(0030, "Leonardo DaVinci");

INSERT INTO Student(student_ID,student_name)VALUES
(00009045,"Andrew Rodriges"),
(00007832,"Roger Molinari"),
(00004516,"Angus Akedo"),
(00002214,"Sam Smith"),
(00006969,"Cheddar Bob"),
(00003497,"Hank Abrahms");

INSERT INTO Section(course_link,section_ID,capacity,course_ID,instructor_ID) VALUES
(null,001,5,"ANI330",0045),
(null,002,3,"ANI330",0060),
(null,001,8,"DRM150",0040),
(null,001,8,"COM210",0060),
(null,001,10,"ART101",0035),
(null,001,5,"DRM350",0010);

INSERT INTO Enrolls_in(flag, student_ID, course_link) VALUES
("Excess Cred",00003497,(SELECT course_link FROM Section WHERE section_ID=001 AND course_ID="DRM150")),
("None",00003497,(SELECT course_link FROM Section WHERE section_ID=001 AND course_ID="DRM350")),
("None",00003497,(SELECT course_link FROM Section WHERE section_ID=001 AND course_ID="ART101")),
("None",00003497,(SELECT course_link FROM Section WHERE section_ID=001 AND course_ID="COM210"));