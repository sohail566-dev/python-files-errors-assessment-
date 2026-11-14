def format_name(name):
    """Cleans and formats the student's name using strip() and title()."""
    return name.strip().title()

def get_valid_roll_no():
    """Validates that the roll number contains digits only using .isdigit()."""
    while True:
        roll_no = input("Enter student roll number (digits only): ").strip()
        if roll_no.isdigit():
            return roll_no
        print("Error: Roll number must contain digits only. Please try again.")

def get_valid_marks(subject_name):
    """Validates that the entered marks for a subject are between 0 and 100."""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject_name} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Error: Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid numerical value.")

def calculate_percentage(total, max_total):
    """Calculates the percentage given obtained total and maximum total."""
    if max_total == 0:
        return 0.0
    return (total / max_total) * 100

def get_grade(percentage):
    """Determines letter grade based on percentage criteria."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

def main():
    print("=== Student Result Card Generator ===")
    
    # 1. Ask and format student's name
    raw_name = input("Enter student's name: ")
    student_name = format_name(raw_name)
    
    # 2. Ask and validate roll number using .isdigit()
    roll_no = get_valid_roll_no()
    
    # 3. Ask for marks in five subjects with validation
    subjects = ["Mathematics", "English", "Physics", "Chemistry", "Computer Science"]
    subject_marks = {}
    
    print("\nEnter marks for the 5 subjects:")
    for subject in subjects:
        subject_marks[subject] = get_valid_marks(subject)
        
    # Calculations
    total_obtained = sum(subject_marks.values())
    max_total = len(subjects) * 100
    percentage = calculate_percentage(total_obtained, max_total)
    grade = get_grade(percentage)
    
    # Important Rule Check: If any subject mark is below 40, final result must be Fail
    has_failed_subject = any(mark < 40 for mark in subject_marks.values())
    
    if has_failed_subject or percentage < 50:
        final_status = "Fail"
    else:
        final_status = "Pass"
        
    # Generate properly formatted result card using f-strings
    print("\n" + "=" * 55)
    print("STUDENT RESULT CARD".center(55))
    print("=" * 55)
    print(f"Student Name : {student_name:<30} Roll No: {roll_no}")
    print("-" * 55)
    print(f"{'Subject':<22} | {'Marks Obtained':<15} | {'Max Marks':<10}")
    print("-" * 55)
    
    for subj, marks in subject_marks.items():
        print(f"{subj:<22} | {marks:<15} | 100")
        
    print("-" * 55)
    print(f"Total Marks  : {total_obtained} / {max_total}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Letter Grade : {grade}")
    print(f"Final Status : {final_status}")
    if has_failed_subject:
        print("Note         : Result marked as Fail due to obtaining < 40 in one or more subjects.")
    print("=" * 55)

if __name__ == "__main__":
    main()