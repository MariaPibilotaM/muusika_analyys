# Muusikateose automaatne kirjeldamine loomulikus eesti keeles
Bakalaureusetöö raames loodud veebirakendus muusikateoste automaatseks kirjeldamiseks.


## Käivitamine
Lokaalseks käivitamiseks on vaja alla laadida Docker: https://www.docker.com/products/docker-desktop

### Projekti seadistamine
```
yarn install
```

### Projekti kompileerimine
```
yarn serve
```

### Docker konteineri käivitamine:
```
docker build -t nimi .

docker run -p 5000:5000 nimi

```

## Tehnoloogiad
* Vue.js
* Docker
* Flask
* Python

## Autorid
Maria Pibilota Murumaa

Sven Aller - Lõputöö juhendaja
