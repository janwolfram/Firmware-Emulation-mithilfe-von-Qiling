# Firmware-Emulation-mithilfe-von-Qiling
In diesem Repo befinden sich alle Ergebnisse und verwendeten Skripte und Dateien. 

## setup.py
Dieses Skirpt kann ganz normal mit python3 ausgeführt werden. Hiermit lassen sich die Emulationen automatisert durchführen. In Zeile 25 müssen dazu die Geräte in das Array eingefügt werden. Aktuell ist nur ein Gerät eingefügt. Es können aber beliebig viele Geräte eingefügt werden oder man kann direkt das Array my_devices für die Schleife in Zeile 27 verwenden. Wichtig ist zudem, dass die Ordnerstruktur genauso ist, wie in folgendem Zip-File (mein gesammelter Datensatz) https://drive.google.com/file/d/186nFpESNtpKrZxJnBbI40qNk_Nsixb8e/view?usp=sharing. Zu beachten ist nur, dass in Zeile 20 der richtige Ordnerpfad angegeben ist. Zudem sind in Zeile 43, 53, 64 und 75 die qltool Befehle für die jeweiligen Unterordner bin, sbin, usr/bin und usr/sbin. Hier kann hinter --args jedes beliebige Argument eingefügt werden.

## Logging der Ergebnisse 
Das Logging wurde mit "script" durchgeführt. Der Befehl für die Konsole lautet "script name.txt". Beendet wird ein Skript mit dem Befehl "exit". Script zeichnet den gesamten Stream der Konsole auf. Das Logging der jeweiligen Flags ist jeweils in den Unterordnern help, version und questionmark zu finden. In jedem Durchlauf wurden immer nur zehn Geräte auf einmal verwendet. 

## Analyseskript
Das Analyseskript kann ebenfalls mit python3 ausgeführt werden. Wichtig ist nur das in Zeile 6 die Logging Datei angegeben wird. Zudem kann mit der Flag -b der detaillierte Modus genutzt werden. 

## Ergebnisse
Im Ordner Ergebnisse sind alle Tabellenkalkulationsdateien gespeichert mit den Ergebnissen. Zudem gibt es dort eine weitere Datei, die nur die daten, die für die Diagramme wichtig sind enthält. Der Unterordner Grafiken enthält alle Grafiken. 

## Übersicht Firmware-Images
Enthält eine Übersicht über alle Geräte und wie viele Images erfolgreich entpackt werden konnten etc.

## Änderungen an Logging-Files
Bei manchen Emulationen kamen unglücklicherweise die Trennzeichen - und * teilweise in der Emulationsausgabe vor. Dies führte dazu, dass der Parser nicht richtig funktioniert hat. Daher habe ich bei manchen Emulationen diese Trennzeichen manuell entfernt, damit der Parser wieder fehlerfrei trennen kann. Das Emulationsergebnis wurde dabei nicht verfälscht oder sonstiges. Die Analyse wird dadurch ebenfalls nicht eingeschränkt. In dem File Änderungen-Logging.txt werden für jede Flag die Geräte und die dazugehöigen Binärdateien gelistet, wo Trennzeichen manuell entfernt wurden.

