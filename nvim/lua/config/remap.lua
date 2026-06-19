vim.g.mapleader = " "

-- Netrw
vim.keymap.set("n", "<leader>e", vim.cmd.Ex)
vim.keymap.set("n", "<leader>E", function()
	vim.cmd.vsplit()
	vim.cmd.Ex()
end)

-- terminal exit
vim.keymap.set("t", "<Esc>", "<C-\\><C-n>")

-- indent file
vim.keymap.set("n", "<leader>=", "gg=G")

-- moving selected sections
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- keep cursor in the middle
vim.keymap.set("n", "<C-u>", "<C-u>zz")
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "n", "nzz")
vim.keymap.set("n", "N", "Nzz")

-- greatest remap ever (thanks Prime)
vim.keymap.set("v", "<leader>p", "\"_dP")
vim.keymap.set("n", "<leader>p", "\"_dP")

-- search current word
vim.keymap.set("n", "<leader>s", ":%s/\\<<C-r><C-w>\\>//gI<Left><Left><Left>")

-- avoid ex mode
vim.keymap.set("n", "q:", "<Nop>")

-- ctrl c to escape
vim.keymap.set("i", "<C-c>", "<Escape>")

-- clang-format
vim.keymap.set("n", "<leader>c", ":!clang-format -i %<cr><cr>")

-- tabs
vim.keymap.set("n", "<leader>t", vim.cmd.tabnew)
-- qwerty keybinds
vim.keymap.set("n", "<C-1>", function() vim.cmd.tabn(1) end)
vim.keymap.set("n", "<C-2>", function() vim.cmd.tabn(2) end)
vim.keymap.set("n", "<C-3>", function() vim.cmd.tabn(3) end)
vim.keymap.set("n", "<C-4>", function() vim.cmd.tabn(4) end)
vim.keymap.set("n", "<C-5>", function() vim.cmd.tabn(5) end)
vim.keymap.set("n", "<C-6>", function() vim.cmd.tabn(6) end)
vim.keymap.set("n", "<C-7>", function() vim.cmd.tabn(7) end)
vim.keymap.set("n", "<C-8>", function() vim.cmd.tabn(8) end)
vim.keymap.set("n", "<C-9>", function() vim.cmd.tabn(9) end)
vim.keymap.set("n", "<C-0>", function() vim.cmd.tabn(10) end)
-- azerty keybinds
vim.keymap.set("n", "<C-&>", function() vim.cmd.tabn(1) end)
vim.keymap.set("n", "<C-é>", function() vim.cmd.tabn(2) end)
vim.keymap.set("n", "<C-\">", function() vim.cmd.tabn(3) end)
vim.keymap.set("n", "<C-'>", function() vim.cmd.tabn(4) end)
vim.keymap.set("n", "<C-(>", function() vim.cmd.tabn(5) end)
vim.keymap.set("n", "<C-->", function() vim.cmd.tabn(6) end)
vim.keymap.set("n", "<C-è>", function() vim.cmd.tabn(7) end)
vim.keymap.set("n", "<C-_>", function() vim.cmd.tabn(8) end)
vim.keymap.set("n", "<C-ç>", function() vim.cmd.tabn(9) end)
vim.keymap.set("n", "<C-à>", function() vim.cmd.tabn(10) end)
