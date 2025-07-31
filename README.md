# Magic8Ball
A simple Python script that simulates a "Magic 8-Ball". Ask a yes-or-no question and get a fun, random answer.

# 🎱 Magic 8-Ball

This is a command-line Python project that recreates the classic "Magic 8-Ball," a toy used for fortune-telling and seeking advice.

The program prompts the user to ask a yes-or-no question and then selects one of several predefined answers completely at random to display as the "magic ball's" verdict.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `Magic8Ball.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python Magic8Ball.py
    ```
5.  Type your yes-or-no question when prompted and press Enter to see the magic answer.

## Program Logic

* A list of string-based answers is defined at the beginning of the code.
* The `random.choice()` function is used to randomly select one item from this list.
* The user's question is captured using `input()` but does not influence the outcome, replicating how the original toy works.
* The selected random answer is then printed to the console.
