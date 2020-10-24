---
Title: O projekcie
Description: MinecraftPlus
Author: Wituch

Template: index

Date: 2020-08-10
---

# Czym jest Minecraft Plus?

**MinecraftPlus** *(Minecraft+, MC+)* jest kompleksowym projektem, którego celem jest stworzenie ulepszonej wersji standardowej gry **Minecraft** studia **Mojang**.

Modyfikacje dokonywane w ramach projektu, obejmują część klienta oraz serwera co pozwala na używanie MC+ do uruchomienia w pełni funkcjonującego serwera, dostępnego dla każdego gracza korzystającego z MC+.

By prawidłowo zrozumieć ideę projektu, należy rozróżnić dwa pojęcia - **modyfikacja do Minecrafta** oraz **zmodyfikowany Minecraft**. Ten projekt, jest tym drugim.

# Dlaczego powstał ten projekt?

MC+ jest wynikiem połączenia sentymentu do gry z pasją i ambicjami skierowanymi na stworzenie czegoś „większego” podsumowującego wszelkie działania związane z Minecraftem.
Można to wszystko uzasadnić chęcią na pozostawienie śladu po swojej aktywności, w tak ogromnej społeczności, jaką tworzą gracze Minecrafta i jednocześnie nie pozwolić by cały poświęcony czas przy serwerach, pluginach, silniku gry i bibliotekach nie został zamknięty w szufladzie i przepadł.

# Dlaczego MC+ skoro w Internecie jest pełno modów na wszystko?

Nie da się zaprzeczyć, że modyfikacje do Minecrafta udostępniane w internecie przez najróżniejszych twórców są często arcydziełami, rozwijającymi grę o najróżniejsze rzeczy. Tak naprawdę, można znaleźć modyfikację na wszystko (no dobra, prawie wszystko).

Jednak nie zanurzając się w plusy takich modyfikacji, a skupiając się na minusach — największymi problemami autonomicznych modyfikacji są:
- ich kompatybilność, co ma ogromne znaczenie przy dużej ilości modyfikacji
- wspieranie danej wersji Minecrafta
- obsługa strony klienta i serwera

Na pewno każdy, kto miał styczność z modowanymi serwerami, doświadczył problemów, jakie potrafią się pojawić przy używaniu popularnych modyfikacji.
Moim subiektywnym zdaniem (możliwe, że się z tym zdaniem zgadzasz) głównym problemem jest ostatecznie natłok zmian, jakie wprowadzają te modyfikacje. Często zdarza się, że istnieje idealny mod z interesującą nas funkcjonalnością — jednak poza tym, zawiera ona więcej funkcjonalności, których nie potrzebujemy.

Właśnie po to powstał ten projekt, by skroić najlepsze zmiany pod konkretne potrzeby, bez zbędnych funkcjonalności, które tylko utrudniają rozgrywkę, szczególnie nowicjuszom.

# Na jakim etapie znajduje się projekt?

Aktualnie projekt znajduje się w **fazie ukończenia wydania pierwszej aktualizacji**.

Pierwsze wykonane kroki przed udostępnieniem projektu publicznie, polegały na skompletowaniu kodu źródłowego wszystkich elementów składowych i połączenie ich w kompletny system.
Pozwoliło to na zbudowanie pierwszego działającego wydania, pozbawionego jakichkolwiek zmian względem oryginalnej wersji gry, opartego na posiadanym kodzie źródłowym. Ułatwiło to testowanie poprawności działania „gołego” MC+, ponieważ zachowywał się on dokładnie tak samo, jak oryginał. Dotychczasowe testy wyłapały kilka błędów, które zostały rozwiązane.  
Następnie zintegrowano zmiany pochodzące z CraftBukkit z podstawową wersją MC+. Pozwoliło to uzyskać działające wydanie, bez żadnych zmian względem oryginalnej wersji gry, z możliwością uruchamiania pluginów opartych o API Bukkit. Seria podstawowych testów pozwoliła kilka z nich wyłapać i rozwiązać.

W celu zaprezentowania nieograniczonych możliwości projektu oraz zebrania feedbacku od społeczności i zbadania zainteresowania, w pierwszej kolejności zdecydowano o udostępnieniu pokazowej modyfikacji [Cannon Update](?updates/released/cannon-update) dodającą do gry działa i kule armatnie. Modyfikacja ma być rozwiązaniem na nieestetyczną realizację „dział” za pomocą TNT.

# Na jakiej wersji bazuje MC+?

Projekt bazuje aktualnie na wersji 1.15.2.
Przed rozpoczęciem prac nad dodawaniem zmian, cały projekt otrzymał odpowiednią strukturę pozwalającą na minimalizację czasu potrzebnego na zintegrowanie zmian z przyszłych, nowszych wersji Minecrafta.

# Jakie oprogramowanie wchodzi w skład projektu?

W skład projektu wchodzi:
- MinecraftPlus-Client - aplikacja klienta gry wraz z modyfikacjami
- MinecraftPlus-Server - aplikacja serwera gry wraz z modyfikacjami
- CraftBukkitPlus-Server* - aplikacja serwera gry wraz z modyfikacjami i API Bukkit** pozwalającym uruchamiać pluginy
- BukkitPlus\*** - API Bukkit uzupełnione o modyfikacje z projektu
- AuthServerLibrary* - biblioteka pozwalająca na autoryzację graczy na serwerze bez pluginów (zamiennik do AuthLib)

\* aktualnie niedostępne, prace nad integracją zmian z aktualizacji [Cannon Update](?updates/released/cannon-update)  
\*\* wariacje projektu oparte na tym API jak Spigot lub Paper są przewidywane w przypadku naprawdę dużego zapotrzebowania  
\*\*\* aktualnie niedostępne z uwagi na prace nad *CraftBukkitPlus*  

# Do kogo skierowany jest projekt?

Z uwagi na charakter modyfikacji, które skupiają się głównie na rozbudowaniu mechanizmów przetrwania, rozszerzeniu dostępnych rud, materiałów, receptur, sposobów wytwarzania, przetwarzania itp. projekt jest skierowany głównie do graczy oraz twórców serwerów, którzy utrzymują rozgrywkę w klimacie **survivalu** (patrz niżej).
Poza uniwersalnymi zmianami, które tak naprawdę pasowałyby do dowolnego typu serwera, projekt nastawiony jest na rozwój funkcjonalności, które od zawsze były bolączką serwerów RPG (patrz niżej).

Jeśli więc lubisz grać lub tworzysz serwer w klimacie survivalu, szczególnie z elementami **RPG** (patrz niżej) to ten projekt jest idealny dla Ciebie!

# Dlaczego ten projekt pasuje do serwerów Survival?

Odpowiedź na to pytanie jest moją subiektywną opinią opartą na wieloletnim doświadczeniu, własnych pomysłach i ambicjach.

Mianowicie, survival serwowany nam przez domyślną wersję gry, jest bardzo uproszczoną wersją prawdziwego survivalu. Chcę tchnąć w grę więcej naturalnych mechanizmów wymagających od gracza większej dbałości o szczegóły, o swoje przetrwanie. Tak, by rozgrywka nie opierała się na bezmyślnym odtwarzaniu wzorów (wykop-przetwórz-posiadaj) a planowaniu kierunku rozgrywki w często wykluczających się kierunkach, by różnicować graczy.
Takie różnicowanie ma wpływać na większą integrację graczy oraz zwiększenie liczby interakcji, z uwagi na znacznie zmniejszoną niezależność graczy. Co nie znaczy, że niemożliwym będzie samodzielne przeżycie — będzie to jednak bardzo wymagające.

Nie sposób jest teraz przedstawić tutaj całość systemu, który ma składać się z serii konkretnych zmian, wzajemnie się uzupełniających. Podam po prostu przykład, który pierwszy przyszedł mi do głowy: choroby i obrażenia wymagające interwencji lekarza (gracza posiadającego odpowiednie umiejętności) i/lub użycie medykamentów (wytworzonych przez gracza posiadającego odpowiednie umiejętności) - które dla postaci ukształtowanej pod walkę wręcz będą śmiertelnym zagrożeniem bez zewnętrznej pomocy. A może do czasu, gdy danej postaci uda się posiąść odpowiednie umiejętności...?

# Dlaczego ten projekt pasuje do serwerów RPG?

Odpowiedź na to pytanie jest moją subiektywną opinią opartą na obserwacjach przeróżnych serwerów, próbujących budować rozgrywkę RPG. Oto co, moim zdaniem najważniejsze.

Żaden serwer RP/RPG nie może obyć się bez możliwości kształtowania swojej postaci i różnicowania jej od innych. Najpopularniejszym rozwiązaniem powszechnie stosowanym przez serwery tego typu są klasy i drzewka umiejętności. Pomimo dobrych pomysłów ich realizacja za pomocą pluginów często pozostawia sporo do życzenia.
Projekt będzie oferował rozwiązanie tego problemu przez natywne wsparcie drzewka umiejętności z możliwością gospodarowania punktami rozwoju, pozwalające na wybranie drogi rozwoju postaci, od której będą zależały możliwości postaci oraz jej mocne i słabe strony.

Kolejnym słabym punktem serwerów RP jest stworzenie odpowiedniego systemu NPC z możliwością interakcji, głównie rozmów i questowania.
Istnieją co prawda odpowiednie pluginy pozwalające realizować opcje dialogowe i wiązanie ich z questami itp. jednak często odbiór wizualny jest utrudniony przez wykorzystanie czatu w grze.
Projekt będzie oferował natywne wsparcie dla interakcji z NPC poprzez odpowiednio przygotowane interfejsy (widoki GUI) odciążając twórców, od technicznych problemów pozwalając skupić się na tworzeniu treści, a nie systemów.

# Jak używać MC+?

Jeśli chcesz uruchomić klienta lub serwer w wydaniu MiecraftPlus, musisz pobrać odpowiedni instalator z sekcji [Pobieranie](?download).
Znajdziesz tam informacje o tym, skąd i jak pobrać odpowiednią konfigurację wersji pozwalającą uruchomić klienta lub serwer MC+.

# Plany na przyszłość:

Kolejnymi krokami zaplanowanymi dla projektu jest:
- zbudowanie zaufanej społeczności zainteresowanej korzystaniem z MC+
- stworzenie instalatora pozwalającego wykorzystywać pliki [delta](https://www.techwalla.com/articles/what-is-a-delta-file) do generowania plików wykonywalnych MC+
- zastąpienie instalatora launcherem automatyzującego instalację MC+
- integracja zaplanowanych modyfikacji.

Lista planowanych modyfikacji jest długa (a zawiera tylko najważniejsze pomysły) niełatwo jest określić konkretny przebieg prac. Dlatego jak wspomniano wcześniej:

> W celu zebrania feedbacku od społeczności i zbadania zainteresowania w pierwszej kolejności udostępniłem pokazową modyfikację [Cannon Update](?updates/released/cannon-update) dodającą do gry działa i kule armatnie. Modyfikacja ma być rozwiązaniem na nieestetyczną realizację „dział” za pomocą TNT.

W skrócie przyszłość tego projektu zależy wyłącznie od jego odbioru przez szersze grono graczy i twórców serwerów Minecraft.

#### Więc jeśli jesteś zainteresowany projektem i chcesz dowiedzieć się więcej, zajrzyj na serwer [Discord](https://discord.gg/qdRMt2m) projektu.