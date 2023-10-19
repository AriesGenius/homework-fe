def provide_stage_feedback(stage, attempt_number, user_answer, correct_answer):
  """Provides stage feedback to a student based on their attempts.

  Args:
    stage: The current stage of the problem.
    attempt_number: The number of attempts the student has made on the current stage.
    user_answer: The student's answer to the current stage.
    correct_answer: The correct answer to the current stage.

  Returns:
    A string containing feedback for the student.
  """

  if attempt_number == 1:
    # This is the student's first attempt.
    if user_answer == correct_answer:
      feedback = "Great job! You got the correct answer on your first attempt."
    else:
      feedback = "Don't worry if you didn't get the correct answer on your first attempt. Here is a hint: "
      feedback += get_hint_for_stage(stage)
  elif attempt_number == 2:
    # This is the student's second attempt.
    if user_answer == correct_answer:
      feedback = "Great job! You got the correct answer on your second attempt."
    else:
      feedback = "Don't worry if you didn't get the correct answer on your second attempt. Here is another hint: "
      feedback += get_hint_for_stage(stage)
  elif attempt_number == 3:
    # This is the student's third attempt.
    if user_answer == correct_answer:
      feedback = "Great job! You got the correct answer on your third attempt."
    else:
      feedback = "I'm sorry, but you didn't get the correct answer on your third attempt. Feedback here: "
      feedback += correct_answer

  return feedback

