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

## Captação de interesse e privacidade

A página informa que o canal de manifestação de interesse está em preparação e não recolhe nem transmite dados pessoais nesta etapa.

Antes de ativar qualquer formulário público de captação:
1. Configurar endpoint dedicado com validação de payload, controles anti-spam (honeypot e rate limiting) e tratamento idempotente.
2. Publicar aviso de privacidade, finalidade, prazo de retenção e canal para solicitações dos titulares, considerando o público UE/Portugal.
3. Testar envio real, cenários de falha, duplicidade e feedback ao usuário.
4. Habilitar o formulário apenas após homologação técnica e de privacidade.

## Histórico: abordagem inicial de CRM (Airtable / Make) — Legado substituído

Na concepção preliminar da landing page, planejou-se um fluxo de CRM inicial baseado em uma base dedicada no Airtable (**AforaONE — Founding Partners**), tabela **Partner Pipeline**, com campos previstos para organização, responsável, contato (e-mail e telefone), categoria, localização, interesse e acompanhamento.

A automação seria operada via Make, mas essa integração nunca chegou a ser ativada por ausência de conexão autenticada entre o Make e a base dedicada.

Essa abordagem inicial foi expressamente **substituída e descontinuada** pela decisão estratégica de desenvolver o **AforaONE Connect** como aplicação própria com backend Laravel, frontend Nuxt, banco de dados PostgreSQL e autenticação segura via Laravel Sanctum.

## Baseline visual RC1

- Tag de referência: `founding-partners-rc1` (commit `3d2e70202694f666913f0bab5ef318eb3d3493a7`).
- Arquivo homologado: `founding-partners.html` (SHA-1 do blob Git: `fc4aacba337beef8d3e0ca2aa42a836790c3e8f4`, SHA-1 do conteúdo: `d254224c2c74845407b006658259d0236abc8886`).
- Capturas de referência (Chromium headless, página completa):
  - `1440 px` (`1440 × 3316`): SHA-256 `e2873134ddada2942038c80f92aee77f53ff23061c9fec4e458781e7f88d38f2`
  - `768 px` (`768 × 3431`): SHA-256 `89e8f41403dc29a7e8c0a579a59a9250d0241d1776e27631c27a7f7c3d64ea8b`
  - `390 px` (`390 × 5033`): SHA-256 `4cd8d5fca5989b69d45e0c72d5a7fa8230f3dbb7c3ae4f6de424ad95a252b190`

## Critério de aceite desta etapa

A página pode ser utilizada como material comercial e institucional de apresentação do programa. A captação ativa de dados permanece desabilitada até a conclusão da infraestrutura dedicada e dos requisitos de privacidade.
