Ohjelmistotekniikka, harjoitustyö - Kevät 2025

# ExpenseTracker

Sovellus mahdollistaa käyttäjälle omien kulujensa seurannan ja hallinnan. Rekisteröityneet käyttäjät voivat tarkastella ja kirjata kuluja ja tehdä niihin muokkauksia.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/n1k1k/ot-harjoitustyo-2025/blob/9e1db73f452c580d0b6135e687d5edce58c4d413/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/n1k1k/ot-harjoitustyo-2025/blob/9e1db73f452c580d0b6135e687d5edce58c4d413/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/n1k1k/ot-harjoitustyo-2025/blob/b29ff84f7de2e688edf4123f19cf08f461a53180/dokumentaatio/changelog.md)

## Asennus
Asenna ensin sovelluksen riippuvuudet komennolla:
 ```bash
 poetry install
 ```
   
Sen jälkeen suorita alustustoimenpiteet komennolla:
 ```bash
 poetry run invoke build
 ```

## Sovelluksen käyttö komentoriviltä ja testaus
Ohjelman voi käynnistää komennolla:
```bash
poetry run invoke start
```

Testit voi suorittaa komennolla:
```bash
poetry run invoke test
```

Testikattavuusraportin saa generoitu komennolla:
```bash
poetry run invoke coverage-report
```
   

## Harjoitustehtävät 

- [Viikko 1](https://github.com/n1k1k/ot-harjoitustyo-2025/tree/main/laskarit/viikko1.md)
- [Viikko 2](https://github.com/n1k1k/ot-harjoitustyo-2025/tree/main/laskarit/viikko2)
- [Viikko 3](https://github.com/n1k1k/ot-harjoitustyo-2025/tree/55a1d42783e6bb7df431962ee193860c5bdc7f2b/laskarit/viikko3)
