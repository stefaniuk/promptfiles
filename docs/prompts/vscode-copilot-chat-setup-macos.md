# VS Code Copilot Chat setup on macOS

This guide explains how to configure Visual Studio Code so GitHub Copilot Chat
uses:

- `Enter` to submit the current prompt
- `Shift+Enter` to insert a new line in the chat input

## Scope

- OS: macOS
- VS Code: 1.109.x (current stable line)
- Copilot: GitHub Copilot Chat extension

## Important note

In current VS Code releases, this behaviour is configured through
`keybindings.json` (keyboard shortcuts), not through a dedicated chat setting.

## Configure keybindings

1. Open the Command Palette (`Shift+Cmd+P`).
2. Run `Preferences: Open Keyboard Shortcuts (JSON)`.
3. Add the following rules to your `keybindings.json`:

```json
[
  {
    "key": "enter",
    "command": "workbench.action.chat.submit",
    "when": "inChatInput && chatAgentKind == 'ask'"
  },
  {
    "key": "enter",
    "command": "workbench.action.edits.submit",
    "when": "inChatInput && chatAgentKind != 'ask'"
  },
  {
    "key": "shift+enter",
    "command": "type",
    "args": {
      "text": "\n"
    },
    "when": "inChatInput"
  }
]
```

## Validate the behaviour

1. Open Chat (`Ctrl+Cmd+I` on macOS by default).
2. Type a multi-line prompt.
3. Press `Shift+Enter` to confirm a new line is inserted.
4. Press `Enter` to submit the prompt.

## If it does not work

- Open Keyboard Shortcuts UI (`Cmd+K`, then `Cmd+S`).
- Search for `workbench.action.chat.submit`.
- Use **Show Same Keybindings** to detect conflicts for `Enter` or
  `Shift+Enter`.
- Keep your custom rule as the effective one for `inChatInput` context.
