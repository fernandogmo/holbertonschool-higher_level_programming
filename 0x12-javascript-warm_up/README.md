# 0x12. JavaScript - Warm Up
Install `nvm`
```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
```

Verify installation
```sh
command -v nvm
```

As of May 2019, the version of `node` used for this project is v6.10.2.
To install that specific version, do this:
```sh
nvm install 6.10.2
```

Use JavaScript Semi-Standard Style to check your code:
```sh
npm install semistandard -g
```

For Vim integration, install Syntastic and add these lines to `.vimrc`:
```sh
let g:syntastic_javascript_checkers=['standard']
let g:syntastic_javascript_standard_exec = 'semistandard'
```
Then for automatic formatting on save, add this to your `.vimrc`:
```sh
autocmd bufwritepost *.js silent !semistandard % --fix
set autoread
```
