# HelpDesk API (Suporte Técnico)

**Foco:** Fluxo de estados (State Machine) e validação de processo.

## 1. Abertura de Chamados

* **RF01 - Abrir Ticket:** O usuário (ou sistema) cadastra um chamado com assunto, descrição e prioridade (*Baixa*, *Média*, *Alta*).
    > **Regra:** O chamado deve nascer automaticamente com status `Novo` e sem técnico atribuído.
* **RF02 - Painel de Tickets:** Listar todos os chamados. Deve permitir filtrar por status (ex: ver apenas os `Novos` ou `Fechados`).

## 2. Fluxo de Atendimento (O Core)

* **RF03 - Atribuição:** Rota para um técnico assumir um chamado.
    > **Automação:** Ao assumir, o status do chamado deve mudar automaticamente de `Novo` para `Em Andamento`.
* **RF04 - Encerramento:** Rota para finalizar o chamado.
    > **Regra de Ouro:** O sistema deve impedir a finalização de um chamado que ainda esteja com status `Novo` (ninguém assumiu) ou sem técnico vinculado. Retornar erro explicativo.
* **RF05 - Histórico por Técnico:** Listar quantos chamados cada técnico resolveu.
