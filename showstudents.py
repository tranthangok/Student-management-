import csv

class ShowStudent:
    @staticmethod
    def get_students_data():
        students = []
        with open('students.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append({
                    'Name': row['Name'],
                    'Date of Birth': row['Date of Birth'],
                    'Student Code': row['Student Code'],
                    'Class Code': row['Class Code'],
                    'ECTs': row['ECTs'],
                    'Score': row['Score']
                })
        return students

    def __init__(self, tree):
        self.tree = tree

    def refresh_student_list(self):
        # Clear existing data in the tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve updated student data and populate the tree
        students = self.get_students_data()
        for student in students:
            self.tree.insert('', 'end', values=(
                student['Name'],
                student['Date of Birth'],
                student['Student Code'],
                student['Class Code'],
                student['ECTs'],
                student['Score']
            ))
