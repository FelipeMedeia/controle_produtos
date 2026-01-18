document.addEventListener("DOMContentLoaded", function () {
    alert("JS carregou!");
    console.log("itemvenda_default.js carregou!");


    function atualizarItem(row) {
        const produtoSelect = row.querySelector("select[name$='produto']");
        const quantidadeField = row.querySelector("input[name$='quantidade']");
        const precoField = row.querySelector("input[name$='preco_unitario']");

        if (!produtoSelect) return;

        // Definir quantidade = 1 por padrão
        if (quantidadeField && !quantidadeField.value) quantidadeField.value = 1;

        // Função para atualizar preço via AJAX
        function atualizarPreco() {
            const produtoId = produtoSelect.value;
            if (!produtoId) return;

            fetch(`/vendas/get_preco_produto/${produtoId}/`)
                .then(response => response.json())
                .then(data => {
                    if (precoField) precoField.value = data.preco;
                });
        }

        // Atualiza quando troca o produto
        produtoSelect.addEventListener("change", atualizarPreco);

        // Se já tiver produto selecionado, já busca o preço
        if (produtoSelect.value) atualizarPreco();
    }

    // Atualiza todos os inlines já existentes
    document.querySelectorAll(".dynamic-itemvenda_set").forEach(atualizarItem);

    // Atualiza novos inlines adicionados dinamicamente
    document.body.addEventListener("click", function (e) {
        if (e.target && e.target.classList.contains("add-row")) {
            setTimeout(() => {
                document.querySelectorAll(".dynamic-itemvenda_set").forEach(atualizarItem);
            }, 500);
        }
    });
});
