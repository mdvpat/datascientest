# datascientest
## projet fraud

L'api tourne sur l'URL suivant : db2m.com

L'endpoint de vérification de la fraude : /verify

## Example requete:

### Transaction non frauduleuse

```
curl -XPOST db2m.com/verify -H "Content-Type: application/json" -d '{"user_id":"22058", "signup_time":"2015-02-24 22:55:49", "purchase_time":"2015-02-24 23:15:11", "purchase_value": "999999999999000000000", "device_id": "QVPSPJUOCKZAR", "source": "piata_centrala", "browser": "Chrome", "sex": "M", "age": "4", "ip_address": "73254878368.8"}'
```
Retour:

```
"{\"0\":{\"purchase_value\":\"999999999999000000000\",\"source\":0,\"browser\":0,\"sex\":0,\"age\":\"4\",\"delta\":0.3227777778,\"is_fraud\":0}}"
```

### Transaction frauduleuse

```
curl -XPOST db2m.com/verify -H "Content-Type: application/json" -d '{"user_id":"22058", "signup_time":"2015-02-24 22:55:49", "purchase_time":"2015-02-24 22:55:50", "purchase_value": "999999999999000000000", "device_id": "QVPSPJUOCKZAR", "source": "piata_centrala", "browser": "Chrome", "sex": "M", "age": "4", "ip_address": "73254878368.8"}'
```
Retour:

```
"{\"0\":{\"purchase_value\":\"999999999999000000000\",\"source\":0,\"browser\":0,\"sex\":0,\"age\":\"4\",\"delta\":0.0002777778,\"is_fraud\":1}}"
```

La variable is_fraud nous indique si la trasaction est frauduleuse, ou pas.
