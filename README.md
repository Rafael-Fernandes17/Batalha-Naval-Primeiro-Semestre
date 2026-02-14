# ⚓ Batalha Naval - Terminal Edition

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![Library](https://img.shields.io/badge/library-termcolor-red)
![Library](https://img.shields.io/badge/library-emoji-green)

## 📝 Sobre o Projeto
Este é um simulador de **Batalha Naval** desenvolvido em Python para rodar diretamente no terminal. O jogo coloca o jogador contra o computador em um tabuleiro de 5x10, exigindo estratégia para posicionar sua frota e precisão para afundar a do adversário.

O projeto demonstra o uso de **matrizes (listas bidimensionais)**, manipulação de bibliotecas externas e tratamento de entradas de dados para evitar falhas durante a execução.

## ✨ Funcionalidades
- **Posicionamento de Frota:** O jogador escolhe onde posicionar suas 5 embarcações.
- **Inteligência Artificial:** O computador realiza jogadas aleatórias e possui seu próprio tabuleiro secreto.
- **Feedback Visual Dinâmico:** Uso de emojis e cores via `termcolor` para representar diferentes estados:
  - 🟦 **Água:** Área ainda não explorada.
  - 🚢 **Embarcação:** Suas unidades posicionadas.
  - 💦 **Tiro na Água:** Quando o disparo erra o alvo.
  - 💥 **Explosão:** Quando uma embarcação é atingida.
- **Validação de Dados:** Sistema que impede jogadas repetidas ou coordenadas fora do limite do tabuleiro.

## 🛠️ Tecnologias Utilizadas
- **Python 3:** Lógica central e estruturas de dados.
- **`termcolor`:** Estilização de cores e atributos de texto (bold, dark).
- **`emoji`:** Renderização de ícones para melhorar a interface (UX).
- **`random`:** Lógica de sorteio para as jogadas da IA.

## 🚀 Como Executar

Certifique-se de ter o Python instalado em sua máquina.

Clone este repositório: https://github.com/Rafael-Fernandes17/Batalha-Naval-Primeiro-Semestre.git

Navegue até a pasta do projeto e execute: python3 batalhaNaval.py

<font color= "red">OBS:</font> Se o seu jogo aparecer um erro como: 

```bash 
import emoji ModuleNotFoundError: No module named 'emoji'
```

Vá até a pasta do projeto e execute esse comando: 
```bash
./run.sh
```

## 👥 Colaboradores

Este projeto foi desenvolvido em conjunto por:

* **Felipe Bresciani** - *Desenvolvedor*
* **Pedro Henrique Junqueira** *Desenvolvedor*
* **Rafael Eliezer** - *Desenvolvedor*

