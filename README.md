# Subtitle Timing Adjuster

Have you ever found yourself in a situation where you have a subtitle, but the timing is just a little off? Here's a simple solution to this conundrum. 

This is a simple Python script that adjusts the timing of subtitles in `.srt` format. It starts by setting a new starting time for the first line of dialogue, then dynamically adjusts all subsequent lines based on their original timing intervals.

## Features
- Precisely adjusts subtitle timings.
- Supports dynamic input and output file paths.
- Easy customization for different initial timings.

---

## Requirements
- Python 3.x installed on your system.
- A valid `.srt` subtitle file encoded in `latin-1`.

---

## How to Use
1. Ensure that the subtitle file you want to adjust is accessible.
2. Run the script in a terminal or Python IDE:
   ```bash
   python adjust_subtitles.py
   ```
3. Provide the following inputs when prompted:
   - The path to the input `.srt` file.
   - The path to save the adjusted `.srt` file.
4. The script will process the subtitle timings and save the adjusted file to the specified output path.

---

## Customization
- To set a different starting time for the first subtitle, modify the value of `initial_start` in the script.
  - Example: Replace `"00:00:17,000"` with your desired starting time.

---

## Example
### Input:
- Original subtitle starts at `00:01:03,285`
- Desired starting time: `00:00:17,000`

### Output:
- Adjusted subtitle starts at `00:00:17,000`, with all subsequent lines shifted dynamically to match the original intervals.

---

## Notes
- Ensure your input `.srt` file uses the `latin-1` encoding. You can convert files using a text editor if necessary.
- The script is designed for flexibility and can be modified further to accommodate specific use cases.


