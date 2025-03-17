week_spending = {
    'Sunday': 300,
    'Monday': 145,
    'Tuesday': 90,
    'Wednesday': 700,
    'Thursday': 100,
    'Friday': 826,
    'Saturday': 210
}
total_spending = (week_spending['Sunday']+week_spending['Monday']+week_spending['Tuesday']+week_spending['Wednesday']+week_spending['Thursday']+week_spending['Friday'])+week_spending['Saturday']
average_spending= total_spending/7
print(f"The total average spending per day is: {average_spending}")


