
Lab-09 — Assoziationen: Waggon und Zug
======================================



1. Util
-------




Wie in der "Theorie" besprochen (siehe [Assoziationen  —  Beziehungen zwischen Klassen](../theorie/a180_assoziationen.html)) verwenden wir eine Klasse Util, die (vorerst) die Methoden System.out.println(…​) und "Verwandte" in Methoden mit sehr kurzem Namen "einpackt" – siehe [theorie/a180\_assoziationen.adoc#id\_util-klasse](../theorie/a180_assoziationen.html#id_util-klasse). Der dortige Source-Code kann kopiert werden, die Verwendung wird darunter gezeigt.
Statt Verwendung von `System.out.pri..(..)` wird `u.prn(…​)` etc. genutzt.










2. Waggon
---------




Zu erstellen ist eine Klasse `**Waggon**` (ein **Personenwaggon**) mit folgenden Eigenschaften:








***Vorgaben:***




* **maximum**: maximale Anzahl von Sitzplätzen dieses Waggons (es gilt: `100 <= maximum <= 200`)
* **belegt**: Anzahl von aktuell belegten Sitzplätzen (es gilt: `0 <= belegt <= maximum`)
* **klasse**: kann nur die Werte `'1'` oder `'2'` annehmen (entspricht der 1. oder 2. Klasse)
* **Konstruktor**(…​): Erzeugt einen `Waggon`, wobei `belegt = 0` ist und `maximum` nur auf einen Wert zwischen `100` und `200` gesetzt werden darf. Bei einem ungültigen Wert für `maximum` soll `100` als Default-Wert verwendet werden. Klasse darf nur `'1'` oder `'2'` sein, Default-Wert hier: `'2'`
* **einsteigen**(…​): Läßt eine bestimmte Anzahl von Personen einsteigen (Parameter: `anzahl`).
 Rückgabewert der Methode ist die Anzahl von Personen die NICHT Platz gefunden haben.
 Finden alle Personen Platz, oder wurde eine ungültige (negative) Anzahl von Personen angegeben dann ist der Rückgabewert der Methode `0`.  

Bsp.: `maximum = 150`, `belegt = 100` und es sollen `60` Personen einsteigen.
Da nur `50` Personen Platz finden, ist der Rückgabewert in diesem Fall `10`.
* **aussteigen**(…​): Läßt eine bestimmte Anzahl von Personen aussteigen. Das Attribut `belegt` soll natürlich nur verändert werden, wenn ein positiver Wert übergeben wurde und es ist sicherzustellen, daß `belegt` niemals negativ wird (z.B.: weil mehr Personen aussteigen sollen, als vorhanden sind!)
Rückgabewert ist die Anzahl der tatsächlich aussteigenden Personen.
Bsp.: `maximum = 150`, `belegt = 30` und es sollen `40` Personen aussteigen.
Da nur `30` Personen vorhanden sind, ist der Rückgabewert in diesem Fall `30`.
* **Die get-Methoden** bedürfen keiner weiteren Erklärung
* **set-Methoden** bitte selbst überlegen.






3. Zug
------




Klasse, die einen Personenzug mit maximal 3 Waggons darstellt.








***Vorgaben:***




* **waggon1 bis waggon3:** unser Zug kann aus bis zu 3 Waggons bestehen, die über diese Referenzvariablen angesprochen werden.
Eine Lokomotive wird hier nicht eigens behandelt.
* **Konstruktor:**
Es kann ein gültiges Objekt vom Typ `Waggon` übergeben werden, das dann als erster Waggon hinzugefügt wird.  

Sollte eine Nullreferenz (`null`) übergeben werden, dann ist ein "Default-Waggon" zu erzeugen ( `…​ new Waggon(…​)` ) und einzufügen, der folgende Eigenschaften hat:




	+ maximale Anzahl der Sitzplätze: 100
	+ keine Plätze belegt
	+ 2. Klasse.
* **waggonHinzufuegen(…​):**
Der als Parameter übergebene Waggon wird hinzugefügt, sofern noch ein Attribut dafür frei ist.
Rückgabewert: true bei erfolgreichem Hinzufügen, andernfalls false (bei Übergabe von null oder wenn kein Platz mehr frei ist)
* **getAnzahlFreieSitzplaetze(…​):**
Rückgabewert: wenn Parameter klasse = 0 …​ die Anzahl aller freien Sitzplätze in allen Waggons,  

wenn Parameter klasse = '1' …​ die Anzahl aller freien Sitzplätze in 1. Klasse Waggons  

wenn Parameter klasse = '2' …​ die Anzahl aller freien Sitzplätze in 2. Klasse Waggons
* **verteilen(…​):**
Diese Methode geht Waggon für Waggon durch (beginnend beim Ersten) und befüllt sozusagen die
Sitzplätze.  

Wenn nicht alle Personen im 1. Waggon Platz finden, dann geht es weiter zum 2., …​  

Wenn am Ende nicht alle Personen einen Platz gefunden haben, dann fahren sie nicht mit.
Der Rückgabewert liefert also die Anzahl der Personen, die NICHT Platz hatten.  

**Achtung:** die Waggons haben Waggons entweder 1. oder 2. Klasse. Die Personen dürfen nur jenen Waggons zugeteilt werden,
deren Klasse mit der hier Übergebenen (Parameter klasse) übereinstimmt!




***Bitte unbedingt beachten:***




* Namenskonventionen (Groß- und Kleinschreibung)
* vorgegebenen Methoden- und Attributnamen beibehalten
* Fehlerfälle (ungültige Werte bei Parametern) wirklich testen






4. Testklasse
-------------




Erstelle eine Testklasse, in der beide obigen Klassen getestet werden. Dabei ist jede Methode im Normalfall mindestens 2 mal aufzurufen - einmal mit einem regulären Parameter, einmal (falls existent) mit einem ungültigen Parameter. Ziel ist es, das Verhalten der Methoden in möglichst allen "wichtigen" Situationen zu überprüfen.




Vor jedem Test ist ein aussagekräftiger Titel, die verwendeten Parameter und das erwartete Ergbenis auszugeben, danach das Ergbenis des Aufrufes: entweder die Fehlermeldung oder der Rückgabewert mit System.out.print…​ (oder `u.prn`).




Es gibt mindestens 4 Methoden: `testNiceCasesWaggon()`, `testBadCasesWaggon()`, `testNiceCasesZug()`, `testBadCasesZug()`






5. Javadoc
----------




Für folgende Klassen/Methoden/Konstruktoren ist ein Javadoc-Kommentar zu verfassen (siehe Theorie: Javadoc):




* beide Klassen
* beide Konstruktoren
* einsteigen
* aussteigen
* waggonHinzufuegen
* verteilen






6. UML-Gesamt-Diagramm
----------------------









