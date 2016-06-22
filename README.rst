.. contents:: Table of contents
   :depth: 2

Notes for Django OSS Equipment Manager (OSSEM, pronounced 'awesome') for LabOps teams:

This OSS is meant to be an alternative to something like Qualisystems, it will
have a resource structure, reservations, equipment automation, and more.

Models:
#######

These are the models we will store in the DB, some of them inherit from others
as indicated by the ().  Names in OSSEM need to be unique within domains.

- Resource
- Device(Resource)
- Interface(Resource)
- CDU(Resource)
- Rack
- Shelf
- Cabinet(Rack)
- Room
- User
- Group
- Domain

Model breakdowns:
=================

Here we will go over each model and its purpose

Room
----

The Room would be where something is stored, valid children would be things
such as Rack, Device, Shelf...

Fields:

- Required

  - Name
  - Location (typically address and floor)
- Optional

  - Square footage

Generated Fields:

- Number of racks
- Number of shelves
- Number of Devices
- Power Capacity

Rack
----

A rack represents an equipment rack.  If tied to a managed CDU it will be able
to better estimate the used and available power, otherwise it will rely on the
power required field for Devices.

Fields:

- Required

  - Name (just a text field so numbers work fine too)
  - Total Rack Units

- Optional

  - Room
  - Power capacity

Generated Fields:

- Occupied U space
- Free U space
- Estimated power utilization
- Estimated free power

Cabinet(Rack)
-------------

A cabinet is essentially fuctionally equivalent to a rack, but it is enclosed.
The separation is mostly based on personal experience of needing to know when
it was one vs the other, and we also have the ability to flag them as locked.

Fields:

- Optional

  - Locked

Resource
--------

This is the parent for most end devices, it holds the important values that are
similar across any Device, Interface, etc...

Fields:
+++++++

- Required

  - Name
  - Manufacturer
  - Model

- Optional

  - Description
  - Address
