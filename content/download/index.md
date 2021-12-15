---
Title: Pobieranie
Description: Strona pobierania
Author: Wituch

Template: tmpl/index

Date: 2020-10-10
Order: 3
---

<style>
table {
    width: 100%;
    font-size: 10pt;
}
th, td {
    vertical-align: middle;
}
</style>

Każda wersja MinecraftPlus działa tak samo jak oryginalny Minecraft. Do uruchomienia gry potrzebny jest launcher Minecraft (dowolny, obsługujący oryginalne pliki konfiguracyjne `.json`).

# Pobieranie klienta MC+

Aby uruchomić klienta gry w wydaniu MiecraftPlus musisz pobrać odpowiednią konfigurację wersji z poniższej listy, a następnie ją zainstalować.  
W przypadku problemu z pobieraniem, kliknij na link PPM i wybierz "Zapisz link jako...".

<table>
    <colgroup>
        <col style="width: 35%">
        <col style="width: auto">
        <col style="width: 100pt">
        <col style="width: 70pt">
    </colgroup>
    <thead><tr><th>Nazwa wydania</th><th>Wersja</th><th>Bazowa wersja*</th><th>Link</th></tr></thead>
    <tbody>
      <tr>
        <td rowspan="3">Cannon Update</td>
        <td>0.0.2</td><td rowspan="4">1.15.2</td>
        <td><a download href="%assets_url%/downloads/minecraft/minecraftplus-0.0.2.json">pobierz</a></td>
      </tr>
      <tr>
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
      <tr><td colspan="4">* wersja oryginalnej wersji gry której zawartość jest obecna w danej wersji MC+</td></tr>
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

<table>
    <colgroup>
        <col style="width: auto">
        <col style="width: 100pt">
        <col style="width: 60pt">
        <col style="width: auto">
        <col style="width: auto">
        <col style="width: 70pt">
    </colgroup>
    <thead>
        <tr><th rowspan="2">Wersja</th>    <th colspan="4">Kompatybilność</th>    <th rowspan="2">Link</th></tr>
        <tr><th>Wydanie</th><th>MC+</th><th>API</th><th>Pluginy*</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>0.0.2</td>
        <td rowspan="2" >Cannon Update</td>    <td>0.0.2</td>    <td>0.0.2</td><td rowspan="3" colspan="1">Spigot 1.15.2</td>
        <td><a download href="%assets_url%/downloads/spigotplus/spigotplus-0.0.2.jar">pobierz</a></td>
      </tr>
      <tr>
        <td>0.0.1-SNAPSHOT</td>
        <td>0.0.1</td>    <td>0.0.2-SNAPSHOT</td>
        <td><a download href="%assets_url%/downloads/spigotplus/spigotplus-0.0.1-SNAPSHOT.jar">pobierz</a></td>
      </tr>
      <tr>
        <td>0.0.0</td>
        <td>Zero Update</td><td>0.0.0</td><td>0.0.1</td>
        <td><a download href="%assets_url%/downloads/spigotplus/spigotplus-0.0.0.jar">pobierz</a></td>
      </tr>
      <tr><td colspan="6">* zgodność z pluginami jest zapewniana na poziomie API; pluginy lub ich funkcjonalności wykraczające poza zakres Spigot+API mogą być niekompatybilne z silnikiem Spigot+ ze względu na jego odmienną strukturę względem oryginalnego silnika Spigot.</td></tr>
    </tbody>
</table>

Jeśli napotkasz błąd w SpigotPlus, masz pomysł na ulepszenie lub dodanie nowej funkcjonalności zgłoś to pod <a href="https://bitbucket.org/minecraftplus/spigotplus/issues" target="_blank">tym linkiem.</a>

# Spigot+ API

API pozwalające na integrację pluginów z nowościami wniesionymi przez aktualizacje zostanie udostępnione w najbliższym czasie, gdy repozytorium projektu zostanie przeniesione do publicznego dostępu.  
Jeśli potrzebujesz dostępu do API już teraz, skontaktuj się z nami na naszym discordzie.
