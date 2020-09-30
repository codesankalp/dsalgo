<div style="text-align:center"><img src="https://miro.medium.com/max/840/1*RJMxLdTHqVBSijKmOO5MAg.jpeg" /></div>

# Contributing:

We love pull requests from everyone. By contributing to this repository, you
agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Get Started: 

* First [fork][fork] the repository and then clone it using:

    git clone `git clone https://github.com/your_username/dsalgo.git`

* Ask for issues to be assigned. If you want, you can open new [issues](#issues) as well

* After that create a branch for your changes. For example:  
  * add_# if you will add new algorithms or data structures.  
  * fix_# if you will fix a bug on a certain algorithm or data structure.  
  * test_# if you wrote a test/s.  
  * doc_# if you added to or edited documentation.

You may contribute by:

- Implementing new algorithms in the repo. Be sure to keep it under
right section [dsalgo/][dsalgo/] (e.g. dsalgo/linked_list,dsalgo/sort, etc). Make a new section for it if
it doesn't fall under any section. Make sure that your implementation works, Also make sure you writes test for same in [dsalgo/tests][tests] 

- Optimizing or improving the existing algorithms.
- Adding a different solution for the problem.
- Finding and fixing bugs.
- Adding examples to explain the algorithms better.
- Adding test cases (Note: use python [unittest][unittest] testing framework for wrritng tests).
- Improving documentation.
  

## How to write good commit messages:

**Use following commit style**:
```
[module/file/feature] Short description #<issue-no.>

Long description here
Fixes #<issue-no.>
```

* **Specify the type of commit**:
*  **feature:** The new feature you're adding to a particular application
* **fix:** A bug fix
*  **style:** Feature and updates related to styling
*  **refactor:** Refactoring a specific section of the codebase
*  **test:** Everything related to testing
*  **docs:** Everything related to documentation
*  **chores:** Regular code maintenance/typos or any other similar error
*  **qa:** Improvement in code readability/ styling etc.
* Separate the subject from the body with a blank line
* Your commit message should not contain any whitespace errors
* Remove unnecessary punctuation marks
* Do not end the subject line with a period
* Capitalize the subject line and each paragraph
* Use the imperative mood in the subject line
* Use the body to explain what changes you have made and why you made * them.
* Do not assume the reviewer understands what the original problem was,ensure you add it.
* Do not think your code is self-explanatory

**Example of a good commit**:

```
[docs] Added contributing file #36

Added contibution file to help new contributors
Fixes #36
```


## Pull Requests:
Push to your fork and [submit a pull request][pr].

We will review and may suggest some changes or improvements or alternatives.
Some things that will increase the chance that your pull request is accepted:

* All algorithms should be written in **Python 3**.
(There are a few algorithms still in _Python 2_ syntax. You can start by converting
 to _Python 3_.)

* Write clean and understandable code.
* Properly comment the code and briefly explain what the algorithm is doing in the [docstrings][docstr].https://www.conventionalcommits.org/en/v1.0.0/
* You may also explain the output using a minimal example.
* Try to also include a couple of test cases for the algorithm.
* Write a [good commit message][commit].


## Issues:
Submit a [new issue][newissue] if there is an algorithm to add, or if a bug was found in an existing algorithm. Before submitting a new issue please review the [existing issues][issues] to avoid creating duplicates. Also, consider resolving current issues or contributing to the discussion on an issue.


[fork]: https://help.github.com/articles/fork-a-repo/
[docstr]: https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings
[commit]: https://www.conventionalcommits.org/en/v1.0.0/
[pr]: https://github.com/codesankalp/dsalgo/compare/
[tests]:https://github.com/codesankalp/dsalgo/tree/master/tests
[dsalgo/]:https://github.com/codesankalp/dsalgo/tree/master/dsalgo
[unittest]:https://docs.python.org/2/library/unittest.html
[newissue]: https://github.com/codesankalp/dsalgo/issues/new
[issues]: https://github.com/codesankalp/dsalgo/issues/
