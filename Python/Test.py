def compare_arrays_detailed(answer_array, user_answer_array):
  """Compares two arrays and prints a detailed error message for each index where the user's answer is incorrect or missing, including the specific difference.

  Args:
    answer_array: A list of the correct answers.
    user_answer_array: A list of the user's answers.
    problem array: A list of problems that user answer input is different with answers
  """
  problem= []
  for i in range(len(answer_array)):
    if user_answer_array[i] is None:
      print(f"Null answer at index {i}")
    elif user_answer_array[i] != answer_array[i]:
      print(f"Different answer at index {i}:")
      print(f"Answer: {answer_array[i]}")
      print(f"User answer: {user_answer_array[i]}")
      print('\n'+"Differences:")
      for j in range(len(answer_array[i])):
        if answer_array[i][j] != user_answer_array[i][j]:
          if j == 0:
            print(f"- Name wrong but okay")
            problem.append(user_answer_array[i][j]+' name is different but okay')
          elif j == 1:
            print(f"- Attribute wrong")
            problem.append(user_answer_array[i][0]+' AttributeType is wrong')
          elif j == 2:
            print(f"- Attribute visibility wrong")
            problem.append(user_answer_array[i][0]+' AtrributeVisibility is wrong')
          else:
            (f"- {answer_array[i][j]} != {user_answer_array[i][j]}")
      for x in problem:
        print(x)



answer_array = ["staff", ["staffID", "string", "-"], ["firstname", "string", "-"]]
user_answer_array = ["staff", ["staffID", "string", "-"], ["firstname", "", "-"]]
compare_arrays_detailed(answer_array, user_answer_array)
