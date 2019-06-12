package models

type Model struct {
	ID             uint
	ManufacturerID uint

	Name         string
	Manufacturer *Manufacturer
}
