return {
    {
        'navarasu/onedark.nvim',
        config = function()
            local theme = require("onedark")
            theme.setup {
                style = "warmer",
                transparent = true,

                lualine = {
                    transparent = true,
                }
            }
            theme.load()
        end,
    }
}
