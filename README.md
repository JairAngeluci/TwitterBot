# Como criar uma aplicação para o Twitter

Após criar alguns bots para o Twitter, a maioria para complementar piadas entre meus amigos, notei que algumas pessoas tinham interesse em criar algo parecido, mas não faziam ideia de como começar e do quão simples pode ser.

Levando isso em consideração, o bot do gamakkkkk foi anexado como exemplo por ser simples. Este, por sua vez, foi feito na linguagem de programação Python e foi criado com base no paradigma estruturado; recursos e conceitos de fácil entedimento/uso.

## Começando

### Pré-requisitos

* ***Developer account* no Twitter**<br />
Para utilizar a *Application Programming Interface* (API) do Twitter, é necessário solicitar uma conta de desenvolvedor. Para acessar a página de solicitação, [clique aqui](https://developer.twitter.com/en/apply-for-access).
* **Criar uma conta no Twitter para o bot**<br />
Caso você vá utilizar a API para realizar ações além da leitura de dados, você precisará de uma conta que a aplicação possa utilizar.
* **[Tweepy](https://www.tweepy.org/)**<br />
A biblioteca utilizada, você não precisa começar exatamente do zero porque alguém já fez isso. Você pode ler toda a documentação do Tweepy, [clicando aqui](http://docs.tweepy.org/en/latest/), e, se precisar da ajuda de outras pessoas ou quiser compartilhar algo que fez, pode entrar e conversar no [servidor do Discord sobre Tweepy](https://discord.gg/bJvqnhg).
O jeito mais fácil de instalar o Tweepy é pelo comando Bash `pip install tweepy`.
* **[PythonAnywhere](https://pythonanywhere.com/)**<br />
"PythonAnywhere é um ambiente de desenvolvimento integrado (IDE) e serviço de hospedagem web baseado na linguagem de programação Python" ([Wikipédia](https://pt.wikipedia.org/wiki/PythonAnywhere)). Nós utilizaremos o mesmo para hospedar o bot criado, então você deverá criar uma conta neste site.

### Ganhando acesso a API
Para utilizar o bot, será necessário códigos de acesso a API e ao usuário do mesmo. Então, após receber a *developer account* do Twiter, você deverá seguir estes passos:
1. Acessar o [site de desenvolvedores do Twitter](https://developer.twitter.com/);
2. Acessar com sua conta do Twitter;
3. Clicar em "Apps" no menu de usuário;
4. Clicar em "Create an app" e crie uma nova aplicação;
5. Abrir a aplicação, clicar em "Keys and tokens";
6. Copiar a "API key", a "API secret key" e guardar estes códigos.

Você pode ver o passo-a-passo [neste vídeo](https://www.youtube.com/watch?v=LpLYQz_3hA0).

Após ter o código de acesso a aplicação, você deverá coletar o código para acesso ao usuário, você pode conseguir os mesmos com o seguinte trecho de código Python:
```
import tweepy
consumer_key = input("Your Consumer Key: ")
consumer_secret = input("Your Consumer Secret: ")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print("Enter this site to get the verification site: " + auth.get_authorization_url())
verify = input("Verification code: ")
auth.request_token = {
    'oauth_token': auth.request_token['oauth_token'],
    'oauth_token_secret': verify
}
auth.get_access_token(verify)
print(f"acc token: {auth.access_token}")
print(f"acc secret: {auth.access_token_secret}")
```

### Criando a aplicação
Após ter tanto os códigos para acesso a API quanto para acesso ao usuário do bot, você poderá utilizar a seguinte função para autentificação:
```
def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    print("Authenticating...")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print("...Authenticated!")
    return tweepy.API(auth)
```
Em contrapartida, o restante do código dependerá do seu objetivo com a API do Twitter, então você está por sua conta nessa parte, mas não se esqueça de escrever o `import tweepy` no início do seu código!

### Colocando a aplicação para funcionar

Finalmente, o momento mais esperado: fazer funcionar!

Para isso, você vai acessar a sua conta no [PythonAnywhere](https://www.pythonanywhere.com/) e seguir os seguintes passos:
1. Criar novo comando Bash e rodar o comando `pip install tweepy`;
2. Criar novo arquivo *py* e colar seu código OU importar os arquivos do mesmo.
3. Clicar em "Run" e admirar sua criação.

## Dicas

* **Trabalhe com o ID dos usuários**
	* Os usuários podem mudar seus nomes de usuários, mas o ID é permanente, ou seja, se você basear seu código no nome de um usuário, terá que realizar uma manutenção sempre que o mesmo editar seu cadastro;
	* Você pode facilmente verificar o ID de um usuário pelo site [TweeterID.](https://tweeterid.com/)
* **Procure exemplos**<br />
Procure outras aplicações que utilizem os mesmos recursos que você e/ou tenham objetivos parecidos, um bom exemplo é sempre uma ótima fonte de informações.
* **Entre no servidor do Discord do Tweepy**<br />
É provável que alguma já tenha passado pelo mesmo problema que você ou, pelo menos, tenha alguma ideia que possa facilitar sua vida, então é bom ter um lugar onde possa pedir ajuda.
