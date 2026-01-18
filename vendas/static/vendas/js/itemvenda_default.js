function atualizarItem(row) {
    const produtoSelect = row.querySelector("select[name$='produto']");
    const quantidadeField = row.querySelector("input[name$='quantidade']");
    const precoField = row.querySelector("input[name$='preco_unitario']");

    if (!produtoSelect) return;

    // Definir quantidade padrão = 1
    if (quantidadeField && !quantidadeField.value) quantidadeField.value = 1;

    produtoSelect.addEventListener("change", function() {
        const produtoId = produtoSelect.value;
        if (!produtoId) return;

        fetch(`/vendas/get_preco_produto/${produtoId}/`)
            .then(response => response.json())
            .then(data => {
                if (precoField) precoField.value = data.preco;
            });
    });

    // Se já tiver produto selecionado, preencher preço automaticamente
    if (produtoSelect.value) {
        const produtoId = produtoSelect.value;
        fetch(`/vendas/get_preco_produto/${produtoId}/`)
            .then(response => response.json())
            .then(data => {
                if (precoField) precoField.value = data.preco;
            });
    }
}

// Inicializa todos os inlines existentes
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".dynamic-itemvenda_set").forEach(atualizarItem);

    // Observador para novos inlines adicionados dinamicamente
    document.body.addEventListener("click", function(e) {
        if (e.target && e.target.classList.contains("add-row")) {
            setTimeout(() => {
                document.querySelectorAll(".dynamic-itemvenda_set").forEach(atualizarItem);
            }, 500); // esperar o Django criar o novo inline
        }
    });
});
