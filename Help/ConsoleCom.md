# Команды терминала

использовал [Этот сайт](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line), в нём ещё много информации, пока что обработал только самое базисное

*К каждой команде можно приписать `help` что бы найти нужный аргумент*

## `**cd**` - основная команда движения в терминале. Она позволяет перемещаться по всем папкам на компьютере. 

>!ВАЖНО! изначально открывается в корреной папке по умолчанию. Что бы в неё перейти можно использовать __`cd ~`__

> Папка в который мы сейчас находимся всегда пишется в строке терминала. На это стоит обращать внимание. 

* cd `..` - возвращает на папку назад
* cd `< name >` - где `< name >` название подпапки, где мы сейчас находимся - перемести нас внутрь этой папки 
* cd /d - переведёт на диск D , соответсвенно можно так-же прописывать полностью адрес папки для того что бы перейти откуда угодно - куда угодно
> Важно! если название папки содердит пробел или символ как ! название папки нужно обрамить ' пример - **`'!GeekBrains'`** или **`'Program Files' `**

> Другое примечание - если в Windows путь папки пишется через обратный сплэш **`\`** то в терминале нужно использовать нормальный **`/ `**

## ls - команда отображающая что находится в папке , в которой мы сейчас находимся. Внузи будет перечень вариантов, взятый через `ls --help`

1. -a, --all  do not ignore entries starting with .
2. -b, --escape   print C-style escapes for nongraphic characters
3. -c    with -lt: sort by, and show, ctime (time of last
4. -d, --directory  list directories themselves, not their contents
5. -f    do not sort, enable -aU, disable -ls --color
6. -g      like -l, but do not list owner
7. -h, --human-readable  with -l and -s, print sizes like 1K 234M 2G etc.
8. -i, --inode                print the index number of each file
9. -k, --kibibytes            default to 1024-byte blocks for disk usage;
10. -l                         use a long listing format
11. -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
12. -o     like -l, but do not list group information
13. -p, --indicator-style=slash append / indicator to directories
14. -q, --hide-control-chars   print ? instead of nongraphic characters
15. -r, --reverse              reverse order while sorting
16. -s, --size       print the allocated size of each file, in blocks
 

 ## Работа с файлами/папками

 **`mkdir`** - *создать папку в текущей дирректории, пример : __mkdir `GeekBrains`__*

 **`rmdir`** - *удаляет папку в дирректории, но не сможет это сделать, леси в папка не пустая, для этого нужно добавить **`-r`**, пример __rmdir `GeekBrains`__*

 **`touch`** - *создаёт файл в текущей папке, пример : __touch `GeekBrains.md`__*

 **`mv`** - *перемещает файл, так-же можно использовать как способ переименовать файл : __mv `GeekBrains` `Geek`__ - тереименут файл*

  **`cp`** - *копирует файл с другим названием : __mv `GeekBrains` `Geek`__ - создат второй файл на примере GeekBrains , но с названием Brains*

   **`rm`** - *Удаляет файл.*
   > Важно! файлы удалённые таким способо `rm` не возможно восстановить!

   > Примеры работы с функциями - находятся в ветке Test , в которой находится папка - Test и файл Test.md. В нём копии команд в терминале и примечание - что они сделали 

   >ещё пример использования : `rm -R “/path/to/root/directory”` - принудительно удалит целую дирректорию

   ## Ещё команды

   Нашёл топ 17 комманд  [Тут](https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/), для начала опишу те которых не было сверху.

   `open` - открывает файл, пример: `open text.md`

   `clear` - очищает экран терминала

   `pwd` - print worcking dictionary - выводит строку с адресом текущей дирректории. 
   > Важно, он всё равно ввыводит её так что нельзя использовать с cd

   `cat` - отображает содержимое файла

   `less` - отображает первую страницу

   `grep` - ищет <Содержимое> в файле и выводит всю строчку , пример: `grep touch Terminal_commands.md`

   `which` - интересная команда - показывает путь, откуда будет запускаться та или иная программа, пример: `which python3` - выдаст /c/Users/artio/AppData/Local/Microsoft/WindowsApps/python3

   `history` - показывает историю комманд. Можно так-же указывает `history -5` что бы показать последние 5 комманд 


