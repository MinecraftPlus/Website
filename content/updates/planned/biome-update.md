---
Title: Biome Update
Description: Aktualizacja regulująca występowanie surowców, roślin oraz zwierząt na mapie w zależności od biomu
Author: Wituch
Date:

Template: page-update

Dependencies:
    - id: Dep Update
      desc: desc of dependency
      type: dependent
    - id: Character Update
      desc: Poprzez wpływ biomu na obszarze w którym znajduje się postać gracza np. drastyczny spadek temperatury ciała w biomach zimnych, śnieżnych
      type: extension
    - id: Animal Update
      desc: Poprzez lepszą regulację występowania w różnych obszarach mapy, zależnie od biomu
      type: extension
---

# Biome Update - różnicowanie obszarów mapy
-----

W oryginalnym wydaniu gry, zróżnicowanie między obszarami zależnie od biomu jaki na nich występuje jest zauważalne choćby w tak podstawowych przypadkach jakim jest piasek. Na biomie pustynnym znajdzie się go wszędzie w olbrzymich ilościach, a na biomie nizinnym, w niewielkich ilościach, głównie nieopodal zbiorników wodnych. Innym przykładem jest szmaragd, którego występowanie ogranicza się do biomów górskich.  
W przypadku innych surowców jakim jest węgiel nie wygląda to już tak samo. Węgiel w grze jest najczęściej spotykanym złożem w grze i można go znaleźć praktycznie w każdym miejscu na mapie. Taka sytuacja powoduje niską wartość tego surowca, co niekoniecznie jest uzasadnione z punktu widzenia przydatności.

> Odpowiednie zróżnicowanie dostępności towarów zależnie od regionu mapy zwiększy znaczenie kontroli terytorialnej, co przekłada się na dostęp do odpowiednich towarów.

Sytuacja ma się podobnie w przypadku roślinności oraz zwierząt. Co prawda naturalne występowanie w wielu przypadkach jest ograniczane (np. bambus tylko przy zbiornikach wodnych, niedźwiedzie polarne tylko w biomach zimowych) ale nie ma ograniczeń jeśli chodzi o ich transport w inne miejsce. W każdym momencie możemy zebrać znaleziony bambus i zasadzić go w innym biomie. Tak samo z zwierzętami - po znalezieniu upragnionej parki krów, można je hodować na pustyni.

Modyfikacja ma na celu regulację ww. wymienionych oraz innych przypadków. Regulacja ma polegać na przydzieleniu do biomów odpowiednich bloków surowców oraz stworzeń, dopasowaniu ich ilości (rzadkości występowania) oraz warunków występowania (np. zakresy wysokości w chunku dla bloków). W przypadku zwierząt regulacji ulegnie zdolność przeżycia w danym biomie (np. niedźwiedź polarny nie przeżyje na pustyni) lub funkcjonowania w danym biomie (np. krowa nie będzie rodzić młodych cieląt na pustyni).

## Zalety modyfikacji
 - zróżnicowanie terenów pod względem atrakcyjności i przydatności
 - kontrola terytorialna nabiera znaczenia w przypadku zabezpieczania źródeł surowców
