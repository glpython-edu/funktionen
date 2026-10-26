<!--
author:   Cédric Vogel
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Gemeinsame Makros und Stile der Einheit «Funktionen – vom Aufruf zur eigenen Sprache».
          Jede Etappe bindet diese Datei per import: ein.

@style
.lia-code--inline {
  background: #F3F4F6;
  color: #1A1A1A;
  border: none;
  border-radius: 3px;
  padding: 0.05em 0.3em;
}
@end

@Baustein.Name: <code class="lia-code lia-code--inline" style="background:#5EC4A0;color:#000">@0</code>
@Baustein.Parameter: <code class="lia-code lia-code--inline" style="background:#56B4E9;color:#000">@0</code>
@Baustein.Rumpf: <code class="lia-code lia-code--inline" style="background:#F0E442;color:#000">@0</code>
@Baustein.Argument: <code class="lia-code lia-code--inline" style="background:#CC79A7;color:#000">@0</code>

@Dezimal
<script>
  let input = `@input`.trim()
  if (input.includes(",")) {
    send.lia("Hinweis: In Python schreibt man Dezimalzahlen mit einem Punkt, z. B. 1.75 statt 1,75.", [], false)
  } else {
    input == "@0"
  }
</script>
@end

@Code.erkunden: @GLPython.eval(features=run,repl,visualize,ide @0)
@Code.rezept: @GLPython.eval(features=run,repl,visualize,tests,ide @0)
@Code.pruefung: @GLPython.eval(features=run @0)
@Code.voll: @GLPython.eval(@0)
@Code.demo: @GLPython.visual(large @0)
@Code.anschauen: @GLPython.visual(features=visualize @0)

@Notiz: @Notiz.block(@uid)

@Notiz.block
<script>
window.setTimeout(() => send.lia("LIA: stop"), 0)
"LIA: wait"
</script>

<script run-once>
(() => {
  const id = "notiz-save-@0"
  const findBlock = (button) => {
    const blocks = [...(button.closest(".lia-slide__content")?.querySelectorAll(".lia-code--block") ?? [])]
    return blocks.findLast((block) => block.compareDocumentPosition(button) & Node.DOCUMENT_POSITION_FOLLOWING) ?? null
  }
  const liaRunButton = (block) => block?.querySelector(".lia-code-control__action button") ?? null
  const attach = () => {
    const button = document.getElementById(id)
    if (!button) return
    // Set the label here: LiaScript drops the space inside the macro's HTML.
    if (!button.dataset.saving && !/^Notizen\s+speichern$/.test(button.textContent)) button.textContent = "Notizen\u00A0speichern"
    const block = findBlock(button)
    const run = liaRunButton(block)
    if (run && run.style.display !== "none") run.style.display = "none"
    // Mark the notes block and the element holding the button, so the course
    // @style can frame both as one unit; hide empty LiaScript paragraphs in
    // between. Only attributes and styles change, so the MutationObserver
    // (childList) is not triggered again.
    if (!block) return
    if (block.dataset.notiz !== "1") block.dataset.notiz = "1"
    // The element that holds the button on the same level as the code block
    // (LiaScript may wrap the button), or its direct parent as a fallback.
    let holder = button
    while (holder.parentElement && holder.parentElement !== block.parentElement) holder = holder.parentElement
    if (holder.parentElement !== block.parentElement) holder = button.parentElement
    if (holder.dataset.notizActions !== "1") holder.dataset.notizActions = "1"
    for (let el = block.nextElementSibling; el && el !== holder; el = el.nextElementSibling) {
      if (el.matches("p.lia-paragraph") && !el.textContent.trim() && !el.children.length && el.style.display !== "none") el.style.display = "none"
    }
    if (button.dataset.wired) return
    button.dataset.wired = "1"
    button.onclick = () => {
      const current = liaRunButton(findBlock(button))
      if (!current) return
      current.click()
      button.dataset.saving = "1"
      button.textContent = "Gespeichert ✓"
      window.setTimeout(() => { delete button.dataset.saving; button.textContent = "Notizen\u00A0speichern" }, 1500)
    }
  }
  attach()
  new MutationObserver(attach).observe(document.body, { childList: true, subtree: true })
})()
</script>

<div class="notiz-actions"><button id="notiz-save-@0" type="button" style="margin:0;padding:6px 12px;border:1px solid #6B7280;border-radius:4px;background:#FFFFFF;color:#1A1A1A;font:14px system-ui, sans-serif;cursor:pointer">Notizen&nbsp;speichern</button></div>
@end
-->

# Makros der Einheit

Diese Datei enthält die gemeinsamen Makros der Einheit. Jede Etappe bindet sie mit `import: ../00-makros/README.md` ein.

Der `@style`-Block für Inline-Code wirkt nur in dieser Datei selbst: LiaScript übernimmt beim Import die Makros, nicht aber `@style`. Jede Etappe braucht den Block deshalb zusätzlich im eigenen Header (Vorlage: `journal.md` → `## Visual Identity` → «LiaScript Theme»).

## Farbcodierung der Bausteine

@Baustein.Name(f) · @Baustein.Parameter(x) · @Baustein.Rumpf(x * x) · @Baustein.Argument(3)

Verwendung im Text: `@Baustein.Name(f)`, `@Baustein.Parameter(x)`, `@Baustein.Rumpf(x * x)`, `@Baustein.Argument(3)`. Code mit Komma in Backticks setzen, z. B. ``@Baustein.Argument(`2, 5`)``.

## Hinweis bei Dezimalkomma

Nach einem Text-Quiz mit Dezimalzahl: `@Dezimal(1.75)`. Gibt jemand `1,75` ein, erscheint ein Hinweis auf den Dezimalpunkt.

Was ergibt `7 / 4`?

[[1.75]]
@Dezimal(1.75)

## glpython-Profile

Welche glpython-Funktionen sichtbar sind, folgt dem Lernweg (`journal.md` → `## Didactics` → «glpython-Profile pro Etappe»). Statt `@GLPython.eval` steht unter einem Python-Block eines dieser Makros:

| Makro | Wo | Sichtbar |
|---|---|---|
| `@Code.erkunden` | Etappe 1 | Ausführen, REPL, Visualisieren, IDE-Link |
| `@Code.rezept` | Etappen 2–5 | zusätzlich Tests |
| `@Code.pruefung` | Prüfungsprobe (Etappe 6) | nur Ausführen – wie auf exam.net |
| `@Code.voll` | Etappe 7 | alles, inkl. →-Export |
| `@Code.demo` | 🎓-Folien | nur der Visualizer, grosse Schrift, nicht bearbeitbar, mit →-Export |
| `@Code.anschauen` | Arbeitsphase | nur der Visualizer, normale Grösse, nicht bearbeitbar, **ohne** →-Export (z. B. nach Vorhersagen von Hand) |

Weitere Optionen werden angehängt, z. B. der Startmodus oder Bibliotheken: `@Code.erkunden(box)`, `@Code.rezept(https://…/parser.py)`. Der →-Export ist für Lernende in den Etappen 1–6 bewusst ausgeblendet.

Die Profile brauchen den Import von glpython-liascript im Header der Etappe.

## Notizfeld

Ein Notizfeld für eigene Schritte, z. B. eine Auswertungskette, die nicht geprüft wird. Unter einen leeren (oder vorbelegten) `text`-Block gesetzt:

````markdown
```text
f(a) + g(b)
-> 
```
@Notiz
````

Statt LiaScripts `</>` erscheint der Button «Notizen speichern»; jeder Klick legt eine Version im Verlauf (|< < n > >|) ab. Gespeicherte Notizen bleiben online ab Version 1.0.0 auch nach einem Neuladen erhalten (in der VS-Code-Vorschau nicht). Der Rahmen um Feld und Button kommt aus dem `@style`-Block der Etappe (Vorlage: `journal.md` → `## Visual Identity` → «Ein Block im Kurs»).
