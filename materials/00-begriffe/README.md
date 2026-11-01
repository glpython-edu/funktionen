<!--
author:   Cédric Vogel
version:  0.1.0
license:  CC BY-SA 4.0
language: de
narrator: Deutsch Female

comment:  Begriffsübersicht zur Einheit «Funktionen – vom Aufruf zur eigenen
          Sprache». Flach in der Reihenfolge, in der die Begriffe im Kurs
          vorkommen; jeder Eintrag mit seiner Etappe und einem Link auf die
          Folie, die ihn einführt. Wird ergänzt, sobald eine Etappe einen
          neuen Begriff einführt (Coauthor-Regel 28).

@style
.lia-code--inline {
  background: #F3F4F6;
  color: #1A1A1A;
  border: none;
  border-radius: 3px;
  padding: 0.05em 0.3em;
}
@end

-->

# Begriffe der Einheit «Funktionen»

Die Begriffe der Einheit in der Reihenfolge, in der sie vorkommen – jeder mit der Folie, auf der er eingeführt wird. Fehlermeldungen stehen im [Fehler-Lexikon](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/00-fehler-lexikon/README.md).

- **Ausdruck, Wert** *(Etappe 1)* – Ein Ausdruck lässt sich zu einem Wert auswerten; ein Wert ist ein Ausdruck, der schon ausgewertet ist. → [Ausdrücke auswerten](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#5)
- **Auswerten mit «→»** *(Etappe 1)* – Ein Ausdruck wird Schritt für Schritt vereinfacht, bis ein Wert übrig bleibt; «→» steht für genau einen Schritt. → [Ausdrücke auswerten](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#5)
- **Funktionsdefinition** *(Etappe 1)* – Legt mit Name, Parametern und Rumpf fest, was bei einem Aufruf der Funktion passiert. → [Die Bausteine einer Funktion](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#7)
- **Parameter** *(Etappe 1)* – Ein Platzhalter in der Funktionsdefinition für einen Wert, der erst beim Aufruf feststeht. → [Die Bausteine einer Funktion](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#7)
- **Rumpf** *(Etappe 1)* – Die eingerückten Zeilen unter der Zeile mit `def`; sie legen fest, was beim Aufruf berechnet wird. → [Die Bausteine einer Funktion](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#7)
- **Funktionsaufruf** *(Etappe 1)* – Ein Ausdruck aus dem Namen einer Funktion und Argumenten in Klammern. → [Die Bausteine einer Funktion](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#7)
- **Argument** *(Etappe 1)* – Ein Ausdruck in den Klammern eines Aufrufs; sein Wert wird für den Parameter eingesetzt. → [Die Bausteine einer Funktion](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#7)
- **`return`** *(Etappe 1)* – Gibt den Wert des folgenden Ausdrucks zurück, wie `report` in Snap!. → [Die Bausteine einer Funktion](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#7)
- **Auswerten von Funktionsaufrufen** *(Etappe 1)* – Zuerst werden die Argumente ausgewertet, dann wird der Aufruf durch den Ausdruck nach `return` ersetzt, mit den Argumenten an der Stelle der Parameter. → [Ein Aufruf Schritt für Schritt](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#8)
- **REPL** *(Etappe 1)* – Die Zeile mit `>>>` in der Konsole; sie wertet einen Ausdruck aus und zeigt seinen Wert. → [Werte anschauen wie in Snap!](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#9)
- **Visualizer** *(Etappe 1)* – Zeigt die Auswertung eines Funktionsaufrufs Schritt für Schritt. → [Werte anschauen wie in Snap!](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#9)
- **Division mit `/`** *(Etappe 1)* – Ergibt immer eine Dezimalzahl. → [Aufgabe 5: Kreis mit Durchmesser](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/01-von-snap-reportern-zu-python-funktionen/README.md#17)
- **Design-Rezept** *(Etappe 2)* – Eine Methode, um Funktionen strukturiert zu entwerfen: ein klarer Weg und eine gewisse Sicherheit, dass die Funktion stimmt. → [Von der Aufgabe zur Funktion](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/02-das-design-rezept/README.md#4)
- **Docstring** *(Etappe 2)* – Der Text zwischen `"""` und `"""` direkt unter der Zeile `def`; er beschreibt die Funktion. → [Doctests: eine REPL-Sitzung als Test](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/02-das-design-rezept/README.md#5)
- **Doctest** *(Etappe 2)* – Ein Beispiel im Docstring in der Form einer REPL-Sitzung; Python prüft, ob der Aufruf diesen Wert ergibt. → [Doctests: eine REPL-Sitzung als Test](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/02-das-design-rezept/README.md#5)
- **Bibliothek** *(Etappe 2)* – Eine Datei mit fertigen Funktionen, die man benutzt, ohne zu wissen, wie sie rechnen. → [Eine Bibliothek benutzen](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/02-das-design-rezept/README.md#7)
- **`import`** *(Etappe 2)* – Holt eine Funktion aus einer Bibliothek ins eigene Programm. → [Eine Funktion ruft eine andere auf](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/02-das-design-rezept/README.md#8)
- **`help`** *(Etappe 2)* – Zeigt in der REPL den Docstring einer Funktion. → [Eine Bibliothek benutzen](https://liascript.github.io/course/?https://raw.githubusercontent.com/glpython-edu/funktionen/main/materials/02-das-design-rezept/README.md#7)
