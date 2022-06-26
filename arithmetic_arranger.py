# Arranges addition/subtraction math problems into basic arithmetic format.
# Ability to display solutions is turned off by default.
# Display solution by passing 'True' as second
# argument to 'arithmetic_arranger'.

def arithmetic_arranger(problems, show_soln=False):
    # Check that 5 or fewer problems supplied to function.
    num_probs = check_num_probs(problems)
        
    if num_probs == 0:
        return "Error: Too many problems."

    # Extract numbers and operator from each expression.
    # Store first and second number in their own respective lists.
    nums1_list, operators, nums2_list = arithmetic_parser(problems, num_probs)

    x = check_num_digits(nums1_list, nums2_list)
    if x == 0:
        return "Error: Numbers cannot be more than four digits."

    # Check that all problems contain only digits.
    # If they don't, display error.
    nums1_list, nums2_list, operators, x = check_for_ints(nums1_list, 
    operators, nums2_list, num_probs)

    if x == 0:
        return "Error: Numbers must only contain digits."

    # Return number of underscores required for problem format.
    underscores_list = get_underscores(nums1_list, nums2_list, num_probs)

    # Calculate problem soln.
    prob_solns, x = get_prob_soln(nums1_list, operators, nums2_list,
    num_probs, show_soln)

    if 0 in x:
        return "Error: Operator must be '+' or '-'."

    # Right justify all parts of problem.
    nums1_fmt_list, nums2_fmt_list, solns_fmt_list = right_just(nums1_list,
    nums2_list, underscores_list, num_probs, prob_solns)

    # Return properly formatted problems.
    return print_fmtd_probs(nums1_fmt_list, operators, nums2_fmt_list,
    num_probs, underscores_list, solns_fmt_list, show_soln)


# Check that 5 or fewer problems supplied to function.
def check_num_probs(problems):
    num_probs = len(problems)
    if num_probs > 5:
        num_probs = 0
        return num_probs
    else:
        return num_probs


def check_num_digits(nums1_list, nums2_list):
    for num in nums1_list:
        if len(num) > 4:
            x = 0
            return x
        else:
            x = 1
    
    for num in nums2_list:
        if len(num) > 4:
            x = 0
            return x
        else:
            x = 1

# Check that all problems contain only digits.
# If they don't, skip them.
def check_for_ints(nums1_list, operators, nums2_list, num_probs):
    i = 0
    x = 1
    while i < num_probs:
        try:
            int(nums1_list[i])
            int(nums2_list[i])
        except ValueError:
            x = 0
        i += 1
    
    return nums1_list, nums2_list, operators, x


# Parses each problem into its parts. Stores parts into separate lists.
def arithmetic_parser(problems, num_probs):
    nums1_list = []
    nums2_list = []
    operators = []

    i = 0
    # Loop through 'problems' list to extract numbers and operators.
    while i < num_probs:
        # Parse each str in 'problems'.
        # Store each item in their own lists.
        nums1_list.append(str.split(problems[i])[0])
        operators.append(str.split(problems[i])[1])
        nums2_list.append(str.split(problems[i])[2])
        i += 1

    return nums1_list, operators, nums2_list


# Returns number of underscores required for problem format.
def get_underscores(nums1_list, nums2_list, num_probs):
    digits1_list = []
    digits2_list = []
    # Get digits in num1 for entire list.
    for num in nums1_list:
        digits1 = len(num)
        digits1_list.append(digits1)

    # Get digits in num2 for entire list.
    for num in nums2_list:
        digits2 = len(num)
        digits2_list.append(digits2)

    # Calculate number of underscores needed for arithmetic format.
    # Number of underscores for each problem given by following equation:
    # (underscores = highest_num_digits + 1)
    # +1 accounts for space and operator.
    i = 0
    underscores_list = []
    while i < num_probs:
        underscores = ''

        # Does num1 have more digits than num2?
        if digits1_list[i] > digits2_list[i]:
            n = digits1_list[i] + 2
            while len(underscores) < n:
                underscores += '-'
            underscores_list.append(underscores)

        # Does num1 have fewer digits than num2?
        elif digits1_list[i] < digits2_list[i]:
            n = digits2_list[i] + 2
            while len(underscores) < n:
                underscores += '-'
            underscores_list.append(underscores)
            
        # Do num1 and num2 have same number of digits?
        elif digits1_list[i] == digits2_list[i]:
            n = digits1_list[i] + 2
            while len(underscores) < n:
                underscores += '-'
            underscores_list.append(underscores)
        i += 1

    return underscores_list


# Right justify all parts of problem.
def right_just(nums1_list, nums2_list, underscores_list, num_probs,
prob_solns):
    nums1_fmt_list = []
    nums2_fmt_list = []
    solns_fmt_list = []
    i = 0
    j = 0
    n = 0

    # Set rjust for first number of each problem.
    # Store in list 'nums1_fmt_list'.
    while i < num_probs:
        fmt1 = nums1_list[i].rjust(len(underscores_list[i]))
        nums1_fmt_list.append(fmt1)
        i += 1
    # Set rjust for second number of each problem.
    # Store in list 'nums2_fmt_list'.
    while j < num_probs:
        fmt2 = nums2_list[j].rjust(len(underscores_list[j])-1)
        nums2_fmt_list.append(fmt2)
        j += 1

    # Set rjust for solution of each problem.
    # Store in list 'solns_fmt_list'.
    while n < num_probs:
        fmt_soln = prob_solns[n].rjust(len(underscores_list[n]))
        solns_fmt_list.append(fmt_soln)
        n += 1

    return nums1_fmt_list, nums2_fmt_list, solns_fmt_list


# Calculate problem solution.
def get_prob_soln(nums1_list, operators, nums2_list, num_probs,
show_soln):
    # Display solution when second argument passed to
    # 'arithmetic_arranger' is True.
    prob_solns = []
    i = 0
    x = []
    # Check if answers are to be displayed.
    if show_soln == True:
        # Loop through problems and perform math.
        while i < num_probs:
            # Convert numbers from str to int.
            num1, num2 = int(nums1_list[i]), int(nums2_list[i])

            # If problem is addition, perform addition.
            if operators[i] == '+':
                soln = num1 + num2
                soln = str(soln)
                prob_solns.append(soln)
                x.append(1)
            # If problem is subtraction, perform subtraction.
            elif operators[i] == '-':
                soln = num1 - num2
                soln = str(soln)
                prob_solns.append(soln)
                x.append(1)
            # If problem is anything else, return error.
            elif operators[i] == '*' or '/':
                x.append(0)
                
            i += 1
    elif show_soln == False:
        while i < num_probs:
            prob_solns.append('')
            if operators[i] == '*':
                x.append(0)
            elif operators[i] == '/':
                x.append(0)
            i += 1

    return prob_solns, x


# Print problems formatted appropriately.
def print_fmtd_probs(nums1_fmt_list, operators, nums2_fmt_list, num_probs,
underscores_list, solns_fmt_list, show_soln):
    # Initialize each row of print format.
    master_line1 = ''
    master_line2 = ''
    master_line3 = ''
    master_line4 = ''
    i = 0

     # Check if solution should be displayed.
    # If True, display solution in output.
    if show_soln == True:
        # Loop through created lists.
        # Put pieces of lists together to create formatted output.
        while i < num_probs:
            # Create each line of formatted output using pieces of each problem.
            line1 = f"{nums1_fmt_list[i]}" # Formatted output 1st line.
            line2 = f"{operators[i]}{nums2_fmt_list[i]}" # Formatted output 2nd line.
            line3 = f"{underscores_list[i]}" # Formatted output 3rd line.
            line4 = f"{solns_fmt_list[i]}" # Formatted output 4th line.
            if i < num_probs - 1:
                # Place 4 spaces between each displayed problem.
                line1, line2 = f"{line1}    ", f"{line2}    "
                line3, line4 = f"{line3}    ", f"{line4}    "
            master_line1 += line1 # Concatenate line 1.
            master_line2 += line2 # Concatenate line 2.
            master_line3 += line3 # Concatenate line 3.
            master_line4 += line4 # Concatenate line 4.
            i += 1
        arranged_problems = f"{master_line1}\n{master_line2}\n{master_line3}\n{master_line4}"
        return arranged_problems

    # If false, do not display solution in output.
    elif show_soln == False:
        while i < num_probs:
            # Create each line of formatted output using pieces of each problem.
            line1 = f"{nums1_fmt_list[i]}" # Formatted output 1st line.
            line2 = f"{operators[i]}{nums2_fmt_list[i]}" # Formatted output 2nd line.
            line3 = f"{underscores_list[i]}" # Formatted output 3rd line.
            if i < num_probs - 1:
                # Places 4 spaces between each displayed problem.
                line1, line2 = f"{line1}    ", f"{line2}    "
                line3 = f"{line3}    "
            master_line1 += line1 # Concatenate line 1.
            master_line2 += line2 # Concatenate line 2.
            master_line3 += line3 # Concatenate line 3.
            i += 1
        arranged_problems = f"{master_line1}\n{master_line2}\n{master_line3}"
        return arranged_problems




problems1 = ['3801 - 2', '123 + 49']
problems2 = ['1 + 2', '1 - 9380']
problems3 = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
problems4 = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
problems5 = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']
problems6 = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
problems7 = ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']
problems8 = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
problems9 = ['3 + 855', '988 + 40']
problems10 = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']
print(arithmetic_arranger(problems1))
print(arithmetic_arranger(problems2))
print(arithmetic_arranger(problems3))
print(arithmetic_arranger(problems4))
print(arithmetic_arranger(problems5))
print(arithmetic_arranger(problems6))
print(arithmetic_arranger(problems7))
print(arithmetic_arranger(problems8))
print(arithmetic_arranger(problems9, True))
print(arithmetic_arranger(problems10, True))

