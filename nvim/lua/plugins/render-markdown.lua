return {
    "MeanderingProgrammer/render-markdown.nvim",
    after = { "nvim-treesitter" },
    config = function()
        require("render-markdown").setup({
            yaml = { enabled = false },
        })
    end,
}
