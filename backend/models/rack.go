package models

type Rack struct {
	ID uint
	DatacenterID uint

	Name string
	Datacenter *Datacenter
}
