from database import *
from datetime import date

create_table()

def show_menu():
    print("\n" + "=" * 35)
    print("       🚀 JOBTRACK")
    print("=" * 35)
    print("1. Add Application")
    print("2. View Applications")
    print("3. Search Company")
    print("4. Delete Application")
    print("5. Exit")

while True:

    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":

        company = input("Company: ")
        role = input("Job Role: ")

        print("\n1. Applied")
        print("2. Interview")
        print("3. Selected")
        print("4. Rejected")

        status_choice = input("Status: ")

        statuses = {
            "1": "Applied",
            "2": "Interview",
            "3": "Selected",
            "4": "Rejected"
        }

        status = statuses.get(status_choice, "Applied")

        add_application(
            company,
            role,
            status,
            str(date.today())
        )

        print("✅ Application added!")

    elif choice == "2":

        applications = get_applications()

        print("\n📋 APPLICATIONS")

        if not applications:
            print("No applications found.")
        else:
            for app in applications:
                print(
                    f"ID: {app[0]} | "
                    f"{app[1]} | "
                    f"{app[2]} | "
                    f"{app[3]} | "
                    f"{app[4]}"
                )

    elif choice == "3":

        company = input("Search company: ")
        results = search_company(company)

        if results:
            for app in results:
                print(app)
        else:
            print("❌ No results found.")

    elif choice == "4":

        try:
            app_id = int(input("Application ID: "))
            delete_application(app_id)
            print("🗑️ Application deleted.")
        except ValueError:
            print("❌ Enter a valid ID.")

    elif choice == "5":

        print("Thanks for using JobTrack! 👋")
        break

    else:
        print("❌ Invalid option.")
