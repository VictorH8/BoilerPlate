# 🛠️ **BoilerPlate CLI**

**BoilerPlate** é uma ferramenta de linha de comando escrita em Python, projetada para automatizar a criação de estruturas iniciais de projetos em diversas linguagens e frameworks.

Com o BoilerPlate, você pode iniciar novos projetos rapidamente, sem perder tempo configurando pastas, arquivos e configurações básicas. Basta rodar um comando e voilà! Tudo pronto para você começar a codar.

> **"Comece seus projetos com o pé direito, sem complicação."**

---

## 🎯 **Objetivo do Projeto**

O BoilerPlate visa fornecer uma maneira rápida e fácil de gerar a estrutura básica de um novo projeto, permitindo que você foque no que realmente importa: o código. Ele oferece:

- Templates prontos para diferentes linguagens e frameworks.
- Estruturas de diretórios e arquivos padronizadas.
- Um processo simples de personalização para que você possa começar de forma eficiente.

---

## ⚙️ **Como Funciona**

A ferramenta funciona através de um script CLI (`boilerplate.py`), que gera a estrutura de um novo projeto com base nos parâmetros passados. Você define o nome do projeto e o template (linguagem ou framework) a ser utilizado.

### 💡 **Exemplo de uso:**

1. **Criação de projeto Python básico:**

```bash
boilerplate --name meu-projeto --template python
```

Isso criará um novo diretório chamado `meu-projeto` com a estrutura básica de um projeto Python.

2. **Criação de projeto Flask:**

```bash
boilerplate --name meu-projeto-flask --template flask
```

Isso criará um novo projeto baseado no Flask, com as pastas e arquivos necessários para começar a desenvolver uma aplicação web.

3. **Especificando a licença:**

Você pode também especificar a licença do projeto com a opção `--license`:

```bash
boilerplate --name meu-projeto --template python --license MIT
```

Se você não fornecer uma licença, o padrão será **MIT**.

### 🔧 **Argumentos Disponíveis:**

- `--name`: Nome do diretório/projeto a ser criado.
- `--template`: Define o template a ser utilizado (ex: `python`, `flask`, `javascript`).
- `--license`: Especifica a licença do projeto (opcional, o padrão é **MIT**).
- `--list`: Exibe uma lista dos templates e licenças disponíveis.

---

## 🛠️ **Instalação**

Para instalar e rodar o **BoilerPlate CLI** no seu sistema, siga os passos abaixo:

### 1. **Clone o repositório:**

Primeiro, clone o repositório do BoilerPlate para sua máquina:

```bash
git clone https://github.com/VictorH8/BoilerPlate.git
cd BoilerPlate
```

### 2. **Torne o script `boilerplate.py` executável:**

Dê permissão de execução ao script para poder rodá-lo diretamente do terminal:

```bash
chmod +x boilerplate.py
```

### 3. **Adicione ao seu PATH (opcional):**

Se você quiser rodar o comando `boilerplate` de qualquer lugar no sistema, adicione o diretório do script ao seu PATH. Para isso, crie um link simbólico no diretório `/usr/local/bin` (ou outro diretório já incluído no seu PATH):

```bash
sudo ln -s $(pwd)/boilerplate.py /usr/local/bin/boilerplate
```

Agora você pode rodar o comando `boilerplate` de qualquer lugar no terminal.

---

## 🚧 **Status**

O projeto está em desenvolvimento ativo. Atualmente, os principais recursos já estão implementados:

- Criação de projetos com templates básicos como **Python**, **Flask** e **JavaScript**.
- Suporte para escolha de licenças (com MIT como padrão).
- Estrutura simples e fácil de expandir.

**Próximos passos:**

- Adicionar mais templates de linguagens e frameworks populares.
- Melhorias na personalização da estrutura gerada.

---

## 🤝 **Contribua**

Gostou do projeto e quer contribuir? Aqui estão algumas formas de ajudar:

- Abra uma **issue** para sugerir novos templates, melhorias ou relatar bugs.
- Envie um **pull request** com suas contribuições! Fique à vontade para melhorar o código.

---

## 📝 **Licença**

Este projeto está licenciado sob a **MIT License**. Para mais detalhes, consulte o arquivo `LICENSE`.

---

### 🧑‍💻 **Feito para desenvolvedores que querem começar seus projetos com o pé direito.**