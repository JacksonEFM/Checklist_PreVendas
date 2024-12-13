def sug():
    suggestions = {
        "4.2": [
            "Verificar se a senha padrão atende aos critérios mínimos: no mínimo 8 caracteres, contendo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial."
        ],
        "4.3": [
            "a) Garantir que as senhas padrão sejam únicas para cada dispositivo fabricado, evitando duplicidade.",
            "b) Certificar-se de que as senhas não sejam derivadas de informações acessíveis, como endereços MAC.",
            "c) Validar que não sejam permitidas senhas em branco ou que não atendam aos critérios mínimos de segurança."
        ],
        "4.4": [
            "Implementar um mecanismo para exigir a alteração da senha padrão na primeira utilização ou após um reset para configurações de fábrica.",
            "4.4.1: Configurar o dispositivo para bloquear operações até que novas senhas válidas sejam definidas pelo usuário."
        ],
        "4.5": [
            "Certificar-se de que as senhas padrão estejam claramente especificadas em uma etiqueta no dispositivo e que sejam restauradas após o reset para configurações de fábrica."
        ],
        "5.2": [
            "Garantir que o sistema bloqueie senhas em branco ou fracas, com critérios mínimos claros.",
            "Certificar-se de que o manual do produto detalhe os requisitos de senhas, incluindo limites mínimos e máximos de caracteres e regras de formação."
        ],
        "5.3": [
            "Implementar uma verificação automática para garantir que as senhas do usuário sejam fortes e comparar com um dicionário de senhas fracas.",
            "5.3.1: Informar claramente no manual o método utilizado para validação de senhas e fornecer um dicionário de senhas proibidas."
        ],
        "6.1": [
            "a) Implementar mecanismos para limitar tentativas de acesso por força bruta, como bloqueio temporário após várias tentativas falhas.",
            "b) Evitar o uso de senhas ou credenciais hard-coded. Solicite o envio do código-fonte para análise se necessário.",
            "c) Utilizar algoritmos de criptografia seguros, como SHA-256 ou superiores, evitando MD5, SHA-1 e protocolos SSL obsoletos.",
            "d) Configurar um tempo limite para encerrar automaticamente sessões inativas.",
            "e) Identificar e desativar portas ou serviços desnecessários para reduzir a superfície de ataque.",
            "f) Permitir ao usuário desativar funções e serviços não essenciais diretamente pela interface de configuração."
        ],
        "6.2": [
            "Certificar-se de que o sistema de recuperação de senha seja robusto contra tentativas de roubo de credenciais, como envio de links seguros por e-mail ou perguntas de segurança confiáveis.",
            "6.2.1: Documentar claramente no manual do dispositivo o método de recuperação de senha implementado."
        ]
    }
    return suggestions
