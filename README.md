# POSTAGEM COM TWEEPY
🚀ESTE BOT SERVE PARA AUTOMATIZAR POSTAGENS NO TWITTER.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
Este bot serve para automatizar postagens no Twitter. Ele é fácil de configurar e usar, lendo as credenciais de um arquivo `.env` e o texto do tweet de um arquivo `MENSAGEM.json`.

## FUNCIONALIDADES:
1. **Autenticação Automática**: O bot autentica automaticamente com a API do Twitter usando credenciais armazenadas de forma segura.
2. **Postagem Automatizada**: Lê o texto de um tweet de um arquivo JSON e faz a postagem automaticamente no Twitter.
3. **Atualização Fácil de Mensagem**: Permite alterar a mensagem do tweet facilmente editando um arquivo JSON, sem precisar modificar o código do bot.

## EXECUTANDO O PROJETO:
1. **Autenticação como Desenvolvedor:**
   - Acesse o [Twitter Developer Portal](https://developer.twitter.com/) e inscreva-se para uma conta de desenvolvedor.
   - Crie um novo projeto e, dentro deste projeto, crie um novo aplicativo. O Twitter fornecerá as chaves e tokens de acesso necessários: API Key, API Key Secret, Bearer Token, Access Token, e Access Token Secret.
   - Edite o arquivo `./CODIGO/.env` com suas credenciais:
     ```plaintext
      API_KEY=Sua_API_Key
      API_KEY_SECRET=Sua_API_Key_Secret
      BEARER_TOKEN=Seu_Bearer_Token
      ACCESS_TOKEN=Seu_Access_Token
      ACCESS_TOKEN_SECRET=Seu_Access_Token_Secret
     ```

2. **Instalando as dependências:**
   - Antes de executar o bot, certifique-se de instalar todas as dependências necessárias. No terminal, execute o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt` em `CODIGO`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Editando o `MENSAGEM.json`:**
   - A sintaxe correta para o arquivo `./CODIGO/MENSAGEM.json` deve ser:

   ```json
   {
      "tweet_text": "Olá Twitter22!"
   }
   ```

   - Certifique-se de que o arquivo esteja formatado corretamente como JSON.
   - Substitua `"Olá Twitter22!"` pelo texto que deseja que o bot publique no Twitter.

   Exemplo:

   ```json
   {
      "tweet_text": "Este é um tweet automatizado usando tweepy e Python! 🚀"
   }
   ```

   Depois de salvar o arquivo, o bot usará o texto especificado em `tweet_text` para criar o tweet.

4. **Inicie o Bot:**
   - Execute o bot iniciando-o com o seguinte comando:
    ```bash
    python CODIGO.py
    ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias relacionadas, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE TWEEPY](https://github.com/VILHALVA/CURSO-DE-TWEEPY)
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE JSON](https://github.com/VILHALVA/CURSO-DE-JSON)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)

