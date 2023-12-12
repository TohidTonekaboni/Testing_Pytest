import pytest
from unittest.mock import MagicMock
from source.school import Person, Teacher, Classroom, Student, TooManyStudents


@pytest.fixture
def empty_classroom():
    teacher = Teacher(name="Professor McGonagall")
    return Classroom(teacher=teacher, students=[], course_title="Transfiguration")


@pytest.fixture
def full_classroom():
    teacher = Teacher(name="Professor Snape")
    students = [Student(name=f"Student{i}") for i in range(11)]
    return Classroom(teacher=teacher, students=students, course_title="Potions")


def test_add_student(empty_classroom):
    student = Student(name="Harry Potter")
    empty_classroom.add_student(student)
    assert len(empty_classroom.students) == 1


def test_add_student_raises_exception(full_classroom):
    with pytest.raises(TooManyStudents):
        student = Student(name="Ron Weasley")
        full_classroom.add_student(student)


def test_remove_student(empty_classroom):
    student = Student(name="Hermione Granger")
    empty_classroom.add_student(student)
    empty_classroom.remove_student("Hermione Granger")
    assert len(empty_classroom.students) == 0


def test_change_teacher(empty_classroom):
    new_teacher = Teacher(name="Professor Dumbledore")
    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher == new_teacher


def test_change_teacher_mock(empty_classroom):
    new_teacher = MagicMock(spec=Teacher)
    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher == new_teacher


# Additional test using parameterize
@pytest.mark.parametrize("initial_students, expected_count", [
    ([], 0),
    ([Student(name=f"Student{i}") for i in range(5)], 5),
    ([Student(name=f"Student{i}") for i in range(12)], 12),  # Adjusted expected_count to 10
])
def test_classroom_student_count(empty_classroom, initial_students, expected_count):
    empty_classroom.students = initial_students
    assert len(empty_classroom.students) == expected_count
