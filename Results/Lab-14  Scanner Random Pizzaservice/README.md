
Lab-14 — Scanner, Random: Pizzaservice
======================================



1. Überblick
------------




Es soll ein Pizza-Bestell-Formular mithilfe der 3 unten beschriebenen Klassen simuliert werden.




Die Klasse `PizzaBestellung` ist für ALLE interaktiven Eingaben zuständig. Klasse `Pizza` für das konkrete Setzen und Prüfen der Daten einer einzelnen Pizza.




Klasse `Util` stellt neben den Ausgabe-Funktionen auch noch eine Formatierung von Cent-Beträgen als `€ 123,99` bereit (allgemeine Basisfuntionalität - kann in weiteren Projekten genutzt werden).




Eine Bestellung hat Platz für bis zu 3 Pizzen. Es gibt 3 vorgegebene Pizza-Arten.
Jede Pizza kann individuell (freie Text-Eingabe) mit bis zu 6 Zutaten aufgewertet werden.




Es werden erstmals intensiv Konstante benutzt – siehe [Konstante](../theorie/a270_pkg+konst+random+scanner.html#id_konstante).










2. Klasse "Pizza"
-----------------




Hier erfolgt **KEINE** interaktive Eingabe. Die gesamte **Benutzer-Interaktion** erfolgt in Klasse `**PizzaBestellung**`. Dort Programmstart mit Methode `**runBestellung()**`.




Es gibt 3 gültige Pizza-Arten, deren Name in den obigen Konstanten festgelegt ist.




Die Zutaten sind als Text gespeichert, mit Beistrich getrennt (daher kein Beistrich innerhalb einer Zutat erlaubt - Prüfen mit `txt.contains(…​)`).




Die ZutatenListe kann maximal 6 Zutaten enthalten, sieht z.B. so aus: `Salat,Artischocke,Tomate,Ei`




* `**Konstruktor(name)**` …​ prüft mit Methode `validPizzaName(name)`. Wenn alles ok, wird Name gesetzt, ansonsten bleibt er `null` mit Fehlermeldung:  

`FEHLER in Konstruktor: 'this.name' bleibt null`
* Methode `**pizzaOk()**` …​ prüft, ob Pizza-Name null – d.h. der übergebene Name im Konstruktor wurde nicht akzeptiert (von Methode `validPizzaName(..)`).  

Wird in diesm Beispiel eigentlich nicht benötigt, da die Pizza-Namen vom Menü automatisch vergeben werden (nicht vom Benutzer einzugeben).
* Methode `**anzahlZutaten()**` …​ prüft, ob String-Länge 0 (0 Zutaten), sonst wird die Anzahl der Beistriche gezählt (und 1 addiert): Schleife mit `txt.charAt(i)`
* Statische Methode `**validPizzaName(name)**` …​ prüft gegen die 3 als Konstate festgelegten erlaubten Namen. Mögliche Fehlermeldungen:




	+ `FEHLER in validatePizzaName() - übergebener Name null`
	+ `FEHLER in validatePizzaName() - ungültig: '{?name?}'`
* Methode `**addZutat(…​)**` …​ hat 3 mögliche Rückgabewerte (Typ `char`):




	+ 'f' …​ Fehler (Info: Eingabe wird ignoriert):
	
	
	
	
		- Pizza-Name null
		- Zutat null
		- Zutat leer (mit `txt.isBlank()`)
		- Zutat enthält `','` (ist Trennzeichen, für Zählen der Zutaten nötig)
	+ '#' …​ fertig (Info: Zutateneingabe wurde beendet):
	
	
	
	
		- wegen User-Ende per Eingabe von '#'
		- weil schon 6 Zutaten
	+ '>' …​ ok (Info: Zutat wurde regulär hinzugefügt)
* Methode `**calcPreis()**` hat Fixpreise:




	+ Margaritha: 599 Cent
	+ Salami: 699 Cent
	+ Tonno: 799 Cent


Jede Zutat erhöht den Preis um 60 Cent  

Guter Lösungsansatz: Switch-Statement!
* Methode `**printPizza()**` liefert ca. folgendes Ergebnis :





```
Pizza 'Salami' mit 3 Zutaten:
    Salat,Ei,Gurke    Endpreis: € 8,79
```




oder bei 0 Zutaten:






```
Pizza 'Salami' mit 0 Zutaten:
        Endpreis: € 6,99
```






3. Klasse PizzaBestellung
-------------------------




Das Programm wird mit Methode '**runBestellung()**' gestartet.




In dieser Klasse ist das Bestell-Menü implementiert.
Es wird folgendes (nach jeder Pizza-Eingabe neuerlich) angezeigt:






```
+----- Menü ------------------------------+
|  (noch 3 Pizzen hinzufügbar)            |
| m ... Pizza 'Margaritha'                |
| s ... Pizza 'Salami'                    |
| t ... Pizza 'Tonno'                     |
| a ... Bestellung aufgeben               |
| q ... ENDE (quit)                       |
|  --> Auswahlzeichen (hinterher [RETURN]):
```




Nach Eingeben eines der am linken Rand angezeigten Buchstaben (m, s, t, a, q) folgt die Anzeige:






```
| a ... ...                               |
| q ... ENDE (quit)                       |
|  --> Auswahlzeichen (hinterher [RETURN]): t
Pizza 'Tonno' belegen:
  noch 6 Zutaten möglich (FERTIG mit '#'):
```




Danach lassen sich Schritt für Schritt bis zu 6 Zutaten (z.B. 'Eier' oder 'Oliven'), jeweils bestätigt mit [EINGABE] eingeben (Zeichen ',' verboten). Schließlich ergibt sich nach Abschließen mit `'#'+[EINGABE]` folgendes Bild (die rechts außerhalb der Menü-Grenze stehenden Texte sind die Benutzer-Eingaben …​ 't', 'Oliven', 'Eier', '#'):






```
+----- Menü ------------------------------+
|  (noch 3 Pizzen hinzufügbar)            |
| m ... Pizza 'Margaritha'                |
| s ... Pizza 'Salami'                    |
| t ... Pizza 'Tonno'                     |
| a ... Bestellung aufgeben               |
| q ... ENDE (quit)                       |
|  --> Auswahlzeichen (hinterher [RETURN]): t
Pizza 'Tonno' belegen:
  noch 6 Zutaten möglich (FERTIG mit '#'): Oliven
    bisher belegt mit: Oliven
  noch 5 Zutaten möglich (FERTIG mit '#'): Eier
    bisher belegt mit: Oliven,Eier
  noch 4 Zutaten möglich (FERTIG mit '#'): #
---------------------------------
Pizza 'Tonno' mit 2 Zutaten:
    Oliven,Eier    Endpreis: € 9,19

+----- Menü ------------------------------+
|  (noch 2 Pizzen hinzufügbar)            |
| m ... Pizza 'Margaritha'                |
| s ... Pizza 'Salami'                    |
| t ... Pizza 'Tonno'                     |
| a ... Bestellung aufgeben               |
| q ... ENDE (quit)                       |
|  --> Auswahlzeichen (hinterher [RETURN]):
```




Bis zu 3 Pizzen lassen sich so in einer Bestellung unterbringen. Zum Finalisieren der Bestellung muss nun `'a'+[EINGABE]` eingegeben werden (zum Abbruch `'q'+[EINGABE]`).




Nun wird bei Abbruch eine End-Meldung des ungefähren Inhalts ausgegeben:






```
Programm wird beendet ...
Keine (gültige) Bestellung vorhanden - auf Wiedersehen"
```




oder bei gültiger Bestellung (noch eine 'Margaritha' ohne Zutaten danach):






```
+----- Menü ------------------------------+
|  (noch 1 Pizzen hinzufügbar)            |
| m ... Pizza 'Margaritha'                |
| s ... Pizza 'Salami'                    |
| t ... Pizza 'Tonno'                     |
| a ... Bestellung aufgeben               |
| q ... ENDE (quit)                       |
|  --> Auswahlzeichen (hinterher [RETURN]): a
==== Pizzabestellung ====
Anzahl: 2
---------------------------------
Pizza 'Tonno' mit 2 Zutaten:
    Oliven,Eier    Endpreis: € 9,19
---------------------------------
Pizza 'Margaritha' mit 0 Zutaten:
        Endpreis: € 5,99
---------------------------------
Gesamtpreis: € 15,18    Abholcode: 'VSP'
```




* Methode `**anzPizzen()**` …​ zählt die besetzten der "Plätze" `pizza1`, `pizza2`, `pizza3` und liefert den Wert zurück.
* Methode `**runBestellung()**` …​ ist ähnlich zu Methode aus Unterlagen: [Text-Menus zur interaktiven Programm-Steuerung](../theorie/a270_pkg+konst+random+scanner.html#id_text-menu).



Wenn durch Eingabe von `'m'`, `'s'` oder `'t'` eine neue Pizza hnzugefügt wurde,
wird zuerst `neuePizza` erzeugt, danach `vorbereiten(neuePizza)` wird aufgerufen, bei Erfolg (Rückgabewert `true`) wird `belegen(neuePizza)` und danach `neuePizza.printPizza())` ausgeführt.  

Wenn `anzPizzen()` den in `MAX_PIZZEN` festgelegten Wert liefert, wird die Bestellung automatisch abgeschlossen, sonst muss der Benutzer dies durch Eingabe von `'a'+[EINGABE]` händisch tun.
Den Abschluss bildet ein Aufruf von `printBestellung()`
* Methode `**vorbereiten(..)**` …​ versucht die übergebene Pizza zu platzieren. Prüft, ob `!= null`, sucht ersten freien Platz in `pizza1`…​`pizza3`, liefert `true` bei Erfolg, sonst `false`..
* Methode `**belegen(..)**` …​ erledigt die interaktive Belegung, nutzt Methode `pizza.addZutat(..)` und ihre Rückgabewerte, liefert die Anzahl der erfassten Zutaten zurück. Zu Beginn Ausgabe von: `Pizza '{?name?}' belegen:`
* Methode `**erzeugenAbholCode()**` …​ produziert mit `Random` einen 3-Stelligen Zufallstext mit US-Großbuchstaben (26^3 = 17576 Möglichkeiten). Details siehe [Nutzen von Zufallszahlen zum Generieren zufälliger Texte](../theorie/a270_pkg+konst+random+scanner.html#id_random-text))
* Methode `**printBestellung()**` …​ Ausgabe siehe Erläuterungen und Ausgabebeispiele oben.






4. Klasse Util
--------------




Siehe [Assoziationen - Util-Klasse](../theorie/a180_assoziationen.html#id_util-klasse)




Zusätzlich: Methode `formattedEuroFromCent(cent; int): String` …​ diese liefert für Parameterwert `199` des String `"€ 1,99"`.




Umrechnen von Cent nach Euro: `int euro = cent/100`, `int restCent = cent%100`





