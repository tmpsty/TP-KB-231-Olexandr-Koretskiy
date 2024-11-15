input_string = "abcdefg123"
if len(input_string) == 10:
    letters = input_string[:7]
    numbers = input_string[7:]
    result_string = numbers[::-1] + letters[::-1]
    print("Result", result_string)
else:
    print("The line must contain exactly 10 characters")