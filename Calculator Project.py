def calculator_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def main():
   print("Welcome to the grading calculator.")

   total = 0
   num_scores = 4

   for i in range(num_scores):
       score = float(input("Enter your score: "))
       total += score

       average = total/num_scores

   letter_grade = calculator_letter_grade(average)

   print("---Results---")
   print(f"Average Score: {average:.2f}")
   print(f"Letter Grade: {letter_grade}")

   if letter_grade == "F":
       print("Status: Failed")
   else:
       print("Status: Passed")

if __name__ == "__main__":
    main()

