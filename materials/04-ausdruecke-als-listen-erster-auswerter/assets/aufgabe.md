# Aufgabe 4: Weitere Operatoren

Ihr Auswerter kann bisher nur `+`. In dieser Aufgabe bringen Sie ihm alle Rechenoperatoren bei: `-`, `*`, `/`, `//`, `%` und `**`.

## Das Projekt hat drei Tabs

- **aufgabe.md** – diese Anleitung. Sie können sie nur lesen.
- **auswerter.py** – Ihre Datei. Hier arbeiten Sie. «Ausführen», «Tests» und «Visualisieren» gelten immer für diese Datei, auch wenn gerade ein anderer Tab offen ist.
- **parser.py** – die Bibliothek mit `parse`. Sie können sie nur lesen, und Sie müssen nicht wissen, wie sie funktioniert.

Wechseln Sie jetzt zum Tab **auswerter.py**. Im Docstring von `anwenden` steht für jeden neuen Operator schon ein Beispiel – diese Tests scheitern noch.

## So gehen Sie vor

1. Drücken Sie «Tests». Sechs Beispiele scheitern mit «Got nothing» – lesen Sie eine Meldung genau.
2. Beim Operator `-` fehlt nur noch etwas: Die Zeile `if op == "-":` steht schon, aber nach dem `return` fehlt der Ausdruck. Ergänzen Sie ihn und drücken Sie wieder «Tests» – jetzt scheitern nur noch fünf.
3. Ergänzen Sie in `anwenden` eine `if`-Zeile pro Operator, bis alle Tests bestehen.
4. Schreiben Sie zum Schluss in den Docstring von `berechnen` für jeden neuen Operator ein eigenes Beispiel, zum Beispiel `berechnen("9 - 4")`, und prüfen Sie, indem Sie auf «Tests» klicken.

«Got nothing» heisst: Die Funktion hat `None` zurückgegeben – für diesen Operator gibt es in `anwenden` noch keine passende `if`-Zeile.

## Noch nicht fertig?

Die IDE merkt sich Ihre Arbeit nur in diesem Browser – auf einem anderen Gerät oder nach einiger Zeit ist sie nicht mehr da. Drücken Sie deshalb am Ende jeder Lektion «Teilen» und speichern Sie den Link in Ihren eigenen Notizen in OneNote (nicht in der Zeile für die Abgabe). In der nächsten Lektion öffnen Sie die IDE über diesen Link.

## 📌 Abgabe

Wenn alle Tests bestehen: Drücken Sie «Teilen» – das kopiert einen Link auf Ihren Stand. Fügen Sie den Link auf der OneNote-Seite «1201» im Abschnitt «1200 - Funktionen» in der Zeile «Etappe 4» ein – mit dem Namen «Aufgabe 4» (Namen schreiben und markieren, dann ⌘K bzw. Ctrl+K).
