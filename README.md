### HelpDesk API (Suporte Técnico)

**Cenário:** Um sistema de abertura de chamados para TI (Tickets).
**Desafio de Lógica:** Fluxo de Status e Prioridade.

#### 🗄️ Entidades (Banco de Dados)
* **Tecnicos:** `id`, `nome`, `especialidade` (Redes, Hardware, Software).
* **Chamados:** `id`, `titulo`, `descricao`, `prioridade` (Alta/Media/Baixa), `status` (Aberto, Em Andamento, Fechado), `tecnico_id` (FK).

#### 🔌 Requisitos Funcionais (Endpoints)

* `POST /chamados`
    * Abre um chamado novo.
    * **Regra de Negócio:** O `status` nasce sempre como "Aberto" e o `tecnico_id` como `NULL`.

* `PATCH /atribuir`
    * Define qual técnico vai assumir o chamado.
    * **Automação:** O `status` deve mudar automaticamente para "Em Andamento".

* `PATCH /finalizar/<id>`
    * Muda o status para "Fechado".
    * **Regra de Ouro:** Só pode finalizar se já tiver um técnico atribuído (`tecnico_id` não for nulo).

* `GET /chamados/prioridade/<nivel>`
    * Filtra chamados por prioridade (ex: listar só as "Alta").

* `GET /tecnicos/<id>/tarefas`
    * Lista quantos e quais chamados aquele técnico tem em aberto/andamento.
