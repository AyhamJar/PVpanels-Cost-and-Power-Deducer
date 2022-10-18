# PVpanels-Cost-and-Power-Deducer
A python code where the user enters the Solar Panels specifications required for an area, and it will calculate the expected outcome of Cost and Power generated.<br> <br>

Run the file `PVcalculate.py` <br>
-----

The function defined `CalculateFromArea()` is called to deduce the **estimated cost** and **power generated** based on the following parameters the user chooses: <br>

- The type of solar panel <br>
- The area available to install PV panels on <br>
- The tilt angle of the panels <br>
- The azimuth angle based on the location <br>
- Length and width of the solar panels  <br>

The user would see the following: <br>

> Input the type of solar panel:   <br> 
> [Mono] for Monocrystalline PV type. <br>
> [Poly] for Polycrystalline PV type. <br>
> [Thin] for Thin Film PV type.       <br>
> ---> **thin** <br>
> Input the length of solar panel in meters: **4** <br>
> Input the width of solar panel in meters: **2** <br>
> Input the area length available in meters: **34** <br>
> Input the area width available in meters: **45** <br>
> Input the tilt angle of the solar panels: **20** <br>
> Input the azimuth angle of your location: **45** <br> 




### Output
------------
- The units expected for area is **m** and unit **degrees** for the angles. <br>
- Power generated is in **Watt hour (Wh)** <br>
- Cost estimated is in **US dollar ($)** <br> 

The output would look like this: <br>

> Total costs of your solar panels for Thin Film is: **$49500.0** <br>

> Number of panels you can have with zero shading effect is: **132** <br>

> Total power generated is: **33000 Wh**
