import sys

def print_statistics(total_size, status_codes):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            line = line.strip()

            # Split the line into parts based on spaces
            parts = line.split()

            # Check if the line contains all the required components
            if len(parts) != 10:
                continue

            # Extract the file size and status code from the line
            try:
                file_size = int(parts[-1])
                status_code = parts[-2]

                # Update the total size and status code count
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            except ValueError:
                # If file size or status code is not an integer, skip the line
                continue

            # Print statistics every 10 lines
            if line_number % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        # Print statistics when CTRL + C is pressed
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()

