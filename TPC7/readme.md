# Dicionário Médico em Web

Este projeto consiste numa plataforma web desenvolvida para consulta e gestão de termos técnicos de saúde. Foi concebido como um projeto de aprendizagem prática para consolidar conhecimentos em Flask e desenvolvimento frontend responsivo com Bootstrap.

---

## Funcionalidades

- **Exploração por Lista:** Visualização organizada de centenas de conceitos médicos.
- **Filtro Alfabético:** Sistema de filtragem inteligente para encontrar termos rapidamente de A a Z.
- **Paginação Dinâmica:** Divisão automática de conceitos (20 por página) para garantir carregamentos rápidos.
- **Página de Detalhe:** Espaço dedicado para cada termo, com definições claras e legíveis.
- **Tratamento de Erros:** Página 404 personalizada para uma melhor experiência de utilizador.

---

## Arquitetura e Tecnologias

O projeto utiliza uma combinação estratégica de tecnologias para garantir um equilíbrio entre rapidez de processamento e estética visual:

### Flask (Backend)
O Flask atua como o motor da aplicação. No projeto, ele desempenha os seguintes papéis:
- **Gestão de Rotas:** Mapeamento inteligente de URLs para funções específicas.
- **Lógica de Paginação:** Cálculo dinâmico de "fatias" de dados (`slicing`) baseado no pedido do utilizador.
- **Jinja2:** Permite a integração de lógica Python diretamente no HTML, facilitando a criação de listas dinâmicas e estados ativos (como destacar a página atual).

### Bootstrap (Frontend)
O uso do Bootstrap garantiu um visual moderno e profissional, alguns dos exemplos utilizados são:
- **Grid System:** Utilizado para centralizar o dicionário em containers, evitando que o texto se disperse em ecrãs largos.
- **Componentes Prontos:** Uso de `cards` para definições, `list-groups` para os termos e `pagination` para a navegação.
- **Tipografia:** Integração de fontes limpas (Roboto) e classes utilitárias de espaçamento (`py-5`, `ps-4`) para máxima legibilidade.

### Sinergia Tecnológica
O Flask processa os dados médicos e a lógica de filtros no servidor, enviando apenas a informação necessária para o frontend. O Bootstrap recebe esses dados e apresenta-os de forma organizada, garantindo que o utilizador tenha uma experiência fluida, independentemente do dispositivo que utiliza.

---

## Instalação e Execução


### 1. Certifica-te que tens o Python instalado (versão 3.8 ou superior).
### 2. Certifica-te que tens o Flask instalado.
### 3. Executa a aplicação.
Para correr este projeto localmente:

   ```bash
   python aula_7_2.py
   ```
### 4. Explora o dicionario:
Abre o navegador e acede a  http://127.0.0.1:5000/