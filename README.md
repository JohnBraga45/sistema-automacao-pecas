# 🏭 Sistema de Automação Digital – Gestão de Peças

## 📌 Descrição do Projeto
Este projeto consiste em um sistema de automação digital desenvolvido em Python, com o objetivo de simular o controle de produção, inspeção de qualidade e armazenamento de peças em uma linha de montagem industrial.

O sistema avalia automaticamente se cada peça está aprovada ou reprovada de acordo com critérios de qualidade pré-definidos e organiza as peças aprovadas em caixas com capacidade limitada.

---

## 🎯 Objetivo
Automatizar o processo de inspeção e organização de peças industriais, reduzindo falhas humanas, aumentando a eficiência do controle de qualidade e facilitando a geração de relatórios.

---

## ⚙️ Funcionalidades
- Cadastro de novas peças
- Avaliação automática de qualidade
- Separação entre peças aprovadas e reprovadas
- Registro do motivo da reprovação
- Armazenamento automático em caixas (10 peças por caixa)
- Remoção de peças cadastradas
- Geração de relatório final consolidado
- Execução em modo interativo ou simulação automática

---

## 🧪 Critérios de Qualidade
Uma peça será considerada **APROVADA** se atender a todos os critérios abaixo:

- **Peso:** entre 95g e 105g  
- **Cor:** azul ou verde  
- **Comprimento:** entre 10cm e 20cm  

Caso contrário, a peça será **REPROVADA**, com o motivo registrado.

---

## ▶️ Como Executar o Projeto

### 📋 Pré-requisitos
- Python 3 instalado

### 🚀 Passo a passo
1. Clone o repositório:
```bash
git clone https://github.com/JohnBraga45/sistema-automacao-pecas.git


cd seu-repositorio

python main.py

```
 🖥️ Menu do Sistema

Ao executar o programa, o seguinte menu será exibido:
```
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
```
📥 Exemplo de Entrada

ID da peça: P1

Peso (g): 100

Cor: azul

Comprimento (cm): 15

```
📤 Exemplo de Saída
Peça APROVADA e armazenada em caixa.
```
📊 Relatório Final

O sistema gera automaticamente um relatório contendo:

Total de peças aprovadas

Total de peças reprovadas

Motivos das reprovações

Quantidade de caixas utilizadas
```

🧠 Tecnologias Utilizadas

Python 3

Conceitos de Algoritmos e Lógica de Programação

Estruturas de decisão e repetição

Funções, listas e dicionários

🔮 Possíveis Melhorias Futuras

Integração com sensores industriais

Uso de visão computacional para inspeção automática

Armazenamento em banco de dados

Interface gráfica ou aplicação web

Integração com sistemas ERP/MES
