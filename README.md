# IoT_Project
L'architecture est composée d'un broker MQTT auquel on peut publier les 3 paramètres:
classification, probabilité et le Timestamp à partir de l’application SONAL.\
Selon ces valeurs, si la probabilité de classification est inférieure à un threshold donné,
c’est qui montre que le model est  incertain de cette classification ou bien si la classe est inconnue, 
alors le client.py retournera au images capturées par la caméra . \
En prenant les 5 dernières images, le programme crée une vidéo ensuite il l'envoi vers le S3 sur à travers le presigned URL.
Afin d'éviter de remplir la mémoire avec des images inutilisables et à cause de contraintes au niveau du hardware, 
nous avons pensé à supprimer les images qui dépassent une minute.

# 2 Versions
Ce repo contient 2 vesions du code:
* Le premier consiste à prendre les image chaque seconde cette version 
nous offre la qualité en envoyant plusieurs une video du durée 4 secondes au lieu d'envoyer une image 
au moment d'une classification faible.
* le deuxieme represente une version économique en prennant seulement une seule image à chaque détection de low classification.

