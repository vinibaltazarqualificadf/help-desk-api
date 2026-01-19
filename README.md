### EventPass API (Gestão de Eventos)

**Cenário:** Um sistema para gerenciar pequenos shows, workshops ou palestras e seus participantes.
**Desafio de Lógica:** Controle de Capacidade (Vagas).

#### 🗄️ Entidades (Banco de Dados)
* **Eventos:** `id`, `nome`, `data`, `capacidade_maxima`, `local`.
* **Participantes:** `id`, `nome`, `email`, `evento_id` (FK).

#### 🔌 Requisitos Funcionais (Endpoints)

* `POST /eventos`
    * Criar um evento definindo quantas pessoas cabem.

* `POST /inscricao`
    * Inscrever um participante em um evento.
    * **Regra de Ouro:** Antes de salvar, o sistema deve verificar se o número de inscritos é menor que a `capacidade_maxima`. Se estiver lotado, retornar erro `400` ("Evento Lotado").

* `GET /eventos/<id>/participantes`
    * Listar todos os nomes confirmados naquele evento.

* `DELETE /inscricao/<id>`
    * Cancelar uma inscrição (liberando a vaga para outra pessoa).

* `GET /eventos/lotados`
    * Retornar apenas os eventos que já atingiram a capacidade máxima.
