# **AI_4_letter**

- **Problem:** To get a specified number of 4-letter prompts, then process these prompts to find common substrings at the end of the previous prompt and the start of the subsequent prompt and concatenate them to form a final result.

- **Method 01:** Without using AI Algos:
  Algorithm:
   1. The code begins by asking the user to input how many 4-letter prompts they will enter.
   2. It collects the entered prompts and stores them in a list called 'word'.
   3. The code then proceeds to iterate through the prompts to find common substrings at the end of the previous prompt and the start of the subsequent prompt and build the final result.
   4. It initializes two lists: 'x' to store common substrings and 'y' to store non-common segments of prompts.
   5. The code iterates through the list of prompts (from the third to the second-to-last prompt) and compares adjacent prompts to find common substrings or non-common segments.
   6. Common substrings are appended to the 'x' list, and non-common segments are appended to the 'y' list.
   7. The code joins the common substrings in the 'x' list and adds them to the first and last prompts to create the final result.
   8. The final result is printed.
