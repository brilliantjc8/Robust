#!/usr/bin/env python3
"""Course information system using parallel dictionaries."""

room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

# Meeting times were omitted from the assignment prompt table; standard course times are populated below.
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def main() -> None:
    course_number = input("Enter a course number (for example, CSC101): ").strip().upper()

    if course_number in room_numbers:
        print(f"\nCourse: {course_number}")
        print(f"Room Number: {room_numbers[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting Time: {meeting_times[course_number]}")
    else:
        print(f"\nSorry, {course_number} was not found in the course catalog.")
        print("Please check the course number and try again.")


if __name__ == "__main__":
    main()
