return {
    "linux-cultist/venv-selector.nvim",
    dependencies = {
        "nvim-telescope/telescope.nvim",
    },
    config = function() require("venv-selector").setup() end,
}
