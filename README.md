# blackJack
Blackjack made with python

A command-line Blackjack game built in Python as part of the 100 Days of Code - Python Pro Bootcamp.

## How to Play

Run `main.py` and follow the prompts:

1. Type `y` to start a game, or `n` to skip.
2. You and the computer are each dealt two cards. Only one of the computer's cards is shown.
3. Choose whether to draw another card (`y`) or stand (`n`).
4. Once you stand (or bust), the computer plays automatically, drawing until its score is 17 or higher.
5. The final hands and scores are compared to determine a win, loss, or tie.
6. After each round, you'll be asked if you want to play again.

## Features

- Ace handling — an Ace counts as 11, or drops to 1 automatically if the hand would otherwise bust
- Blackjack detection on the opening deal (Ace + 10-value card)
- Automatic dealer turn following standard "dealer stands on 17" rules
- Replayable — play multiple rounds without restarting the program
- Input validation on all yes/no prompts

## Files

- `main.py` — game logic
- `art.py` — ASCII art logo was provided (not written by me)

## What I Learned

This project helped me get comfortable with nested conditionals, loop control (`while`, `break`), tracking multiple pieces of state (hands and scores) as they change, and debugging indentation-based logic errors by tracing through code carefully rather than guessing.

## What I'd Change

Right now the game logic lives mostly in one long sequence with a lot of nested conditionals. I'd like to go back and refactor it into smaller functions (like separating out the dealer's turn and the score comparison), which should make the code shorter, easier to follow, and easier to test.