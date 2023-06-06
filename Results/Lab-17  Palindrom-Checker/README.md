
Aufgabe Palindrom-Checker
=========================



Erstelle eine Klasse `**PalindromChecker**` nach folgender Spezifikation:








Die Klasse `**PalindromChecker**` dient zur Benutzer-Engabe eines Satzes und zum Feststellen, ob der Satz nach Entfernen aller Satzzeichen und Leerzeichen und Umwandeln auf Kleinbuchstaben ein Palindrom ist (Letztes und erstes Zeichen gleich, vorletztes und zweites, …​).
(Bei ungerader Zeichenzahl ist das Mittelzeichen klarerweise mit sich selbst gleich)




* Attribut `**pali**` wird wie oben beschrieben initialisiert und dient als erstes Beispiel (ohne vorheriges Einlesen).
* Methode `**eingabePalindrom()**` liest vom Benutzer (mit Klasse `java.util.Scanner`) einen Text ein und speichert diesen im Attribut `**pali**`.
* Methode `istLoeschChar(ch: char)` prüft das übergebene Zeichen gegen alle Zeichen im Array `LOESCH_CHARS` (muss auch bei Hinzufügen/Entfernen von Lösch-Zeichen funktionieren!). Liefert `true`, wenn Zeichen zu entfernen ist, sonst `false`.
* Methode `**loescheSpcUndSatzzeichen(txt: String): String**` entfernt aus dem übergebenen String alle Spaces und Satzzeichen (aus Array-Konstante LOESCH\_CHARS) und gibt den veränderten String zurück. Wandle in der Methode den String in ein `char`-Array um, entferne alle LOESCH\_CHARS (`'.'`, `'!'`, `'?'`, `','`, `':'`, …​) aus dem char-Array und schreibe das Ergebnis vom char-Array wieder in einen String, den du zurückgibst.  




*Siehe auch Hinweise unten!*
* Methode `**istPalindrom(): boolean**` stellt fest, ob der Satz, der in pali gespeichert ist, ein Palindrom ist (ein Palindrom ist eine Zeichenkette, die von vorn und von hinten gelesen gleich bleibt).
Dabei wird NICHT zwischen Groß- und Kleinbuchstaben unterschieden und alle LOESCH\_CHARS (Leerzeichen, Satzzeichen) entfernt.






|  |  |
| --- | --- |
|  | 
Verwende in deiner Methode die Methode `**loescheSpcUndSatzzeichen(String txt)**` um zunächst die LOESCH\_CHARS aus dem String zu entfernen.
Achte dabei aber darauf, dass dein Attribut `pali` nicht verändert wird.
 |




Wenn ein zweites Array für den bereinigten Satz verwendet wird, sollte die Arraykapazität mit Methode `laengeOhneLoeschChars()` zu definieren.




* Methode `**check()**`: starte einen Check-Vorgang: `eingabePalindrom()`, dann `istPalindrom()`, zuletzt Ausgabe:
Gib auf dem Bildschirm den Inhalt von `pali` (der unveränderte, eingegebene Satz) aus und anschließend das Ergebnis deiner Überprüfung:




	+ Ist der Satz ein Palindrom, so gib „Der Satz ist ein Palindrom“ auf dem Bildschirm aus,
	+ anderenfalls gib „Leider KEIN Palindrom!“ auf dem Bildschirm aus




z.B. `Text "Lag er im Kajak? Mir egal." ist ein Palindrom`  

oder `"Sei fein, nie mies." ist KEIN Palindrom`




Beispiele für Palindrome finden sich z.B. unter:
[Liste deutscher Palindrome – Wikipedia](https://de.wikipedia.org/wiki/Liste_deutscher_Palindrome)




**Hinweise:**  

Ausgangstext: `String srcTxt = "Hallo";`




* Umwandeln String in `char`-Array: `char[] txtChars = txt.toCharArray();`
* Umwandeln `char`-Array nach String: String `finalTxt = new String(txtChars);`



