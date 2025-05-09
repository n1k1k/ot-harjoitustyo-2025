Ohjelmistotekniikka, harjoitustyö - Kevät 2025

# ExpenseTracker

Sovellus mahdollistaa käyttäjälle omien kulujensa seurannan ja hallinnan. Rekisteröityneet käyttäjät voivat tarkastella ja kirjata kuluja ja tehdä niihin muokkauksia.

<br/>

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Testaus](dokumentaatio/testaus.md)

<br/>

## Releases
  - [Loppupalautus](https://github.com/n1k1k/ot-harjoitustyo-2025/releases/tag/loppupalautus)
  - [Viikko 6](https://github.com/n1k1k/ot-harjoitustyo-2025/releases/tag/viikko6)
  - [Viikko 5](https://github.com/n1k1k/ot-harjoitustyo-2025/releases/tag/viikko5)

<br/>

## Asennus

Asenna ensin sovelluksen riippuvuudet komennolla:
 ```bash
 poetry install
 ```
   
Sen jälkeen suorita alustustoimenpiteet komennolla:
 ```bash
 poetry run invoke build
 ```

<br/>

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

Pylint tarkistuksen voi suorittaa komennolla:
```bash
poetry run invoke lint
```

