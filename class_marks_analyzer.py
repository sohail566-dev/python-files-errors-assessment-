def get_valid_mark(student_name):
    """Validates that the entered mark is between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {student_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Error: Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def calculate_statistics(names, marks):
    """Calculates and displays class statistics, averages, highest/lowest scorers, and pass/fail counts."""
    if not marks:
        print("No student records found.")
        return None

    total_marks = sum(marks)
    class_average = total_marks / len(marks)
    
    highest_mark = max(marks)
    lowest_mark = min(marks)
    
    # Find all students with highest and lowest marks (handles potential ties)
    highest_students = [names[i] for i, m in enumerate(marks) if m == highest_mark]
    lowest_students = [names[i] for i, m in enumerate(marks) if m == lowest_mark]
    
    passing_count = sum(1 for m in marks if m >= 50)
    failing_count = sum(1 for m in marks if m < 50)
    
    print("\n" + "=" * 55)
    print("CLASS PERFORMANCE SUMMARY".center(55))
    print("=" * 55)
    print(f"Total Students     : {len(names)}")
    print(f"Class Average      : {class_average:.2f}")
    print(f"Highest Marks      : {highest_mark} (Achieved by: {', '.join(highest_students)})")
    print(f"Lowest Marks       : {lowest_mark} (Achieved by: {', '.join(lowest_students)})")
    print(f"Passing Students   : {passing_count} (>= 50)")
    print(f"Failing Students   : {failing_count} (< 50)")
    print("=" * 55)
    
    return class_average

def display_above_average_and_sorted(names, marks, class_average):
    """Displays students scoring above average and shows marks sorted from highest to lowest."""
    # Display students scoring above the class average
    print(f"\nStudents Scoring Above Class Average ({class_average:.2f}):")
    print("-" * 55)
    above_avg_found = False
    for i in range(len(names)):
        if marks[i] > class_average:
            print(f"• {names[i]}: {marks[i]}")
            above_avg_found = True
    if not above_avg_found:
        print("No students scored above the class average.")

    # Display student marks sorted from highest to lowest
    print("\nStudent Marks Sorted (Highest to Lowest):")
    print("-" * 55)
    sorted_pairs = sorted(zip(marks, names), reverse=True)
    for mark, name in sorted_pairs:
        print(f"{name:<20} : {mark}")
    print("=" * 55)

def main():
    # Maintain two separate lists as requested
    student_names = []
    student_marks = []

    print("=== Class Marks Analyzer ===")
    
    # Get number of students with validation
    while True:
        try:
            num_students = int(input("Enter how many students are in the class: "))
            if num_students > 0:
                break
            print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    # Collect student names and marks using .append()
    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        name = input("Enter student's name: ").strip().title()
        mark = get_valid_mark(name)
        
        student_names.append(name)
        student_marks.append(mark)

    # Calculate statistics using custom function
    class_avg = calculate_statistics(student_names, student_marks)
    
    # Display analytics if data exists
    if class_avg is not None:
        display_above_average_and_sorted(student_names, student_marks, class_avg)

if __name__ == "__main__":
    main()