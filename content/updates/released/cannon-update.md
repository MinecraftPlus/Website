---
Title: Cannon Update
Description: Aktualizacja dodająca do gry działa i kule armatnie, pozwalające na ostrzał artyleryjski
Author: Wituch
Date:

Template: page-update

Dependencies:
    - id: Block Mechanics Update
      desc: Poprzez zmianę systemu niszczenia bloków, w której blok po otrzymaniu obrażeń po trafieniu przez pocisk, niewystarczających do jego zniszczenia, przetrzymuje te informacje (na bloku widać ślad obrażeń, pęknięcia). Jeśli blok otrzyma kolejne obrażenia, zsumują się one z poprzednimi i jeśli przekroczą one wytrzymałość bloku ulegnie on zniszczeniu.
      type: dependent
---

# Cannon Update - krótko o modyfikacji pokazowej
-----

Jest to pierwsza aktualizacja mająca na celu zaprezentować możliwości całego projektu *MinecraftPlus*.

W tej aktualizacji do gry dodane zostały działa armatnie wraz z kulami armatnimi. Wraz z dodaniem dział, zmieniona została natura TNT które zostaje zgaszone po wpadnięciu do wody.

> Z uwagi na to, że w grach multiplayer rywalizacja między grupami jest motorem napędowym dobrej rozgrywki sądzę, że takie rozwiązanie problemu spodoba się wielu graczom.


## Działo armatnie

Działo armatnie dodane w aktualizacji posiada naturę pojazdu jak łódka lub wagonik. Gracz może przejąć kontrolę nad działem poprzez kliknięcie `PPM` na działo. Poruszanie działem jest analogiczne do poruszania się postacią - `lewo/prawo` obraca działo a `przód/tył` pozwala pchać działo do przodu lub ciągnąc do tyłu.

Aby zmienić kąt nachylenia lufy, należy użyć ruchu `przód/tył` z wcisniętym klawiszem `skoku`. Kierunek `przód` powoduje uniesienie lufy w górę, kierunek `tył` opuszczenie w dół.


## Pociski

Aktualizacja dodaje do gry dwa warianty pocisków artyleryjskich - pociski burzące oraz zapalające.

Pociski burzące posiadają dużą siłę przebicia i powodują wybuch, który zadaje sporą ilość obrażeń trafionym blokom.

Pociski zapalające posiadają zdolność zapalania otoczenia w które uderzą. Nie posiadają zdolności przebijających pozwalających na niszczenie silnych fortyfikacji, szczególnie tych niepalnych.


## Moździerze - alternatywa dla dział armatnich

W finalnej wersji aktualizacji dodane zostaną moździerze z pociskami moździerzowymi, jako alternatywa do dział które mają głównie poziomy tor lotu - te pozwoliłyby na ostrzał wroga ukrytego za fortyfikacjami z powietrza. Zarówno pociski moździerzowe tak jak armatnie posiadają dwa warianty warianty - burzące oraz zapalające.


## Zalety modyfikacji
 - zwiększenie realizmu oblężeń
 - kontrola toru lotu przez zmianę kąta lufy lub ilość prochu
 - kontrola uzyskanych efektu ostrzału przez uzycie pocisków burzących lub zapalających
 - możliwość stosowania różnych strategii ostrzału przez zmianę siły strzału lub rodzaj pocisku
 - mobilność maszyn oblężniczych
