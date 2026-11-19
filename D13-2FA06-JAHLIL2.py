# --- STUDENT INFORMATION FORMATTER ---
# General Information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")
fav_subject = input("Enter your favorite subject: ")

# Version 2.0

clean_name = first_name.strip().title() + " " + last_name.strip().title()
clean_section = section.strip().upper()
clean_subject = fav_subject.strip().title()

print("=== Formatted Output ===\n")
print("Name: ", clean_name)
print("Name Code: ", clean_name.upper())
print("Character Count: ", len(clean_name))
print("Section: ", clean_section)
print("Favorite Subject: ", clean_subject)
print()
