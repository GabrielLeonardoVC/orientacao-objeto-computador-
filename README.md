# 🖥️ Projeto: Computador e Componentes (POO - Composição)

Este projeto demonstra o **conceito de Composição em Programação Orientada a Objetos (POO)** por meio da modelagem de um **Computador** e seus componentes essenciais: **Processador**, **Memória RAM** e **Armazenamento**.

A Composição significa que um objeto é **formado por outros objetos** que não existem independentemente fora do contexto principal.  
Ou seja: se o **Computador** for destruído, seus **componentes deixam de existir**.

---

## 📂 Estrutura do Projeto

📁 projeto_computador
- 📜 classes.py  -  Definição das classes (Processador, MemoriaRAM, Armazenamento, Computador)
- 📜 app.py  -  Script principal para testar o sistema
- 📜 README.md   -  Documentação do projeto

---

## 📌 Classes Implementadas

### 🔹 `Processador`
- Atributos: `modelo`, `velocidade_ghz`
- Métodos: `get_modelo()`, `get_velocidade_ghz()`, `__str__()`

### 🔹 `MemoriaRAM`
- Atributos: `capacidade_gb`, `tipo`
- Métodos: `get_capacidade_gb()`, `get_tipo()`, `__str__()`

### 🔹 `Armazenamento`
- Atributos: `tipo (SSD/HDD)`, `capacidade_gb`
- Métodos: `get_tipo()`, `get_capacidade_gb()`, `__str__()`

### 🔹 `Computador`
- Atributos: `marca`, `modelo`, `Processador`, `MemoriaRAM`, `Armazenamento`
- Métodos:  
  - `get_marca()`, `get_modelo()`  
  - `get_processador()`, `get_memoria_ram()`, `get_armazenamento()`  
  - `ligar()` → exibe informações do computador e de seus componentes  
  - `__str__()` → representação amigável  
  - `__del__()` → mostra que os componentes deixam de existir quando o computador é destruído

---

## ▶️ Exemplo de Uso

### `app.py`

```python
from classes import Computador

# Criando um objeto Computador com seus componentes
meu_pc = Computador(
    "Dell", "XPS 15",
    "Intel Core i7-11800H", 2.3,
    16, "DDR4",
    "SSD", 512
)

# Ligando o computador
meu_pc.ligar()

# Exibindo representação amigável
print(meu_pc)

# Acessando os componentes
print("\nAcessando componentes...\n")
print("Processador:", meu_pc.get_processador().get_modelo(), "-", meu_pc.get_processador().get_velocidade_ghz(), "GHz")
print("Memória RAM:", meu_pc.get_memoria_ram().get_capacidade_gb(), "GB", meu_pc.get_memoria_ram().get_tipo())
print("Armazenamento:", meu_pc.get_armazenamento().get_tipo(), "-", meu_pc.get_armazenamento().get_capacidade_gb(), "GB")

# Destruindo o computador
del meu_pc
📌 Saída Esperada
vbnet
Copiar código
Ligando o computador...
Carregando...
Pronto!

Dell XPS 15...
Processador:Intel Core i7-11800H,Velocidade:2.3GHz
Memória RAM:16GBDDR4
Armazenamento:SSD de 512GB
Computador: Dell XPS 15

Acessando componentes...

Processador: Intel Core i7-11800H - 2.3 GHz
Memória RAM: 16 GB DDR4
Armazenamento: SSD - 512 GB

O computador Dell XPS 15 foi destruído. Seus componentes não existem mais...
🧠 Conceito Aplicado
Agregação → Objetos podem existir separadamente.

Composição → Objetos só existem dentro do objeto principal.

➡️ Neste caso, o Computador é composto por Processador, MemóriaRAM e Armazenamento.
Se o Computador deixar de existir, os componentes também são destruídos.

🚀 Tecnologias
Python

Programação Orientada a Objetos (POO)

Conceito de Composição
