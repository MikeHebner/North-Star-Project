DROP TABLE IF EXISTS Course;
CREATE TABLE Course
(
  description VARCHAR NOT NULL,
  course_ID VARCHAR NOT NULL,
  credits INT NOT NULL,
  PRIMARY KEY (course_ID)
);

DROP TABLE IF EXISTS Instructor;
CREATE TABLE Instructor
(
  instructor_ID INT NOT NULL,
  instructor_name VARCHAR NOT NULL,
  PRIMARY KEY (instructor_ID)
);


DROP TABLE IF EXISTS Student;
CREATE TABLE Student
(
  student_name VARCHAR NOT NULL,
  student_ID INT NOT NULL,
  PRIMARY KEY (student_ID)
);

DROP TABLE IF EXISTS Section;
CREATE TABLE Section
(
  course_link INTEGER PRIMARY KEY,
  section_ID INT NOT NULL,
  capacity INT NOT NULL,
  course_ID VARCHAR NOT NULL,
  instructor_ID INT NOT NULL,
  FOREIGN KEY (course_ID) REFERENCES Course(course_ID),
  FOREIGN KEY (instructor_ID) REFERENCES Instructor(instructor_ID)
);

DROP TABLE IF EXISTS Enrolls_in;
CREATE TABLE Enrolls_in
(
  flag VARCHAR NOT NULL,
  student_ID INT NOT NULL,
  course_link INT NOT NULL,
  PRIMARY KEY (student_ID, course_link),
  FOREIGN KEY (student_ID) REFERENCES Student(student_ID),
  FOREIGN KEY (course_link) REFERENCES Section(course_link)
);