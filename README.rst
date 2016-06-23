Welcome to OSSEM!
+++++++++++++++++

.. contents:: **Table of contents**
   :depth: 3

Overview
########

Notes for Django OSS Equipment Manager (OSSEM, pronounced 'awesome') for LabOps teams:

This OSS is meant to be an alternative to something like Qualisystems, it will
have a resource structure, reservations, equipment automation, and more.

Models:
#######

These are the models we will store in the DB, some of them inherit from others
as indicated by the ().  Names in OSSEM need to be unique within domains Unless
otherwise specified.

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
- `Topology`_
- `User`_
- `Group`_
- `Domain`_

Model breakdowns:
=================

Here we will go over each model and its purpose

Site
----

A site is a large physical location, typically a city, campus, or building

**Fields:**

- Required

  - Name

Room
----

The Room would be where something is stored, valid children would be things
such as `Rack`_, `Device`_, `Shelf`_...

**Fields:**

- Required

  - Name
  - Location (typically address and floor)
- Optional

  - Square footage

**Generated Fields:**

- Number of racks
- Number of shelves
- Number of Devices
- Power Capacity

Rack
----

A rack represents an equipment rack.  If tied to a managed `CDU`_ it will be able
to better estimate the used and available power, otherwise it will rely on the
power required field for Devices.

**Fields:**

- Required

  - Name (just a text field so numbers work fine too)
  - Total Rack Units
  - `Room`_

- Optional

  - Power capacity

**Generated Fields:**

- Occupied U space
- Free U space
- Estimated power utilization
- Estimated free power

Cabinet
-------------

Inherits from `Rack`_

A cabinet is essentially functionally equivalent to a `Rack`_, but it is enclosed.
The separation is mostly based on personal experience of needing to know when
it was one vs the other, and we also have the ability to flag them as locked.

**Fields:**

- Optional

  - Locked

Shelf
------

A shelf is just that, a shelf, though not a shelf in a `Rack`_.  This is for
shelves that are in storage rooms, or just not actually a rack.  This is mainly
a bucket to put equipment in.

**Fields:**

- Required

  - `Room`_

- Generated

  - Power

    - If a `CDU`_ is associated with it

Bench
-----

A workbench.

**Fields:**

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

**Fields:**

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

**Fields:**

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

This class/model is considered abstract and should not be instantiated directly.

**Fields:**

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

**Fields:**
- Required

  - Location

    - Picklist of `Site`_\=>\ `Room`_\=>\ `Rack`_

      - Maybe not picklist, but filtered text box?  Something to easily type in
        the name of the final spot (let's say a rack) and it would filter based on
        that criteria, so you do not need to pick each object individually.

  - Rack unit

    - Only if in a Rack

- Optional

  - Console server

    - Serial console server or aggregator that you can connect to for serial
      access to the Device

  - Console Server Port(s)

    - A comma separated list of port numbers that the Device is connected to,
      this supports a more or less unlimited number of ports.

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

**Fields:**

- Required

  - Power capcity
  - Number of ports

Topology
--------

A group of equipment that is tied together in a specific manner.  The equipment
can be generic, just a specific `Model`_, or needing a specific piece of equipment.

Reservation
-----------

A time-frame in which a `User`_ has claimed a set of equipment for use.  You can
use a topology as a base for reserving equipment, or reserve equipment ad-hoc
as needed.

User
----

A user

**Fields:**

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

Views
#####

We will end up needing many, many views, here is a start to that list that will
almost definitely get bigger.  I will leave out the admin based views until it
is decided that the Django admin cannot cope with what we need, or end up being
counter intuitive.

- `Login`_
- `Login Domain Error`_
- `Equipment`_
- `Equipment List`_
- `Equipment Search`_
- `User View`_
- `Group View`_
- `Domain View`_
- `Topology View`_
- Connections
- Reservation View

Views breakdown
===============

Login
-----

A simple login page.  It should be clean and clear, you will enter your username
and password, and select a `Domain`_ to login to, if no domain is picked it will
log you into the first `Domain`_ on your list.

If you try to login to a `Domain`_ you do not have access to, you should be presented
with a 2nd view that let's you pick a domain you have access to.

Login Domain Error
------------------

This view is a simple picklist of `Domain`_\s the `User`_ has access to.  This
view is only presented when a `User`_ attempts to login to a `Domain`_ they do
not have permissions for.

Equipment
---------

The equipment view will list the required fields and custom attributes for the
current `Device`_.  If the `User`_ is an admin they should be able to edit any of
the fields that are not generated or locked.

Equipment List
--------------

This will show a list of `Device`_\s that will show the required fields side by
side by default, with the option to show the custom attributes.

We should have the ability to show and hide the custom attributes on a per attribute
level.  This would allow `User`_\s to compare these fields if they need to check
for consistency.

Equipment Search
----------------

A search page that lets you search based on any field for any device.  When
searching a custom field, you will need to specify the Key at a minimum, and
optionally a value to search by.  You can search based on just key if, for instance,
you need to find all devices that share a key so you can compare.

The search page should use a nested list page for the results, but leave the search
parameters intact between searches.

User View
---------

A simple view for the User model to display the `User`_\s info, as well as their
`Group`_ and `Domain`_ membership.

Group View
----------

A simple view that lists the `User`_\s in a `Group`_, as well as what `Domain`_\s
the group has access to.

Domain View
-----------

A simple view for `Domain`_\s that lists the `Group`_\s and `User`_\s that have
access to this `Domain`_.

Topology View
-------------

This view is probably one of the more complex views, we would need to be able
to display both specific and generic `Device`_\s and the connections between
them in a view that is clean and sensible.  It might be best to turn this into
a JavaScript canvas to display the equipment and it's relations.

We should have the ability to search for equipment to add to this `Topology`_
and select 1-2 `Device`_\s to bring up a connection dialogue and create the
desired connections.
