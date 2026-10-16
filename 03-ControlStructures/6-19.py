#dobrze, ale nwm czy tak chcieli to w zadaniu
interested="No"
comp_games="No"
Instagram="No"

if input("SURVEY Are you interested in computer science? (y/n): ")=='y':
    interested="Yes"
    
if input("Do you like playing computer games? (y/n): ")=='y':
    comp_games="Yes"
    
if input("Do you have an Instagram account? (y/n): ")=='y':
    Instagram="Yes"

print(f"SURVEY RESULTS Interested in computer science: {interested}")
print(f"Playing computer games: {comp_games}")
print(f"Has an Instagram account: {Instagram}")


