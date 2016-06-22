.. contents:: Table of contents
   :depth: 3

Notes for Django OSS Equipment Manager (OSSEM, pronounced 'awesome') for LabOps teams:

This OSS is meant to be an alternative to something like Qualisystems, it will
have a resource structure, reservations, equipment automation, and more.

Models:
#######

These are the models we will store in the DB, some of them inherit from others
as indicated by the ().  Names in OSSEM need to be unique within domains.

- `Resource`_
- `Device`_\(`Resource`_)
- `Interface`_\(`Resource`_)
- `CDU`_\(`Resource`_)
- `Manufacturer`_
- `Model`_
- `Rack`_
- `Shelf`_
- `Bench`_
- `Cabinet`_\(`Rack`_)
- `Site`_
- `Room`_
- `User`_
- `Group`_
- `Domain`_

Model breakdowns:
=================

Here we will go over each model and its purpose

Site
----

A site is a large physical location, typically a city, campus, or building

Fields:
+++++++

- Required

  - Name

Room
----

The Room would be where something is stored, valid children would be things
such as `Rack`_, `Device`_, `Shelf`_...

Fields:
+++++++

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

A rack represents an equipment rack.  If tied to a managed `CDU`_ it will be able
to better estimate the used and available power, otherwise it will rely on the
power required field for Devices.

Fields:
+++++++

- Required

  - Name (just a text field so numbers work fine too)
  - Total Rack Units
  - `Room`_

- Optional

  - Power capacity

Generated Fields:

- Occupied U space
- Free U space
- Estimated power utilization
- Estimated free power

Cabinet
-------------

Inherits from `Rack`_

A cabinet is essentially fuctionally equivalent to a `Rack`_, but it is enclosed.
The separation is mostly based on personal experience of needing to know when
it was one vs the other, and we also have the ability to flag them as locked.

Fields:
+++++++

- Optional

  - Locked

Shelf
------

A shelf is just that, a shelf, though not a shelf in a `Rack`_.  This is for
shelves that are in storage rooms, or just not actually a rack.  This is mainly
a bucket to put equipment in.

Fields:
+++++++

- Required

  - `Room`_

- Generated

  - Power

    - If a `CDU`_ is associated with it

Bench
-----

A workbench.

Fields:
+++++++

- Required

  - `Room`_

Manufacturer
------------

A text field of the company that manufactures the unit.

Examples:

- Dell
- Ericsson
- Riverbed
- Netgear

Fields:
+++++++

- Required

  - Name

- Optional

  - Description
  - Custom attributes

    - These are Key/Value pairs of interesting things that one would want to
      track, Models under the Manufacturer will inherit these
    - Models can override these to add to them as well, in other words, if you
      had a field called "port_count" that had a picklist of [ 48, 32 ] a Model
      could override that and add or remove values.
    - `Model`_\s **cannot** remove these fields entirely

Model
-----

A representation of a model from a `Manufacturer`_.

Example:

- S6000
- R720
- Nexus 9000

Fields:
+++++++

- Required

  - `Manufacturer`_

    - Picklist of Manufacturers, this is a one-to-many Man. -> Model

  - Name

    - Need to be unique within `Manufacturer`_

  - Size in rack units

    - Most devices that end up in datacenters are sized by rack units, for instance
      a Dell S6000 is 1 rack unit (RU) in height, whereas a Dell S6100 is 3 RU.
    - If a device is not rackable, you can measure it, 1.75" per RU

  - Shared rack unit

    - Some devices can be in a rack and share thier space with another device
      like the Riverbed Steelhead CX255

  - Number of Power ports

- Optional

  - Description
  - Custom Attributes

    - See Manufacturer description above

Resource
--------

This is the parent for most end devices, it holds the important values that are
similar across any `Device`_, `Interface`_, etc...

This class/model is considered abstract and should not be instaciated directly.

Fields:
+++++++

- Required

  - Name
  - `Model`_

- Optional

  - Description
  - Address

Device
----------------

Inherits from `Resource`_

This is a generic representation of a device that one would rack or store somewhere.
Most objects will derive from this model

Fields:
+++++++

- Required

  - Location

    - Picklist of `Site`_\=>`Room`_\=>`Rack`_

      - Maybe not picklist, but filtered text box?  Something to easily type in
        the name of the final spot (let's say a rack) and it would filter based on
        that criteria, so you do not need to pick each object individually.

  - Rack unit

    - Only if in a Rack

Interface
---------

Inherits from `Resource`_

CDU
-------------

Inherits from `Device`_

A CDU is a power distribution device, it may be managed or unmanaged.  If OSSEM
has a "driver" written for the `Manufacturer`_ and `Model`_ and the CDU is capable it will
pull the power readings from the CDU.

We assume the CDU is serving the rack it is associated with, and if a device from
an adjacent `Rack`_ is pulling power from it, then we judge that unit as borrowing
power from the `Rack`_ that the CDU is in.

We also assume that vertical CDUs are not occupying any rack units, and will omit
the rack unit field from it.

Fields:
+++++++

- Required

  - Power capcity
  - Number of ports

User
----

A user

Fields:
+++++++

- Required

  - Name
  - Username
  - Email
  - Password

- Optional

  - Is system admin
  - Admin of `Group`_\s...

    - A list of groups this user can administer

  - Admin of `Domain`_\s...

    - A list of domains this user can administer

Group
-----

A group of users who share a common set of permissions

Domain
------

A domain of equipment.  This can be used to isolate equipment groups, hide some
equipment from users such as storage, and just get a better division of equipment
