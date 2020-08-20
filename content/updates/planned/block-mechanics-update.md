---
Title: Block Mechanics Update
Description: Aktualizacja zmieniająca sposób niszczenia bloków
Author: Wituch
Date:

Template: page-update

Dependencies:
    - id: Character Update
      desc: Poprzez wpływ statystk postaci (np. siły) na ilośc zadawanych "obrażen" - analogicznie silniejsza postać gracza uderza z większą siłą
      type: dependent
    - id: Cannon Update
      desc: Poprzez możliwość kumulowania obrażeń zadawanych przez kule armatnie
      type: extension
---

# Block Mechanics Update - nowe zasady
-----

Aktualizacja wprowadzić ma całkowicie nowe spojrzenie na funkcjonowanie bloków w grze - każdy z bloków będzie w stanie przechowywać informacje o otrzymanych obrażeniach.

W oryginalnej wersji, każdy blok który jest możliwy do wydobycia posiada odpowiednią "twardość" definiującą czas który potrzebny jest do wydobycia bloku narzędziem wykonanym z konkretnego materiału.  Przykładowo dla dowolnego bloku drewna jego ścięcie przy pomocy żelaznej siekierki trwa 0,5s (wg. Minecraft Wiki).  
Sprawa wygląda zupełnie inaczej w przypadku twardszych bloków np. obsydianu którego wydobycie przy użyciu diamentowej siekierki trwa 9,4s. Jeśli w trakcie wydobywania obsydianu przerwiemy kopanie, cały postęp przepada...

> Co jeśliby sprawić, by wydobycie konkretnych bloków wymagało zadania odpowiedniej ilości "obrażeń" powodujących jego wydobycie?

Każdy blok posiadać będzie określoną wytrzymałość (maksymalne "HP" bloku). Wraz z otrzymywaniem obrażeń i obniżaniem poziomu "HP" na bloku pojawią się postępujące ślady zniszczenia (tak jak w oryginalnym wydaniu, podczas kopania). Gdy poziom "HP" bloku spadnie do 0 lub mniej, zostanie on zależnie od źródła obrażeń, wydobyty (np. siekierą, kilofem) lub zniszczony (np. przez wybuch).

W przypadku używania narzędzi do wydobywania bloków (co dotyczy wszystkich bloków, nie tylko surowców) każde użycie (ruch) narzędziem powoduje jego stopniowe żużywanie.


## Zalety modyfikacji
 - większy realizm wydobycia (każdy ruch narzędzia wykonuje konkretną pracę, bez bezsensowanego machania)
 - możliwość łatwego skalowania zdolności wydobywania poprzez statystyki postaci np. siłę
 - możliwość współpracy kilku graczy przy wydobywaniu tego samego bloku
 - synergia z modyfikacją [Cannon-Update](?updates/cannon-update) pozwalającą tworzyć mocne fortyfikacje (wymagające kilku trafień do przebicia) , ale nie niezniszczalne!
 - możliwość zaimplementowania erozji z biegiem czasu nadniszczonych powyżej określonego limitu bloków np. cegieł w fortyfikacjach jak i "samogojenie" np. bloków piasku 
