# 0x01 Shell Permissions

Project done during **Full Stack Software Engineering studies** at **ALX**. It aims to learn about permissions (owner, group and other) of files and directories in **Shell**.

## Technologies
* Scripts written in Bash 5.0.17(1)
* Tested on Ubuntu 20.04 LTS

## Tasks

### Mandatory tasks

0. [My name is Betty](./0-iam_betty) : A script that switches the current user to the user `betty`.
1. [Who am I](./1-who_am_i) : A script that prints the effective username of the current user.
2. [Groups](./2-groups) : A script that prints all the groups the current user is part of.
3. [New owner](./3-new_owner) : A script that changes the owner of the file `hello` to the user `betty`.
4. [Empty!](./4-empty) : A script that creates an empty file called `hello`.
5. [Execute](./5-execute) : A script that adds execute permission to the owner of the file `hello`.
6. [Multiple permissions](./6-multiple_permissions) : A script that adds execute permission to the owner and the group owner, and read permission to the other users, to the file `hello`.
7. [Everybody!](./7-everybody) : A script that adds execution permissions to the owner, the group owner and the other users, to the file `hello`.
8. [James Bond](./8-James_Bond) : A script that gives other users all the permissions and removes all permission for the owner and the group owner.
9. [John Doe](./9-John_Doe) : that sets the mode of the file `hello` to this: ` -rwxr-x-wx `
10. [Look in the mirror](./10-mirror_permissions) : A script that sets the mode of the file `hello` the same as `olleh`'s mode. (*The files `hello` and `olleh` will be in the working directory*)
11. [Directories](./11-directories_permissions) : A script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. (*Regular files should not be changed.*)
12. [More directories](./12-directory_permissions) : A script that creates a directory called `my_dir` with permissions **751** in the working directory.
13. [Change group](./13-change_group) : A script that changes the group owner to `school` for the file `hello`.

### Advanced tasks

14. [Owner and group](./100-change_owner_and_group) : A script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.
15. [Symbolic links](./101-symbolic_link_permissions) : A script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively. (*The file `_hello` is a symbolic link in the working directory*)
16. [If only](./102-if_only) : A script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
17. [Star Wars](./103-Star_Wars) : A script that will play the StarWars IV episode in the terminal.
