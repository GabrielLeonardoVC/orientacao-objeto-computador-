class Processador:
    def __init__(self,modelo,velocidade_ghz):
        self._modelo=modelo
        self._velocidade_ghz=velocidade_ghz

    def get_modelo(self):
        return self._modelo

    def get_velocidade_ghz(self):
        return self._velocidade_ghz

    def __str__(self):
        return f"Processador:{self._modelo},Velocidade:{self._velocidade_ghz}GHz"

class MemoriaRAM:
    def __init__(self,capacidade_gb,tipo):
        self._capacidade_gb=capacidade_gb
        self._tipo=tipo

    def get_capacidade_gb(self):
        return self._capacidade_gb

    def get_tipo(self):
        return self._tipo

    def __str__(self):
        return f"Memória RAM:{self._capacidade_gb}GB{self._tipo}"

class Armazenamento:
    def __init__(self,tipo,capacidade_gb):
        self._tipo=tipo
        self._capacidade_gb=capacidade_gb

    def get_tipo(self):
        return self._tipo

    def get_capacidade_gb(self):
        return self._capacidade_gb

    def __str__(self):
        return f"Armazenamento:{self._tipo} de {self._capacidade_gb}GB"

class Computador:
    def __init__(self,marca,modelo,processador_modelo,processador_velocidade,ram_capacidade,ram_tipo,armazenamento_tipo,armazenamento_capacidade):
        self._marca=marca
        self._modelo=modelo

        self._processador=Processador(processador_modelo,processador_velocidade)
        self._memoria_ram=MemoriaRAM(ram_capacidade,ram_tipo)
        self._armazenamento=Armazenamento(armazenamento_tipo,armazenamento_capacidade)

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_processador(self):
        return self._processador

    def get_memoria_ram(self):
        return self._memoria_ram

    def get_armazenamento(self):
        return self._armazenamento

    def ligar(self):
        print(f"\nLigando o computador...")
        print("Carregando...")
        print("Pronto!")
        print()
        print(f"{self._marca} {self._modelo}...")
        print(f"{self._processador}")
        print(f"{self._memoria_ram}")
        print(f"{self._armazenamento}")
        return self 

    def __str__(self):
        return f"Computador: {self._marca} {self._modelo}"

    def __del__(self):
        print(f"\nO computador {self._marca} {self._modelo} foi destruído. Seus componentes não existem mais...")

if __name__=="__main__":
    meu_pc=Computador(
        "Dell","XPS 15",
        "Intel Core i7-11800H",2.3,
        16,"DDR4",
        "SSD",512
    )
    meu_pc.ligar()
    print(meu_pc)
    del meu_pc