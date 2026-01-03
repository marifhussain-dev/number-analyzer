import os

print("Current working directory:")
print(os.getcwd())

print("\nFiles in this folder:")
for item in os.listdir():
    print(item)

filename = input("Enter filename (default: data.txt): ").strip()
if filename == "":
    filename = "data.txt"
file_path = os.path.join(os.getcwd(), filename)

print("Full file path:")
print(file_path)

print("\nDoes the file exist?")
print(os.path.exists(file_path))

if not os.path.exists(file_path):
    print("\nFile doest not exist. Creating it now...")
    with open(file_path, "w") as file:
        pass
    print("File created successfully.")
else:
    print("File already exist.")

if os.path.getsize(file_path) == 0:
    print("\nFile is empty. writing initial content...")
    with open(file_path, "w") as file:
        file.write("10\n20\n30\n40\n")
    print("Initial content written to file.")
else:
    ("\nFile is not empty. Skipping write.")

print("\nReading file contents:")

def read_lines(file_path):
    with open(file_path, "r") as f:
        return f.readlines()

lines = read_lines(file_path)
print(lines)

def prase_numbers(lines):
    numbers = []
    skipped = 0
    for line in lines:
        cleaned = line.strip() #remove spaces and \n
        if cleaned.isdigit():
            numbers.append(int(cleaned))
        else:
            skipped += 1
    return numbers, skipped


numbers, skipped = prase_numbers(lines)
print("converted number:", numbers)
print("Skipped lines:", skipped)


def compute_stats(numbers):
    return {
        "Count": len(numbers),
        "Sum": sum(numbers),
        "Min": min(numbers),
        "Max": max(numbers),
        "Average": sum(numbers)/len(numbers),
    }

def main():
    if numbers:
        stats = compute_stats(numbers)
    
        print("Count:", stats["Count"])
        print("Sum:", stats["Sum"])
        print("Min:", stats["Min"])
        print("Max:", stats["Max"])
        print("Average:", stats["Average"])
    
        with open("summary.txt", "w") as f:
            f.write(f"Count: {len(numbers)}\n")
            f.write(f"Sum: {sum(numbers)}\n")
            f.write(f"Min: {min(numbers)}\n")
            f.write(f"Max: {max(numbers)}\n")
            f.write(f"Average: {sum(numbers)/len(numbers)}\n")
        print("Summary saved to summary.txt")
    else:
        print("No valid numbers found to analyze.")

if __name__ == "__main__":
    main()









