import os.path

def timeAdder(time,add):
    #adds a number of minuets to a time, input data must be in the form hh:mm, output will be in the form hh:mm. Can only corectly add 1 hour, eg. can add 75 minuets to 09:20 correctly (10:35), but not 105 minuets as this goes over 1 hour (11:05) more, so from 09:00 any time upto 10:59 can be done only.
    result=""
    if int(time[-2:])+add>59:#check if 1 needs to be added to the hour (14:45+20=15:05...)
        result=str(int(time[:2])+1)
        result=result+":"
        if int(time[-2:])+add-60<10:
            result=result+"0"
        result=result+str(int(time[-2:])+add-60)
    else:
        result=time[:2]
        result=result+":"
        result=result+str(int(time[-2:])+add)
    return result


true=1
false=0
stationNameList=[]
stationTimeList=[]
while true:
    stationToCheck=input("Station name")
    stationToCheck=stationToCheck.replace(" ","")
    if stationToCheck=="end":
        break
    elif os.path.isfile(stationToCheck+"Times.csv")==True:
        confirm=input("Station found, continue? (y/n)")
        if confirm=="y":
            print(stationToCheck)
            stationNameList.append(stationToCheck)
    else:
        confirm=input("Station not found, create? (y/n)")
        if confirm=="y":
            print(stationToCheck)
            stationNameList.append(stationToCheck)
            file = open(stationToCheck+'Times.csv', 'w')
            file.write('1,Destination,Route,Towards,Notes,'+stationToCheck+'\n')
            file.close()

print(stationNameList)

for i in range (len(stationNameList)):
    time=""
    while time.isdigit()==False:
        time=input("Enter the travel line (minuets) from the routes start to "+stationNameList[i])
        if (time.isdigit()==True):
            stationTimeList.append(int(time))
        else:
            print("Please enter an integer")

direction=0
while direction!="t" and direction != "f":
    direction=input("Does this service from to or from Klosters Platz? (t/f)")
    if direction=="t":
        direction="To"
        break
    elif direction=="f":
        direction="From"
        break

destination=input("Destination - this is shown to the user as the route, use a : to seperate sections (app will switch between sections). Anything can be written here")

towords=""
towordsList=[]
while true:
    towords=input("Towords - this is not shown to the user and is used by the filter and route finder, what major stops are served by this route.")
    if towords=="end" and len(towordsList)!=0:
        break
    elif towords=="Klosters Platz - Station":
        towordsList.append("Klosters Platz - Station")
    elif towords=="Serneus":
        towordsList.append("Serneus")
    elif towords=="Kublis":
        towordsList.append("Kublis")
    elif towords=="Monobiel Parkplatz":
        towordsList.append("Monobiel Parkplatz")
    elif towords=="Oberselfranga":
        towordsList.append("Oberselfranga")
    elif towords=="Russna":
        towordsList.append("Russna")
    elif towords=="Sportzentrum (for skilift Selfranga)":
        towordsList.append("Sportzentrum (for skilift Selfranga)")
    elif towords=="Aeuja Post":
        towordsList.append("Aeuja Post")
    elif towords=="Nutlihuschi":
        towordsList.append("Nutlihuschi")
    elif towords=="Dorf":
        towordsList.append("Dorf")
    elif towords=="Bad":
        towordsList.append("Bad")
    else:
        print("Erorr, stop not found")
    print(towordsList)

number=""
while number.isdigit()==False:
    number=input("Enter route number")
    if number.isdigit()==True:
        break

notes=""
while notes=="":
    notes=input("Any notes on this service? (Enter No if there arnt)")

time=""
while time!="end":
    time=input("Enter a departure time from "+stationNameList[0])
    if time == "end":
        break
    elif time == "change":
        while true:
            changeitem=input("Enter item to change")
            if changeitem=="end":
                break
            elif changeitem=="destination":
                print("Current value, ",destination)
                destination=input("Destination - this is shown to the user as the route, use a : to seperate sections (app will switch between sections). Anything can be written here")
            elif changeitem=="towords":
                print(towordsList)
                towords=""
                towordsList=[]
                while true:
                    towords=input("Towords - this is not shown to the user and is used by the filter and route finder, what major stops are served by this route.")
                    if towords=="end" and len(towordsList)!=0:
                        break
                    elif towords=="Klosters Platz - Station":
                        towordsList.append("Klosters Platz - Station")
                    elif towords=="Serneus":
                        towordsList.append("Serneus")
                    elif towords=="Kublis":
                        towordsList.append("Kublis")
                    elif towords=="Monobiel Parkplatz":
                        towordsList.append("Monobiel Parkplatz")
                    elif towords=="Oberselfranga":
                        towordsList.append("Oberselfranga")
                    elif towords=="Russna":
                        towordsList.append("Russna")
                    elif towords=="Sportzentrum (for skilift Selfranga)":
                        towordsList.append("Sportzentrum (for skilift Selfranga)")
                    elif towords=="Aeuja Post":
                        towordsList.append("Aeuja Post")
                    elif towords=="Nutlihuschi":
                        towordsList.append("Nutlihuschi")
                    elif towords=="Dorf":
                        towordsList.append("Dorf")
                    elif towords=="Bad":
                        towordsList.append("Bad")
                    else:
                        print("Erorr, stop not found")
                    print(towordsList)
            elif changeitem=="notes":
                print("Current value, ",notes)
                notes=""
                while notes=="":
                    notes=input("Any notes on this service? (Enter No if there arnt)")
            else:
                print("It is currently only possible to change destination and towords, enter end to leave this section")

    else:
        print(time)
        for i in range (len(stationNameList)):
            file = open(stationNameList[i]+'Times.csv', 'a')
            file.write(direction+','+destination+','+number+',')
            if len(towordsList)==1:
                file.write(str(towordsList[0]))
            else:
                for j in range (len(towordsList)-1):
                    file.write(str(towordsList[j])+':')
                file.write(str(towordsList[len(towordsList)-1]))
            file.write(','+notes+','+timeAdder(time,stationTimeList[i])+'\n')
            file.close()