# AforaONE Founding Partners — implementação inicial

## Objetivo

Criar uma página comercial dedicada ao programa Founding Partners, para apoiar conversas exploratórias com empresas, comunidades, associações e parceiros de distribuição. O primeiro mercado-piloto permanece uma hipótese: Portugal.

## Estado do produto

- Página independente: `founding-partners.html`.
- Identidade visual alinhada ao protótipo atual (Deep Navy, Champagne Gold, Playfair Display e DM Sans).
- Conteúdo responsivo e acessível, com navegação de retorno à homepage.
- Explica o piloto de descoberta comercial de 15 dias.
- Distingue o que existe no protótipo do que ainda não está operacional.
- Explicita que a página não é oferta pública de investimento, participação societária ou promessa de retorno.
- Não apresenta números de audiência, leads, clientes ou métricas fictícias como tração real.

## Decisão técnica: Airtable

Foi criada uma base dedicada **AforaONE — Founding Partners**, tabela **Partner Pipeline**, para centralizar o CRM inicial. Os campos incluem organização, responsável, e-mail, telefone, categoria, localização, interesse, consentimento, status, origem e follow-up.

A base disponível anteriormente chamada **Serra Social OS** não foi reutilizada, para manter os dados do AforaONE separados de outras operações.

## Integração ainda pendente

A conexão Make disponível não possui uma conexão Airtable autenticada. Por isso, não foi criado nem ativado um cenário de automação, e a página informa que o canal de interesse está em preparação.

Antes de ativar o formulário público:
1. Criar/autenticar uma conexão Airtable no Make com acesso apenas à base dedicada.
2. Configurar webhook com validação de payload, honeypot e rate limiting.
3. Mapear campos para `Partner Pipeline`.
4. Definir aviso de privacidade, finalidade, retenção, acesso e procedimento para solicitações dos titulares, considerando o público UE/Portugal.
5. Testar envio real, falhas, duplicidade e resposta ao usuário.
6. Só então habilitar o formulário no frontend.

## Governança

- Branch: `feat/founding-partners-intake`.
- Base de trabalho: commit `fe31e034b4edafe9b3b779b274a080071a016c63` da `main`.
- Não alterar `main`, não fazer merge e não publicar sem aprovação explícita.
- A Issue #1 registra a sprint comercial e seus critérios de validação.

## Critério de aceite desta etapa

A página pode ser revisada como material comercial e institucional. A captação real de dados ainda não está habilitada; isso é intencional até concluir a integração segura com Airtable e os requisitos de privacidade.
