# AI Tools Setup

This repository documents the installation and setup of Cursor IDE, Claude Code, and Codex on my computer.

## Tools I installed

- Node.js
- Claude Code (CLI, version 2.1.142)
- Cursor IDE (desktop app)
- Claude Code extension for Cursor
- Codex extension for Cursor
- Git and a GitHub account

## Steps I completed

1. Installed Node.js on Windows 11.
2. Installed Claude Code from the terminal with `npm install -g @anthropic-ai/claude-code`.
3. Logged in with my Anthropic account.
4. Downloaded Cursor from cursor.com and installed the desktop app.
5. Installed the Claude Code extension in Cursor.
6. Installed the Codex extension in Cursor and logged in with my OpenAI account.
7. Created this public GitHub repository.
8. Opened the repository in Cursor, wrote this README, and pushed it with commit and push.

## Issues I ran into and how I solved them

**PowerShell wouldn't let me install Claude Code.** It threw a security error saying it couldn't run scripts. I fixed it by opening PowerShell as administrator and running `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`. After that, the `npm install` worked.

**The Claude Code extension didn't show up in Cursor's extension search.** No matter how I searched for "Claude Code", nothing came up. I solved it by downloading the `.vsix` file directly from Anthropic's official extension page and installing it from the terminal with `cursor --install-extension`. After restarting Cursor, the Claude Code icon appeared in the top right corner.

**I initially confused Cursor with its web version.** At first I was using Cursor Agents (the web interface at cursor.com/agents) instead of the actual desktop IDE, so I couldn't clone the repo or commit anything. Once I realized the difference, I downloaded and installed the desktop app from cursor.com and everything worked as expected.

**The `.vsix` file wasn't bundled in the npm package.** Older versions of the Claude Code npm package included the Cursor extension file, but version 2.1.142 didn't. I had to download it manually from the official gallery instead of extracting it from the package.

## What I learned

Setting everything up took longer than expected, but most problems had a solution one search away. The main lesson: always check whether you're using the desktop app or a web version of a tool, and don't assume an extension marketplace has everything — sometimes you need to install things manually.
