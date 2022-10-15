class Examination:
    def __init__(self, questions, answer):
        self.questions = questions
        self.answer = answer


qns = ["1. What is a programming language?\nA. Python\nB. Food\nC. Computer\nD. House\n  ",
       "2. Is a computer part of a computer system?"
       "\nA. Maybe\nB. It's the computer system itself\nC. No\nD. Yes\n  ",
       "3. State which of the given are input devices?\nA. Monitor\nB. Keyboard\nC. Printer\nD. Hen\n  ",
       "4. tomorrow is what?\nA. Monday\nB. Saturday\nC. Python paper day\nD. Holiday\n  "]

ans = [Examination(qns[0], "A"),
       Examination(qns[1], "D"),
       Examination(qns[2], "B"),
       Examination(qns[3], "C")
       ]


def run_result(ans):
    score = 0
    for answer in ans:
        a_qn = input(answer.questions).upper()
        if a_qn == answer.answer:
            print("correct")
            score += 1
        else:
            print("wrong")
    print(f"you have got {score}/4")


run_result(ans)


            


