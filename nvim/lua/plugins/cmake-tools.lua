return {
    "CivitasV/cmake-tools.nvim",
    config = function()
        require("cmake-tools").setup({
            cmake_build_directory = "build/${variant:buildType}",
            cmake_compile_commands_options = {
                action = "soft_link",
                target = vim.fn.getcwd(),
            },
        })
    end,
}
