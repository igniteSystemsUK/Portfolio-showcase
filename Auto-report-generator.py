import datetime

def generate_business_report(client_name, data_points):
    """Automates the creation of a daily summary report."""
    date = datetime.date.today()
    print(f"--- Report for {client_name} ({date}) ---")
    for i, point in enumerate(data_points, 1):
        print(f"Task {i}: {point} - COMPLETED")
    print("--- End of Report ---")

if __name__ == "__main__":
    tasks = ["Server Check", "Database Backup", "UI Optimization"]
    generate_business_report("Software Solutions Client", tasks)
