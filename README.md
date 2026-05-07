#  Pipeline de Données IoT pour la Chaîne du Froid (Vaccins)

Ce projet propose une solution technologique innovante pour répondre aux défis critiques de la logistique pharmaceutique, en alliant l'automatisation industrielle (IIoT) et la puissance du Cloud AWS.

<details>
  <summary><b>Click to view detailed Architecture Diagram</b></summary>
  <br>
  <img src="Architecture.png" width="100%">
</details>

## Problématique : Le Risque Thermique
Dans l'industrie pharmaceutique, la **chaîne du froid** est vitale. Une simple variation de température non détectée peut rendre des lots entiers de vaccins inutilisables, entraînant :
* **Pertes financières** massives.
* **Risques sanitaires** majeurs pour les patients.
* **Non-conformité** aux réglementations strictes (comme celles de la FDA ou de l'EMA).

---

##  La Solution : Surveillance Intelligente & Cloud
Pour résoudre ce problème, j'ai conçu une architecture intégrée qui garantit une visibilité totale et une optimisation des coûts :

1.  **Collecte en Temps Réel (IIoT) :** Utilisation des protocoles **OPC UA** et **OpenPLC** pour extraire les données de température directement des capteurs industriels.
2.  **Infrastructure Scalable (AWS) :** Déploiement automatisé via **Terraform** pour créer un pipeline de données sécurisé (Kinesis Firehose, S3).
3.  **Gouvernance Financière (FinOps) :** Intégration d'un script d'optimisation pour s'assurer que l'infrastructure cloud reste rentable et sans gaspillage.

---

##  Technologies Utilisées
* **Cloud :** AWS (EC2, S3, Firehose, IAM).
* **Infrastructure as Code :** Terraform.
* **Programmation :** Python (Boto3) pour l'automatisation.
* **Industriel :** OpenPLC, OPC UA.

---

## Optimisation FinOps (Le Plus de ce Projet)
Le fichier `finops_optimizer.py` permet de :
* Détecter automatiquement les instances EC2 arrêtées ou inutilisées depuis plus de 7 jours.
* Réduire les coûts opérationnels en recommandant la suppression ou l'archivage des ressources inutiles.
* Assurer une gestion proactive du budget Cloud, une compétence clé pour les entreprises modernes.
