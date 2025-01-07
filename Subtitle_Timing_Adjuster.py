import os
from datetime import timedelta

def timestamp_to_seconds(timestamp):
    """
    Converts a timestamp in HH:MM:SS,mmm format to seconds.

    Args:
        timestamp (str): The timestamp in HH:MM:SS,mmm format.

    Returns:
        float: The total time in seconds.
    """
    hours, minutes, seconds = map(float, timestamp.replace(',', '.').split(':'))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()

def seconds_to_timestamp(seconds):
    """
    Converts seconds to a timestamp in HH:MM:SS,mmm format.

    Args:
        seconds (float): The time in seconds.

    Returns:
        str: The timestamp in HH:MM:SS,mmm format.
    """
    adjusted_time = timedelta(seconds=seconds)
    adjusted_hours, remainder = divmod(adjusted_time.seconds, 3600)
    adjusted_minutes, adjusted_seconds = divmod(remainder, 60)
    return f"{adjusted_hours:02}:{adjusted_minutes:02}:{adjusted_seconds:02},{int(adjusted_time.microseconds / 1000):03}"

def adjust_subtitles(file_path, output_path, initial_start):
    """
    Adjusts subtitle timings based on user-defined logic.

    Args:
        file_path (str): Path to the input subtitle file.
        output_path (str): Path to save the adjusted subtitle file.
        initial_start (float): Start time for the first subtitle in seconds.
    """
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    adjusted_lines = []
    prev_end = initial_start  # Set initial start time for the first line
    prev_original_end = initial_start  # Initialize previous original end time

    for i, line in enumerate(lines):
        if '-->' in line:  # If it's a timestamp line
            start_time, end_time = line.split(' --> ')
            # Convert timestamps to seconds
            start_sec = timestamp_to_seconds(start_time.strip())
            end_sec = timestamp_to_seconds(end_time.strip())
            # Calculate the duration of the current line
            duration = end_sec - start_sec

            if i == 0:  # First line
                new_start = initial_start
                new_end = new_start + duration
            else:  # Subsequent lines
                # Calculate gap based on original timing
                gap = start_sec - prev_original_end
                new_start = prev_end + gap
                new_end = new_start + duration

            # Format and append the adjusted timestamp
            adjusted_lines.append(f"{seconds_to_timestamp(new_start)} --> {seconds_to_timestamp(new_end)}\n")

            # Update for the next iteration
            prev_end = new_end
            prev_original_end = end_sec
        else:
            adjusted_lines.append(line)  # Keep other lines unchanged

    # Write the adjusted subtitles to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(adjusted_lines)

if __name__ == "__main__":
    # Example usage
    input_file_path = input("Enter the path to the input subtitle file: ")
    output_file_path = input("Enter the path to save the adjusted subtitle file: ")

    # Initial start time for the first subtitle
    initial_start = timestamp_to_seconds("00:00:17,000")

    # Adjust the subtitles
    adjust_subtitles(input_file_path, output_file_path, initial_start)

    print(f"Adjusted subtitles saved to: {output_file_path}")
