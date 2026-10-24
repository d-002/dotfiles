return {
    "smoka7/hop.nvim",
    version = "*",
    config = function()
        require("hop").setup({
            keys = "sadfjklewcmpgh"
        })

        vim.keymap.set("n", "à", "<cmd>HopWord<CR>", { silent = true })
    end,
}
