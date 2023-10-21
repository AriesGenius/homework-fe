def feedback_function(answer_array, user_answer_array, attempt_number):
  """Generates feedback for a user based on their attempts.

  Args:
    answer_array: A list of the correct answers.
    user_answer_array: A list of the user's answers.
    attempt_number: The number of the user's attempt.

  Returns:
    A string containing the feedback.
  """
  
  # First attempt: General and summary feedback.
  if attempt_number == 1:
    feedback = "Overall, your first attempt was good. You were able to identify the main components of the system. However, there are a few areas where you could improve. "

  # Second attempt: More detailed feedback, such as checking components and attribute types.
  elif attempt_number == 2:
    feedback = "Your second attempt was better than your first. You were able to identify more components and their relationships. However, there are still a few areas where you could improve."

  # Last attempt: More detailed feedback, but don't show the answer directly.
  else:
    feedback = "Your last attempt was the best. You were able to identify almost all of the components and their relationships. "

  # Add specific feedback based on the user's attempts.
  for i in range(len(answer_array)):
    if user_answer_array[i] is None:
      feedback += "\n- You missed the components. "
    elif user_answer_array[i] != answer_array[i]:
      feedback += "\n- The component is not correct showing as below. "
      for j in range(len(answer_array[i])):
        if answer_array[i][j] != user_answer_array[i][j]:
          if j == 0:
            feedback += "\n- in "+user_answer_array[i][0]+" Name wrong but okay "
          elif j == 1:
            feedback += "\n- in "+user_answer_array[i][0]+" Attribute type wrong "
          elif j == 2:
            feedback += "\n- in "+user_answer_array[i][0]+" Attribute visibility wrong "
          else:
            feedback += "\n- {} != {}".format(answer_array[i][j], user_answer_array[i][j])

  return feedback

# Example usage:

answer_array = ["staff", ["staffID", "string", "-"], ["firstname", "string", "-"]]
user_answer_array = ["staff", ["staffID", "int", "-"], ["firstname", "string", "-"]]

# First attempt feedback
feedback = feedback_function(answer_array, user_answer_array, 1)
print(feedback)

# Second attempt feedback
user_answer_array = ["staff", ["StaffID", "int", "-"], ["firstname", "string", "-"]]
feedback = feedback_function(answer_array, user_answer_array, 2)
print(feedback)

# Last attempt feedback
user_answer_array = ["staff", ["staffID", "int", "+"], ["firstname", "string", "-"]]
feedback = feedback_function(answer_array, user_answer_array, 3)
print(feedback)
