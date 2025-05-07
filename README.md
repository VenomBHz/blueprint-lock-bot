# 🔒 Bot de Locks para Blueprints (Unreal + Discord)

Este bot gerencia o bloqueio de arquivos sensíveis (Blueprints, Maps, etc.) para evitar conflitos durante o desenvolvimento colaborativo com Unreal Engine.

## ✅ Como usar

### 🔒 Bloquear arquivo

!lock categoria:nome_do_arquivo

Exemplo: 

!lock BP:BP_Player

---

Se não quiser usar uma categoria, o arquivo será salvo como `UNCATEGORIZED`: 

!lock MenuPrincipal

---

### 🔓 Desbloquear arquivo

!unlock categoria:nome_do_arquivo

Exemplo:

!unlock BP:BP_Player

---

### 📄 Ver todos os arquivos bloqueados

!locks

---

### 🙋 Ver apenas os seus locks

!mylocks

---

## 🧩 Recomendações
- Sempre bloqueie arquivos antes de editar.
- Desbloqueie assim que terminar.
- Não edite arquivos já bloqueados por outro usuário.
- Prefira usar categorias para melhor organização: `BP:`, `MAP:`, `DATAASSET:`, etc.



Todos os locks são salvos automaticamente no arquivo `locks.json`.
