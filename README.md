# vim-dict

English to Chinese dictionary.

## How to install

```
git clone https://github.com/MDGSF/vim-dict.git ~/.vim/bundle
```

`stardict.db` 下载地址。把 `stardict.db` 放到目录 `vim-dict/python` 下面。

```
链接: https://pan.baidu.com/s/15MTRjf3Kzxgmpz6MdOp4mQ
提取码: hr8q
```

## Add map to vimrc

```
nnoremap <F2> :QueryWord<CR>
vnoremap <F2> :call QueryWord()<CR>
```

