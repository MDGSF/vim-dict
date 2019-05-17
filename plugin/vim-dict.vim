" Vim global plugin for dict
" Last Change:	17/05/19 14:58:10 
" Maintainer:	Huang Jian <1342042894@qq.com>
" License:	This file is placed in the public domain.

if !has("python3")
    echo "vim has to be compiled with +python3 to run this"
    finish
endif

if exists("g:loaded_vim_dict")
  finish
endif
let g:loaded_vim_dict = 1

let s:save_cpo = &cpo
set cpo&vim

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')
py3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
from vimdict import *
EOF

function! NQueryWord()
    py3 Normal_Python_QueryWord()
endfunction

function! VQueryWord()
    py3 Visual_Python_QueryWord()
endfunction

command! -nargs=0 QueryWord call NQueryWord()

let &cpo = s:save_cpo
unlet s:save_cpo

