"""
J'Accuse! — A Detective Game to Determine Liars and Truth-Tellers
Run: python jaccuse_game.py

A terminal-based logic mystery game. Each suspect makes a statement.
Exactly one suspect is the culprit in each case. The case rules tell you
whether each suspect is truthful or lying. Use the clues to identify the
culprit before your attempts run out.
"""

import random
import textwrap

CASES = [
    {
        "title": "The Missing Diamond",
        "story": "A diamond disappeared from the museum at 8 PM.",
        "culprit": "Bruno",
        "suspects": [
            ("Alice", "I was in the library."),
            ("Bruno", "I did not enter the museum."),
            ("Chloe", "Bruno is lying."),
            ("David", "Alice is telling the truth."),
        ],
        "truth": {"Alice": True, "Bruno": False, "Chloe": True, "David": True},
        "clues": [
            "The museum camera shows the thief entered through the east door.",
            "Bruno's fingerprint was found on the display case.",
        ],
        "explanation": "Bruno's denial is false, and the fingerprint places him at the display case."
    },
    {
        "title": "The Stolen Painting",
        "story": "A valuable painting vanished during the gallery opening.",
        "culprit": "Maya",
        "suspects": [
            ("Ethan", "Maya was near the gallery."),
            ("Maya", "I never touched the painting."),
            ("Noah", "Ethan is telling the truth."),
            ("Zara", "Maya is lying."),
        ],
        "truth": {"Ethan": True, "Maya": False, "Noah": True, "Zara": True},
        "clues": [
            "A witness saw Maya carrying a large covered frame.",
            "The gallery alarm was disabled using Maya's access card.",
        ],
        "explanation": "Maya's statement is false; the witness and access-card evidence support the accusation."
    },
    {
        "title": "The Library Mystery",
        "story": "The original research notebook went missing from a locked room.",
        "culprit": "Leo",
        "suspects": [
            ("Ivy", "Leo had the only spare key."),
            ("Leo", "I was outside the building."),
            ("Omar", "Ivy is telling the truth."),
            ("Sara", "Leo is telling the truth."),
        ],
        "truth": {"Ivy": True, "Leo": False, "Omar": True, "Sara": False},
        "clues": [
            "The spare key was checked out under Leo's name.",
            "A hallway camera recorded Leo entering the locked room.",
        ],
        "explanation": "Leo's alibi is false. The key record and camera footage identify him."
    },
]

def line(char="=", width=64):
    print(char * width)

def show_case(case, number, total):
    print("\n")
    line()
    print(f"CASE {number}/{total}: {case['title']}".center(64))
    line()
    print(textwrap.fill(case["story"], 64))
    print("\nSUSPECT STATEMENTS")
    for i, (name, statement) in enumerate(case["suspects"], 1):
        print(f"  {i}. {name}: “{statement}”")
    print("\nEVIDENCE")
    for clue in case["clues"]:
        print(f"  • {clue}")

def play_case(case):
    attempts = 2
    while attempts:
        answer = input("\nWho do you accuse? Enter a suspect's name: ").strip().lower()
        names = [s[0].lower() for s in case["suspects"]]
        if answer not in names:
            print("That name is not on the suspect list. Try again.")
            continue
        accused = next(s[0] for s in case["suspects"] if s[0].lower() == answer)
        if accused == case["culprit"]:
            print(f"\nCorrect! {accused} is the culprit.")
            print("CASE SOLVED:", case["explanation"])
            return True
        attempts -= 1
        if attempts:
            print(f"Not quite. You have {attempts} attempt left. Re-examine the evidence.")
    print(f"\nCase closed. The culprit was {case['culprit']}.")
    print(case["explanation"])
    return False

def main():
    print("\n" + "J'ACCUSE!".center(64))
    print("A Detective Game: Liars, Truth-Tellers & Logic".center(64))
    line()
    print("MISSION: Read each statement, study the evidence, and identify")
    print("the culprit. You get two attempts for every case.")
    input("\nPress Enter to begin...")
    score = 0
    random.shuffle(CASES)
    for number, case in enumerate(CASES, 1):
        show_case(case, number, len(CASES))
        if play_case(case):
            score += 1
        if number < len(CASES):
            input("\nPress Enter for the next case...")
    line()
    print("FINAL REPORT".center(64))
    print(f"You solved {score} out of {len(CASES)} cases.")
    if score == len(CASES):
        print("Excellent detective work! You spotted every culprit.")
    elif score >= 2:
        print("Good investigation! Keep sharpening your logic.")
    else:
        print("Keep practising. Every clue matters!")
    line()
    print("Thank you for playing J'Accuse!")

if __name__ == "__main__":
    main()
