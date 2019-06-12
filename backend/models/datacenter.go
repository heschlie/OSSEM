package models

type Datacenter struct {
	ID     uint
	SiteID uint

	Name string
	Site *Site
}
