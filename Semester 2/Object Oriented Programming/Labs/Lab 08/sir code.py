import csv

def read_error_file(error_file):
    errors = {}
    with open(error_file, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            record_number = int(lines[i].strip())
            record_data = lines[i+1].strip()
            errors[record_number] = record_data
    return errors

def update_grades_file(original_file, error_file, updated_file):
    errors = read_error_file(error_file)
    with open(original_file, 'r') as original, open(updated_file, 'w') as updated:
        reader = csv.reader(original, delimiter=' ')
        writer = csv.writer(updated, delimiter=' ')
        for row in reader:
            record_number = int(row[0][-3:])
            if record_number in errors:
                corrected_data = errors[record_number].split(' ')
                row[3:] = corrected_data[1:]  # Update columns with corrected data
            writer.writerow(row)

def validate_grades_file(updated_file):
    with open(updated_file, 'r') as file:
        lines = file.readlines()
        error_count = 0
        for i, line in enumerate(lines, start=1):
            if len(line.split()) != 7:  # Check if there are exactly 7 columns in each line
                print(f"Error in line {i}: {line}")
                error_count += 1
    return error_count

# Example usage
original_file = 'grades.txt'
error_file = 'errors.txt'
updated_file = 'updated_grades.txt'

# Assuming you manually correct the errors in the 'errors.txt' file
update_grades_file(original_file, error_file, updated_file)

# Validate the updated file
error_count = validate_grades_file(updated_file)

print(f"Total errors in the updated file: {error_count}")
