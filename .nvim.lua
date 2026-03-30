-- Citation completion: type @ in markdown/tex to get citation keys from bib/labels.bib
vim.api.nvim_create_autocmd("FileType", {
  pattern = { "markdown", "tex", "quarto" },
  callback = function(ev)
    vim.keymap.set("i", "@", function()
      local root = vim.fn.getcwd()
      local bib = root .. "/bib/labels.bib"
      if vim.fn.filereadable(bib) == 0 then
        return "@"
      end
      local keys = {}
      for line in io.lines(bib) do
        local key = line:match("^@%w+{(.+),$")
        if key then table.insert(keys, key) end
      end
      if #keys == 0 then
        return "@"
      end
      vim.api.nvim_feedkeys("@", "n", false)
      vim.schedule(function()
        vim.fn.complete(vim.fn.col("."), keys)
      end)
      return ""
    end, { buffer = ev.buf, expr = true })
  end,
})
