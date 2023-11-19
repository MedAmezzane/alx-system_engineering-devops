# Command Line Mastery Showcase

Welcome to my Command Line journey documented through screenshots from the [CMDCHALLENGE](https://cmdchallenge.com/). 

CMD CHALLENGE is an engaging game that tests your proficiency in Bash. With challenges evolving in complexity, it serves as excellent training to enhance your command line skills.

This repository exhibits screenshots representing my successful completion of all CMD CHALLENGE levels, provided in both .png and .jpg formats.

## SFTP Upload Guide

For those interested in replicating the process, here are the steps I followed to utilize the SFTP command-line tool:

**Step 1:** Navigate to the local machine's 'screenshots' directory:
```bash
cd ~/Desktop/screenshots
```
**Step 2:** Establish a connection to the sandbox environment:

```bash
sftp <username>@<sandbox-address>
```
**Step 3:**: Navigate to the target directory for screenshot uploads:

```bash
cd alx-system_engineering-devops/command_line_for_the_win/
```
**Step 4:** Upload the file '0-first_9_tasks.png':

```bash
put 0-first_9_tasks.png
```
**Step 5:** Confirm successful transfer by checking the sandbox directory:

```bash
ls -l
```


