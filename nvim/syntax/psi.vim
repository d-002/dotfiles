" Vim syntax file
" Language:		PUSSI-8 Assembler
" Maintainer:		d-002

" quit when a syntax file was already loaded
if exists("b:current_syntax")
  finish
endif

let s:cpo_save = &cpo
set cpo&vim

syn case ignore

syn match psiNumberBin "\<0b[01]\+\>"
syn match psiNumberHex "\<0x[0-9a-f]\+\>"
syn match psiNumberDec "\<[0-9]\+\>"

syn match psiRegister "%r[0-9]\+\>"
syn match psiMemory "%m[0-9]\+\>"
syn match psiPort "%p[0-9]\+\>"

syn match psiLabel "^\.[a-z_][a-z0-9_]*\>"
syn match psiIdentifier "\<[a-z_][a-z0-9_]*\>"

syn match psiOpcode "^[ ]\+[a-z]\+"
"syn keyword psiOpcode halt

syn match psiComment ";.*"

syn case match

hi def link psiNumberBin Number
hi def link psiNumberHex Number
hi def link psiNumberDec Number

hi def link psiRegister String
hi def link psiMemory Type
hi def link psiPort Type

hi def link psiLabel Label
hi def link psiIdentifier Identifier

hi def link psiOpcode Function

hi def link psiComment Comment

let b:current_syntax = "psi"

let &cpo = s:cpo_save
unlet s:cpo_save

" vim: nowrap sw=2 sts=2 ts=8 noet
