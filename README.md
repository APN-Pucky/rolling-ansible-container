rolling-ansible-container
==========================

fast development of containers

Why?
-----

One major drawback of working with docker containers is that a small change in the one of the first steps results in a cascade of steps that need to be redone.
When one is only installing software (by source or binary) these installation steps are mostly commuting.

In this pilot project we try to solve this by reusing the container and reuse already installed software.
If however some steps actually depend on one another ansible can be used to manage these.

In doing so we solve another issue with Docker containers, namely that they can get quite ugly with more features being added.


Advantages
-----------

  * Combining the best of two world: Ansible and containers
  * Easy way to have commutable installations in a container (i.e. you don't have to bother with the order of the installations, but can order them if necessary)
  * Well suited for rolling release systems
  * Use the same technology on your containers as on your hardware (-> ansible)
  * Ansible sort-of provides an operating system/distro independent way of installing software
  * Ansible is better structured than e.g. Dockerfiles
  * Reuse of missing binaries
  * No need to force single commands into a single line

Disadvantages
---------------

  * Containers will grow with time. However, one can solve this by either clearing logs or rerun ansible on a fresh container  
  * Overhead of ansible (and thereby python). However, they can be purged after the installation if one aims for a clean production container.
  * No linear installation history