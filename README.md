# vim-dict

**vim-dict** 英汉字典。

## 安装

```
cd ~/.vim/bundle
git clone https://github.com/MDGSF/vim-dict.git
```

### stardict.db 字典数据库

`stardict.db` 下载地址。

```
链接: https://pan.baidu.com/s/15MTRjf3Kzxgmpz6MdOp4mQ
提取码: hr8q
```

把 `stardict.db` 放到目录 `vim-dict/python` 下面。

## 添加映射

```
nnoremap <F2> :QueryWord<CR>
vnoremap <F2> :call QueryWord()<CR>
```

