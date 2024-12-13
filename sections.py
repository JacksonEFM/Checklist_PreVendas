def sec():
    sections = {

        "DOCUMENTOS SOLICITANTE": [
            "Temos Contrato Social?",
            "O Contrato Social e/ou Cartão CNPJ possui o CNAE para o TSC?",
            "O cliente possui vínculo com o OCD Moderna Tecnologia?",
            "Caso não possua vínculo, foi pedido o Vínculo junto ao OCD?"
        ],

        "DOCUMENTOS FABRICANTE": [
            "Temos ISO Original da Unidade Fabril?",
            "Temos ISO Traduzida da Unidade Fabril?",
            "A ISO está com data de validade correta?",
            "A Unidade Fabril possui cadastro na ANATEL?",
            "A Unidade Fabril possui escopo de fabricação do TSC?",
            "Temos Carta de Representação do Fabricante?",
            "A Carta de Representação contempla qualquer modelo à ser certificado?",
            "O fabricante possui cadastro na ANATEL?"
        ],

        "ESPECIFICACOES": [
            "Os produtos possuem ou recebemos a especificação?",
            "Se o produto for câmera, informar especificação de saída. Se não vier, colocar: DC 12V/1A",
            "Se for Smartwatch e não for comercializado com o carregador, informar ao OCD",
            "Foi informado a marca dos produtos?",
            "Foi informado o nome comercial dos produtos?",
            "Foi informada descrição dos nomes comerciais ou nome de modelo dos produtos?",
            "Foi informado o critério de formação de família?",
            "Se o produto for carregador e critério de família for por similaridade, colocar fotos externas comparando os modelos",
            "Foi informado o modelo a ser testado? (se houver família)"
        ],

        "APROVEITAMENTO": [
            "Os relatórios do modelo aproveitados estão com a validade de menos de 2 meses? Se sim mudar o aproveitamento",
            "Foi informado o critério de aproveitamento de todos os aproveitamentos?",
            "O fabricante bate com o fabricante do modelo aproveitado?",
            "O relatório do modelo aproveitado ainda está homologado? Ou dentro de 2 anos?",
            "O modelo aproveitado foi testado com fonte?",
            "Se sim, possui foto da fonte no relatório ou nas fotos?",
            "Se for aproveitamento completo, colocar no Jira 'sem marcações'",
            "O aproveitamento é AC? Se sim, pedir ensaio de SEG - Marcações (exceto câmeras - acima de 2 metros, ou seja, acesso restrito. Ou caso o aproveitamento tenha testado marcações e o produto AC for idêntico ao aproveitado)"
        ],

        "MARCACOES": [
            "Confirmar o laboratório que será enviado o produto",
            "Marcar os produtos com os nomes de modelos com etiqueta provisória",
            "Foi atualizado para o Danilo a aba de testes? Inserido o LAB?",
            "Foi destinada a amostra da família dentro de uma caixa identificada?"
        ],

        "JIRA": [
            "Foi atualizada todas as subtarefas do Jira?",
            "Possui config?",
            "Preencheu 'Details'?",
            "Colocou qual é o tipo de produto na descrição e em 'details'?",
            "A amostra tem código Antecipado?",
            "Se o produto for CLASSE A ou CLASSE I colocar na descrição",
            "Foi atualizado para a Giovana a aba 'Envio para OCD'?",
            "Foi atualizado todos os responsáveis em cada aba?",
            "Foi atualizado o cabeçalho do Jira com todas as informações? (ex.: Nome do produto, Especificações para Ensaios, Descrição do Aproveitamento se aplicável, etc)",
            "Foi feito um comentário para o Danilo e Filipe de 'Fotos Externas e Internas'?",
            "Colocou 'Em Andamento' e a Gabriella como responsável? (Se estiver tudo ok)",
            "Quando estiver faltando algum tipo de informação colocar em 'Aguardando Informações' e responsável Projetos ETS",
            "Possui produto associado?"
        ],

        "MANUTENCAO": [
            "Se manutenção, colocar data de validade do certificado na descrição",
            "Se manutenção, colocar a rastreabilidade que vem no produto",
            "Era módulo e agora passou a ser produto final? Se sim, testar tudo (EMC/SEG)",
            "Colocou em Aguardando Informações e responsável Projeto ETS?",
            "Se manutenção do certificado Moderna, checar se teve ocorrência (falha) na certificação inicial. Se teve, na formalização perguntar quais ensaios precisarão ser feitos, e segurar a amostra no setor de fotos e marcações, não enviando pro laboratório, aguardando RT.",
            "Se Produto alimentado AC e estiver diferente de '100-240V', verificar se o ensaio de Choque Elétrico de EMC testou em 240V. Se testou em 240, considerar '100-240V', se não testou, manter a espec",
            "Se for sem testes, o formato da rastreabilidade atual é igual da inicial?",
            "Conferir fotos externas certificação inicial e o produto de agora"
        ],

        "TROCA DE OCD": [
            "Gerar declaração de troca de OCD e encaminhar pro comercial"
        ],

        "KIC": [
            "O KIC foi formalizado para o OCD?",
            "O KIC foi concluído?",
            "Colocar na planilha de projetos",
            "Já tem um ETS para esse projeto?",
            "Foi feita folha de SLA?"
        ]

    }
    return sections
