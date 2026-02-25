content = """# Day 21 - Introduction to Machine Learning

Machine Learning is a method of teaching computers to learn patterns from data instead of programming every rule manually. In traditional programming, we give the computer data and clear instructions (rules) to get the output. But in Machine Learning, we provide the computer with data and the correct outputs (answers), and the system automatically learns the rules or patterns that connect them. This allows computers to make predictions or decisions on new data without being explicitly programmed for every situation.
"""

with open("Day21_Intro_to_ML.md", "w") as file:
    file.write(content)

print("Markdown file created successfully!")