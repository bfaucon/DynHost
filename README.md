Source:
http://dev.kprod.net/?q=dns-dynamique-avec-dynhost-ovh

DNS Dynamique avec un DynHost OVH
Contexte
Mise à jour 10/09/2014
Je me suis apercu que parfois l'IP n'était pas correctement mise à jour malgré le fait que le script tourne réguliérement.

Il semble que parfois ipcheck.py renvoie une erreur, qui n'est pas prise en compte. La nouvelle IP est sauvegardée dans le fichier ; au lancement suivant, le script agit comme si l'IP était à jour.

J'ai tenté un moment de tout remplacer par ddclient, mais IMPOSSIBLE de le faire fonctionner sur ma box linux.

J'ai donc revu et corrigé le script en V2 !

FAI et IP dynamique
Récemment, je suis passé de Free ADSL à une offre Numéricable FTTLA.

Pour l'instant, le service est de bonne qualité. Download x20, Upload x10 par rapport à Free. On est encore loin d'une bonne ligne FTTH symétrique, mais on ne va pas se plaindre, au regard de la connexion "moyenne" en France.

Point noir : La partie routeur de la box est vraiment basique de chez basique.

En vrac : On ne peut pas associer de nom à une adresse mac fixe (pas très pratique), le forwarding de port ne permet pas d'avoir un port extérieur différent de l'intérieur (franchement énervant). J'attends sagement de trouver un remplacant à mon WRT54G, quelque peu dépassé par ces débits. En attendant on fait avec.

Autre soucis, objet de cet article : Pas d'IP fixe chez Numéricable (L'option semble exister mais est payante).

Pour bénéficier d'un point  d'accès permanent depuis l'extérieur, il faut donc se rabattre sur une solution type "DynDNS".

Le (double) hic : DynDNS est devenu payant (25$/an), et la box Numéricable ne propose seulement que ce service.

Une solution alternative à DynDNS
La solution alternative : Utiliser un DynHost (compris avec mon domaine enregistré chez OVH) et le mettre à jour depuis une box Linux via un script.

Cette solution est décrite ici http://guides.ovh.com/DynDns par OVH

Avantages :

Moins cher qu'un compte DynDNS (25$ vs 6€ annuel)
Nom de domaine personnalisable
Le nom de domaine peut servir à d'autres usages...
Inconvénients :

Nécessite une box Linux allumée en permanence
Un peu de config et de shell
Pré-requis :

Une box Linux (ou un RasPi..) allumée en permanence
Un domaine OVH, ou équivalent proposant l'option DynHost (6€ / an chez OVH)
Mise en oeuvre

Configuration DynHost OVH

Etape 1
Se connecter à la console OVH (https://www.ovh.com/managerv3)
Sélectionner le domaine concerné (si il y en a plusieurs sur le compte)
puis dans l'onglet de navigation "Domaine & DNS"
puis "Zone DNS"

Etape 2
Créer un Alias "Type DynHOST"
Il permet la création d'un sous domaine dynamique

Etape 3
Entrer un nom de sous-domaine au choix,
l'IP actuelle de votre box,
et cocher "Voulez-vous créer un identifiant DynHOST ?"

Etape 4
Revenir à l'écran "Zone DNS"
Sélectionner "Identifiants DynHOST"
Ces identifiants permettent une mise à jour extérieure de la zone dynamique précédemment créée

Etape 5
Remplir les champs avec :
Un login au choix
Le sous-domaine précédemment créé (Choix dans le select)
Un mot de passe
Ces informations seront à reporter dans le script de mise à jour (section suivante)

Script de mise à jour de l'IP
Le script suivant, appelé à intervalle régulier à l'aide d'une règle cron, permet de vérifier l'adresse IP publique de la box.

Il est basé sur le script proposé par OVH http://www.bozorokus.net/DynHost.tgz et nécessite le script python qui y est également fourni.

A chaque appel, le script vérifie l'adresse IP courante. Si cette dernière est modifiée depuis la dernière occurence, la zone DynHost est modifiée.

J'ai modifié le script fourni par OVH :

Pour obtenir l'adresse IP publique depuis Internet (monip.org) et non depuis l'interface ppp
Pour permettre un meilleur fonctionnement avec cron (chemins complets, plus de log..)

cf: DynHost.sh

Il ne reste qu'a mettre en place une règle cron adéquate, qui lance le script toute les 5 minutes par exemple :
 
> crontab -e
*/5 * * * * /home/YOURUSER/DynHost/dynhost.sh
 
Ouvrir le fichier de log dynhost.log pour vérifier que les appels depuis cron passent.
 
Depuis l'interface OVH, on constatera également les changements d'IP.
Pour éviter d'attendre un changement d'IP de la box internet, forcer une adresse IP fictive dans le script)
 
Version sans vérification de changement d'IP
Ce script permet de forcer la mise à jour de l'IP sans vérifier de vérification au préalable.

Attention à ne pas tomber en abuse.



