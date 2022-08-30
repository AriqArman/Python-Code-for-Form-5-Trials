ticket_type = ["Adult", "Child", "Senior", "Family", "Groups>=6"]
ticketquantitylist = [0, 0, 0, 0, 0]
onedayprice = [20,12,16,60,15]
twodayprice = [30,18,24,90,22.5]
extra_attraction = ["Lion feeding", "Penguin feeding", "Evening barbeque"]
attractionquantitylist = [0,0,0]
attractionprice = [2.5, 2, 5]
exclusive_attraction = "Evening barbeque"

print("Welcome to Wildlife Park!")

print(f"Ticket type \t\t One day cost($) \t Two day cost($)")
for index in range(len(ticket_type)):
    print(f"{index + 1}. {ticket_type[index]:<10} \t\t  {onedayprice[index]:^10}{twodayprice[index]:>20}")

print(f"\nExtra Attractions:")
for index in range(len(extra_attraction)):
    print(f"{index + 1}. {extra_attraction[index]} \t      {attractionprice[index]}")

#date/day booking
month = int(input("Enter the current month: " ))
while month < 1 or month > 12:
    month = int(input("Enter the current month correctly: "))

day = int(input("Enter today's date: "))
while day < 1 or day > 31 or (month == 2 and day > 28):
    day = int(input("Enter today's date correctly: "))

print("The days available for booking are: ")

available_days = []
available_dates = []
for count in range(7):
    if month == 2 and day == 28:
        day = 0
        month += 1
    elif day == 31:
        day = 0
        month += 1
    day += 1
    available_days.append(day)

    dates = str(day)+"/"+str(month)
    available_dates.append(dates)

print(available_days)

#task 2

daychoice = int(input("Enter 1 for One Day Booking or 2 for Two Days Booking: "))
while daychoice != 1 and daychoice != 2:
    daychoice = int(input("Enter 1 for One Day Booking or 2 for Two Days Booking: "))

while True:
    ticketchoice = int(input("Which ticket type would you like to book (1-5) or 0 to proceed: "))
    match ticketchoice:
        case 1: 
            adultqty = int(input("Enter the number of adults in your group: "))
            while adultqty < 0:
                adultqty = int(input("Enter the number of adults in your group: "))
            ticketquantitylist[0] += adultqty
        
        case 2:
            if ticketquantitylist[0] == 0 and ticketquantitylist[2] == 0:
                print("You cannot book this ticket without an adult/senior")
            else:
                adultsenior = ticketquantitylist[0] + ticketquantitylist[2]
                maxchildren = adultsenior * 2
                print(f"Your can book for a maximum of {maxchildren} children")

                childqty = int(input("Enter the number of children in your group: "))
                while childqty < 0 or childqty > maxchildren:
                    childqty = int(input("Enter the number of children in your group: "))
                
                ticketquantitylist[1] += childqty

        case 3:
            seniorqty = int(input("Enter the number of seniors in your group: "))
            while seniorqty < 0:
                seniorqty = int(input("Enter the number of seniors in your group: "))
            ticketquantitylist[2] += seniorqty
            
        case 4:
            familyqty = int(input("How many family tickets do you want: "))
            while familyqty < 0:
                familyqty = int(input("How many family tickets do you want: "))

            maxchildren = familyqty * 3
            maxadultsenior = familyqty * 2

            print(f"Your can book for a maximum of {maxchildren} children and a maximum of {maxadultsenior} adults/seniors")

            adultqty = int(input("Enter the number of adults in your family: "))
            while adultqty < 0 or adultqty > maxadultsenior:
                adultqty = int(input("Enter the number of adults in your family: "))

            seniorqty = int(input("Enter the number of seniors in your family: "))
            while seniorqty < 0 or (seniorqty + adultqty) > maxadultsenior:
                seniorqty = int(input("Enter the number of seniors in your family: "))
            
            childqty = int(input("Enter the number of children in your family"))
            while childqty < 0 or childqty > maxchildren:
                childqty = int(input("Enter the number of children in your family"))
                    
            ticketquantitylist[0] += adultqty
            ticketquantitylist[1] += childqty
            ticketquantitylist[2] += seniorqty
            ticketquantitylist[3] += familyqty

        case 5:
            groupnumber = int(input("Enter the number of people in your group: "))
            while groupnumber < 6:
                print("You must have at least 6 or more people in your group")
                groupnumber = int(input("Enter the number of people in your group: "))
            groupvalidation = True
            while groupvalidation == True:

                adultqty = int(input("Enter the number of adults in your group: "))
                while adultqty < 0 or adultqty > groupnumber:
                    adultqty = int(input("Enter the number of adults in your group: "))

                seniorqty = int(input("Enter the number of seniors in your group: "))
                while seniorqty < 0 or (seniorqty + adultqty) > groupnumber:
                    seniorqty = int(input("Enter the number of seniors in your group: "))
                
                maxchild = groupnumber - (seniorqty + adultqty) 
                print(f"You can only book for a maximum of {maxchild} children")

                childqty = int(input("Enter the number of children in your group: "))
                while childqty < maxchild or (childqty + seniorqty + adultqty) > groupnumber:
                    childqty = int(input("Enter the number of children in your group: "))
                    if childqty == maxchild:
                        groupvalidation = False
                    

            ticketquantitylist[0] += adultqty
            ticketquantitylist[1] += childqty
            ticketquantitylist[2] += seniorqty
            ticketquantitylist[4] += groupnumber

        case 0:
            break
        case _:
            continue

attractionloop = True

while attractionloop == True:
    attractionchoice = int(input("Which extra attractions would you like to add on (1-3) or 0 if you wish to proceed: "))
    while attractionchoice < 0 or attractionchoice > 3:
        attractionchoice = int(input("Which extra attractions would you like to add on (1-3) or 0 if you wish to proceed: "))

    attractionindex = attractionchoice - 1

    if attractionchoice == 1 or attractionchoice == 2:
        attractionquantitylist[attractionindex] = 1
    
    elif attractionchoice == 3:
        if daychoice == 1:
            print("You are not allowed to book this ticket for one day tickets!")
        
        else:
            attractionquantitylist[attractionindex] = 1
    
    else: 
        attractionloop = False

def totalCost(daychoice, ticketquantitylist, attractionquantitylist, onedayprice, twodayprice, 
              attractionprice):

    ticketcost = 0
    attractioncost = 0
    for index in range(len(ticketquantitylist)):
        if daychoice == 1:
            ticketcost += (ticketquantitylist[index] * onedayprice[index])
        else:
            ticketcost += (ticketquantitylist[index] * twodayprice[index])
    
    for attractionindex in range(len(attractionquantitylist)):
        attractioncost += (attractionquantitylist[attractionindex] * attractionprice[attractionindex])

    totalcost = ticketcost + attractioncost
    return totalcost, attractioncost

totalcost = totalCost(daychoice, ticketquantitylist, attractionquantitylist, onedayprice, twodayprice, attractionprice)[0]
attractioncost = totalCost(daychoice, ticketquantitylist, attractionquantitylist, onedayprice, twodayprice, attractionprice)[1]

#display booking details

for index in range(len(ticket_type)):
    if ticketquantitylist[index] != 0:
        print(f"You have booked for {ticketquantitylist[index]} {ticket_type[index]}")

for index in range(len(extra_attraction)):
    if attractionquantitylist[index] != 0:
        print(f"You have booked for {extra_attraction[index]}")

bookingnumber = str(day)+str(totalcost)+str(ticketquantitylist[4])
print(f"Your booking number is {bookingnumber}")
print(f"Your total cost is: ${totalcost}")
        
#task 3
altprice = 1000
altprice2 = 1000

checkbestprice = True

while checkbestprice == True:
    family_ticket = 0

    adsen = ticketquantitylist[0] + ticketquantitylist[2]
    child = ticketquantitylist[1]
    groupnumber = ticketquantitylist[0] + ticketquantitylist[1] + ticketquantitylist[2]

    while adsen >= 2 and child >= 3:
        adsen -= 2 
        child -= 3
        family_ticket += 1
    
    if daychoice == 1:
        if groupnumber >= 6:
            altprice = (onedayprice[4] * groupnumber) + attractioncost
        family_price = onedayprice[3] * family_ticket
        child_price = onedayprice[1] * child
        adsen_price = onedayprice[0] * adsen
    else:
        if groupnumber >= 6:
            altprice = (twodayprice[4] * groupnumber) + attractioncost
        family_price = twodayprice[3] * family_ticket
        child_price = twodayprice[1] * child 
        adsen_price = twodayprice[0] * adsen

    altprice2 = family_price + adsen_price + child_price + attractioncost
    
    
    if altprice < altprice2:
        print(f"Alternate price is: ${altprice}")
    elif altprice2 < altprice:
        print(f"Alternate price is: ${altprice2}")
    
    checkbestprice = False

if altprice > 0 and altprice2 > 0:
    altpricetake = int(input("Do you wish to take this price? Enter 1 for Yes or 2 for No: "))

    if altpricetake == 1:    
        bookingnumber = str(day)+str(int(totalcost))+str(ticketquantitylist[4])
        print(f"Your booking number is {bookingnumber}")
        
        if altprice < altprice2:
            print(f"Your total cost is: ${altprice}")
        else:
            print(f"Your total cost is: ${altprice2}")    
print("Thank you for booking with us!")
