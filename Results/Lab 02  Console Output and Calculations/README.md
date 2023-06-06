
Lab 02 — Console Output and Calculations
========================================





We will use geometrical objects to get used
Write the classes specified below and do thorough testing with BlueJ:






1. Class "Rectangle"
--------------------









Hints


* The constructor has to use the setters
* `**printInfo()**` should print all infos of the rectangle to the **console**.
* the `Constructor` within UML has to be named exactly after the class I(including the uppercase first letter): `Rectangle`
* in UML the declaration ordering is `+/- name : type`, in Java it is `public/private type name`!
* *"circumference"* is the German *"Umfang"*



Example:






```
===== Rectangle: =====
  Length = 5m
  Width = 2m
  Circumference = 14m
  Area = 10m²
======================
```
* Do **not reimplement** the calculations, but simply call the methods where this value is needed.









2. Class "Circle"
-----------------









Hints


* The needed value of `**π**` should be provided by an attribute with `**double**` value `3.14159265`.
* Again please **no calculations within method printInfo()** – call the existing methods instead!









3. Class "Cuboid" (Quader)
--------------------------









Hints


* Formulas for surface area (sum of all enclosing areas) and volume should be known!
* mass = density \* volume
* check the calculated values for correctness !



Typical density values for several materials:  

Water: 1000 kg/m³  

Steel: 7860 kg/m³  

Wood: 400 to 800 kg/m³  

Concrete: 1800 to 2450 kg/m³









4. More Classes (Cylinder, Sphere, …​)
--------------------------------------




If you finished early, you should think about implementing other classes for geometrical objects (cylinder, sphere, cone, …​). Formulas are available online.






5. Further Info
---------------




Links to topics "data types" and "arithmetische operators" in Java:




* <http://de.wikibooks.org/wiki/Java_Standard:_Primitive_Datentypen>
* <http://openbook.rheinwerk-verlag.de/javainsel/javainsel_02_003.html>
* <http://openbook.rheinwerk-verlag.de/javainsel/javainsel_02_004.html>





