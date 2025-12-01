Application capable de gerer une kiosk/boulangerie/microfiance à base de la comptabilité


1. à l'installation on crée un plan comtable
============================================
- pas besoin de preciser si une compte est enfant ou parent d'un autre. on le deduit par numero de compte
ex: 1011 est enfant de 101 enfant de 10,...
- le compte est par defaut inactif
- peut etre lié à une quantité (la on precise le prix unitaire)


2. On crée les menus:
=====================
ex: stock/approvisionnement, stock/produit, vente/client, vente/historique...
- doit preciser les champs
- peut etre (listable/Creable/Validable)

3. Un champ:
============
- peut influencer directement la comptabilité (on aura besoin du debiteur/crediteur/ammortissement,...)
- peut etre lié à un utilisateur (ex: 10111 caisse en BIF de Jean)

4. Operation/historique
=======================
- peut necessiter une validation de l'utilisateur qui subit l'action pour entrer dans le journal
- ne sont supprimable que si ils ne sont pas dejà dans le journal (donc seul les validable)
- jamais modifiable

5. permission
=============
on accorde les permissions par menu
