# Creating a New Exercise

Three files must be organized into a single folder to create a new exercise:


: Table Caption {tbl-colwidths="[20,80]"}

| Filename | Description |
|:---------:|:------------------------------------------------------------------------------------------------|
| exercise_name.py | This is the code block presented to the user to solve. |
| exercise_name_solution.py | This is the working solution to the exercise. The code in this file will be used by the grader to determine the expected output. This entire file will be displayed to the user as the suggested solution(s) after succesffuly solving completing the exercise. |
| exercise_name_test.py | This code creates the exercise subclass that defines the specifics of this exercise. For instance, code that defines the static test cases and how to generate random test cases is located here. |

These three files go inside a folder that is given the same name as the exercise. Naming conventions are important. The exercise architecture depends on these naming conventions to find the files needed to execute successfully.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise_name<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_test.py<BR>

<BR>

Consider the "Hello, World?" example. The following structure results from the steps above:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 hello_world<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_test.py<BR>
<BR>

Finally, the exercise_name folder must be placed inside a _topic group_ folder. A topic group is a group of exercises that are all displayed on a single markdown page. Consider the PySkillz welcome page. This is a single markdown page with two exercises that introduce the reader to the two types of exercises - print-based exercises and exercises that return an answer. These two exercises are grouped into a topic group called welcome. The resulting structure looks like this:

📂 python-project<BR>
&nbsp;&nbsp;&nbsp;&nbsp;📂 welcome<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 hello_world<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_test.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 add_two_numbers<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 add_two_numbers.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 add_two_numbers_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 add_two_numbers_test.py<BR>

# Testing Your New Exercise

Because your GitHub branch is not connected to a playground, you need to test your code locally using the following three steps.

1. Inside timinator_tools.py located in the python-project folder, make sure RUNNING_ON_TECH_IO has been set to False
2. Code a solution inside exercise_name.py just as if you were the user of the playground. Make sure these changes are saved.
3. Run exercise_name_test.py.

When the exercise runs, you will see all the same output the user will see in the playground. The formatting has been changed for terminal output, but all content remains the same. On Tech.io, all output is directed to a "channel" and Tech.io does a beautiful job of organizing and displaying the channels. In your terminal output, channels are indicated on each line of output similar to this:

```text
Win🎉> This is the success channel in Tech.io.
Bug🐞> This is the bug channel in Tech.io.
Sol✅> This is the solution channel in Tech.io.
StdOut> This is the standard output channel in Tech.io
```

The user can also print debug output to `sys.stderr`. The PySkillz playground uses Tech.io defaults for any debug output. It does not create a specific channel, nor is a channel specified when running locally.

On the next page, we'll explore the details of each of the three files that make up an exercise.

************

[![Skillz Catalog](../../graphics/PySkillzFooter.png)](skillz-catalog)
