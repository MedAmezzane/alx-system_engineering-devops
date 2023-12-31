# 0x00 Shell Basics

Project done during **Full Stack Software Engineering studies** at **ALX**. It aims to learn about basics commands, navigation, files and directories in **Shell**.

## Technologies
* Scripts written in Bash 5.0.17(1)
* Tested on Ubuntu 20.04 LTS

## Tasks

### Mandatory tasks

0. [Where am I?](./0-current_working_directory) : A script that prints the absolute path of the current working directory.
1. [What's in there?](./1-listit) : A script that displays the contents of your current directory.
2. [There is no place like home](./2-bring_me_home) : A script that changes the working directory to the user's home directory.
3. [The long format](./3-listfiles) : A script that displays the current directory contents in a long format.
4. [Hidden files](./4-listmorefiles) : A script that display current directory contents, including hidden files (starting with .) and use the long format.
5. [I love numbers](./5-listfilesdigitonly) : A script that displays the current directory contents, using long format, while displaying group IDs in numeral and show hidden files.
6. [Welcome](./6-firstdirectory) : A script that will create a directory named `my_first_directory` in the `/tmp/` directory.
7. [Betty in my first directory](./7-movethatfile) : A scipt that will move a file called `betty` from `/tmp/` to `/tmp/my_first_directory`.
8. [Bye bye Betty](./8-firstdelete) : A script that will delete file `betty` from `/tmp/my_first_directory`.
9. [Bye bye My first directory](./9-firstdirdeletion) : A script that will delete the directory `my_first_directory` that is in the `/tmp/` directory.
10. [Back to the future](./10-back) Change working directory to the previous one.
11. [Lists](./11-lists) List all files (*even ones with names beginning with a period character, which are normally hidden*) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.
12. [File type](./12-file_type) A script that prints the type of the named file `iamafile`. The file `iamafile` will be in the `/tmp/` directory when we will run the script.
13. [We are symbols, and inhabit symbols](./13-symbolic_link) Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.
14. [Copy HTML files](./14-copy_html) Create a script that copies all `html` files from the current working directory to the parent working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

### Advanced tasks

15. [Let's move](./100-lets_move) A script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
16. [Clean Emacs](./101-clean_emacs) A script that deletes all files in the current directory that end with the character `~`.
17. [Tree](./102-tree) A script that creates the directory `welcome/`, `welcome/to/` and `welcome/to/school`.
18. [Life is a series of commas, not periods](./103-commas) A script that lists all the files and directories of the current directory separated by commas `,`.
19. [File type: School](./school.mgc) Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files always contain the string `SCHOOL` at offset 0.

