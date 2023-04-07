# CMDS Helper

This modul will help us to automate CLI Command we usually use in projects.

### Installation

Using pip :

```pip
pip install cmds-helper
```

### How To Use

- Install cmds-helper module using `pip`
- Make runner file in root of your project files directory (i.e `run.py`)
  ```
  --ProjectDir
      --{{Your project files/folder}}
      --run.py
      --{{your cmd json file}}cmd.json
  ```
- Import cmdshelper `Helper` class
  ```py
  from cmdshelper.helper import Helper
  ```
- Instantiate the `Helper` class
  ```py
  cmd = Helper()
  ```
- Make command json file. You can make many cmd json file for grouping cmd or just make 1 cmd json file. The program will read all json file ends with `cmd.json` in your project directory and add it to `list_command` in `Helper` class. The syntax is :

  ```json
  {
      "{your_cmd_identifier}" : [
          "{cmd_command_to_run}",
          "{cmd_command_to_run}",
          ...
      ],
      "{your_cmd_identifier}" : [
          "{cmd_command_to_run}",
          "{cmd_command_to_run}",
          ...
      ],
      ...
  }
  ```

  - `{your_cmd_identifier}` is identifier for calling all cmd command under that identifier. every identifier must be unique

  - `cmd_command_to_run` is the cmd command you want to run. The command is string you usually type in CLI, but in the json file, you separate every command/optional/arguments using space / ' ' like usual.

  - In `cmd_command_to_run`, you can add argument to pass, with type `%{i}` (`i` is index arguments passes)

- Example :

  ```json
  "gitACP" : [
          "git add .",
          "git commit -m %1",
          "git push"
      ]
  ```

  the identifier to call that command is `gitACP` (command to call git common command `[add, commit, and push]`). under that identifier, we specify all command we want to call

  - `"git add ."`
  - `"git commit -m "{message}" "` is typed `"git commit -m %1"`
    - `%1` means that the first argument passed when calling that command identifier, will replacing `%1` into the passed string
    - If you just want add same commit message for each commit, you can just change `%1` into your message like `feat: add something`
  - `"git push"`

  You can see another command examples in `example_cmd.json`

- There are 4 ways to run this `file`, by CLI with passing `arg`, by hardcode the command in `script`, or by using `python -m`

  - CLI Passing argument :

    - After instantiate the class, you can type this code :

      ```py
      import sys

      cmd.run(sys.argv[1:])
      ```

    - To run it, you just need to run the file and passing the `command identifier` and `argument` if needed
    - Example run it in CommandPrompt
      ```sh
      py run.py gitACP "feat: add something
      ```
      that will call the `gitACP` command and pass `feat: add something` as commit message

  - Hardcoded Command :

    - After instantiate the class, you can type this code :

      ```py

      cmd.run([{your command here}])
      ```

    - Example :

      ```py

      cmd.run(["gitACP","feat: add something"])
      ```

      to run it, you just need to run `run.py` file

  - Straight from Python module

    It is just as simple as you open the folder that you want to run the command

    ```
    python -m cmdshelper [command] [args_1] [args_2] ... [args_3]
    ```

    for example:

    ```
    python -m cmdshelper gitACP "feat: add something"
    ```

  - Simply just cdmshelper

    It is just as simple as you open the folder that you want to run the command

    ```
    cmdshelper [command] [args_1] [args_2] ... [args_3]
    ```

    for example:

    ```
    cmdshelper gitACP "feat: add something"
    ```

- Full code in `run.py ` will be :

  ```py
  from cmdshelper.helper import Helper
  import sys

  cmd = Helper()

  # run using cli
  cmd.run(sys.argv[1:])

  # run using hardcode command
  #cmd.run(["gitACP","feat: add something"])

  ```

### License

This project is licensed under the terms of the MIT license.
