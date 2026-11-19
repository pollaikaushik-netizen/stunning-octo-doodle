module_hours = {
    "Module 1 — Beginner": 7,
    "Module 2 — Intermediate": 11,
    "Module 3 — Advanced": 15,
    "Assessment & Wrap-up": 3,
}
total = sum(module_hours.values())
for name, hrs in module_hours.items():
    print(f"{name}: {hrs} h")
print(f"Total: {total} h")