# mylab_py
My preferred python imports etc.

```
from mylab import *
```

If you fork this, it will be yourlab.

If you use omzsh (for zsh) then from the shell you can
```
cp mylab.zsh $ZSH_CUSTOM
```
or in other shells find some place to
```
alias mylab='~/repo/mylab_py/.venv/bin/ipython -i -c "from mylab import *"
```
but in either case you will have to set the path to the .venv if is is not right.

Then whenever you need an ipython REPL with the libraries preloaded, just run 
```zsh
mylab
```
