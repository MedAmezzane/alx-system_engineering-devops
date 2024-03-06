# Web stack debugging #3

Project done during **Full Stack Software Engineering studies** at **ALX**.
This project marked the fourth installment in a series of web stack debugging tasks. In these assignments, malfunctioning web stacks were provided within isolated containers, and I was assigned the responsibility of rectifying the issues to restore functionality. For each task, I authored a script to automate the commands required for resolving the issues within the web stack.

### Mandatory tasks

* **0. Strace is your friend**
  * [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp): Puppet manifest that fixes a typo error causing a WordPress application being served by an Apache web server to fail.
  * Usage: `puppet apply 0-strace_is_your_friend.pp`
