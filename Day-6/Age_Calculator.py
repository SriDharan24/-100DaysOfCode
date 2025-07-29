# age_calculator.py

from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        age_months -= 1
        age_days += 30  # Approximation

    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

def main():
    print("📆 Welcome to the Age Calculator!")
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_age(birth_date)
        print(f"🎉 You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
