<!--
author:   Cédric Vogel
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Fehler-Lexikon zur Einheit «Funktionen – vom Aufruf zur eigenen Sprache».
          Jeder Eintrag ist ein Makro (@Fehler.<Name>), das die Etappen per
          import: einbinden. Neue Einträge werden am Ende ergänzt.

@Fehler.AssertionError
> **`AssertionError`** – Eine Prüfung mit `assert` ist fehlgeschlagen.
>
> **Was bedeutet das?** Die Bedingung nach `assert` wurde zu `False` ausgewertet. Ist die Bedingung `True`, passiert gar nichts.
>
> **Typische Ursache:** Entweder ist die Funktion falsch oder Ihr Beispiel. Werten Sie den Aufruf von Hand aus und vergleichen Sie mit dem Visualizer.
>
> ```python
> assert quadrat(3) == 6   # quadrat(3) → 3 * 3 → 9, dann 9 == 6 → False
> ```
@end

@Fehler.NameError
> **`NameError: name '…' is not defined`** – Python kennt diesen Namen nicht.
>
> **Was bedeutet das?** Beim Auswerten trifft Python auf einen Namen (z. B. eine Funktion oder Variable), zu dem es keine Definition gibt.
>
> **Typische Ursache:** Die Funktion wurde nicht definiert, oder der Name ist anders geschrieben (`Quadrat` statt `quadrat`).
>
> ```python
> s(5)   # NameError: name 's' is not defined – es gibt kein def s(...)
> ```
@end

@Fehler.ZeroDivisionError
> **`ZeroDivisionError: division by zero`** – Es wurde durch 0 geteilt.
>
> **Was bedeutet das?** Beim Auswerten ist ein Ausdruck der Form `… / 0` entstanden. Das ist in Python wie in der Mathematik nicht definiert.
>
> **Typische Ursache:** Ein Argument macht den Nenner zu 0. Werten Sie den Nenner von Hand aus.
>
> ```python
> g(-2)   # g(x) gibt 1 / (2 + x) zurück: 1 / (2 + -2) → 1 / 0 → ZeroDivisionError
> ```
@end

@Fehler.RecursionError
> **`RecursionError: maximum recursion depth exceeded`** – Eine Funktion ruft sich immer wieder selbst auf, ohne je anzukommen.
>
> **Was bedeutet das?** Python hat zu viele Aufrufe ineinander geöffnet und bricht ab, statt endlos weiterzurechnen.
>
> **Typische Ursache:** Es fehlt eine Verzweigung, welche weitere Aufrufe verhindern kann (der Rekursionsanfang) – oder die Verzweigung verhindert weitere Aufrufe nie.
>
> ```python
> def k(x):
>     return x + k(x + 1)   # jeder Aufruf öffnet einen neuen Aufruf
> ```
@end
@Fehler.Doctest
> **`Failed example`** – Ein Beispiel im Docstring liefert nicht das, was dort steht.
>
> Unter `Expected` steht, was im Beispiel steht, unter `Got`, was Python berechnet hat. Prüfen Sie zuerst das Beispiel: Stimmt es, wenn Sie es aus der Aufgabe heraus überlegen? Wenn ja, liegt der Fehler in der Funktion – der Visualizer zeigt, an welcher Stelle. `Got nothing` heisst: Die Funktion gibt nichts zurück. Fehlt das `return`?
>
> ```text
> Failed example:
>     average(2, 5)
> Expected:
>     3
> Got:
>     3.5
> ```
@end

@Fehler.DoctestLeerzeichen
> **`ValueError: … lacks blank after >>>`** – Nach `>>>` fehlt ein Leerzeichen.
>
> **Was bedeutet das?** Doctest erkennt ein Beispiel nur, wenn nach `>>>` genau ein Leerzeichen folgt. Fehlt es, bricht doctest ab, bevor überhaupt ein Beispiel geprüft wird. Die Meldung ist lang, weil sie durch das Innere von doctest führt – wichtig ist nur die letzte Zeile: Sie nennt die Zeile im Docstring und die Funktion.
>
> **Typische Ursache:** `>>>f(3)` statt `>>> f(3)`.
>
> ```text
> ValueError: line 2 of the docstring for __main__.f lacks blank after >>>: '>>>f(3)'
> ```
@end

@Fehler.Argumente
> **`TypeError: … missing 1 required positional argument`** oder **`… takes 2 positional arguments but 3 were given`** – Die Funktion wurde mit der falschen Anzahl Argumente aufgerufen.
>
> **Was bedeutet das?** Jeder Parameter braucht beim Aufruf genau ein Argument. Fehlt eines, nennt Python den Parameter, für den kein Wert da ist; ist eines zu viel, nennt Python, wie viele erwartet und wie viele übergeben wurden.
>
> **Typische Ursache:** Ein Argument vergessen oder eines zu viel geschrieben – oft nach einer Änderung der Parameterliste. Vergleichen Sie den Aufruf mit der Zeile `def …(…)`.
>
> ```text
> note(15)          # TypeError: note() missing 1 required positional argument: 'maximum'
> note(15, 20, 3)   # TypeError: note() takes 2 positional arguments but 3 were given
> ```
@end

@Fehler.IndexError
> **`IndexError: list index out of range`** – Diese Adresse gibt es in der Liste nicht.
>
> **Was bedeutet das?** Die Zahl in den eckigen Klammern ist eine Adresse (der Index). Adressen beginnen bei 0: Eine Liste mit drei Werten hat die Adressen 0, 1 und 2 – die Adresse 3 gibt es nicht.
>
> **Typische Ursache:** Beim Zählen bei 1 statt bei 0 begonnen, oder den Wert statt der Adresse in die Klammern geschrieben.
>
> ```python
> dauer = [1, 2, 30]
> dauer[3]   # IndexError: list index out of range – die letzte Adresse ist 2
> ```
@end

@Fehler.NoneType
> **`TypeError: … 'NoneType' …`** – Mit dem Wert `None` wurde weitergerechnet, z. B. `unsupported operand type(s) for +: 'NoneType' and 'int'` oder `'NoneType' object is not subscriptable`.
>
> **Was bedeutet das?** `None` ist der Wert für «kein Wert». Eine Funktion ohne `return` gibt `None` zurück – auch wenn sie mit `print` etwas anzeigt. Mit `None` lässt sich nicht rechnen, und es hat keine Adressen.
>
> **Typische Ursache:** Die Funktion zeigt ihr Ergebnis mit `print` an, statt es mit `return` zurückzugeben. Prüfen Sie den Rumpf: Steht dort `return`?
>
> ```python
> zeige_schnitt([4, 5, 4.5]) + 1   # zeigt 4.5 an, dann TypeError: … 'NoneType' and 'int'
> ```
@end
-->

# Fehler-Lexikon

Hier finden Sie die Fehlermeldungen, die Ihnen in dieser Einheit begegnen. Python zeigt sie auf Englisch an – genau so wie in der Prüfung. Lesen Sie zuerst die Meldung selbst, dann die Erklärung.

## AssertionError

@Fehler.AssertionError

## NameError

@Fehler.NameError

## ZeroDivisionError

@Fehler.ZeroDivisionError

## RecursionError

@Fehler.RecursionError

## Fehlgeschlagener Doctest

@Fehler.Doctest

## Doctest: Leerzeichen nach >>>

@Fehler.DoctestLeerzeichen

## Falsche Anzahl Argumente

@Fehler.Argumente

## Adresse gibt es nicht (IndexError)

@Fehler.IndexError

## Rechnen mit None (TypeError … NoneType)

@Fehler.NoneType
