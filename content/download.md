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

Aby uruchomić klienta gry w wydaniu MiecraftPlus musisz pobrać odpowiednią konfigurację wersji z poniższej listy, a następnie ją zainstalować.  
W przypadku problemu z pobieraniem, kliknij na link PPM i wybierz "Zapisz link jako...".

<table style="table-layout: fixed; width: 100%">
	<colgroup><col style="width: 35%"><col style="width: 35%"><col style="width: auto"></colgroup>
	<thead><tr><th>Nazwa wydania</th><th>Wersja</th><th>Link</th></tr></thead>
	<tbody>
	  <tr>
		<td rowspan="2">Cannon Update</td>
		<td>0.0.1</td>
		<td><a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.1.json">pobierz</a></td>
	  </tr>
	  <tr>
		<td>0.0.1-SNAPSHOT</td>
		<td><a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.1-SNAPSHOT.json">pobierz</a></td>
	  </tr>
	  <tr>
		<td>Zero Update</td>
		<td>0.0.0</td>
		<td><a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.0.json">pobierz</a></td>
	  </tr>
	</tbody>
</table>

Jeśli napotkasz błąd w MinecraftPlus, masz pomysł na ulepszenie lub dodanie nowej funkcjonalności zgłoś to pod <a href="https://bitbucket.org/minecraftplus/minecraftplus/issues" target="_blank">tym linkiem.</a>

# Instalacja klienta MC+

Pobrany plik konfiguracyjny wersji `minecraftplus-x.x.x.json` (lub dla wersji przejściowych `minecraftplus-x.x.x-SNAPSHOT.json`) należy umieścić w folderze o takiej samej nazwie jak plik, bez rozszerzenia `.json`.
Tak przygotowany folder z zawartym w nim plikiem konfiguracyjnym, należy przenieść do folderu wersji `.minecraft/versions/` (najczęściej jest to `%appdata%/.minecraft/versions/`) z którego korzysta używany launcher Minecraft.

# Uruchamianie klienta MC+

Aby uruchomić grę w wersji MinecraftPlus należy w launcherze gry dodać nową wersję. W tym celu należy skonfigurować nową instalację, która wykorzystywać będzie pobraną konfigurację wersji gry.
Należy zwrócić uwagę na rodzaj pobranej konfiguracji - w przypadku gdy nazwa zawiera słowo `SNAPSHOT` jest to wydanie przejściowe i w launcherze należy odblokować używanie wersji przejściowych.

# Uruchamianie Spigot+

Uruchomienie serwera SpigotPlus jest analogiczne jak w przypadku standardowego serwera Spigot.

Aby uruchomić serwer SpigotPlus musisz pobrać gotowy silnik z poniższej listy.  
W przypadku problemu z pobieraniem, kliknij na link PPM i wybierz "Zapisz link jako...".

<table style="table-layout: fixed; width: 100%">
	<colgroup><col style="width: auto"><col style="width: 75pt"><col style="width: 75pt"><col style="width: 25%"><col style="width: 15%"></colgroup>
	<thead>
		<tr><th colspan="3">Kompatybilność</th>	<th rowspan="2">Wersja</th>	<th rowspan="2">Link</th></tr>
		<tr><th>Wydanie</th><th>MC+</th><th>Pluginy</th></tr>
	</thead>
	<tbody>
	  <tr>
		<td>Cannon Update</td>
		<td>???</td>
		<td>1.15.2</td>
		<td>???</td>
		<td><a href="#???">???</a></td>
	  </tr>
	  <tr>
		<td>Zero Update</td>
		<td>0.0.0</td>
		<td>1.15.2</td>
		<td>0.0.0</td>
		<td><a download href="%assets_url%/downloads/spigotplus/spigotplus-0.0.0.jar">pobierz</a></td>
	  </tr>
	</tbody>
</table>

Jeśli napotkasz błąd w SpigotPlus, masz pomysł na ulepszenie lub dodanie nowej funkcjonalności zgłoś to pod <a href="https://bitbucket.org/minecraftplus/spigotplus/issues" target="_blank">tym linkiem.</a>
