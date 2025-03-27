#!/usr/bin/python3
class StudentGradeCalculator:
    def __init__(self):
        """Initialize with an empty list for assignments."""
        self.assignments = []
    
    def add_assignment(self, title, category, weight, score):
        """Validate and store assignment details."""
        if not (0 <= weight <= 100):
            raise ValueError("Weight must be between 0 and 100")
        if not (0 <= score <= 100):
            raise ValueError("Grade must be between 0 and 100")
        
        self.assignments.append({
            "title": title,
            "category": category.lower(),
            "weight": weight,
            "score": score
        })
    
    def compute_weighted_scores(self):
        """Calculate overall and category-wise weighted averages."""
        total_weighted, total_weight = 0, 0
        category_data = {"formative": {"score": 0, "weight": 0}, "summative": {"score": 0, "weight": 0}}
        
        for task in self.assignments:
            weighted_score = (task["score"] * task["weight"]) / 100
            total_weighted += weighted_score
            total_weight += task["weight"]
            category_data[task["category"]]["score"] += weighted_score
            category_data[task["category"]]["weight"] += task["weight"]
        
        overall = (total_weighted / total_weight * 100) if total_weight else 0
        avg_formative = (category_data["formative"]["score"] / category_data["formative"]["weight"] * 100) if category_data["formative"]["weight"] else 0
        avg_summative = (category_data["summative"]["score"] / category_data["summative"]["weight"] * 100) if category_data["summative"]["weight"] else 0
        
        return overall, avg_formative, avg_summative
    
    def calculate_gpa(self, final_score):
        """Convert the percentage score to a GPA scale (out of 5)."""
        return (final_score / 100) * 5
    
    def assess_performance(self, avg_formative, avg_summative):
        """Determine pass/fail status based on averages."""
        return "Pass" if avg_formative >= 50 and avg_summative >= 50 else "Fail and Repeat"
    
    def start(self):
        """Handle user input, process data, and display results."""
        print("Welcome to the Student Grade Calculator!")
        print("Enter assignment details (or type 'done' to finish).\n")
        
        while True:
            title = input("Assignment Name (or 'done' to finish): ")
            if title.lower() == 'done':
                break
            category = input("Category (Formative/Summative): ")
            weight = float(input("Weight (%): "))
            score = float(input("Grade (%): "))
            
            try:
                self.add_assignment(title, category, weight, score)
                print("Assignment recorded successfully!\n")
            except ValueError as e:
                print(f"Error: {e}\n")
        
        overall, avg_formative, avg_summative = self.compute_weighted_scores()
        gpa = self.calculate_gpa(overall)
        status = self.assess_performance(avg_formative, avg_summative)
        
        print("\nFinal Report:")
        print(f"Overall Grade: {overall:.2f}%")
        print(f"GPA: {gpa:.2f} / 5")
        print(f"Formative Average: {avg_formative:.2f}%")
        print(f"Summative Average: {avg_summative:.2f}%")
        print(f"Status: {status}")

# Run the program
calculator = StudentGradeCalculator()
calculator.start()


#  Concepts Used:
# - Data Structures: Lists, Dictionaries
# - Conditional Logic: If-Else statements
# - Loops: For loops, While loops
# - Object-Oriented Programming: Classes, Objects
# - Error Handling: Exception handling with try-except
