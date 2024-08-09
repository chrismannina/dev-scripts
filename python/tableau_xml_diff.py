import subprocess
import os
import sys
import datetime

def format_xml(input_file, output_file):
    try:
        subprocess.run(['xmllint', '--format', input_file], stdout=open(output_file, 'w'), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to format {input_file}")
        print(f"xmllint error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: xmllint not found. Please ensure it's installed and in your PATH.")
        sys.exit(1)

def generate_diff(file1, file2, output_file):
    try:
        with open(output_file, 'w') as f:
            subprocess.run(['diff', '-u', file1, file2], stdout=f, stderr=subprocess.PIPE, check=False)
        print(f"Diff output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to generate diff. {e}")
        print(f"diff error output: {e.stderr.decode()}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: diff command not found. Please ensure it's installed and in your PATH.")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1.twb> <file2.twb>")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    
    if not (os.path.exists(file1) and os.path.exists(file2)):
        print("Error: One or both input files do not exist.")
        sys.exit(1)

    formatted1 = "formatted1.xml"
    formatted2 = "formatted2.xml"

    print("Formatting XML files...")
    format_xml(file1, formatted1)
    format_xml(file2, formatted2)

    # Generate a unique filename for the diff output
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    diff_output_file = f"diff_output_{timestamp}.txt"

    print("Generating diff...")
    generate_diff(formatted1, formatted2, diff_output_file)

    # Clean up temporary files
    os.remove(formatted1)
    os.remove(formatted2)

if __name__ == "__main__":
    main()