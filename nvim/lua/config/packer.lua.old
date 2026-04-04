-- This file can be loaded by calling `lua require("plugins")` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require("packer").startup(function(use)
    -- Packer can manage itself
    use "wbthomason/packer.nvim"

    use {
        "nvim-telescope/telescope.nvim", tag = "0.1.8",
        requires = "nvim-lua/plenary.nvim"
    }

    use "navarasu/onedark.nvim"

    use "wakatime/vim-wakatime"

    use ("nvim-treesitter/nvim-treesitter", { run = ":TSUpdate" })

    use {
        "ThePrimeagen/harpoon",
        requires = "nvim-lua/plenary.nvim",
    }

    use {
        "mbbill/undotree",
        requires = "nvim-lua/plenary.nvim",
    }

    use {
        "tpope/vim-fugitive",
        requires = "BurntSushi/ripgrep",
    }

    use {
        "d-002/vim-qbuild",
        requires = "ahmedkhalf/project.nvim",
    }

    use "lewis6991/gitsigns.nvim"

    use {
        "nvim-lualine/lualine.nvim",
        requires = "nvim-tree/nvim-web-devicons",
        config = function() require("lualine").setup() end,
    }

    use "dstein64/vim-startuptime"

    -- lsp
    use {
        "mason-org/mason.nvim",
        requires = {
            "williamboman/mason-lspconfig.nvim",
            "williamboman/mason.nvim",
            "neovim/nvim-lspconfig",
            "nvimtools/none-ls.nvim",
            "jay-babu/mason-null-ls.nvim",
        },
    }

    use {
        "MeanderingProgrammer/render-markdown.nvim",
        after = { "nvim-treesitter" },
        config = function()
            require("render-markdown").setup({ yaml = { enabled = false } })
        end,
    }

    use "andweeb/presence.nvim"

    -- use "mfussenegger/nvim-jdtls"
end)
