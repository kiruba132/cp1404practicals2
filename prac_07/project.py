from datetime import datetime

class Project:
    """Class to store a single project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date() \
            if isinstance(start_date, str) else start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Enable sorting by project priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion_percentage == 100

    def update_completion(self, completion_percentage):
        """Update the completion percentage of the project."""
        self.completion_percentage = int(completion_percentage)

    def update_priority(self, priority):
        """Update the priority of the project."""
        self.priority = int(priority)

    def starts_after(self, date):
        """Check if the project starts after the given date."""
        return self.start_date > date

    def to_tab_string(self):
        """Return a tab-separated string for saving."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"
