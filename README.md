# Zadatak 10

Implementirati na programskom jeziku Python algoritam za indeksirano pretraživanje stringova u zatadom tekstu koristeći Burrows-Wheeler transformaciju i FM index. Inicijalna verzija algoritma treba da bude realizovana na tradicionalan način opisan na predavanju, bez optimizicije memorije i vremena izvršavanja (10 poena).

Za svaku od funkcija u kodu, kao i za sam finalni algoritam napisati testove (5 poena).

Izvršiti optimizaciju koda iz aspekta zauzeća memorije i vremena izvršavanja. Pokrenuti prethodno definisane testove i proveriti da li i dalje svi prolaze (regresiono testiranje). Izmeriti unapređenje zauzeća memorije i vremena izvršavanja koristeći kao test podatke 3 seta (10 poena):

Coffea arabica, Chromosome 1c i paterni: ATGCATG, TCTCTCTA, TTCACTACTCTCA

Mus pahari chromosome X, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA

Genom po slobodnom izboru iz NIH baze i proizvoljna 3 paterna različite dužine.

Pripremiti prezentaciju (Google slides ili power point) inicijalnog i optimizovanog algoritma, kao i samih rezultata (5 poena).

Pripremiti video prezentaciju projekta (3 - 5 minuta trajanja) koja će biti dostupna na YouTube ili drugom on-line video servisu (10 poena).

## Kreiranje sufiksnog niza i bwt fajla

Kreiranje sufiksnog niza i bwt fajla vrsi se pomocu *SAIS* biblioteke. Egzekutabilan fajl se pokrece preko komandne linije gde su parametri puna putanja do *.fa* fajla, a zatim proizvoljna imena za fajlove koji ce sadrzati sufiksni niz i bwt.
```
main.exe /full/path/to/fa/file [OUTPUT_FILE_SA] [OUTPUT_FILE_BWT]
```

## Pretrazivanje paterna

Pokretanjem skripte `main.py` pokrece se izvrsavanje programa. Korisnik preko terminala unosi punu putanju do *.fa* fajla, bira tip algoritma (standardni ili optimizovan). Nakon toga unosi pune putanje do *bwt* i *sa* fajlova. Ukoliko je korisnik odabrao optimizovani tip algoritma potrebno je da unese i parametre optimizacije *sa factor* i *tally factor*. Kao poslednji input od korisnika se ocekuje da unese paterne koji ce se pretrazivati u originalnom stringu razdvojene razmakom.


## Testiranje

Testiranje algoritama pokrece se pomocu skripte `bwt_fm_test.py`. Test skripta zahteva fajlove koji sadrže sufiksni niz za svaki od tekstova koji se testira ("", "ABAABA", "BANANA", "ABRACADABRA") i jedan fajl koji sadrži BWT teksta "ABRACADABRA". Svi neophodni test fajlovi nalaze se u *test* folderu.

## Prezentacija

Video:

Slides:
