import math


def CalculateFromArea():
    PanelTypes = [input("Input the type of solar panel:\n[Mono] for Monocrystalline PV type.\n[Poly] for Polycrystalline PV type.\n[Thin] for Thin Film PV type.\n---> ")]
    lengthPanel = float(input("Input the length of solar panel in meters: "))
    widthPanel = float(input("Input the width of solar panel in meters: "))
    Arealength = float(input("Input the area length available in meters: "))
    Areawidth = float(input("Input the area width available in meters: "))
    tilt = float(input("Input the tilt angle of the solar panels: "))
    azimuth = float(input("Input the azimuth angle of your location: "))
    PVtype = [word.lower() for word in PanelTypes]
    for x in PVtype:
        if x == "monocrystalline" or x == "mono":
            type = "Monocrystalline"
            Wattpower = 400
            Wattprice = 1.50
            RowDistance = lengthPanel * math.cos((math.radians(tilt))) + (lengthPanel * (math.sin((math.radians(tilt))) / math.tan((math.radians(azimuth)))))
            PanelsBehind = math.floor(Arealength / RowDistance)
            PanelsNext = math.floor(Areawidth / widthPanel)
            TotalPanels = PanelsBehind * PanelsNext
            CostPanels = TotalPanels * Wattpower * Wattprice
            PowerGenerated = TotalPanels * Wattpower

            print("\nTotal costs of your solar panels for " + type + " is: $" + str(CostPanels) + "\n")
            print("Number of panels you can have with zero shading effect is: " + str(TotalPanels) + "\n")
            print("Total power generated is: " + str(PowerGenerated) + " Wh\n")


        elif x == "polycrstalline" or x == "poly":
              type = "Polycrstalline"
              Wattpower = 300
              Wattprice = 1
              RowDistance = lengthPanel * math.cos((math.radians(tilt))) + (lengthPanel * (math.sin((math.radians(tilt))) / math.tan((math.radians(azimuth)))))
              PanelsBehind = math.floor(Arealength / RowDistance)
              PanelsNext = math.floor(Areawidth / widthPanel)
              TotalPanels = PanelsBehind * PanelsNext
              CostPanels = TotalPanels * Wattpower * Wattprice
              PowerGenerated = TotalPanels * Wattpower

              print("\nTotal costs of your solar panels for " + type + " is: $" + str(CostPanels) + "\n")
              print("Number of panels you can have with zero shading effect is: " + str(TotalPanels) + "\n")
              print("Total power generated is: " + str(PowerGenerated) + " Wh\n")


        elif x == "thin film" or x == "thin":
              type = "Thin Film"
              Wattpower = 250
              Wattprice = 1.5
              RowDistance = lengthPanel * math.cos((math.radians(tilt))) + (lengthPanel * (math.sin((math.radians(tilt))) / math.tan((math.radians(azimuth)))))
              PanelsBehind = math.floor(Arealength / RowDistance)
              PanelsNext = math.floor(Areawidth / widthPanel)
              TotalPanels = PanelsBehind * PanelsNext
              CostPanels = TotalPanels * Wattpower * Wattprice
              PowerGenerated = TotalPanels * Wattpower

              print("\nTotal costs of your solar panels for " + type + " is: $" + str(CostPanels) + "\n")
              print("Number of panels you can have with zero shading effect is: " + str(TotalPanels) + "\n")
              print("Total power generated is: " + str(PowerGenerated) + " Wh\n")

        else:
            print("\nYou have written the solar panel type incorrectly")


CalculateFromArea()



