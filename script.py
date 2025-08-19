import qrcode

data=input("Enter the text or URL: ").strip() #strip sert a supprimer les espaces au debut et a la fin d'une chaine de caracteres






filename=input('Enter the filename: ').strip()# le fichier dans lequel le qr code sera enregistré










qr=qrcode.QRCode(box_size=10,border=4)
"""Tu crées un objet QRCode :

box_size=10 → chaque petit carré du QR code aura une taille de 10 pixels

border=4 → il y aura une bordure blanche de 4 carrés autour du QR code"""









qr.add_data(data)#Tu ajoutes les données (texte ou URL) que l’utilisateur a tapées dans le QR code


image=qr.make_image(fill_color='black',back_color="white")
"""génères l’image du QR code :

fill_color='black' → la couleur des carrés du QR code sera noire.

back_color='white' → le fond sera blanc"""


image.save(filename)#Tu sauvegardes l’image générée dans le fichier que l’utilisateur a choisi


print(f'QR code saved as {filename}')#confirmer que le qr code a bien été enregistré

