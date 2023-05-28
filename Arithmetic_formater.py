def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arranged_problems = ["", "", "", ""]
    
    for problem in problems:
     
        operand1, operator, operand2 = problem.split()
        

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
    
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
     
        result = str(eval(problem))
    
        max_length = max(len(operand1), len(operand2)) + 2
        
     
        arranged_problems[0] += operand1.rjust(max_length)
        
      
        arranged_problems[1] += operator + " " + operand2.rjust(max_length - 2)
        
      
        arranged_problems[2] += "-" * max_length
        
      
        if show_answers:
            arranged_problems[3] += result.rjust(max_length)
        
  
    arranged_problems = "\n".join(arranged_problems)
    
    return arranged_problems

problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems, show_answers=True))
