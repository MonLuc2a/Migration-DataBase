# projet-SQL

Sujet :

Projet SQL - B2 - 2022/2023
Vous avez été contacté(e) par l'équipe Likwright pour migrer l'ancienne base de données vers leur nouveau schéma. 
Vous devez : 
- Créer un script .sql qui créera le nouveau schéma de la base de données 
- Créer un second script qui transférera les données de l'ancienne base de données vers la nouvelle. 

De plus, pour s'assurer que l'équipe peut accéder aux données, ils veulent afficher les requêtes et les résultats pour les éléments suivants : 
- Lister tous les tournois pour un nom de jeu donné 
- Pour un nom de jeu, récupérer le salaire moyen des joueurs 
- Lister tous les tournois par lieu 
- Obtenir le nombre de joueurs par sexe.


ChatGPT: 


Il est important de noter que le processus de migration de bases de données peut être complexe et dépend de nombreux facteurs tels que la structure de l'ancienne base de données, les contraintes de clé étrangère et de données, ainsi que les différences entre les systèmes de gestion de bases de données utilisés pour l'ancienne et la nouvelle base de données.

Voici comment vous pouvez aborder ce projet :

Étudiez le schéma de l'ancienne base de données et comprenez comment les données sont organisées et liées entre elles. Identifiez les tables et les colonnes clés de l'ancienne base de données.

Étudiez le nouveau schéma de base de données fourni par l'équipe Likwright et comprenez comment il diffère de l'ancien schéma. Identifiez les tables et les colonnes clés de la nouvelle base de données.

Écrivez un script SQL qui crée le nouveau schéma de base de données en utilisant les commandes CREATE TABLE et CREATE INDEX. Assurez-vous de définir les contraintes de clé étrangère appropriées pour garantir l'intégrité des données.

Écrivez un second script SQL qui transfère les données de l'ancienne base de données vers la nouvelle en utilisant les commandes INSERT INTO et SELECT. Vous devrez peut-être utiliser des jointures pour combiner les données de plusieurs tables de l'ancienne base de données dans une seule table de la nouvelle base de données.

Écrivez les requêtes SQL demandées pour lister tous les tournois pour un nom de jeu donné, pour récupérer le salaire moyen des joueurs pour un nom de jeu donné, pour lister tous les tournois par lieu et pour obtenir le nombre de joueurs par sexe. Utilisez les commandes SELECT, FROM, WHERE, GROUP BY et HAVING pour construire ces requêtes.

Testez vos scripts et requêtes en utilisant un logiciel de gestion de bases de données pour exécuter votre code et vérifier que les résultats sont corrects.

Je vous recommande également de documenter soigneusement votre travail afin de faciliter la maintenance et la compréhension de votre code par d'autres personnes.


Ce script crée six tables dans une base de données SQL: "place", "tournament", "game", "coach", "player" et "staff".
La table "place" a quatre colonnes: "IdPlace" (une clé primaire auto-incrémentée), "Name", "Address" et "City".
La table "tournament" a cinq colonnes: "IdTournament" (une clé primaire auto-incrémentée), "IdPlace" (une clé étrangère référençant la table "place"), "IdGame" (une clé étrangère référençant la table "game"), "Date" et "Duration".
La table "game" a deux colonnes: "idGame" (une clé primaire auto-incrémentée) et "Name".
La table "coach" a quatre colonnes: "IdCoach" (une clé primaire auto-incrémentée), "IdGame" (une clé étrangère référençant la table "game"), "LicenseDate" et "IdEmployeeData" (une clé étrangère référençant la table "employee_Data").
La table "player" a quatre colonnes: "IdPlayer" (une clé primaire auto-incrémentée), "IdGame" (une clé étrangère référençant la table "game"), "Ranking" et "IdEmployeeData" (une clé étrangère référençant la table "employee_Data").
La table "staff" a deux colonnes: "IdStaff" (une clé primaire auto-incrémentée) et "IdEmployeeData" (une clé étrangère référençant la table "employee_Data").
La table "employee_data" a six colonnes: "IdEmployee" (une clé primaire auto-incrémentée), "LastName", "FirstName", "Gender", "Age" et "Wage".