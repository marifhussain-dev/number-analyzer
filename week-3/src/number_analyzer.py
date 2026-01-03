import os
import argparse

def show_environment(args):
    if not args.quiet:
        print("Current working directory:")
        print(os.getcwd())

        print("\nFiles in this folder:")
        for item in os.listdir():
            print(item)

def get_input_filename(default="data.txt"):
    filename = input(f"Enter filename (default: {default}): ").strip()
    return filename if filename else default

def read_lines(file_path):
    with open(file_path, "r") as f:
        return f.readlines()
    

def parse_numbers(lines):
    numbers = []
    skipped = 0
    for line in lines:
        cleaned = line.strip() #remove spaces and \n
        if cleaned.isdigit():
            numbers.append(int(cleaned))
        else:
            skipped += 1
    return numbers, skipped

def compute_stats(numbers):
    return {
        "Count": len(numbers),
        "Sum": sum(numbers),
        "Min": min(numbers),
        "Max": max(numbers),
        "Average": sum(numbers)/len(numbers),
    }



def write_summary(stats, outfile):
    with open(outfile, "w") as f:
        for k, v in stats.items():
            f.write(f"{k}: {v}\n")
    print(f"Summary saved to {outfile}")#output_file
    print("Done. You can analyze another file now.")


def get_args():
    parser = argparse.ArgumentParser(description="Analize numbers in a text file.")
    parser.add_argument("--in", dest="infile", default="data.txt", help="input filename(default: data.txt)")
    parser.add_argument("--out", dest="outfile", default = "summary.txt", help="Output filename (default: summary.txt)")
    parser.add_argument("--quiet", action="store_true", help="Hide extra prints (show only results/errors)")
    return parser.parse_args()
    

def main():
    args = get_args()
    print("DEBUG infile", args.infile)
    while True:
        show_environment(args)

        filename = args.infile
        file_path = os.path.join(os.getcwd(), filename)

        if not os.path.exists(file_path):
            print("\nFile not found.", file_path)
            return
            print("File already exist.")

        lines = read_lines(file_path)
        if not args.quiet:
            print("\nReading file contents:")
            print(lines)
        if not lines:
            print("File is empty.")
        else:
            numbers, skipped = parse_numbers(lines)
            print("converted number:", numbers)
            print("Skipped lines:", skipped)

            if not numbers:
                print("No valid numbers found to analyze.")
                return
            
            stats = compute_stats(numbers)
            print("Count:", stats["Count"])
            print("Sum:", stats["Sum"])
            print("Min:", stats["Min"])
            print("Max:", stats["Max"])
            print("Average:", stats["Average"])

            write_summary(stats, args.outfile)

        while True:
            choice = input("Analyze another file? (y/n): ").strip().lower()
            if choice == "y":
                break
            elif choice == "n":
                return
            print ("please enter 'y' or 'n'.")
        
        filename = input("Enter filename (default: data.txt): ").strip()
        if filename == "":
            filename = "data.txt"
        args.infile = filename

if __name__ == "__main__":
    main()
