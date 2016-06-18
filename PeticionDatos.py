from firebase import firebase
firebase = firebase.FirebaseApplication('https://electrofactura.firebaseio.com/', None)
result = firebase.get('/0/Emisor/0/CP', None)
print (result)
