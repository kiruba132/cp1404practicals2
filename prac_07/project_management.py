"""
Project Management Program
Estimate: 1 hours
Actual Time: 3 hours

"""
from project import Project
from datetime import datetime
from operator import attrgetter


FILENAME = "projects.txt"


def main():
    """Main menu-driven program for managing projects."""
    print("Welcome to Pythonic Project Management")

    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n" \
           "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

    print(menu)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid option.")

        print(menu)
        choice = input(">>> ").lower()

    save_on_quit = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_on_quit in ('yes', 'y'):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a tab-delimited file into a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                parts = line.strip().split('\t')
                project = Project(*parts)
                projects.append(project)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty project list.")
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_tab_string() + '\n')


def display_projects(projects):
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    completed_projects = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects starting after a user-entered date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        filtered_projects.sort(key=attrgetter("start_date"))
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project():
    """Prompt the user to input and return a new Project object."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    return Project(name, start_date_string, priority, cost_estimate, completion_percentage)


def update_project(projects):
    """Allow the user to choose a project and update its fields."""
    print("Projects:")
    for index, project in enumerate(projects):
        print(f"{index} {project}")

    try:
        project_index = int(input("Project choice: "))
        selected_project = projects[project_index]
        print(f"Selected project:\n{selected_project}")

        new_completion_percentage = input("New Percentage: ")
        if new_completion_percentage.strip():
            selected_project.completion_percentage = int(new_completion_percentage)

        new_priority = input("New Priority: ")
        if new_priority.strip():
            selected_project.priority = int(new_priority)

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid project number and numeric values where required.")



if __name__ == "__main__":
    main()
