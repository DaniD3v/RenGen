
Aufgabe zu Arrays, Sortieren, String-Methoden: Bibliothek
=========================================================





Es sollen lückenlose Arrays mit `freeIdx` zur Verwaltung in `Verlag` und in `Bibliothek` verwendet werden.










1. Klasse Buch
--------------




***Standard-Elemente***




* **Konstruktor** …​ selbsterklärend (Setter verwenden!)
* **Setters und Getters** …​ in den Settern ist Text (Titel, Autor) auf null und `isBlank()` zu prüfen, `publJahr` muss zw. `1600` und `2021` liegen, Verlag ist auf `**null**` zu prüfen.



Bei ungültigem Wert soll sinngemäß folgende Fehlermeldung ausgegeben werden:  

**"FEHLER in setPublJahr - publJahr = %d - bleibt auf %d"** (das erste `%d` ist durch den fehlerhaften Übergabe-Parameter zu ersetzen, das zweite `%d` durch den bestehenden Wert der Instanzvariablen).




Das kann entweder wie gewohnt oder eleganter mit  

`System.out.format("FEHLER in setPublJahr - publJahr = %d - bleibt auf %d", publJahr, this.publJahr);`  

erfolgen (Bei Strings wird statt `%d` ein `%s` verwendet, Zeilenschaltung erfolgt durch `%n`, standardmäßig wird keine Zeilenschaltung angefügt).
* **toString(): String** …​ siehe Beispiel-Code
* **equals(other Buch)** …​ vereinfachtes equals (für PLÜ ausreichend, hier darf aber NICHT `@Override` darübergeschrieben werden!)
* **compareTo(other: Buch): int** …​ wird zum Sortieren von Bücher-Listen aufgerufen (siehe Beispiel-Implementation von `**Verlag**` – Hilfsmethode `**findMinValPos(..)**` und damit indirekt von `**selectionSort(..)**`).






2. Klasse Verlag
----------------




Wird im vorliegenden Beispiel hauptsächlich als Attribut von Buch verwendet. Zusätzlich verwaltet der Verlag eine Liste von ihm veröffentlichter Bücher und stellt sicher, dass jede Buch-Instanz nur einmal enthalten ist (beim erstmaligen Auftreten eines Buches wird es in die Bücherliste aufgenommen). Viele Methoden, die auch in Bibliothek implementiert werden sollen, sind hier zu finden.




***Standard-Elemente***




* **Konstruktor(name: String, kapazitaet: int)** …​ Name darf nicht null oder "blank" (siehe `Buch`) sein.
* **Konstruktor(name: String)** …​ verwendet Kapazität 10
* **Getter für Name** …​ *Setter hier nicht zwingend nötig*, da nachträgliche Änderung nicht vorgesehen. Prüfung kann direkt im Konstruktor erfolgen.
* **toString()** …​ wird automatisch aufgerufen, wenn Klasse aufgerufen wird, wo Text erwartet wird
* **equals(other: Verlag)** …​ hier wird nur der Name herangezogen.
* **compareTo(other: Verlag)** …​ es wird nur der Name herangezogen. Tückgabe 0 bei Gleichheit,
 negativer Wert wenn this.name kleiner, + 1 wenn größer  

Rückgabe von 0 bei Gleichheit, negativer Wert, wenn this.wert 'kleiner' als other.wert, positiv bei umgekehrter Sachlage.




***Spezifisch***




* **erfasseBuch(buch: Buch)** …​ fügt Buch hinzu. Prüfen auf `null`, dass Buch nicht schon in Verlag erfasst und sicherstellen, dass Verlag `**verlagPasst(…​)**` `true` liefert
* **verlagPasst(buch: Buch): boolean** …​ prüft, ob der Verlag im übergebenen Buch dem aktuellen Verlag entspricht.
* **schonErfasst(buch: Buch): boolean** …​ sicherstellen, dass nicht gleiches Buch schon in Liste




***Sortieren***




* **findMinValPos(anfIdx: int, endIdxExcl: int)** …​ Hilfsmethode für SelectionSort im Buecher-Array. anfIdx - ab dieser Position wird gesucht; endIdxExcl: bis zu dieser (excl → letzter Index eins davor!)
* **tauschen(idx0: int, idx1: int)** …​ Hilfsmethode für Dreieckstausch im Buecher-Array
* **selectionSort()** …​ Einfache Umsetzung des SelectionSort bei Verwendung obiger Hilfsmethoden.
* **buecherSortieren()** …​ Ruft einfach nur `selectionSort()` auf (alternativ z.B. bubbleSort).




***Ausgabe + Filtern***




* **printBuecher(ueberschrift: String)** …​ gibt alle Bücher aus (unterhalb von freeIdx!!!)
* **printBuecherWoTitelEnthaelt(teilstueck: String)** …​ gibt alle Bücher aus, die im Titel die Zeichenfolge in Param `teilstueck` enthalten.






3. Klasse Bibliothek
--------------------




In vielen Bereichen analog zu Verlag …​




***Standard-Elemente***




* **Konstruktor(kapazitaet: int)** …​ selbsterklärend
* **toString(): String** …​ gibt Anzahl der enthaltenen Bücher aus




***Array-Verwaltung***




* **add(buch: Buch): boolean** …​ nimmt das Buch in die Sammlung auf
* **remove(buch: Buch): Buch** …​ entfernt das Buch (Lücke schließen nicht vergessen!)




***Sortieren***




* **findMinValPos(anfIdx: int, endIdxExcl: int): int** …​ analog zu Verlag
* **tauschen(idx0: int, idx1: int)** …​ analog zu Verlag
* **selectionSort()** …​ analog zu Verlag
* **buchPoolSortieren()** …​ analog zu Verlag




***Ausgabe + Filtern***




* **printBuecher()** …​ Alle Bücher ausgeben (toString-Methode wird automatisch verwendet, wenn Objekt ohne Methode in textuellem Kontext vorkommt)
* **printBuecherVonAutor(namensteil: String)** …​ nach angegebenem Autor-Namensteil) filtern
* **printBuecherVonVerlag(verlag: Verlag)** …​ nach angegebenem Verlag filtern
* **printBuecherJuengerAb(jahrIncl: int)** …​ alles ab incl. dem gegebenen Jahr (Richtung zu jünger)
* **printBuecherWoTitelEnthaelt(teilstueck: String)** …​ analog zu `Verlag`






4. Testen mit JUnit
-------------------




Für jede der 3 Klasse ist eine Testklasse zu erstellen: `**BuchTest**`, `**VerlagTest**`, `**BibliothekTest**` und einige Methoden zu testen:




* `**Buch**` …​ die `Setter` mit gültigen und ungültigen Werten, `equals(..)` mit Erwartungswerten `true`, `false`, compareTo(..) mit >, =, <, autorInitialen()
* `**Verlag**` …​ `compareTo(..)`, `findMinValPos(anfIdx, endIdxExcl)`
* `**Bibliothek**` …​ `toString()`, `tauschen(idx0, idx1)`





