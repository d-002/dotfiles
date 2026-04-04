return {
    {
        "mason-org/mason.nvim",
        dependencies = {
            "williamboman/mason-lspconfig.nvim",
            "williamboman/mason.nvim",
            "neovim/nvim-lspconfig",
            "nvimtools/none-ls.nvim",
            "jay-babu/mason-null-ls.nvim",
        },
        config = function()
            require("mason").setup({
                PATH = "append"
            })

            local servers = {
                "clangd",
                "lua_ls",
                "pyright",
                "phpactor",
                "denols",
                "texlab",
            }

            require("mason-lspconfig").setup({
                ensure_installed = servers,
                automatic_installation = true,
            })

            for _, server in ipairs(servers) do
                if server == "pylsp" then
                    vim.lsp.config(server, {
                        settings = {
                            pylsp = {
                                plugins = {
                                    flake8 = {
                                        enabled = true,
                                    },
                                    pycodestyle = {
                                        enabled = true,
                                    },
                                },
                            },
                        },
                    })
                elseif server == "lua_ls" then
                    vim.lsp.config(server, {
                        settings = {
                            Lua = {
                                runtime = {
                                    version = "LuaJIT",
                                },
                                diagnostics = {
                                    globals = {
                                        "vim",
                                        "require",
                                    },
                                },
                            },
                        },
                    })
                else
                    vim.lsp.config(server, {})
                end
            end

            vim.diagnostic.config({
                virtual_text = true,
                virtual_lines = false,
                signs = true,
                underline = true,
                update_in_insert = false,
                severity_sort = true,
            })
        end,
    }
}
