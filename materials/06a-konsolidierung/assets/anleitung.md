# Auswerter für beliebig grosse Bäume

Dieses Projekt ist freiwillig und kein Prüfungsstoff. Es zeigt, wie der Auswerter aus Etappe 4 auch verschachtelte Bäume ausrechnet, zum Beispiel `['+', 2, ['*', 3, 4]]`.

## Das Projekt hat drei Tabs

- **anleitung.md** – diese Anleitung. Sie können sie nur lesen.
- **auswerter.py** – der Auswerter aus Etappe 4, mit allen Rechenoperatoren. Hier arbeiten Sie. «Ausführen», «Tests» und «Visualisieren» gelten immer für diese Datei, auch wenn gerade ein anderer Tab offen ist.
- **parser.py** – die Bibliothek mit `parse`. Sie können sie nur lesen.

## So gehen Sie vor

1. Wechseln Sie zum Tab **auswerter.py** und drücken Sie «Tests». Vier Beispiele scheitern, alle mit verschachtelten Bäumen, und alle mit einem `TypeError` mit `'list'`. Lesen Sie eine Meldung genau.
2. Klicken Sie bei einem gescheiterten Beispiel auf «Beispiel visualisieren» und gehen Sie bis zum Fehler. Was bekommt `operator_anwenden` als `x` oder `y`?
3. Ein Teilbaum wie `['*', 3, 4]` ist selbst wieder ein Ausdrucksbaum – und Ausdrucksbäume rechnet `auswerten` aus. Ändern Sie in **Zeile 84** die Zeile

   ```python
   return operator_anwenden(baum[0], baum[1], baum[2])
   ```

   so, dass die beiden Teile zuerst mit `auswerten` ausgerechnet werden:

   ```python
   return operator_anwenden(baum[0], auswerten(baum[1]), auswerten(baum[2]))
   ```

4. Drücken Sie wieder «Tests». Jetzt bestehen alle Beispiele.
5. Visualisieren Sie ein Beispiel noch einmal: Jeder Aufruf von `auswerten` bekommt einen kleineren Teil des Baums, bis ein Teil eine Zahl ist.

`auswerten` ruft sich jetzt selbst auf. Eine solche Funktion heisst **rekursiv**.
