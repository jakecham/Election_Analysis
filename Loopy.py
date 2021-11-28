print('WHILE LOOP')
print(' ')

x = 0
while x <= 5:
    print(x)
    x = x + 1

print('--------------------')
print(' ')
print('FOR LOOPS')
print(' ')

counties = ['Arapahoe','Denver','Jefferson']

for county in counties:
    print(county)

print('--------------------')

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
print('--------------------')

for num in range(5):
    print(num)

print('--------------------')

for i in range(len(counties)):
    print(counties[i])

print('--------------------')
print(' ')
print('Iterating thru Dictionary')
print(' ')

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

print(' ')

for voters in counties_dict.values():
    print(voters)

print(' ')

for County,Voters in counties_dict.items():
    print(County,Voters)

print(' ')

for county, voters in counties_dict.items():
    print(county, voters)

print(' ')

for key, value in counties_dict.items():
    print(key + ' County has ' + str(value) + ' registered voters')

print(' ')
print('--------------------')
print(' ')
print('Iterating thru a List of Dictionaries')
print(' ')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print(' ')

for q in range(len(voting_data)):
    print(voting_data[q])

print(' ')

for county_dict in voting_data:
    for voters in county_dict.values():
        print(voters)

print(' ')

for county_dict in voting_data:  
     print(county_dict.values())

print(' ')

for voters in voting_data:
     print(voters['registered_voters'])

print(' ')

for county_dict in voting_data:
    print(county_dict['county'])

print(' ')
print('--------------------')
print('PRINTING STUFF')
print(' ')

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

print(' ')
print('--------------------')

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.6f}% of the total votes.")

print(message_to_candidate)