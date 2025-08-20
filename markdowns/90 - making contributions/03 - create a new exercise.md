# Creating a New Exercise

Three files must be organized into a single folder to create a new exercise:

| Filename | Description |
|:---------|:------------|
| exercise_name.py | This is the code block presented to the user to solve. |
| exercise_name_solution.py | This is the working solution to the exercise. The code in this file will be used by the grader to determine the expected output. This entire file will be displayed to the user as the suggested solution(s) after succesffuly solving completing the exercise.
| exercise_name_test.py | This code creates the exercise subclass that defines the specifics of this exercise. For instance, code that defines the static test cases and how to generate random test cases is located here.

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


************

[![Skillz Catalog](../../graphics/PySkillzFooter.png)](skillz-catalog)
