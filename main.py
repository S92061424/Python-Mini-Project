Travalvehiles = {
    'Car':
    {
            'Maximum Passengers': 4,
            'minimum passengers': 3,
            'coundition' : ["AC","NON/AC"]

    },

    'Van':
    {
            'Maximum Passengers': 6,
            'minimum passengers': 8,
            'coundition' : ["AC","NON/AC"]
    },

    'Threewheel':
    {
            'Maximum Passengers': 3,
            'minimum passengers': 1,
            'coundition' : "NON/AC"
     }
}

HeavyVehicles = {
    'Truck':
        {
            'size': ['7ft', '12ft']
        },

    'Lorry':
        {
            'Max_Load': "3500kg"
        }
}

def Dashboard():
    print("""
     Type NO 1 to Show Travelling Vehicle List
     Type NO 2 to Show Heavy Vehicles List
     Type NO 3 to Show Add a Travelling Vehicle List 
     Type NO 4 to Show Add a Havy Vehicles List
     Type NO 5 to Show Search Vehicle
     Type NO 6 to Show Book a Vehicle
     Type NO 0 to Show Exit
    """)

def TravelVehi():
    i = 1
    for vehi,Special in Travalvehiles.items():
        print("\t", i, "vehi : ", vehi)
        i += 1
        for Key in Special:
            print("\t", Key + ':', Special[Key])
        print("\n")

def HevyLoadVehi():
    i=1
    for vehi,Special in HeavyVehicles.items():
        print("\t", i, "Vehicle: ", vehi)
        i +=1
        for key in Special:
            print("\t", key + ':', Special[key])
        print("\n")

while True:
    Dashboard()

    #VEhicle List
    try:
        userInput = int(input("Enter your choice: "))
    except ValueError:
        print("!!! Give a valid input !!! ")
    else:

        if userInput != 0:

            if userInput == 1:
                HevyLoadVehi()

            elif userInput == 2:
                HevyLoadVehi()

        #ADD VEHICLE

            elif userInput == 3:
                vehicleName = input("Enter Vehicle name: ")
                Travalvehiles[vehicleName] = {}

                MAX =input("Maximum Passengers")
                Travalvehiles[Travalvehiles]['Maximum Passengers'] = MAX

                MIN = input("Minimum Passengers")
                Travalvehiles[Travalvehiles]['minimum passengers'] = MIN

                condition = input("condition [AC / Non AC]: ")
                Travalvehiles[vehicleName]["condition"] = condition

            elif userInput == 4:
                HeavyVehicles = input("Enter Vehicle name: ")
                Travalvehiles[HeavyVehicles] = {}

                size = input("size of the vehicel: ")
                Travalvehiles[HeavyVehicles]["size"] = size

                Max_Load = input("Maximum Load of the vehicle: ")
                Travalvehiles[HeavyVehicles]["Max_Load"] = Max_Load

                print(HeavyVehicles)

        #Search

        elif userInput == 5:
            tname = input("Chose vehicle")
            hname = tname.lower()
            if tname in Travalvehiles.keys():
                print(tname,Travalvehiles[hname])
            elif tname in HeavyVehicles.keys():
                print(tname,HeavyVehicles[hname])
            else:
                print("Not found")


        #Hire a vehicle
        elif userInput == 6:
                HireVehicle = input("Which vehicle you want to heaire? ")
                SVehicle = HireVehicle.lower()
                if SVehicle in Travalvehiles.keys():
                    del Travalvehiles[SVehicle]
                    print("Vehicle ", HireVehicle, " Ready ")
                elif SVehicle in HeavyVehicles.keys():
                    del HeavyVehicles[SVehicle]
                    print("Vehicle ", HireVehicle, " Ready to Heaire for you")
                else:
                    print(" Vehicle is not avaliable ")

        else:
            print("Program Exit")
            break