# 🎮 Hangman — Jogo da Forca

## 🎯 Objetivo

Desenvolver uma versão do clássico jogo da Forca em Python, praticando manipulação de strings, controle de fluxo e interação com o usuário.

## 📝 Descrição

O jogador deve adivinhar uma palavra letra a letra antes de esgotar suas tentativas. A palavra é escolhida aleatoriamente a partir de uma lista interna.

## 🎯 Objetivos de Aprendizagem

- Trabalhar com strings e listas em Python
- Usar laços (`for`/`while`) e condicionais para controlar o fluxo do jogo
- Ler e validar entrada do usuário
- Gerenciar estado do jogo (letras já chutadas, tentativas restantes)

## 📋 Pré-requisitos

- Python 3 instalado
- Conhecimentos básicos de programação em Python

## 🗂️ Arquivos fornecidos

- `starter-code.py` — esqueleto com funções iniciais para facilitar a implementação

## 🛠️ Tarefas

### 1) Implementar o jogo básico (obrigatório)

Descrição

Implemente o jogo da Forca com todas as funcionalidades mínimas listadas abaixo.

Requisitos

- Selecionar aleatoriamente uma palavra a partir de uma lista interna
- Exibir o progresso atual da palavra (ex.: `a _ _ l e`)
- Aceitar palpites de letras do usuário
- Evitar palpitar a mesma letra mais de uma vez
- Controlar e exibir as tentativas restantes
- Mostrar mensagem de vitória ou derrota ao final

### 2) Melhorias opcionais (bônus)

- Carregar palavras a partir de um arquivo `words.txt`
- Mostrar uma dica/definição curta para cada palavra
- Implementar um modo para duas pessoas
- Melhorar a interface de linha de comando (cores, limpeza da tela)

## ▶️ Como executar

No terminal, dentro da pasta `assignments/games-in-python`, execute:

```bash
python3 starter-code.py
```

Se o seu ambiente usa `python` apontando para o Python 3, também pode usar `python starter-code.py`.

## 📦 Como submeter

- Faça commit das suas alterações no diretório `assignments/games-in-python` e crie um Pull Request.
- Em alternativa, compacte a pasta `games-in-python` em `.zip` e envie conforme instruções do instrutor.

## ⏱️ Dificuldade e estimativa de tempo

- Dificuldade: Fácil → Intermediária
- Tempo estimado: 1–3 horas

## 📚 Recursos úteis

- Documentação Python: https://docs.python.org/3/
- Tutoriais sobre manipulação de strings e listas

---

Se quiser, posso:

- adicionar um arquivo `words.txt` com uma lista de palavras
- incluir exemplos de entrada/saída ou testes automatizados

Diga qual melhoria prefere que eu implemente em seguida.

# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## � What You'll Build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:
- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages
