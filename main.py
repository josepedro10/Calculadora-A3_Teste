import tkinter as tk

from telas.home import Home
from telas.calc_simples import CalculadoraSimples
from telas.imc import CalculadoraIMC
from telas.media import CalculadoraMedia
from telas.consumo import CalculadoraConsumo

# =====================================
# JANELA PRINCIPAL
# =====================================
janela = tk.Tk()
janela.title("Calculadora Estendida")

# Tela cheia
janela.state("zoomed")

# Fundo
janela.config(bg="#a466a8")

# =====================================
# FRAME MENU
# =====================================
menu = tk.Frame(janela, bg="#a466a8")
menu.pack(side="left", fill="y", padx=20, pady=20)

# =====================================
# FRAME CONTEÚDO
# =====================================
container = tk.Frame(janela, bg="#a466a8")
container.pack(side="right", expand=True, fill="both")

# =====================================
# TELAS
# =====================================
frames = {}

for Tela in (
    Home,
    CalculadoraSimples,
    CalculadoraIMC,
    CalculadoraMedia,
    CalculadoraConsumo
):
    frame = Tela(container)

    frames[Tela.__name__] = frame

    frame.place(
        relwidth=1,
        relheight=1
    )

# =====================================
# FUNÇÃO TROCAR TELA
# =====================================
def mostrar(nome):
    frames[nome].tkraise()

# =====================================
# ESTILO BOTÕES
# =====================================
def criar_botao(texto, tela):

    return tk.Button(
        menu,
        text=texto,
        command=lambda: mostrar(tela),
        font=("Arial", 22, "bold"),
        bg="#3f11c4",
        fg="white",
        activebackground="#2d0c8f",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=20,
        width=18,
        cursor="hand2"
    )

# =====================================
# BOTÕES MENU
# =====================================
criar_botao("Home", "Home").pack(pady=15)

criar_botao(
    "Calculadora\nSimples",
    "CalculadoraSimples"
).pack(pady=15)

criar_botao(
    "Calculadora\nIMC",
    "CalculadoraIMC"
).pack(pady=15)

criar_botao(
    "Calculadora\nMédia",
    "CalculadoraMedia"
).pack(pady=15)

criar_botao(
    "Calculadora\nConsumo",
    "CalculadoraConsumo"
).pack(pady=15)

# Tela inicial
mostrar("Home")

janela.mainloop()