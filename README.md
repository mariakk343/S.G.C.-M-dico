# 🏥 Sistema de Gerenciamento Clínico

Este projeto é um sistema simples para gerenciar **clientes (pacientes)** e **atendimentos médicos**, desenvolvido com **Flask** e **SQLite**.

## 📌 Entidades e Relacionamentos

### 1. Cliente
Representa um paciente cadastrado na clínica.
- **id**: Identificador único do cliente (chave primária)
- **nome**: Nome completo do paciente
- **telefone**: Telefone para contato
- **data_nascimento**: Data de nascimento do paciente

### 2. Atendimento
Representa um atendimento médico realizado ou agendado.
- **id**: Identificador único do atendimento (chave primária)
- **data**: Data do atendimento
- **hora**: Horário do atendimento
- **motivo**: Motivo da consulta
- **id_cliente**: Chave estrangeira referenciando o cliente

### 🔗 Relacionamento
O relacionamento entre as entidades é **1:N** (um cliente pode ter vários atendimentos, mas cada atendimento pertence a um único cliente).


### Executar o projeto
1. Criar ambiente virtual
    ```
    python -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    source venv\Scripts\activate
    ```
   2.1. Atualizar o pip
   ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Execute o projeto
    ```
    python run.py
    ```