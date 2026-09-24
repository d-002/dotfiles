return {
    "github/copilot.vim",
    setup = function()
        -- fix tab mapping
        vim.g.copilot_no_tab_map = true
        vim.g.copilot_filetypes = {
            ['*'] = false,
        }

        vim.keymap.set('i', '<Tab>', function()
            if vim.fn['copilot#Accept']('') ~= '' then
                return vim.fn['copilot#Accept']('')
            else
                return '<Tab>'
            end
        end, { expr = true, silent = true })

        -- manually trigger copilot suggestions
        vim.keymap.set('i', '<C-Space>', 'copilot#Suggest()', { expr = true, silent = true })
    end
}
