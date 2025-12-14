# Sistema de Automação Digital: Gestão de Peças, Qualidade e Armazenamento
# Disciplina: Algoritmos e Lógica de Programação
# --------------------------------------------------
# Observação IMPORTANTE:
# Este arquivo possui DOIS MODOS DE EXECUÇÃO:
# 1) Modo Interativo (terminal local, com input())
# 2) Modo Simulação/Testes (ambientes sem input, como sandbox)
# --------------------------------------------------

# ==========================
# Estruturas de Dados
# ==========================
pecas_aprovadas = []
pecas_reprovadas = []
caixas = []  # lista de caixas, cada caixa é uma lista de peças

CAPACIDADE_CAIXA = 10

# ==========================
# Funções de Validação
# ==========================
def avaliar_peca(peca):
    motivos = []

    if not (95 <= peca['peso'] <= 105):
        motivos.append('Peso fora do padrão')
    if peca['cor'].lower() not in ['azul', 'verde']:
        motivos.append('Cor inválida')
    if not (10 <= peca['comprimento'] <= 20):
        motivos.append('Comprimento fora do padrão')

    if not motivos:
        return True, 'Aprovada'
    return False, ', '.join(motivos)

# ==========================
# Funções Principais (Lógica)
# ==========================
def processar_peca(peca):
    aprovada, resultado = avaliar_peca(peca)

    if aprovada:
        pecas_aprovadas.append(peca)
        armazenar_em_caixa(peca)
        return 'APROVADA'
    else:
        peca['motivo'] = resultado
        pecas_reprovadas.append(peca)
        return f"REPROVADA: {resultado}"


def armazenar_em_caixa(peca):
    if not caixas or len(caixas[-1]) == CAPACIDADE_CAIXA:
        caixas.append([])
    caixas[-1].append(peca)


def remover_peca_por_id(id_peca):
    for lista in (pecas_aprovadas, pecas_reprovadas):
        for p in lista:
            if p['id'] == id_peca:
                lista.remove(p)
                return True
    return False


def gerar_relatorio():
    return {
        'total_aprovadas': len(pecas_aprovadas),
        'total_reprovadas': len(pecas_reprovadas),
        'motivos_reprovacao': [
            f"ID {p['id']} - {p['motivo']}" for p in pecas_reprovadas
        ],
        'quantidade_caixas': len(caixas)
    }

# ==========================
# Modo Interativo (Terminal Local)
# ==========================
def menu_interativo():
    while True:
        print('\n===== MENU =====')
        print('1. Cadastrar nova peça')
        print('2. Listar peças aprovadas/reprovadas')
        print('3. Remover peça cadastrada')
        print('4. Listar caixas fechadas')
        print('5. Gerar relatório final')
        print('0. Sair')

        try:
            opcao = input('Escolha uma opção: ')
        except OSError:
            print('Ambiente sem suporte a input(). Use o modo de simulação.')
            break

        if opcao == '1':
            try:
                peca = {
                    'id': input('ID da peça: '),
                    'peso': float(input('Peso (g): ')),
                    'cor': input('Cor: '),
                    'comprimento': float(input('Comprimento (cm): '))
                }
                print(processar_peca(peca))
            except ValueError:
                print('Erro: valores inválidos.')

        elif opcao == '2':
            print('Aprovadas:', pecas_aprovadas)
            print('Reprovadas:', pecas_reprovadas)

        elif opcao == '3':
            pid = input('ID da peça: ')
            print('Removida' if remover_peca_por_id(pid) else 'Não encontrada')

        elif opcao == '4':
            for i, caixa in enumerate(caixas, start=1):
                print(f'Caixa {i} - {len(caixa)} peças')

        elif opcao == '5':
            print(gerar_relatorio())

        elif opcao == '0':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção inválida!')

# ==========================
# Modo Simulação / Testes
# ==========================
def executar_simulacao():
    print('Executando simulação automática...')

    dados_teste = [
        {'id': 'P1', 'peso': 100, 'cor': 'azul', 'comprimento': 15},
        {'id': 'P2', 'peso': 110, 'cor': 'azul', 'comprimento': 15},
        {'id': 'P3', 'peso': 98, 'cor': 'vermelho', 'comprimento': 12},
        {'id': 'P4', 'peso': 102, 'cor': 'verde', 'comprimento': 25},
        {'id': 'P5', 'peso': 97, 'cor': 'verde', 'comprimento': 18},
    ]

    for peca in dados_teste:
        resultado = processar_peca(peca)
        print(f"Peça {peca['id']}: {resultado}")

    relatorio = gerar_relatorio()

    print('\n===== RELATÓRIO FINAL =====')
    print('Aprovadas:', relatorio['total_aprovadas'])
    print('Reprovadas:', relatorio['total_reprovadas'])
    print('Motivos:', relatorio['motivos_reprovacao'])
    print('Caixas utilizadas:', relatorio['quantidade_caixas'])

# ==========================
# Execução Automática
# ==========================
if __name__ == '__main__':
    try:
        menu_interativo()
    except OSError:
        executar_simulacao()
