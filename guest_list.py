guests = ['Sylvester Stallone' , 'Arnold Shwarzenegger' , 'Lee Evans']
print(guests)

guest_one = guests[0]
guest_two = guests[1]
guest_three = guests[2]


#print(guest_one)
#print(guest_two)
#print(guest_three)

invitation = 'Dear ' + guest_one + " come to my party."
invitation_two = 'Dear ' + guest_two + " come to my party."
invitation_three = 'Dear ' + guest_three + " come to my party."
invitation_four = 'Dear ' + guest_three + " come to my party."
invitation_five = 'Dear ' + guest_three + " come to my party."
invitation_six = 'Dear ' + guest_three + " come to my party."

print(invitation)
print(invitation_two)
print(invitation_three)

guest_not_attending = guests.pop(0)
not_attending_message = 'Unfortunately, ' + guest_not_attending + ' will not be attending.'

print(not_attending_message)

print(guests)

guests.append('Anne Frank')
replacement_guest = guests[2].title()
replacement_guest_message = replacement_guest + " will attend instead of " + guest_not_attending

print(replacement_guest_message)

print(guests)

bigger_table = "Dear guests, we have found a bigger dinner table"
print(bigger_table)

guests.insert(0, 'Basshunter')
print(guests)
guests.insert(1, 'Madonna')
print(guests)
guests.append('Corey Taylor')
print(guests)

guest_one = guests[0]
guest_two = guests[1]
guest_three = guests[2]
guest_four = guests[3]
guest_five = guests[4]
guest_six = guests[5]

invitation = 'Dear ' + guest_one + " come to my party."
invitation_two = 'Dear ' + guest_two + " come to my party."
invitation_three = 'Dear ' + guest_three + " come to my party."
invitation_four = 'Dear ' + guest_four + " come to my party."
invitation_five = 'Dear ' + guest_five + " come to my party."
invitation_six = 'Dear ' + guest_six + " come to my party."

print(invitation)
print(invitation_two)
print(invitation_three)
print(invitation_four)
print(invitation_five)
print(invitation_six)
