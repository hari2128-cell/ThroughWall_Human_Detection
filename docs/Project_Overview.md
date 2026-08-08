# Project Overview

**Through-Wall Human Motion Detection** is an embedded sensing system capable of
detecting the presence and movement of a human behind non-metallic obstacles such
as wooden doors, drywall, or thin brick walls, using microwave Doppler radar.

Unlike cameras, infrared sensors, or ultrasonic sensors, microwave radar does not
require direct line of sight. It transmits electromagnetic waves that penetrate
many common building materials and analyzes the reflected signal from moving
objects.

## Components

- Microwave Doppler radar sensor
- ESP32 microcontroller
- Signal conditioning
- Digital signal processing (MATLAB)
- Real-time visualization

## Goal

Detect human motion, remove unwanted noise, extract useful signal features, and
visualize detected motion in real time.

## Motivation

- Cameras cannot see through walls.
- PIR sensors require direct infrared exposure.
- Ultrasonic sensors need a clear propagation path.
- Vision systems fail in smoke, darkness, or obstructed environments.

Microwave Doppler radar overcomes these limitations by sensing motion through
changes in reflected radio waves, enabling use in disaster rescue, security
surveillance, smart homes, and occupancy monitoring.
