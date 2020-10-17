---
Title: Pobieranie
Description: Strona pobierania
Author: Wituch
Date: 2020-10-10
Robots: noindex,nofollow
Template: index
---

Każda wersja MinecraftPlus działa tak samo jak oryginalny Minecraft. Do uruchomienia gry potrzebny jest launcher Minecraft (dowolny, obsługujący oryginalne pliki konfiguracyjne `.json`).

# Pobieranie klienta MC+

Aby uruchomić klienta gry w wydaniu MiecraftPlus musisz pobrać odpowiednią konfigurację wersji z poniższej listy:

 * [0.0.1 - *Cannon Update R1*](%assets_url%/downloads/minecraft/minecraftplus-0.0.1.json)
 * [0.0.1-SNAPSHOT - *Cannon Update S1*](%assets_url%/downloads/minecraftplus-0.0.1-SNAPSHOT.json)

# Instalacja klienta MC+

Pobrany plik konfiguracyjny wersji `minecraftplus-x.x.x.json` (lub dla wersji przejściowych `minecraftplus-x.x.x-SNAPSHOT.json`) należy umieścić w folderze o takiej samej nazwie jak plik, bez rozszerzenia `.json`.
Tak przygotowany folder z zawartym w nim plikiem konfiguracyjnym, należy przenieść do folderu wersji `.minecraft/versions/` (najczęściej jest to `%appdata%/.minecraft/versions/`) z którego korzysta używany launcher Minecraft.

# Uruchamianie klienta MC+

Aby uruchomić grę w wersji MinecraftPlus należy w launcherze gry dodać nową wersję. W tym celu należy skonfigurować nową instalację, która wykorzystywać będzie pobraną konfigurację wersji gry.
Należy zwrócić uwagę na rodzaj pobranej konfiguracji - w przypadku gdy nazwa zawiera słowo `SNAPSHOT` jest to wydanie przejściowe i w launcherze należy odblokować używanie wersji przejściowych.
