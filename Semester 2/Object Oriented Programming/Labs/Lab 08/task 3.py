def is_valid_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def validate_record(record, line_number):
    
    parts = record.split()

    if len(parts) != 7:
        return f"Error in line {line_number}: Incorrect number of elements"

    if not parts[0].startswith("BSEF") and not parts[0].startswith("BITF"):
        return f"Error in line {line_number}: Invalid Roll Number format"

    if not is_valid_number(parts[5]):
        return f"Error in line {line_number}: Invalid Credit Hours"

    if not is_valid_number(parts[6]) and parts[6] != 'AB':
        return f"Error in line {line_number}: Invalid Marks"

    return None

def main():
    input_file_path = 'grades.txt'
    error_file_path = 'errors.txt'

    with open(input_file_path, 'r') as input_file, open(error_file_path, 'w') as error_file:
        line_number = 1
        error_count = 0

        next(input_file)
        next(input_file)

        for line in input_file:
            line = line.strip()
            error_message = validate_record(line, line_number)

            if error_message:
                error_file.write(f"{line_number}\n{line}\n{error_message}\n\n")
                error_count += 1

            line_number += 1

    print(f"Total errors found: {error_count}")

if __name__ == "__main__":
    main()
