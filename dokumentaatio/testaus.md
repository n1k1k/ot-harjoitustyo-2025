# Testausdokumentti

## Yksikkö- ja integraatiotestaus

Sovellusta on yksikkö- ja integraatiotestattu automatisoidusti unittest-kirjaston avulla.

<br/>

TestExpenseService -luokka testaa sovelluslogiikasta vastaavaa ExpenseService -luokkaa. TextExpenseService -luokalle injektoidaan instanssit ExpenseRepository ja UserRepository -luokista.

Tiedon pysyväistallennuksesta vastaavia ExpenseRepository ja UserRepository - luokkia testataan TestExpenseService ja TestUserRepository -luokilla. Testauksessa on käytössä eri tiedosto, kuin sovelluksen käytössä on muuton. Testaustiedostojen nimet on konfiguroitu .env.test tiedostoon seuraavast:

```
DATABASE_FILENAME=database_test.sqlite
EXPENSES_FILENAME=expenses_test.csv

```

### Testien haarautumakattavuus 

Testien haarautumakattavuus on 86%. Haarautumakattavuuden ulkopuolelle on jätetty käyttöliittymä. 

![](./images/testcoverage.png)

## Järjestelmätestaus

Sovellusta on testattu järjestelmätasolla manuaalisesti.

### Toiminnallisuus

Kaikki sovelluksen ominaisuudet, jotka on listattu käyttöohjeessa ja vaatimusmäärittely-dokumentissa on testattu manuaalisesti. Toiminnallisuuksien testauksen yhteydessä on myös kokeiltu syöttää virheellisiä arvoja tai jättää syötekentät tyhjiksi virheiden käsittelyn varmistamiseksi.