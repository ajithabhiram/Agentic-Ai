# Day 10 - Dictionary Summary
# Dictionary Creation
student = {
    "id": 101,
    "name": "Abhiram",
    "skills": ["Python", "AI"],
    "place": ("Hyderabad", "Bengaluru")
}

# Accessing Dictionary
print(student["name"])
print(student.keys())
print(student.values())
print(student.items())
# Updating Dictionary
student["course"] = "Agentic AI"
student["skills"].extend(["FastAPI", "RAG"])
student["place"] = list(student["place"])
student["place"].append("Vizag")
# Dictionary Methods
print(student.get("branch", "CSE"))
student.setdefault("cgpa", 8.5)
student.update({"year": 4, "college": "Amrita"})
print(student)
# Membership
print("name" in student)
# Remove Elements
student.pop("year")
print(student.popitem())
# Create Dictionary using fromkeys()
subjects = ["Python", "Java", "AI"]
marks = dict.fromkeys(subjects, 0)
marks["Python"] = 95
print(marks)
# Nested Dictionary
students = {
    "S1": {"name": "Abhiram", "age": 22},
    "S2": {"name": "Rahul", "age": 21}
}
print(students["S1"]["name"])
