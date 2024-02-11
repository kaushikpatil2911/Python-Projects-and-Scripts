# Project 10 - Score Checker

# Instructions

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# Grade	Score
# A	>= 0.9
# B	>= 0.8
# C	>= 0.7
# D	>= 0.6
# F	< 0.6
# Example

# Enter score: perfect
# > Bad score
# Enter score: 10.0
# > Bad score
# Enter score: 0.75
# > C
# Enter score: 0.5
# > F

score = (input("Enter score : "))

try:
    score = float(score)
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print("A Grade")
        if score >= 0.8 and score < 0.9:
            print("B Grade")
        if score >= 0.7 and score < 0.8:
            print("C Grade")
        if score >= 0.6 and score < 0.7:
            print("D Grade")
        if score < 0.6:
            print("F Grade")
    else: print("Bad Score")                      

except ValueError:
    print("Bad Score")
    exit()

