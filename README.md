# ItConnect

ItConnect est une application web qui permet aux utilisateur de s'inscrire, de se connecter, de creer des post sur differents secteurs de la tech, de consulter
les posts des autres, de les liker, et d'y laisser des commentaires.

## Prerequis 

Sur la machine hote (la machine qui vas heberger et lancer le prtojet, il faut avoir installe :

- `Docker`
- `Git`
- `pnpm`
- `Node.js`

## Demarrage (Getting started)

1. Copier le fichier d'environnement et renseigner les vraies valeurs (notament `JWT_SECRET_KEY`) :

``` bash
	cp .env.example .env
```

2. Construire les images et lancer les 3 services (base de donnees, backend, frontend) :

``` bash
	docker compose up --build
```

3. Verifier que le backend repond, en ouvrant dans le navigateur :

```http://localhost:8000/health```

la route nous renvoie juste {"status: "ok}

La doc interactive de l'API (generee automatiquement par FastAPI la (Swagger UI) a partir du contrat) est disponible sur :

```https://localhost:8000/docs
