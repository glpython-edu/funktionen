"""
Parser für die Ausdruckssprache der Einheit «Funktionen – vom Aufruf zur eigenen Sprache».

Übersetzt einen Ausdruck (Python-Text wie "2 + 3") in einen Ausdrucksbaum:
eine verschachtelte Liste in Präfixform wie ['+', 2, 3].
Sie müssen diese Datei nicht verstehen – Sie verwenden nur ihre Funktionen
parse(text), ist_liste(x) und code_lesen(path).
"""

import ast

_OPERATOREN = {
    ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/",
    ast.FloorDiv: "//", ast.Mod: "%", ast.Pow: "**",
    ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=",
    ast.Gt: ">", ast.GtE: ">=",
    ast.And: "and", ast.Or: "or",
}

_WERTE = (int, float, bool, str)


def parse(text):
    """
    Gibt den Ausdrucksbaum zum Ausdruck text zurück.

    Alle Rechenoperatoren (+ - * / // % **) und Vergleiche (< <= > >= == !=)
    werden gleich übersetzt: [Operator, links, rechts].

    >>> parse("2 + 3")
    ['+', 2, 3]
    >>> parse("2 < 3")
    ['<', 2, 3]

    Vorrang, Klammern und Gruppierung wie in Python:

    >>> parse("2 + 3 * 4")
    ['+', 2, ['*', 3, 4]]
    >>> parse("(2 + 3) * 4")
    ['*', ['+', 2, 3], 4]
    >>> parse("1 + 2 + 3")
    ['+', ['+', 1, 2], 3]
    >>> parse("1 + 1 == 2")
    ['==', ['+', 1, 1], 2]

    Zahlen sind schon ausgewertet, auch negative Zahlen und Dezimalzahlen:

    >>> parse("42")
    42
    >>> parse("-3")
    -3
    >>> parse("1.5 + 2")
    ['+', 1.5, 2]

    Was kein Ausdruck ist, wird abgelehnt:

    >>> parse("x = 3")
    Traceback (most recent call last):
    ...
    ValueError: «x = 3» ist kein Ausdruck.
    """
    try:
        baum = ast.parse(text.strip(), mode="eval")
    except SyntaxError:
        raise ValueError("«" + text.strip() + "» ist kein Ausdruck.") from None
    return _kodieren(baum.body)


def code_lesen(path):
    """
    Gibt den Inhalt der Datei path als Text zurück.

    Ohne Beispiele: Das Ergebnis hängt nicht nur vom Argument ab, sondern vom
    Inhalt einer Datei – derselbe Aufruf kann morgen etwas anderes liefern.
    Beispiele im Design-Rezept eignen sich für Funktionen, die ihren Wert
    allein aus den Argumenten berechnen.
    """
    with open(path, encoding="utf-8") as datei:
        return datei.read()



def ist_liste(x):
    """
    Gibt True zurück, wenn x eine Liste ist.

    >>> ist_liste(['+', 1, 2])
    True
    >>> ist_liste([])
    True
    >>> ist_liste(3)
    False
    >>> ist_liste('+')
    False
    """
    return type(x) == list


def _kodieren(knoten):
    """
    Gibt den ast-Knoten knoten als verschachtelte Liste zurück (Hilfsfunktion von parse).

    >>> _kodieren(ast.parse("42", mode="eval").body)
    42
    >>> _kodieren(ast.parse("2 + 3 * 4", mode="eval").body)
    ['+', 2, ['*', 3, 4]]
    >>> _kodieren(ast.parse("-3", mode="eval").body)
    -3
    >>> _kodieren(ast.parse("-(1 + 2)", mode="eval").body)
    ['-', ['+', 1, 2]]
    """
    if isinstance(knoten, ast.Constant) and type(knoten.value) in _WERTE:
        return knoten.value

    if isinstance(knoten, ast.BinOp) and type(knoten.op) in _OPERATOREN:
        return [_OPERATOREN[type(knoten.op)], _kodieren(knoten.left), _kodieren(knoten.right)]

    if isinstance(knoten, ast.Compare):
        if len(knoten.ops) > 1:
            raise ValueError("Verkettete Vergleiche werden nicht unterstützt.")
        return [_OPERATOREN[type(knoten.ops[0])], _kodieren(knoten.left), _kodieren(knoten.comparators[0])]

    if isinstance(knoten, ast.UnaryOp) and isinstance(knoten.op, ast.USub):
        # Minus direkt vor einer Zahl ergibt eine negative Zahl.
        if isinstance(knoten.operand, ast.Constant) and type(knoten.operand.value) in (int, float):
            return -knoten.operand.value
        return ["-", _kodieren(knoten.operand)]

    if isinstance(knoten, ast.UnaryOp) and isinstance(knoten.op, ast.Not):
        return ["not", _kodieren(knoten.operand)]

    if isinstance(knoten, ast.BoolOp):
        # a and b and c wird zu ["and", ["and", a, b], c].
        operator = _OPERATOREN[type(knoten.op)]
        ergebnis = _kodieren(knoten.values[0])
        for wert in knoten.values[1:]:
            ergebnis = [operator, ergebnis, _kodieren(wert)]
        return ergebnis

    if isinstance(knoten, ast.Call) and isinstance(knoten.func, ast.Name) and not knoten.keywords:
        if not any(isinstance(argument, ast.Starred) for argument in knoten.args):
            return [knoten.func.id] + [_kodieren(argument) for argument in knoten.args]

    if isinstance(knoten, ast.Name):
        return ["var", knoten.id]

    if isinstance(knoten, ast.List):
        return ["liste"] + [_kodieren(element) for element in knoten.elts]

    raise ValueError("«" + ast.unparse(knoten) + "» gehört nicht zur Ausdruckssprache.")
