
Lab-08 — Auto
=============





Wichtiger Lehrstoff: if, gleichnamige Methoden mit unterschiedlicher Parametertyp-Liste (unterschiedliche Signatur), typecast, Javadoc, Testklasse






1. UML-Klassendiagramm
----------------------




Zu erstellen ist folgenden Klasse:










2. Erläuterungen:
-----------------




Für die Klasse sowie alle Konstruktoren und Methoden sind Javadoc-Kommentare zu erstellen.  

Details siehe [Klasse mit Javadoc-Kommentaren](../theorie/a200_javadoc.html#id_bsp-kl-mit-javadoc), einfaches Beispiel siehe [ganz unten](#id_minibsp-javadoc).





Hinweis

In BlueJ kann, wenn Klasse frei von Sysntaxfehlern, rechts oben von **Quelltext** auf **Dokumentation** umgeschaltet werden.






### 2.1. Attribute



* **normverbrauch** …​ Verbrauch in Liter pro 100 km, z.B.: 4,9 [l / 100km]
* **tankinhalt** …​ aktueller Tankinhalt, kann natürlich niemals kleiner als 0 oder größer als die Tankgröße sein.
* **tankgroesse** …​ maximaler Tankinhalt (in Litern), soll bei der Instanziierung (dem
* Erzeugen eines Objektes) einmalig gesetzt und **später nicht mehr verändert** werden können.
* **kilometerstand** …​ aktueller Kilometerstand des Autos (kann nur erhöht werden)
* **kennzeichen** …​ eine Referenz auf ein String-Objekt mit mindestens 6 Zeichen oder eine Nullreferenz, wenn das Fahrzeug nicht angemeldet ist.




Tipp:Sieh Dir in der Java-API-Documantation die Methoden der String-Klasse an
length(), empty(), indexOf(String str), ev. contains(…​)





### 2.2. Methoden und Konstruktoren:



Übergabewerte sollen überprüft werden (Konstruktoren mit set-Methoden).
Falls notwendig: Fehlermeldungen auszugeben und Werte NICHT verändern (Voraussetzung: sinnvolle **Standardwerte bei Attribut-Deklaration**).




* Konstrukor **Auto()** …​
Parameterloser Standardkonstruktor. Da keine Werte für die Instanzvariablen zur Verfügung stehen, sind sinnvolle Anfangswerte zu wählen.
Z.B.:
`normverbrauch = 4.9`
`tankinhalt = 33.5`
`tankgroesse = 50`
`kilometerstand = 40000`
`kennzeichen = null`
* Konstruktor **Auto(normverbrauch : float, tankinhalt : float, …​ , kennzeichen : String)** …​  

Setzt die Instanzvariablen auf die angegebenen Werte.
Achtung: dabei sind natürlich Überprüfungen / Korrekturen durchzuführen
(diese sollten an entsprechenden set-Methoden delegiert werden).
* **tanken( ) : float** …​
Füllt den Tank randvoll und gibt die getankte Treibstoffmenge zurück.
* **tanken(preis : float, liter : float) : float** …​
Füllt die angegebene Treibstoffmenge in den Tank (zum angegebenen Literpreis) und gibt den zu bezahlenden Gesamtbetrag zurück.
Achtung: Tankgröße berücksichtigen!
* **tanken(preis : float, betrag : int) : float**
Tankt für einen bestimmten, angegebenen Geldbetrag (z.B.: 20 Euro).
D.h. hier ist die dafür erhältlich Treibstoffmenge zu berechnen und natürlich auch wieder die Tankgröße zu berücksichtigen.
Rückgabewert ist die tatsächlich getankte Treibstoffmenge in Litern.
Zusatzfrage: Was passiert, wenn der Typ des Betrages von int auf float geändert wird?
Warum?
* **getKilometerstand( ) : int** …​
Gibt den aktuellen Kilometerstand zurück.
* getTankinhalt( ) : float
Gibt den aktuellen Tankinhalt in Litern zurück.
* **getRestreichweite( ) : float** …​
Berechnet die Restreichweite (basierend auf dem Normverbrauch und dem aktuellen
Tankinhalt) und gibt diesen Wert zurück.
* **fahren( ) : int** …​
Fährt soweit, als es der aktuelle Tankinhalt zulässt. Dabei wird natürlich der Kilometerstand
entsprechend erhöht. Rückgabewert ist die tatsächlich zurückgelegte Strecke.
* **fahren(strecke : int) : int** …​
Fährt die angegebene Strecke. Dabei erhöht sich der Kilometerstand und reduziert sich der Tankinhalt entsprechend.
Achtung: wird eine zu große Strecke eingegeben, dann kann natürlich nicht wirklich soweit gefahren werden.
Rückgabewert soll auch hier die tatsächlich zurückgelegte Strecke sein!
* **printInfo( )**
Gibt die Informationen zu diesem Fahrzeug auf der Konsole aus. Zum Beispiel:  

`Normverbrauch: 4.9 l/100km`  

`aktueller Tankinhalt: 33.5 l / Tankgröße: 50 l`  

`Kilometerstand: 40000 km`  

`Kennzeichen: “W 1234 TX“ - als Taxi angemeldet`



Zum Kennzeichen:





	+ gibt es kein Kennzeichen, dann lautet die letzte Zeile der Ausgabe:
	`**Kennzeichen: Auto nicht angemeldet**`
	+ für normale Kennzeichen wird einfach nur das Kennzeichen ausgegeben, z.B.:
	`**Kennzeichen: “TU 423 AL“**`
	+ bei Taxis endet das Kennzeichen mit „TX“, hier soll z.B.:
	`**Kennzeichen: “W 1234 TX“ - als Taxi angemeldet**`
	ausgegeben werden







3. Testklasse
-------------




Implementiere eine Testklasse `**TestenAuto**`, die die mindestens die folgenden 4 Methoden enthält:




* `**testAutoNiceCases()**` …​
* `**testAutoBadCases()**`
* `**testAuto()**`




Weitere Hinweise zum Testen siehe [Testen, 'this', Kommentare](../theorie/a175_testen+this+kommentar.html).






4. Beispielklasse mit Javadoc
-----------------------------






```
/**
 * Einfache Kreis-Klasse.
 *
 * @author Max Renkin <renkin@spengergasse.at>
 * @version 2022-11-28
 */
public class Kreis
{
    // Javadoc privater Elemente normalerweise nicht angezeigt
    private double radius = 1.0;  // Einheitskreis

    /**
     * Konstruktor fuer Objekte der Klasse Kreis.
     * @param radius siehe {@link #setRadius(double)}
     */
    public Kreis(double radius) {
        setRadius(radius);
    }

    /**
     * Setter f&uuml;r den Radius.
     * @param radius der Radius in cm
     */
    public void setRadius(double radius) {
        if (radius <= 0) {
            System.out.println("Radius muss positiv sein, gegeben war aber: "
                    + radius + " -> bleibt auf " + this.radius);
        } else {
            this.radius = radius;
        }
    }

    // Selbsterklaerend - kein Javadoc-Kommentar nötig
    public double getRadius() {
        return radius;
    }

    /**
     * Berechnet den Kreisumfang.
     * @return den Kreisumfang in cm
     */
    public double calcUmfang() {
        return 2*radius*Math.PI;
    }

    /**
     * Berechnet die Kreisflaeche.
     * @return die Kreisflaeche in cm²
     */
    public double calcFlaeche() {
        return radius*radius*Math.PI;
    }

    /**
     * Bildschirmausgabe der Eckdaten. <br>
     * Beispiel:
     * <pre>=== Kreis mit Radius 3.0cm: ===
     *  Umfang: 18.84955592153876cm
     *  Flaeche: 28.274333882308138cm²
     * </pre>
     */
    public void printInfo() {
        System.out.println("=== Kreis mit Radius " + this.radius + "cm: ===");
        System.out.println("  Umfang: " + calcUmfang() + "cm");
        System.out.println("  Flaeche: " + calcFlaeche() + "cm²");
        System.out.println();  // Leerzeile
    }
}
```





