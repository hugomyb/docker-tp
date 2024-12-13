# Docker Multi-Service Application

## Description

Ce projet implémente une stack multi-services avec **Docker Compose** et **Docker Swarm**. Il inclut :
- Une application backend **Flask**.
- Un reverse proxy **Nginx**.
- Une base de données **PostgreSQL**.
- Une interface d'administration **Portainer** pour gérer les conteneurs.

---

## Prérequis

Avoir installé les outils suivants :
- [Docker](https://www.docker.com/) version 20.10 ou supérieure
- [Docker Compose](https://docs.docker.com/compose/) version 1.29 ou supérieure
- Un environnement **Docker Swarm** initialisé (pour tester sur plusieurs nœuds).
- Un accès à un cluster Docker Swarm, ou alors il est possible de tester localement avec un seul nœud en exécutant `docker swarm init`.

---

## Instructions d'Installation

1. Cloner le projet :
   ```bash
   git clone https://github.com/hugomyb/docker-tp.git
   cd docker-tp
    ```
   
2. Créer les secrets nécessaires pour PostgreSQL :
    ```bash
    echo "password" | docker secret create pg_password -
    echo "user" | docker secret create pg_user -
    echo "mydatabase" | docker secret create pg_db -
    ```
   
## Démarrage du projet

1. Initialiser Docker Swarm :
    ```bash
    docker swarm init
    ```
   
2. Déployer la stack avec Docker Compose :
    ```bash
    docker stack deploy -c docker-compose.yml app_stack
    ```
   
3. Vérifier que les services sont en fonctionnement :
    ```bash
    docker service ls
    ```
   
## Structure du Projet

- Dockerfile : Construction de l'image Flask avec Gunicorn.
- docker-compose.yml : Définition des services pour la stack.
- nginx.conf : Configuration de Nginx pour rediriger les requêtes vers Flask.
- flask-app/ : Application Flask.

## Exécution des Services Docker Swarm

Pour redéployer ou mettre à jour la stack :
```bash
docker stack deploy -c docker-compose.yml app_stack
```

## Services Déployés

- Flask : Backend accessible via le reverse proxy.
- Nginx : Reverse proxy redirigeant les requêtes HTTP vers Flask.
- PostgreSQL : Base de données persistante.
- Portainer : Interface de gestion des conteneurs, accessible sur http://localhost:9000.

## Accès à Portainer

Accéder à l'interface Portainer pour visualiser et gérer les services :

- URL : http://localhost:9000
- Ajouter l'environnement local pour gérer Docker.

Tests

Vérifier l'état de santé des services :

## Tests

1. **Healthcheck Flask :** Vérifier l'état de santé du service Flask avec la commande suivante :
```bash
docker service logs app_stack_flask
```
2. Vérifier Nginx en accédant à http://localhost.

## Contributeurs

- Hugo Mayonobe
- Gabriel Boig