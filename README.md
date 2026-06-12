# Seismic Activity Detector using Micro:bit

## Overview

This project is a simple seismic activity detection prototype built using a Microsoft Micro:bit and its onboard 3-axis accelerometer.

The system continuously monitors vibration levels and classifies activity into three states:

* Safe
* Warning
* Danger

Visual and audio alerts are triggered when vibration thresholds are exceeded.

## Features

* Real-time vibration monitoring
* Accelerometer-based sensing
* Multi-level alert system
* Audio and visual notifications
* Live data visualization through serial graphing

## Hardware Used

* Microsoft Micro:bit V2
* Onboard Accelerometer
* USB Connection

## Working Principle

The Micro:bit reads acceleration values along the X, Y, and Z axes.

A vibration score is calculated from the combined acceleration values.

If the score exceeds predefined thresholds, the device enters either Warning or Danger mode and activates corresponding alerts.

## Applications

* Earthquake monitoring prototypes
* Vibration detection systems
* Structural health monitoring demonstrations
* Embedded systems education

## Future Improvements

* Data logging to SD card
* Wireless notifications
* Magnitude estimation algorithms
* Cloud-based monitoring dashboard

## Skills Demonstrated

* Embedded Systems
* Sensor Interfacing
* Signal Processing
* Real-Time Monitoring
* Rapid Prototyping
* Hardware Programming
