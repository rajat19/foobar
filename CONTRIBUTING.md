
# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions
----------------------

### Report Errors in Solutions
```
Report errors on the `issues page`. If you are reporting an issue, please include:

* Question for which issue came
* Language in which the code is not working
```

### Fix Solutions
```
All the solutions available in the website at time of their creation are correct. 
But questions' language might change later and their solution might need to be updated/corrected.
Look through the GitHub issues for some wrong solutions. Anything tagged with "bug"
is open to whoever wants to implement it.
```

### Add Solutions
```
At the time of writing, Google foobar only supported Java and Python. If any new language is added in near future, you can add the solution in that language as well. 
Remember to update codetab.html as well
```

### Add Foobar Questions
```
You can add any foobar question you faced. Check [Sample](_drafts/sample.md) on how to add a foobar question with its solutions
```

## Get Started!
------------
Ready to contribute? Here's how to set up `foobar` for local.

1. Fork the `foobar` repo on GitHub.
2. Clone your fork locally::
```bash
    $ git clone git@github.com:rajat19/foobar.git
```
3. Create a branch for local development::
```bash
    $ git checkout -b name-of-your-bugfix-or-feature
```

4. Commit your changes, quoting github issue in the commit message, if applicable and push your branch to GitHub::
```bash
    $ git add .
    $ git commit -m "Fix #XX - My awesome fix"
    $ git push origin name-of-your-bugfix-or-feature
```

5. Submit a pull request through the GitHub website.

## Things to keep in mind!
---
Some things to keep in mind while adding questions/solutions-
1. Questions are added in `markdown` files which have .md extensions. These are added in `_posts` folder
2. Add a question post inside `_posts` folder starting with current date then question name. For ex- `2021-01-01-foobar-got-interesting.md`
3. You are not necessarily required to add solutions for the foobar question you put. Do not add below line to your post if you do not wish to add any solution
```md
{% include codetab.html btnClass="solution" langs="java py"%}
```
4. The solutions are added in `_includes/code` folder. Add a folder with question name ex- `foobar-got-interesting`. Add your solutions in this folder only.
5. By default, the website requires java and python solutions, if you wish to add only one of them, or just know solution in only one of the language, use `langs="java"` or `langs="py"` while using the line
```md
{% include codetab.html btnClass="solution" langs="java py"%}
```
6. If you have got working solutions in both python/java, don't include the langs part
```md
{% include codetab.html btnClass="solution"%}
```