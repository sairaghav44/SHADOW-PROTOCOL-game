# SHADOW-PROTOCOL

A 2D arena-survival game built with Python and Pygame.

## Current Prototype

The current prototype includes:

- Player movement inside a bounded arena.
- A pursuing enemy that moves toward the player using vector-based movement.
- Collision detection between the player and the enemy.
- Collectible coins that increase the score.
- A game-over state with a restart button.
- Frame-rate-independent movement using delta time.

## Planned Gameplay

The next development phase will expand the prototype into an arena-survival game with multiple enemy types and a player health system.

### Player Health

- The player will have a maximum of 10 hearts.
- Enemy attacks will deal different amounts of damage.
- The game will end when the player's health reaches zero.
- A brief damage-immunity period after being hit is planned.
- Health will be displayed using a heart-based interface.

### Health Apples

- An apple will spawn every 5 seconds.
- Collecting an apple will restore 1 heart.
- Health cannot exceed the maximum of 10 hearts.
- Apples will spawn at random positions that do not overlap the player or enemies.
- The exact behaviour when an apple is not collected will be decided during implementation.

## Planned Enemy Types

The goal is to introduce four enemies with distinct behaviours. These are planned features and are not implemented in the current prototype.

### 1. Pursuer

The existing enemy will be upgraded from basic pursuit to more intelligent movement.

Planned behaviour:
- Predict the player's movement.
- Attempt to intercept the player instead of only following their current position.
- Adjust its movement based on the player's direction.
- Eventually attempt to cut off escape routes.

### 2. Dasher

A burst-attacking enemy.

Planned behaviour:
- Remain stationary while charging.
- Charge for 5 seconds.
- Lock onto the player's position.
- Display a warning before attacking.
- Dash rapidly toward the target.
- Enter a cooldown period before charging again.

### 3. Sniper

A long-range enemy that attacks from a distance.

Planned behaviour:
- Maintain distance from the player.
- Select a target position.
- Charge its shot.
- Display a targeting indicator before firing.
- Fire after a warning period.
- Reposition after attacking.

### 4. Slammer

An area-attack enemy.

Planned behaviour:
- Select a target location.
- Charge its attack.
- Display a circular danger zone.
- Slam the marked area after the warning period.
- Damage the player if they remain inside the danger radius.

## Initial Balancing Values

These values are starting points for testing and may change during development.

| Feature | Initial value |
|---|---:|
| Maximum player health | 10 hearts |
| Health restored by an apple | 1 heart |
| Apple spawn interval | 5 seconds |
| Pursuer contact damage | 1 heart |
| Dasher hit damage | 2 hearts |
| Sniper hit damage | 2 hearts |
| Slammer impact damage | 3 hearts |
| Game-over condition | 0 hearts |

All planned attacks should provide a readable warning and a reasonable opportunity for the player to react.

## Development Roadmap

| Version | Planned work |
|---|---|
| V0.1–V0.3 | Core game prototype: window, movement, arena, pursuit, coins, score, collision, game-over and restart |
| V0.4 | Multiple enemies using lists and iteration; improve enemy boundary handling |
| V0.5 | Dasher charge, dash and cooldown behaviour |
| V0.6 | Slammer targeting, warning radius and area attack |
| V0.7 | Sniper targeting, warning and projectile attack |
| V0.8 | Predictive behaviour for the Pursuer |
| V0.9 | Difficulty progression, gameplay balancing and polish |

## Technical Concepts

The project will be used to practise and apply:

- Python functions and modular programming.
- Lists and iteration.
- Classes and object-oriented programming.
- State machines for enemy behaviour.
- Vector mathematics and movement prediction.
- Collision detection.
- Timers and cooldowns.
- Health, damage and pickup systems.
- Randomized spawning.
- Difficulty scaling and game balancing.

## Technology

- Python
- Pygame

## Project Status

The core prototype is playable. Multiple enemy classes, the health system, health apples and the advanced AI behaviours described above are planned for future versions.

This README distinguishes existing prototype features from planned work; roadmap items should only be marked complete once they have been implemented and tested.

#hope you like it :)
