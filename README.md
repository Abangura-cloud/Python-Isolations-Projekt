„Squash“-Vorgang: Interne Umsetzung eines Git-Squash

Gegebenes Szenario:

• Vorher: A -- B -- C -- D -- E (main)
• Nachher: ​​A -- B -- E' (main)

Teil 1: Der interne Ausführungsalgorithmus

1. Festlegung des Bereichs: Git identifiziert den vom Benutzer angegebenen Bereich. Das Ende (die „Spitze“) des Branches wird als E markiert; der Commit, der unmittelbar vor dem zu „squashenden“ Bereich liegt (der Anker-Commit), wird als B identifiziert.
2. Extraktion des Ziel-Trees: Git ruft den Hash des Wurzelverzeichnis-Snapshots (das „Tree-Objekt“) direkt vom Commit E ab. Da Git-Snapshots kumulativ sind, enthält dieser Tree-Hash den gesamten Endzustand aller geänderten Dateien aus den Commits C, D und E.
3. Zusammenführung der Commit-Metadaten: Git liest die Commit-Nachrichten von C, D und E aus, öffnet einen interaktiven Editor und fordert den Benutzer auf, diese Texte zu einer einzigen, zusammengefassten Commit-Nachricht zu vereinen.
4. Erstellung des „Squashed“-Commit-Objekts (E'): Git generiert ein völlig neues Commit-Objekt in seiner Datenbank (`.git/objects`) und setzt dessen interne Werte:
• Tree-Pointer: Verweist direkt auf den bereits existierenden Tree-Hash, der aus Commit E extrahiert wurde.
• Parent-Pointer: Verweist direkt auf den Hash von Commit B.
• Commit-Nachricht: Enthält die neu zusammengefasste Nachricht.
5. Aktualisierung der Branch-Referenz: Git aktualisiert die Referenzdatei des aktuell aktiven Branches (`.git/refs/heads/main`), sodass sie nun auf den neu generierten Hash von E' zeigt – die sichtbare Historie wird dadurch umgeschrieben.
___

Teil 2: Wiederverwendung von Objekten

• Blobs (Dateiinhalte): Zu 100 % wiederverwendet. Es werden keine neuen Blob-Objekte erstellt. Da der Endzustand der Dateien in Commit E' exakt dem Zustand in Commit E entspricht, ordnet Git die Daten-Hashes einfach den bereits vorhandenen Datei-Blobs zu, die schon bei den ursprünglichen Commits gespeichert wurden.
• Trees (Verzeichnisstrukturen): Zu 100 % wiederverwendet. Es werden keine neuen Tree-Strukturen erstellt. Git übernimmt den exakten 40-stelligen Hash des Root-Trees, der zum neuesten Commit E gehört, und fügt ihn direkt in die Struktur des neuen Commits E' ein. (Wie wir im Terminal überprüft haben, verweisen beide, voneinander unabhängige Commits auf denselben Tree: c879ddb...).
• Commits (Historien-Markierungen): Neu erstellt. Ein völlig neues Commit-Objekt (E') wird in die Datenbank geschrieben. Obwohl es auf einen bereits existierenden Tree verweist, erfordert die Kombination aus Metadaten – ein eindeutiger Verweis auf den Vorgänger-Commit B, ein neuer Zeitstempel und eine geänderte Commit-Nachricht – einen neuen Datensatz.
___

Teil 3: Lebenszyklus der verworfenen Commits (C, D und E)

• Kurzfristige Auswirkungen (Zustand als „verwaiste“ Commits): Unmittelbar nach Abschluss des Rebase-Vorgangs werden die alten Commits C, D und E zu sogenannten „verwaisten“ Commits (dangling commits). Da der Branch-Pointer nun auf E' zeigt, gibt es keine aktiven Branches oder Tags mehr, die auf diese Commits verweisen; sie sind daher in Standard-Protokollen wie `git log` nicht mehr sichtbar. Sie sind jedoch vor einem plötzlichen Verlust durch das „Reflog“ von Git geschützt, das die historischen Positionen von Pointern für einen Standardzeitraum von 90 Tagen speichert.
• Langfristige Auswirkungen (Garbage Collection): Sobald die 90-tägige Sicherheitsfrist des Reflogs abgelaufen ist, sind die Referenzen endgültig nicht mehr erreichbar. Wenn Git das nächste Mal automatisch seine interne Wartungsroutine – `git gc` (Garbage Collector) – ausführt, durchsucht es die Datenbank nach nicht mehr referenzierten Hashes, entfernt die Commits C, D und E vollständig und löscht sie dauerhaft vom Datenträger.
