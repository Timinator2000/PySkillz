# Testing Your New Exercise

Because your GitHub branch is not connected to a playground, you need to test your code locally using the following three steps.

1. Inside timinator_tools.py, located in the python-project folder, make sure RUNNING_ON_TECH_IO is set to False

3. Code a solution inside exercise_name.py just as if you were the playground user. Make sure your changes are saved.

5. Run exercise_name_test.py.

When the exercise runs, you will see all the same output the user sees in the playground. The formatting has been changed for terminal output, but all content remains the same. On Tech.io, all output is directed to a "channel" and Tech.io does a beautiful job of organizing and displaying the channels. In your terminal output, channels are indicated on each line of output similar to this:

```text
Win🎉> Success Channel on Tech.io.
Bug🐞> Bug Channel on Tech.io.
Sol✅> Suggested Solution Channel on Tech.io.
StdOut> Standard Output Channel on Tech.io
```

The user can also print debug output to `sys.stderr`. The PySkillz playground uses Tech.io defaults for any debug output. It does not create a specific channel, nor is a channel specified when running locally.

On the next page, we'll explore the details of each of the three files that make up an exercise.

************

[![Skillz Catalog](../../graphics/PySkillzFooter.png)](skillz-catalog)
