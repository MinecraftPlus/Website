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
    - id: Interactions Update
      desc: Poprzez zmianę systemu interakcji pozwalającą na wygodniejsze korzystanie i obsługę dział.
      type: dependent
---

# Cannon Update - krótko o modyfikacji pokazowej
-----

Jest to pierwsza aktualizacja mająca na celu zaprezentować możliwości całego projektu *MinecraftPlus*.

W tej aktualizacji do gry dodane zostały działa armatnie wraz z kulami armatnimi. Wraz z dodaniem dział, zmieniona została natura TNT którego czas do wybuchu zostaje skrócony w kontakcie z wybuchem.

> Z uwagi na to, że w grach multiplayer rywalizacja między grupami jest motorem napędowym dobrej rozgrywki sądzę, że takie rozwiązanie problemu spodoba się wielu graczom.



## Działo armatnie

<div style="padding: 10pt 0;">
	<img src="%assets_url%/images/cannon-update_cannon-front.png" style="width: 49%;">
	<img src="%assets_url%/images/cannon-update_cannon-back.png" style="width: 49%;">
</div>

### Crafting działa

<img src="%assets_url%/images/cannon-update_cannon-crafting.png" style="float: right; margin-left: 20pt;">
Receptura pozwalająca craftować działo jest recepturą kształtową.

Aktualnie dostępny jest tylko wariant z dębowymi deskami.
</br>
</br>
</br>


## Pociski

<img src="%assets_url%/images/cannon-update_cannonballs.png" style="float: right; margin-left: 20pt;">
Aktualizacja dodaje do gry dwa warianty pocisków artyleryjskich - pociski burzące oraz zapalające.

Pociski burzące posiadają dużą siłę przebicia i powodują wybuch, który zadaje sporą ilość obrażeń trafionym blokom.  
Pociski zapalające posiadają zdolność zapalania otoczenia w które uderzą. Nie posiadają zdolności przebijających pozwalających na niszczenie silnych fortyfikacji, szczególnie tych niepalnych.

### Crafting pocisku

<img src="%assets_url%/images/cannon-update_cannonball-crafting.png" style="float: right; margin-left: 20pt;">
Receptura pozwalająca craftować kule armatnie również jest recepturą kształtową.

Receptura na zapalającą kulę armatnią jest delikatną wariacją receptury kuli burzącej - nie przedstawiona, do odkrycia dla ciekawskich.



## Obsługa działa

### Poruszanie działem

Działo armatnie dodane w aktualizacji posiada naturę pojazdu jak łódka lub wagonik. Gracz może przejąć kontrolę nad działem poprzez kliknięcie `PPM` na działo.

Poruszanie działem jest analogiczne do poruszania się postacią - `lewo/prawo` obraca działo a `przód/tył` pozwala pchać działo do przodu lub ciągnąc do tyłu.

Aby zmienić kąt nachylenia lufy, należy użyć ruchu `przód/tył` z wciśniętym klawiszem `skoku`. Kierunek `przód` powoduje uniesienie lufy w górę, kierunek `tył` opuszczenie w dół.

<center>
	<video width="80%" controls>
	  <source src="%assets_url%/videos/cannon-update_cannon-steering.mp4" type="video/mp4">
		Your browser does not support the video tag.
	</video>
</center>
</br>

### Ładowanie i odpalanie działa

Podstawowym sposobem na załadowanie działa jest "wrzucenie" pożądanej ilości prochu i kulę armatnią do lufy działa.  
Jako wskaźnik gotowości działa do wystrzału jest lont zapalnika na tylnej części lufy. Gotowość do wystrzału nie wymaga załadowania kuli armatniej!

Aby załadować proch lub kulę do działa, należy stanąć naprzeciw niemu, wycelować w otwór lufy i trzymając w ręku przedmiot do załadowania kliknąć `PPM`.  
Aby oddać strzał, należy stanąć za działem, wycelować w zapalnik i trzymając w ręku pochodnię kliknąć `PPM`.

<center>
	<video width="80%" controls>
	  <source src="%assets_url%/videos/cannon-update_cannon-loading-and-shooting.mp4" type="video/mp4">
		Your browser does not support the video tag.
	</video>
</center>
</br>

### Otwieranie menu działa

Poza metodą ładowania działa poprzez "wrzucenie" przedmiotu do lufy działa, istnieje możliwość otworzenie graficznego menu działa. Menu to pozwala załadować działo poprzez przeniesienie prochu i kuli armatniej w odpowiedni slot.  
Menu to pozwala także na rozładowanie działa poprzez wyciągnięcie kuli - załadowanego prochu nie można już odzyskać.

Aby otowrzyć graficzne menu działa należy kliknąć `PPM` na działo z przytrzymanym klawiszem `skradania` (domyślnie `lewy Shift`).

<center>
	<video width="80%" controls>
	  <source src="%assets_url%/videos/cannon-update_cannon-menu-opening.mp4" type="video/mp4">
		Your browser does not support the video tag.
	</video>
</center>
</br>



## Moździerze - alternatywa dla dział armatnich

W finalnej wersji aktualizacji dodane zostaną moździerze z pociskami moździerzowymi, jako alternatywa do dział które mają głównie poziomy tor lotu - te pozwoliłyby na ostrzał wroga ukrytego za fortyfikacjami z powietrza. Zarówno pociski moździerzowe tak jak armatnie będą posiadać dwa warianty warianty - burzące oraz zapalające.


## Zalety modyfikacji
 - zwiększenie realizmu oblężeń
 - kontrola toru lotu przez zmianę kąta lufy lub ilość prochu
 - kontrola uzyskanych efektu ostrzału przez użycie pocisków burzących lub zapalających
 - możliwość stosowania różnych strategii ostrzału przez zmianę siły strzału lub rodzaj pocisku
 - mobilność maszyn oblężniczych
