# Projet 9 Developpez une application Web en utilisant Django


# LITReview

LITReview est une application web développée en utilisant le framework Django, qui permet aux utilisateurs de demander des critiques de livres ou d'articles, de lire des critiques et de publier des critiques. L'application permet également aux utilisateurs de suivre d'autres utilisateurs pour voir leurs critiques et demandes de critiques.

## Fonctionnalités

- S'inscrire et se connecter à l'application.
- Demander des critiques de livres ou d'articles en créant un billet.
- Lire des critiques de livres ou d'articles.
- Publier des critiques de livres ou d'articles.
- Suivre d'autres utilisateurs pour voir leurs critiques et demandes de critiques via une recherche dynamique.
- Répondre aux critiques d'autres utilisateurs.
- Consulter un flux de critiques et de demandes de critiques des utilisateurs suivis.
- Modifier et supprimer ses propres billets et critiques.
  


## Installation

### `Prérequis`

- Python 3.x
- Git

### `Étapes d'installation`

1. Clonez le dépôt Git sur votre machine locale :

    ```bash
    git clone https://github.com/El-GuiGui/Proj9-Developpez-une-application-Web-en-utilisant-Django.git
    cd litrevu
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv env
    ```

    ```bash
    env\Scripts\activate
    ```

3. Installez les dépendances requises :

    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations pour configurer la base de données :

    ```bash
    python manage.py migrate
    ```

5. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

6. Accédez à l'application via votre navigateur à l'adresse suivante : `http://127.0.0.1:8000/`

## Utilisation

### Flux

Le flux affiche les billets et les avis des utilisateurs suivis par l'utilisateur connecté, ainsi que les avis en réponse aux billets de l'utilisateur connecté.

### Abonnements

L'utilisateur peut rechercher d'autres utilisateurs et les suivre pour voir leurs critiques et demandes de critiques. La recherche dynamique vous permet de trouver facilement des utilisateurs en tapant les premières lettres de leur nom d'utilisateur.

### Créer une demande de critique

Cliquez sur "Demander critique" pour créer un nouveau billet demandant une critique sur un livre ou un article.

### Créer une critique

Cliquez sur "Créer une critique" pour publier une nouvelle critique de livre ou d'article.

### Page des Posts

Sur la page des posts, vous pouvez voir toutes vos créations de billets et de critiques. Vous avez également la possibilité de modifier ou de supprimer vos posts.

### Supprimer ses posts

Les utilisateurs peuvent supprimer leurs propres billets et critiques directement depuis la page des posts.



## Accessibilité (WCAG)

L'application a été développée en tenant compte des normes WCAG pour garantir une accessibilité optimale :

- Tous les éléments d'image ont un attribut alt descriptif.
- Les contrastes de couleurs respectent les normes pour une lisibilité optimale.
- Les éléments interactifs ont des indicateurs de focus clairs pour la navigation au clavier.
- Les liens et éléments cliquables ont des titres explicites.

## Sécurité

- Accès sécurisé avec authentification et autorisation.
- Les utilisateurs non connectés ne peuvent accéder qu'aux pages de connexion et d'inscription.
- Les mots de passe des utilisateurs sont hachés dans la base de données.
- Seul l'auteur d'un post peut modifier ou supprimer ses propres posts.
- Les utilisateurs sont responsables de leurs propres publications.

## Structure du projet Django

- `authentification` : Gère l'inscription et la connexion des utilisateurs.
- `reviews` : Gère la création, la modification et la suppression des critiques.
- `tickets` : Gère la création, la modification et la suppression des demandes de critiques.
- `feeds` : Gère l'affichage du flux et des posts des utilisateurs suivis.
- `subscriptions` : Gère les abonnements aux utilisateurs.

## Informations supplémentaires

### Comptes d'utilisateurs de test

Voici quelques comptes utilisateur pour tester l'application :

- **Utilisateurs standards :**
  - Nom d'utilisateur : `EmmaT21`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `LucasM34`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `ChloeB56`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `AntoineL78`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `SophieN90`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `LeoP12`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `JulietteK23`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `MaximeQ45`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `ClaraS67`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `PaulV89`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `LeaD32`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `ThomasJ54`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `CamilleE76`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `VictorG98`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `AliceF20`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `NathanK11`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `EvaL92`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `LouisP43`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `ManonQ65`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `HugoR77`
  - Mot de passe : `123456`
  - Nom d'utilisateur : `SarahS89`
  - Mot de passe : `123456`

### Compte administrateur

- **admin** (Superutilisateur) via http://127.0.0.1:8000/admin/ 
  - Nom d'utilisateur : admin
  - Mot de passe : litrevu

### Index API

- `/admin/` : Accès à l'interface d'administration de Django.
- `/authentification/login.html` : Page de connexion.
- `/authentification/signup.html` : Page d'inscription.
- `/tickets/create_ticket.html` : Créer un nouveau ticket.
- `/tickets/edit_ticket.html/<int:ticket_id>/` : Modifier un ticket existant.
- `/reviews/create_review.html` : Créer une nouvelle critique.
- `/modify_review/<int:id>/` : Modifier une critique existante.
- `/create_reponse_review/<int:ticket_id>/` : Créer une critique en réponse à un ticket.
- `/subscriptions/subscribe.html` : Page pour gérer les abonnements.
- `/feeds/posts.html` : Voir ses propres posts.
- `/delete_ticket/<int:ticket_id>/` : Supprimer un ticket.
- `/delete_review/<int:review_id>/` : Supprimer une critique.
- `/feeds/flux.html` : Voir le flux d'activités.
- `/logout/` : Se déconnecter.

