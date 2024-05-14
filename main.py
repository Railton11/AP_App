from tela import Tela

if __name__ == "__main__":
    try:
        app = Tela()
        app.run()
    except ImportError:
        print("Erro de execução grave, por favor entre em contato com o desenvolvedor para resolução deste problema.")
    except Exception:
        print("Ocorreu um erro inesperado, por favor entre em contato com o desenvolvedor.")