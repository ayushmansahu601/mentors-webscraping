import csv

from models.mentor import mentor


def is_duplicate_mentor(mentor_name: str, seen_names: set) -> bool:
    return mentor_name in seen_names


def is_complete_mentor(mentor: dict, required_keys: list) -> bool:
    return all(key in mentor for key in required_keys)


def save_mentors_to_csv(mentors: list, filename: str):
    if not mentors:
        print("No mentors to save.")
        return

    # Use field names from the mentor model
    fieldnames = mentor.model_fields.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mentors)
    print(f"Saved {len(mentors)} mentors to '{filename}'.")
