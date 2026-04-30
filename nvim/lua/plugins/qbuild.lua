return {
    "d-002/vim-qbuild",
    dependencies = "ahmedkhalf/project.nvim",
    config = function()
        local qbuild = require("vim-qbuild")
        local qconfig = require("vim-qbuild.config")

        -- add custom options if needed (override defaults)
        qconfig.setup {
            runType = qconfig.TERMINAL
        }

        -- open the build dir in netrw-vexplore
        vim.keymap.set("n", "<leader>qo", qbuild.openBuildDir)

        -- run the default build script
        vim.keymap.set("n", "<leader>b", qbuild.runBuildFile)

        -- run the build script named "main"
        vim.keymap.set("n", "<leader>m", function() qbuild.runBuildFile{ name = "main" } end)

        -- run the first build script
        vim.keymap.set("n", "<leader>q1", function() qbuild.runBuildFile({ index = 1 }) end)
        -- run the second build script
        vim.keymap.set("n", "<leader>q2", function() qbuild.runBuildFile({ index = 2 }) end)
        -- and so on
        vim.keymap.set("n", "<leader>q3", function() qbuild.runBuildFile({ index = 3 }) end)
    end,
}
