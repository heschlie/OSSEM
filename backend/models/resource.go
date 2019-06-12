package models

type Resource struct {
	ID      uint
	ModelID uint

	Model *Model
	Name  string
}
