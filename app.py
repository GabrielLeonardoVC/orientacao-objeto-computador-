from classes import Computador
meu_pc = Computador(
    "Dell","XPS 15",
    "Intel Core i7-11800H",2.3,
    16,"DDR4",
    "SSD",512
)
meu_pc.ligar()
print(meu_pc)

print("\nAcessando componentes...")
print()
print("Processador:",meu_pc.get_processador().get_modelo(),"-",meu_pc.get_processador().get_velocidade_ghz(),"GHz")
print("Memória RAM:",meu_pc.get_memoria_ram().get_capacidade_gb(),"GB", meu_pc.get_memoria_ram().get_tipo())
print("Armazenamento:",meu_pc.get_armazenamento().get_tipo(),"-",meu_pc.get_armazenamento().get_capacidade_gb(),"GB")
del meu_pc
