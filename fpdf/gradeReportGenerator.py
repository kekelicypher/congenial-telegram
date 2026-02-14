from fpdf import FPDF

class MyPDF(FPDF):
    def header(self):
        self.set_font("Courier", "B", 15)
        self.cell(0, 10, "ATORKOR M/A BASIC SCHOOL", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln = True

    def footer(self):
        self.set_font("Courier", "I", 8)
        self.set_y(-15)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = MyPDF()

fields = {"name", "course", "level"}
student_data = {}

subjects = {"Maths", "Science", "Art", "Social"}
student_subjects = {}

for i in fields:
    student_data[i] = input(f"Enter student {i}: ")

for i in subjects:
    student_subjects[i] = input(f"Enter grade for {i}: ").capitalize()


pdf.add_page()
pdf.set_font("Courier", "B", 15)
pdf.cell(0, 15, "STUDENT REPORT CARD", align="C", new_x="LMARGIN", new_y="NEXT", border=1)

for i in fields:
    pdf.cell(0, 15, f"{i.capitalize()}: {student_data[i]}", new_x="LMARGIN", new_y="NEXT")

# pdf.ln(10)

for i in subjects:
    pdf.cell(0, 15, f"{i.capitalize()} : {student_subjects[i]}", new_x="LMARGIN", new_y="NEXT")

pdf.output("report.pdf")

# pdf.cell(0, 12, "PASS?")





