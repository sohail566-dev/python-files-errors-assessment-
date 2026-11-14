Assessment: Functions, Strings, and Lists📌 Project OverviewThis repository contains two Python applications developed for the Functions, Strings, and Lists Assessment. The project demonstrates fundamental Python programming skills, including input validation, custom function creation, string manipulation, and list operations to process and analyze academic marks.📁 Repository Structurepython-functions-lists-assessment/
│
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
📄 Task Descriptions1. Student Result Card Generator (result_card_generator.py)This program collects and processes individual student details to generate a formatted result card.Key Capabilities:Prompts for student name, roll number, and marks across 5 subjects.Validates roll numbers using .isdigit().Formats student names using .strip() and .title().Validates marks to ensure they fall strictly between 0 and 100.Calculates overall percentage, letter grade, and pass/fail status.Strict Failing Rule: If any individual subject mark is below 40, the final result status is set to Fail, regardless of total percentage.2. Class Marks Analyzer (class_marks_analyzer.py)This program processes and analyzes the overall performance of an entire class.Key Capabilities:Maintains parallel lists (student_names and student_marks) using .append().Validates every student's mark within the valid range (0–100).Computes class average, highest score(s), and lowest score(s).Counts passing ($\ge 50$) and failing ($< 50$) students.Identifies students performing above the class average.Displays marks sorted in descending order (highest to lowest).💡 Python Concepts & Core Functions UsedKey Concepts AppliedFunctions (def): Modular code design with parameter passing and return values.String Manipulation: Methods such as .strip(), .title(), and .isdigit() for input formatting and validation.Lists & Operations: Dynamically populating lists with .append() and evaluating data using len(), sum(), max(), min(), and sorted().Control Flow: while loops for input validation and if/elif/else blocks for conditional evaluation.Formatted Output: Python f-strings for clear, readable terminal reports.Custom Functions ImplementedIn result_card_generator.py:format_name(name): Strips extra spaces and converts student names to Title Case.get_valid_marks(subject): Prompts and validates marks ($0 - 100$) for a given subject.calculate_percentage(total, max_total): Returns overall percentage rounded to 2 decimal places.get_grade(percentage): Maps calculated percentage to its corresponding letter grade (A+, A, B, C, D, or Fail).In class_marks_analyzer.py:get_valid_input(prompt, min_val, max_val): Helper function to validate numerical input ranges.analyze_class_data(names, marks): Computes statistical metrics including averages, top/bottom performers, pass/fail counts, and sorted rankings.🚀 Instructions for Running the ProgramsPrerequisitesMake sure you have Python 3.x installed on your system.Running Task 1: Result Card Generatorpython result_card_generator.py
Running Task 2: Class Marks Analyzerpython class_marks_analyzer.py
🧪 Sample Input and OutputSample 1: Task 1 (result_card_generator.py)Sample Input:Enter Student Name:   john doe  
Enter Roll Number: 10123
Enter marks for Subject 1: 85
Enter marks for Subject 2: 92
Enter marks for Subject 3: 78
Enter marks for Subject 4: 88
Enter marks for Subject 5: 95
Sample Output:========================================
           STUDENT RESULT CARD          
========================================
Student Name : John Doe
Roll Number  : 10123
----------------------------------------
Subject 1    : 85.0
Subject 2    : 92.0
Subject 3    : 78.0
Subject 4    : 88.0
Subject 5    : 95.0
----------------------------------------
Total Marks  : 438.0 / 500
Percentage   : 87.60%
Grade        : A
Final Status : PASS
========================================
Sample 2: Task 2 (class_marks_analyzer.py)Sample Input:Enter total number of students: 4

Student 1 Name: Alice
Enter marks for Alice: 92

Student 2 Name: Bob
Enter marks for Bob: 45

Student 3 Name: Charlie
Enter marks for Charlie: 78

Student 4 Name: Diana
Enter marks for Diana: 92
Sample Output:==================================================
              CLASS PERFORMANCE REPORT            
==================================================
Total Students     : 4
Class Average      : 76.75

Highest Score      : 92 (Achieved by: Alice, Diana)
Lowest Score       : 45 (Achieved by: Bob)

Passing Students   : 3
Failing Students   : 1

--- Students Above Class Average ---
- Alice (92)
- Diana (92)
- Charlie (78)

--- Sorted Performance List (Highest to Lowest) ---
1. Alice - 92
2. Diana - 92
3. Charlie - 78
4. Bob - 45
==================================================
