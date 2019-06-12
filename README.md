# OSSEM overview

Notes for OSS Equipment Manager (OSSEM, pronounced 'awesome') for
LabOps teams:

This OSS is meant to be an alternative to something like Qualisystems,
it will have a resource structure, reservations, equipment automation,
and more. We plan to create a software suite that will both manage your 
equipment, allow user reservations, generate topologies to share, and 
automate deployment of equipment and VMs.

# Models

These are the models we will store in the DB, some of them inherit from
others as indicated by the (). Names in OSSEM need to be unique within
domains Unless otherwise specified.

  - [Resource]()
  - [Device]()([Resource]())
  - [Interface]()([Resource]())
  - [CDU]()([Resource]())
  - [Manufacturer]()
  - [Model]()
  - [Rack](#rack)
  - [Site](#site)
  - [Datacenter](#datacenter)
  - [Topology]()
  - [User]()
  - [Group]()
  - [Domain]()

## Model breakdowns

Here we will go over each model and its purpose

### Site

A site is a large physical location, typically a city, campus, or
building

**Fields:**

  - Required
      - Name

**Generated Fields:**

  - Number of Rooms
  - Number of Racks
  - Number of Shelves
  - Number of Benches
  - Number of devices

### Datacenter

The Room would be where something is stored, valid children would be
things such as [Rack](#rack), [Device](), etc...

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

### Rack

A rack represents an equipment rack. If tied to a managed [CDU]() it
will be able to better estimate the used and available power, otherwise
it will rely on the power required field for Devices.

**Fields:**

  - Required
      - Name (just a text field so numbers work fine too)
      - Total Rack Units
      - [Room](#room)
  - Optional
      - Power capacity

**Generated Fields:**

  - Occupied U space
  - Free U space
  - Estimated power utilization
  - Estimated free power

### Location

A wrapper class to encapsulate [Site](#site), [Datacenter](#datacenter),
[Rack](#rack). this allows us to put one location
field in the [Resource]() class in order to make it so you can have any
or all of those classes listed for the location.

On whatever form a user fills out for this, it should populate the other
fields when it can, for instance, if you pick a [Datacenter](#datacenter) it should
populate the [Site](#site) automatically.

  - Required