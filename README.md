# rakendus

## Docker install
To run the project locally, Docker desktop is required: https://www.docker.com/products/docker-desktop

### To run the container:
```
docker build -t nameForEnv .

docker run -p 5000:5000 nameForEnv

```

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
