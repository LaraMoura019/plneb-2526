# Processamento de Dicionário Médico (PDF para Texto) 

Este projeto contém um script Python desenvolvido para limpar e estruturar dados textuais extraídos de um dicionário médico em formato PDF. O objetivo principal é remover artefactos de paginação e organizar os conceitos num formato de dicionário Python.

## Funcionalidades

- Identifica e remove o  `\f` proveniente da conversão de PDF.
- Resolve problemas onde termos ou definições são cortados por saltos de página.
- Converte o texto num dicionário Python `{termo: definicao}`.
- Remove quebras de linha desnecessárias dentro das definições.

## Lógica de Expressões Regulares (Regex)

O script utiliza três regras principais de substituição para tratar os casos críticos de paginação:

1. **Termo isolado da definição**: Corrige o caso onde o termo está no final de uma página e a definição começa na seguinte.
   - Regex: `\n\n([^\n]+)\n\n\f` -> `\n\n\1\n`
   - O padrão encontrado foi um bloco de texto delimitado por quebras de linha (`\n\n`) seguido imediatamente pelo final da página; ao capturarmos esse termo com (`[^\n]+`) e removermos o `\f`, assim como a quebra de linha excessiva, garantimos que o termo se anexe corretamente à definição que o segue através da substituição `\n\n\1\n`.
2. **Definição interrompida**: Corrige o caso onde o salto de página ocorre a meio de uma descrição.
   - Regex: `\n\n\f((.|\n)*?)\n\n` -> ` \1\n\n`
   - Aqui, a expressão procura a sequência `\n\n\f` e utiliza um grupo de captura `((.|\n)*?)` para encontrar o resto do texto até ao próximo conceito, reintegrando-o no bloco anterior com um espaço de compensação (`\1\n\n`).
3. **Limpeza Global**: Remove quaisquer caracteres `\f` onde a quebra de pagina não afeta nem os termos nem a definição.
   - Regex: `\f` -> `""`
   - Foi eliminado qualquer marcador `\f` residual que tenha caído exatamente entre dois conceitos já bem estruturados, assegurando que a divisão final por `\n\n` resulte numa lista de conceitos limpa e pronta para a conversão em JSON.

## Alternativas
Ao realizar o pdftotext para converter o ficheiro PDF em TXT, caso executássemos o comando `-layout`:
``` powershell
pdftotext -layout dicionario_medico.pdf
```
O problema do espaço criado dentro do mesmo conceito seria resolvido. No entanto, tambem não poderíamos, ao realizar a limpeza, retirar apenas os `\f`, uma vez que este método , no caso em que ocorre mudança de página entre conceitos diferentes, estes ficam sem separação (sem `\n\n` entre eles), e por isso, torna-se difícil encontrar um critério de separação entre os diferentes conceitos.
  
Para resolver este problema podíamos procurar o `\f` e substituir por um `\n`, no entanto, isso iria recriar o mesmo problema aqui tratado (quebras de linha indesejadas). Por esse motivo, optou-se pela estratégia de limpeza via Python sem o modo `-layout`.


## Como Utilizar

### Pré-requisitos
- Um ficheiro chamado `dicionario_medico.txt` na mesma diretoria .

### Execução
Basta executar o script no terminal:
```powershell
python dicionario_medico.py
```

## Resultado
O resultado do número de conceitos encontrados neste ficheiro pdf foi de 8723 conceitos.


