import sys

def ask_yes_no(message):
    while True:
        choice = input(message).strip().lower()
        if choice == "y" or choice == "n":
            return choice
        else:
            print("Please enter only 'y' or 'n'.")
def load_file():
    while True:

        filename = input("Enter log filename (example: log.txt): ").strip()

        try:
            with open(filename, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print("File not found", filename)
            choice = ask_yes_no("Do you want to create it? (y/n): ").strip().lower()
            if choice == "y":
                with open(filename, "w") as file:
                    pass #create empty file
                print("Created", filename, "-add logs inside it and run again.")
                sys.exit()
            else:
                print("Okay, exiting.")
            return None
        if content.strip() == "":
            print("The file is empty.")
            print("Add some log lines and run again.")
            return None
        return content

def analyze_logs(content):
        lines = content.splitlines() #safer than split("\n")
        counts = {"ERROR": 0, "WARNING": 0, "INFO": 0, "OTHER": 0}
        valid_lines =0
        for line in lines:
            clean = line.strip()
            if clean == "":
                continue #skip blank lines
            valid_lines += 1
            upper_line = clean.upper()
            if "ERROR" in upper_line:
                counts["ERROR"] += 1
            elif "WARNING" in upper_line:
                counts["WARNING"] += 1
            elif "INFO" in upper_line:
                counts["INFO"] += 1
            else:
                counts["OTHER"] += 1
        return valid_lines, counts
def main():
    while True:
        content = load_file()
        if content is None:
            break
        
        print("File loaded successfully")
        total_lines, counts = analyze_logs(content)
        print("\n----log Summary-----")
        print("Total lines:", total_lines)
        print("ERROR:", counts["ERROR"])
        print("WARNING:", counts["WARNING"])
        print("INFO:", counts["INFO"])
        print("OTHER:", counts["OTHER"])

        if counts["OTHER"] == 0:
            print("\nNo OTHER lines found(only ERROR/WARNING/INFO.)")
        with open("summary_report.txt", "w") as report:
            report.write("\n----log Summary-----")
            report.write(f"Total lines: {total_lines}\n")
            report.write(f"ERROR: {counts["ERROR"]}\n")
            report.write(f"WARNING: {counts["WARNING"]}\n")
            report.write(f"INFO: {counts["INFO"]}\n")
            report.write(f"OTHER: {counts["OTHER"]}\n")
        print("summary saved to summary_report.txt")

        
        again = ask_yes_no("Do you want to analyze another file?(y/n)").strip().lower()
        if again == "n":
            print("Goodbye")
            break
main()












