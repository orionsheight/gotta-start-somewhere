# Initial report
rep = " "

# Build report with task lines.
while True :
    line = input('Enter your task (if all tasks entered, type done): ')
    if sval == 'done' :
        break
    rep = rep + '\n' + line

# Print report
print(rep)
