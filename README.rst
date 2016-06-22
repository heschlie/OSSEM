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

Rack and Cabinet
----------------

A rack represents an equipment rack, and a cabinet is an extension of that, and
really only there to allow a deliniation between the two as they are otherwise
identical.  If tied to a managed CDU it will be able to better estimate the
used and available power, otherwise it will rely on the power required field
for Devices

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

Resource
--------

This is the parent for most end devices, it
